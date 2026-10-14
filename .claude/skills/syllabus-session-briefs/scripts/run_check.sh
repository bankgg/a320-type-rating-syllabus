#!/bin/sh
# Usage: run_check.sh <session-id> [out-dir]
# Runs check_session.py with Playwright + the cached headless Chromium.
# Chromium needs libasound.so.2; it is fetched once without root into ../cache/libs.
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
LD_LIBRARY_PATH="$LIBS/root/usr/lib/x86_64-linux-gnu" UV_CACHE_DIR=${UV_CACHE_DIR:-/tmp/claude-1000/uv-cache} \
  uv run --no-project --with playwright python "$HERE/check_session.py" "$SID" "$OUT"
