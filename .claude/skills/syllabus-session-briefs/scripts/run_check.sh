#!/bin/sh
# Usage: run_check.sh <session-id> [out-dir]
# Runs check_session.py with Playwright 1.63 (matches the cached chromium-1243 and webkit-2359).
# Chromium needs libasound.so.2; WebKit (the engine of Safari and Chrome on iPad) needs ~50 more
# system libraries. Both are fetched once without root into ../cache/libs.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
SID=${1:?session id, e.g. mftd-9}
OUT=${2:-$HERE/../cache/shots/$SID}
LIBS=$HERE/../cache/libs
if [ ! -f "$LIBS/root/usr/lib/x86_64-linux-gnu/libasound.so.2" ]; then
  mkdir -p "$LIBS" && cd "$LIBS"
  apt-get download libasound2t64 >/dev/null 2>&1 || apt-get download libasound2 >/dev/null
  for f in *.deb; do dpkg-deb -x "$f" root; done
  cd - >/dev/null
fi

WK=$HOME/.cache/ms-playwright/webkit-2359/minibrowser-wpe
WKLIBS=$LIBS/webkit
if [ -d "$WK" ] && [ ! -f "$WKLIBS/.ok" ]; then
  mkdir -p "$WKLIBS" && cd "$WKLIBS"
  for pkg in libavif16 libenchant-2-2 libevent-2.1-7t64 libflite1 libgstreamer-gl1.0-0 \
      libgstreamer-plugins-bad1.0-0 libgstreamer-plugins-base1.0-0 libgstreamer1.0-0 libharfbuzz-icu0 \
      libhyphen0 libmanette-0.2-0 libopus0 libsoup-3.0-0 libwayland-server0 libwebpdemux2 libxslt1.1 \
      libjxl0.7 libabsl20220623t64 libsecret-1-0 libx264-164 libwoff1 libdav1d7 libgav1-1 librav1e0 \
      libsvtav1enc1d1 libyuv0 libhwy1t64 libaom3 libgudev-1.0-0 libevdev2 libcairo-gobject2 libpsl5t64 \
      libgraphene-1.0-0 liborc-0.4-0t64 libdw1t64 libunwind8 libvpx9 libvoikko1 libhunspell-1.7-0 \
      libaspell15 libsharpyuv0 libwebp7 libwebpmux3 libgles2 libegl1; do
    apt-get download "$pkg" >/dev/null 2>&1 || echo "webkit deps: could not fetch $pkg" >&2
  done
  for f in *.deb; do dpkg-deb -x "$f" root; done
  L=root/usr/lib/x86_64-linux-gnu
  # This WebKit build links libjxl 0.8 and libbacktrace, which Ubuntu 24.04 lacks:
  # 0.7 serves (image decoding is unused here) and libbacktrace gets an empty stub.
  ln -sf libjxl.so.0.7 $L/libjxl.so.0.8
  printf 'void backtrace_create_state(){}void backtrace_full(){}void backtrace_print(){}void backtrace_simple(){}void backtrace_pcinfo(){}void backtrace_syminfo(){}\n' > bt.c
  cc -shared -fPIC -o $L/libbacktrace.so.0 bt.c
  rm -f *.deb bt.c
  touch .ok
  cd - >/dev/null
fi
if [ -f "$WKLIBS/.ok" ]; then
  WKROOT=$(cd "$WKLIBS/root/usr/lib/x86_64-linux-gnu" && pwd)
  ASROOT=$(cd "$LIBS/root/usr/lib/x86_64-linux-gnu" && pwd)
  cat > "$WKLIBS/run.sh" <<EOF
#!/bin/sh
export WEBKIT_EXEC_PATH="$WK/bin" WEBKIT_INJECTED_BUNDLE_PATH="$WK/lib" WEBKIT_INSPECTOR_RESOURCES_PATH="$WK/share"
export LD_LIBRARY_PATH="$WK/lib:$WK/sys/lib:$WKROOT:$ASROOT" WEBKIT_FORCE_COMPLEX_TEXT=1
exec "$WK/bin/MiniBrowser" "\$@"
EOF
  chmod +x "$WKLIBS/run.sh"
  export WEBKIT_RUN="$WKLIBS/run.sh" PLAYWRIGHT_SKIP_VALIDATE_HOST_REQUIREMENTS=1
fi

LD_LIBRARY_PATH="$LIBS/root/usr/lib/x86_64-linux-gnu" UV_CACHE_DIR=${UV_CACHE_DIR:-/tmp/claude-1000/uv-cache} \
  uv run --no-project --with playwright==1.63.0 python "$HERE/check_session.py" "$SID" "$OUT"
