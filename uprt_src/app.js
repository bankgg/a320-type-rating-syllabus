(() => {
  'use strict';
  const doc = document;
  const DATA = JSON.parse(doc.getElementById('uprt-data').textContent);
  const SOURCES = DATA.sources;
  const EXERCISES = DATA.exercises;

  // ---------------------------------------------------------------- model
  // Keyframed storyboards, not a flight simulator. Pitch (or flight path),
  // bank and IAS are authored; load factor, angle of attack, flight path,
  // altitude and heading are derived so the PFD stays coherent.
  const HZ = 30;
  const G = 9.80665, KT = 0.514444, DEG = Math.PI / 180;
  const K_ALPHA = 324000;            // deg·kt² per g at 64.5 t (illustrative fit)
  const CONF = {                     // a0 = zero-lift AoA; vs = 1 g stall speed (kt)
    clean: { a0: -1.9, vs: 149.3, vls: 1.28, vfe: null, lever: '0' },
    '1+F': { a0: -4.8, vs: 120.7, vls: 1.13, vfe: 215, lever: '1' },
    '3': { a0: -7.4, vs: 111.9, vls: 1.23, vfe: 185, lever: '3' },
    full: { a0: -8.5, vs: 109.3, vls: 1.23, vfe: 177, lever: 'FULL' },
  };
  // Angle-of-attack limits in degrees above the zero-lift AoA, at low Mach (illustrative): stall warning at 1.03 VS1g,
  // stall at VS1g, buffet between them, alpha prot and alpha max at 1.11 and 1.04 VS1g. VS1g is taken as an EAS.
  for (const c of Object.values(CONF)) {
    c.sw = K_ALPHA / Math.pow(1.03 * c.vs, 2);
    c.stall = K_ALPHA / (c.vs * c.vs);
    c.buf = c.sw + 0.6 * (c.stall - c.sw);
    c.prot = K_ALPHA / Math.pow(1.11 * c.vs, 2);
    c.max = K_ALPHA / Math.pow(1.04 * c.vs, 2);
  }
  // Mach effect (illustrative; the books give no values). Above M .45 buffet and stall come at a lower angle of attack.
  // There the stall warning is set at 1.01 times the buffet angle of attack, so the buffet comes just before it (FCTM
  // PR-AEP-MISC P 26/32: the warnings are set close to the buffet; for some Mach numbers the buffet may come just
  // before them). Alpha prot falls with Mach and protects from the buffet boundary at high level (FCOM DSC-27-20-10-20
  // P 10/14). Fitted so that at FL370 and 64.5 t the buffet margin is 0.3 g at M .78 (REC MAX, PDP), and 0.2 g (VLS)
  // about 10 kt below green dot.
  const MACH_FALL = [[0.45, 1], [0.58, 0.725], [0.68, 0.633], [0.78, 0.52], [0.82, 0.47], [0.9, 0.4]];
  function machFactor(m) {
    const k = MACH_FALL;
    if (m <= k[0][0]) return 1;
    for (let i = 1; i < k.length; i++) {
      if (m <= k[i][0]) return k[i - 1][1] + (k[i][1] - k[i - 1][1]) * (m - k[i - 1][0]) / (k[i][0] - k[i - 1][0]);
    }
    return k[k.length - 1][1];
  }
  function limits(c, m) {
    const r = machFactor(m), buf = c.buf * r, prot = Math.min(c.prot, 0.97 * buf);
    return { buf, prot, max: Math.min(c.max, prot + (c.max - c.prot) * r), sw: Math.min(c.sw, 1.01 * buf), stall: Math.min(c.stall, 1.1 * buf) };
  }
  const GREEN_DOT = 209, S_SPEED = 192.6, F_SPEED = 148.5;   // QRH OPS.02B at 64.5 t
  const VMO = 350, MMO = 0.82, VLE = 280;

  function isa(h) { const th = 1 - 6.8756e-6 * h; return { th, d: Math.pow(th, 5.2559) }; }
  // Lift and drag use the true dynamic pressure, so speeds from the angle of attack are EAS: EAS = Mach × easFactor.
  function easFactor(h) { return 661.47 * Math.sqrt(isa(h).d); }
  function easToCas(eas, h) { return machToCas(eas / easFactor(h), h); }
  function casToMach(cas, h) {
    const qc = Math.pow(1 + 0.2 * Math.pow(cas / 661.47, 2), 3.5) - 1;
    return Math.sqrt(5 * (Math.pow(qc / isa(h).d + 1, 2 / 7) - 1));
  }
  function machToTas(m, h) { return m * 661.47 * Math.sqrt(isa(h).th); }
  function machToCas(m, h) {
    const qc = isa(h).d * (Math.pow(1 + 0.2 * m * m, 3.5) - 1);
    return 661.47 * Math.sqrt(5 * (Math.pow(qc + 1, 2 / 7) - 1));
  }
  function tasToCas(tas, h) { return machToCas(tas / (661.47 * Math.sqrt(isa(h).th)), h); }

  // Point-mass model for parts with mode "physics" (the nose-low upsets): load factor,
  // bank and thrust are flown; speed, flight path, heading and altitude follow from
  // gamma' = g/V (n cos(bank) - cos(gamma)) and V' = (T - D)/m - g sin(gamma).
  // Drag and thrust values are illustrative; the entry thrust balances the entry drag.
  const MASS = 64500, WING = 122.6, RHO0 = 1.225, K_IND = 0.045;
  const CD0 = { clean: 0.024, '1+F': 0.04, '3': 0.06, full: 0.085 };
  const CD_GEAR = 0.02, CD_SPDBRK = 0.035;
  function thrustFrac(v) {            // lever position -> share of climb thrust
    v = Math.max(0, Math.min(2, v));
    return v <= 1 ? 0.06 + 0.94 * v : v <= 1.5 ? 1 + (v - 1) * 0.3 : 1.15 + (v - 1.5) * 0.3;
  }
  function n1For(f) { return f <= 1 ? 30 + (f - 0.06) / 0.94 * 56 : 86 + (f - 1) / 0.3 * 8; }
  // EPR from the thrust share, for the beta target rule only: idle 1.0 and CL 1.30 are assumed (the books give no EPR
  // values; user decision: CL EPR above 1.25).
  function eprFor(f) { return 1 + 0.3 * (f - 0.06) / 0.94; }
  function dragCoef(conf, gear, spdbrk, cl) {
    return (CD0[conf] || 0.04) + (gear === 'down' ? CD_GEAR : 0) + CD_SPDBRK * spdbrk + K_IND * cl * cl;
  }
  // Drag rise near the buffet boundary at high Mach (illustrative). It puts the minimum drag speed at green dot at
  // FL370, so below green dot the drag rises as the speed falls (PDP power-drag curve; FCTM PR-NP-SOP-150 P 6/10).
  const CL_DEG = MASS * G / (0.5 * RHO0 * KT * KT * WING * K_ALPHA), SEP = 0.15;
  function sepDrag(m, cl, lim) {
    const w = Math.max(0, Math.min(1, (m - 0.5) / 0.15)), x = cl - 0.75 * CL_DEG * lim.buf;
    return x > 0 ? w * SEP * x * x : 0;
  }

  // Monotone cubic (Fritsch-Carlson): smooth, never overshoots a keyframe.
  function track(keys) {
    const n = keys.length, x = keys.map(k => k[0]), y = keys.map(k => k[1]);
    const d = [], m = [];
    for (let i = 0; i < n - 1; i++) d[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i]);
    m[0] = d[0]; m[n - 1] = d[n - 2];
    for (let i = 1; i < n - 1; i++) m[i] = d[i - 1] * d[i] <= 0 ? 0 : (d[i - 1] + d[i]) / 2;
    for (let i = 0; i < n - 1; i++) {
      if (d[i] === 0) { m[i] = 0; m[i + 1] = 0; continue; }
      const a = m[i] / d[i], b = m[i + 1] / d[i], s = a * a + b * b;
      if (s > 9) { const k = 3 / Math.sqrt(s); m[i] = k * a * d[i]; m[i + 1] = k * b * d[i]; }
    }
    let seg = 0;
    return {
      x0: x[0], x1: x[n - 1],
      at(t) {
        if (t <= x[0]) return y[0];
        if (t >= x[n - 1]) return y[n - 1];
        if (t < x[seg] || t > x[seg + 1]) { seg = 0; while (seg < n - 2 && t > x[seg + 1]) seg++; }
        const h = x[seg + 1] - x[seg], s = (t - x[seg]) / h, s2 = s * s, s3 = s2 * s;
        return (2 * s3 - 3 * s2 + 1) * y[seg] + (s3 - 2 * s2 + s) * h * m[seg]
          + (-2 * s3 + 3 * s2) * y[seg + 1] + (s3 - s2) * h * m[seg + 1];
      },
    };
  }

  // Velocity direction from attitude, AoA and sideslip (body to NED, heading 0).
  function pathAngles(pitch, bank, alpha, beta) {
    const st = Math.sin(pitch * DEG), ct = Math.cos(pitch * DEG);
    const sp = Math.sin(bank * DEG), cp = Math.cos(bank * DEG);
    const vx = Math.cos(alpha * DEG) * Math.cos(beta * DEG), vy = Math.sin(beta * DEG);
    const vz = Math.sin(alpha * DEG) * Math.cos(beta * DEG);
    const ex = ct * vx + sp * st * vy + cp * st * vz;
    const ey = cp * vy - sp * vz;
    const ez = -st * vx + sp * ct * vy + cp * ct * vz;
    return { gamma: Math.asin(Math.max(-1, Math.min(1, -ez))) / DEG, drift: Math.atan2(ey, ex) / DEG };
  }
  // Pitch attitude that gives flight path gamma (inverse of pathAngles).
  function pitchFor(gamma, bank, alpha, beta) {
    const a = Math.cos(alpha * DEG) * Math.cos(beta * DEG);
    const b = Math.sin(bank * DEG) * Math.sin(beta * DEG) + Math.cos(bank * DEG) * Math.sin(alpha * DEG) * Math.cos(beta * DEG);
    const r = Math.hypot(a, b);
    return (Math.atan2(b, a) + Math.asin(Math.max(-1, Math.min(1, Math.sin(gamma * DEG) / r)))) / DEG;
  }
  function overrideWeight(tr, t) {
    if (t < tr.x0) return Math.max(0, 1 - (tr.x0 - t) / 0.6);
    if (t > tr.x1) return Math.max(0, 1 - (t - tr.x1) / 0.6);
    return 1;
  }

  const DEFAULT_STATE = {
    law: 'normal', conf: 'clean', gear: 'up', flaps: '0', ap: '', fd: false, athr: 'off', bird: true,
    spd_target: null, alt_target: null, hdg_target: null, baro: '', active: 'none', mw: false, mc: false, pb: null, fma: null,
    adc: 3, thr_max: null, thr_cmd: null, ewd: null, ils: null,
  };

  function compile(part, mirror) {
    const dur = part.duration, N = Math.round(dur * HZ) + 1, dt = 1 / HZ;
    const sg = mirror ? -1 : 1;
    const T = {};
    for (const k of Object.keys(part.tracks)) T[k] = track(part.tracks[k]);
    const val = (k, t, def) => (T[k] ? T[k].at(t) : def);
    const rate = (k, t) => (T[k].at(t + 0.05) - T[k].at(t - 0.05)) / 0.1;
    const eng = (a, b) => (mirror ? [b, a] : [a, b]);
    const events = (part.events || []).slice().sort((a, b) => a.t - b.t);
    const st = Object.assign({}, DEFAULT_STATE, part.init);
    // trk is the direction of flight, turned by the bank; the heading is the track less the drift, so a
    // sideslip (rudder) moves the nose before the flight path (FCOM DSC-31-40 P 35/54: drift = track - heading).
    let ev = 0, alt = st.alt, trk = st.hdg, gam = 0;
    const mem = { dc: false, trend: false, mach: false, stall: false, gOut: 0, gUntil: -1, bank: false, abn: false, abnDone: false };
    const phys = part.mode === 'physics';
    // ILS raw data (init.ils): distance to the touchdown point and lateral offset from the course, in NM.
    const ils = st.ils;
    let dIls = ils ? ils.dme : 0, yIls = 0;
    // Thrust: share of climb thrust from the lever (or from thr_cmd, the A.FLOOR / TOGA LK thrust, whatever the
    // levers), capped by thr_max where MCT is all the thrust available (high level, FCTM PR-NP-SOP-150 P 5-6/10).
    const thrust = v => Math.min(thrustFrac(st.thr_cmd != null ? st.thr_cmd : v), st.thr_max || Infinity);
    let V = 0, gp = 0, fl1 = 0, fl2 = 0, tcl = 0, iasPrev = null, iasRateF = 0;
    if (phys) {
      const m0 = casToMach(st.ias, alt), lim0 = limits(CONF[st.conf], m0);
      V = machToTas(m0, alt) * KT;
      gp = (st.gamma || 0) * DEG;
      const n0 = val('n', 0, 1), q0 = 0.5 * RHO0 * Math.pow(m0 * easFactor(alt) * KT, 2), cl0 = n0 * MASS * G / (q0 * WING);
      fl1 = thrust(val('tl1', 0, 0)); fl2 = thrust(val('tl2', 0, 0));
      const cd0 = dragCoef(st.conf, st.gear, val('spdbrk', 0, 0), cl0) + sepDrag(m0, cl0, lim0);
      tcl = (q0 * WING * cd0 + MASS * G * Math.sin(gp)) / ((fl1 + fl2) / 2);
    }
    const frames = new Array(N);
    for (let i = 0; i < N; i++) {
      const t = Math.min(i * dt, dur);
      const sounds = [];
      while (ev < events.length && events[ev].t <= t + 1e-9) {
        const e = events[ev++];
        if (e.set) Object.assign(st, e.set);
        if (e.sound) sounds.push(e.sound);
      }
      const conf = CONF[st.conf];
      const ias = phys ? tasToCas(V / KT, alt) : val('ias', t);
      const bank = sg * val('bank', t, 0);
      const beta = sg * val('beta', t, 0);
      const mach = casToMach(ias, alt);
      const tas = machToTas(mach, alt);
      const Vt = tas * KT;
      const eas = mach * easFactor(alt), e2 = eas * eas;
      const lim = limits(conf, mach);
      const cb = Math.cos(bank * DEG);
      let pitch, gamma, n, alpha, drift;
      if (phys) {
        n = val('n', t);
        alpha = conf.a0 + K_ALPHA * n / e2;
        gamma = gp / DEG;
        pitch = pitchFor(gamma, bank, alpha, beta);
        drift = pathAngles(pitch, bank, alpha, beta).drift;
      } else if (T.gamma) {
        gamma = val('gamma', t);
        n = (Vt * rate('gamma', t) * DEG / G + Math.cos(gamma * DEG)) / Math.max(cb, 0.2);
        alpha = conf.a0 + K_ALPHA * n / e2;
        pitch = pitchFor(gamma, bank, alpha, beta);
        drift = pathAngles(pitch, bank, alpha, beta).drift;
      } else {
        pitch = val('pitch', t);
        const nf = (Vt * rate('pitch', t) * DEG / G + Math.cos(gam * DEG)) / Math.max(cb, 0.35);
        n = nf;
        if (T.n) { const w = overrideWeight(T.n, t); if (w > 0) n = w * T.n.at(t) + (1 - w) * nf; }
        alpha = T.alpha && t >= T.alpha.x0 && t <= T.alpha.x1 ? T.alpha.at(t) : conf.a0 + K_ALPHA * n / e2;
        const pa = pathAngles(pitch, bank, alpha, beta);
        gamma = pa.gamma; drift = pa.drift;
      }
      gam = gamma;
      const vs = tas * 101.2686 * Math.sin(gamma * DEG);      // kt -> ft/min
      let iasRate;
      if (phys) {
        if (iasPrev !== null) iasRateF += ((ias - iasPrev) / dt - iasRateF) * Math.min(1, dt / 0.5);
        iasPrev = ias; iasRate = iasRateF;
      } else iasRate = (T.ias.at(t + 0.25) - T.ias.at(t - 0.25)) / 0.5;

      // Display rules (cited in DATA.rules); hysteresis kept in mem.
      const ab = Math.abs(bank);
      if (!mem.dc && (ab > 45 || pitch > 25 || pitch < -13)) mem.dc = true;
      else if (mem.dc && ab < 40 && pitch < 22 && pitch > -10) mem.dc = false;
      const trend = iasRate * 10;
      if (!mem.trend && Math.abs(trend) >= 2) mem.trend = true;
      else if (mem.trend && Math.abs(trend) < 1) mem.trend = false;
      if (!mem.mach && mach >= 0.5) mem.mach = true; else if (mem.mach && mach < 0.45) mem.mach = false;
      // Abnormal attitude law (FCOM DSC-27-20-20 P 18/20): 40° up / 20° down with fewer than two
      // valid ADCs, else 50° / 30°; bank 125°; AoA 40°; 440 kt; M .91. It hands back once the
      // aircraft is inside these values again (assumed: the books give none; user decision).
      const [upLim, dnLim] = st.adc >= 2 ? [50, -30] : [40, -20];
      const beyond = pitch > upLim || pitch < dnLim || ab > 125 || alpha > 40 || ias > 440 || mach > 0.91;
      if (!mem.abn && beyond) { mem.abn = true; sounds.push('chime'); }
      // Disengaged, it leaves pitch ALTN without reduced protection, roll direct, yaw ALTN and
      // F/CTL ALTN LAW on the ECAM for the rest of the flight (FCOM DSC-27-20-20 P 18/20). That is a new
      // amber caution: single chime and MASTER CAUT again (FCOM DSC-31-10 P 4/16; user decision).
      else if (mem.abn && !beyond) { mem.abn = false; mem.abnDone = true; if (st.law === 'normal') st.law = 'altn'; sounds.push('chime'); }
      const law = mem.abn ? 'abnormal' : st.law;
      const bankBank = law !== 'normal' && ab > 45;
      if (bankBank && !mem.bank) sounds.push('bank');
      mem.bank = bankBank;
      if (law !== 'normal') {
        const aSw = conf.a0 + lim.sw;
        if (!mem.stall && alpha > aSw) { mem.stall = true; sounds.push('stall'); }
        else if (mem.stall && alpha < aSw - 0.3) mem.stall = false;
      } else mem.stall = false;
      // OVERSPEED, a level 3 warning: CRC and MASTER WARN (FCOM PRO-ABN-OVERSPEED P 1/2; FCOM DSC-31-10 P 4/16; PDP).
      const over = ias > VMO + 4 || mach > MMO + 0.006 || (st.gear === 'down' && ias > VLE + 4) || (conf.vfe != null && ias > conf.vfe + 4);
      const gOut = n > 1.4 || n < 0.7;
      mem.gOut = gOut ? mem.gOut + dt : 0;
      // Shown after 2 s outside 0.7-1.4 g; it stays 5 s after the excessive load ends, so a new excess while
      // it is shown keeps it on (FCOM DSC-31-20 P 7/10).
      if (mem.gOut > 2 || (gOut && t <= mem.gUntil)) mem.gUntil = t + 5;
      const gload = t <= mem.gUntil;

      // FD bars with HDG V/S as the basic reference (FCOM DSC-31-40 P 37/54); they disappear beyond 45° of bank, 25° up
      // or 13° down (FCOM DSC-22_30-20-40 P 1/2), drawn with the declutter. The orders are illustrative:
      // bank towards the selected heading, flight path towards the selected altitude; +1 = full scale.
      let fdRoll = 0, fdPitch = 0;
      if (st.fd && !st.bird) {
        const hErr = ((((st.hdg_target ?? st.hdg) - (trk - drift)) % 360) + 540) % 360 - 180;
        const bankCmd = Math.max(-25, Math.min(25, 2 * hErr));
        const gCmd = st.alt_target == null ? 0 : Math.max(-3, Math.min(3, (st.alt_target - alt) / 100));
        fdRoll = Math.max(-1, Math.min(1, (bankCmd - bank) / 15));
        // SRS (st.fd_spd): pitch for the speed target, so a slow aircraft gets a nose-down order (FCOM DSC-22_30-60-20
        // P 2/6; FCTM PR-AEP-ENG P 11/26). The gain is illustrative.
        fdPitch = st.fd_spd != null ? Math.max(-1, Math.min(1, (ias - st.fd_spd) / 8))
          : Math.max(-1, Math.min(1, (gCmd - gamma) / 4));
      }
      // Speed scale: the speed at which this load factor would reach each angle-of-attack limit (FCOM DSC-27-20-10-20
      // P 10/14), as CAS. Above 20 000 ft VLS keeps a 0.2 g buffet margin (FCOM DSC-22_10-50-20 P 4/6).
      const nn = Math.max(n, 0.3), vAt = (relAoA, g) => easToCas(Math.sqrt(K_ALPHA * g / relAoA), alt);
      let vls = easToCas(conf.vls * conf.vs, alt);
      if (alt > 20000) vls = Math.max(vls, vAt(lim.buf, 1.2));
      const vmo = Math.min(VMO, machToCas(MMO, alt));
      let vmax = vmo;
      if (st.gear === 'down') vmax = Math.min(vmax, VLE);
      if (conf.vfe) vmax = Math.min(vmax, conf.vfe);
      const [tl1, tl2] = eng(val('tl1', t, 0), val('tl2', t, 0));
      let [n11, n12] = eng(val('n1_1', t, 0), val('n1_2', t, 0));
      if (phys && !T.n1_1) [n11, n12] = eng(n1For(fl1), n1For(fl2));
      // Beta target (FCOM DSC-31-40 P 4/54): CONF 1, 2 or 3, any EPR above 1.25 or a thrust lever beyond MCT, and the
      // two EPRs more than 0.25 apart. The sideslip index then turns blue; centred, the sideslip is the target.
      let btgt = false;
      if (phys && ['1', '2', '3'].includes(conf.lever)) {
        const ep1 = eprFor(fl1), ep2 = eprFor(fl2);
        btgt = (Math.max(ep1, ep2) > 1.25 || tl1 > 1.5 || tl2 > 1.5) && Math.abs(ep1 - ep2) > 0.25;
      }
      // ILS raw data with the LS pushbutton pressed (FCOM DSC-31-40 P 40-41/54): one dot is 0.4° on the glideslope and
      // 0.8° on the localizer. The geometry is illustrative: glideslope and DME from the touchdown point, the localizer
      // antenna 1.5 NM beyond it, the ground at sea level. gs > 0: above the glideslope; loc > 0: right of the course.
      const ilsF = ils ? {
        gs: (Math.atan2(alt, dIls * 6076.12) / DEG - ils.gs) / 0.4, loc: Math.atan2(yIls, dIls + 1.5) / DEG / 0.8,
        dme: dIls, crs: ils.crs, ident: ils.ident, freq: ils.freq,
      } : null;
      // ECAM, by priority: the OVERSPEED warning, then the flight control law cautions, then a memo (A.FLOOR).
      const ecam = over ? { text: 'OVERSPEED', level: 'warn' }
        : mem.abn ? { text: 'F/CTL DIRECT LAW', level: 'caut' } : mem.abnDone ? { text: 'F/CTL ALTN LAW', level: 'caut' }
          : st.ewd ? { text: st.ewd, level: st.ewd_level || 'memo' } : null;
      frames[i] = {
        t, ias, pitch, bank, beta, alpha, n, gamma, drift, alt, hdg: trk - drift, vs, mach, trend, fdRoll, fdPitch,
        law, adc: st.adc, noprot: mem.abnDone, ecam,
        conf: st.conf, gear: st.gear, flaps: st.flaps, ap: st.ap, fd: st.fd, athr: st.athr,
        bird: st.bird, spdTarget: st.spd_target, spdManaged: !!st.spd_managed, altTarget: st.alt_target, baro: st.baro, active: st.active, btgt,
        // MASTER WARN flashes with the stall and overspeed warnings (PDP; FCOM DSC-31-10 P 4/16; user decision).
        // Nobody presses MASTER CAUT in these demonstrations, so it stays lit.
        mw: st.mw || mem.stall || over, mc: st.mc || mem.abn || mem.abnDone, pb: st.pb, fma: st.fma,
        dc: mem.dc, showTrend: mem.trend, showMach: mem.mach, bankBank, stall: mem.stall, overspeed: over,
        buffet: alpha > conf.a0 + lim.buf, gload,
        vls, vsw: vAt(lim.sw, nn), vaprot: vAt(lim.prot, nn), vamax: vAt(lim.max, nn),
        // Speed protection symbol: where high speed protection becomes active (FCOM DSC-31-40 P 13/54).
        vhsp: Math.min(VMO + 6, machToCas(MMO + 0.01, alt)),
        vmax, greenDot: st.conf === 'clean' ? GREEN_DOT + Math.max(0, (alt - 20000) / 1000) : null,
        sSpeed: CONF[st.conf].lever === '1' ? S_SPEED : null,
        fSpeed: (st.flaps === '2' || st.flaps === '3') ? F_SPEED : null,
        capt: [sg * val('capt_x', t, 0), val('capt_y', t, 0)],
        fo: [sg * val('fo_x', t, 0), val('fo_y', t, 0)],
        rud: sg * val('rud', t, 0), tl1, tl2, n11, n12, trim: val('trim', t, 0), spdbrk: val('spdbrk', t, 0),
        // Radio height below 2 500 ft (FCOM DSC-31-40 P 32/54); the ground is taken at sea level (illustrative).
        ils: ilsF, ra: alt < 2500 ? alt : null,
        sounds,
      };
      alt += vs / 60 * dt;
      if (ils) {
        const dn = tas / 3600 * dt, rel = (trk - ils.crs) * DEG;
        dIls -= dn * Math.cos(rel); yIls += dn * Math.sin(rel);
      }
      trk += G * n * Math.sin(bank * DEG) / (Vt * Math.max(Math.cos(gamma * DEG), 0.2)) / DEG * dt;
      if (phys) {
        const lag = Math.min(1, dt / 1.5);                  // engine spool-up, illustrative
        fl1 += (thrust(val('tl1', t, 0)) - fl1) * lag;
        fl2 += (thrust(val('tl2', t, 0)) - fl2) * lag;
        const q = 0.5 * RHO0 * Math.pow(eas * KT, 2), cl = n * MASS * G / (q * WING);
        const drag = q * WING * (dragCoef(st.conf, st.gear, val('spdbrk', t, 0), cl) + sepDrag(mach, cl, lim));
        V += ((tcl * (fl1 + fl2) / 2 - drag) / MASS - G * Math.sin(gp)) * dt;
        gp += G / V * (n * cb - Math.cos(gp)) * dt;
        // A tailwind that grows takes the same amount off the airspeed (the wind shear of row 12).
        if (T.wind) V -= (T.wind.at(t + dt) - T.wind.at(t)) * KT;
      }
    }
    return frames;
  }

  // ------------------------------------------------------------ PFD drawing
  const PK = 5, SK = 3.15, AK = 0.238, HK = 4.8;   // units per degree / kt / ft / heading degree
  const CX = 214, CY = 243;
  // ILS scales: one dot = 45 units, so two dots end about where the FCOM figures draw them (DSC-31-40 P 40-41/54).
  const DOT = 45, GSX = 350, LOCY = 410;
  const COL = {
    sky: '#3c5c9b', ground: '#5a3c14', tape: '#4b4f56', white: '#fff', green: '#3ce05c',
    cyan: '#2fdcff', amber: '#ff9d1c', red: '#ff3b30', yellow: '#ffe11a', magenta: '#ff5cf0',
  };
  const NS = 'http://www.w3.org/2000/svg';
  const fmt = (v, d = 0) => v.toFixed(d);

  function ladderSVG() {
    let s = `<svg viewBox="-400 -400 800 800" width="800" height="800">`
      + `<rect x="-400" y="-400" width="800" height="400" fill="${COL.sky}"/>`
      + `<rect x="-400" y="0" width="800" height="400" fill="${COL.ground}"/>`
      + `<line x1="-400" y1="0" x2="400" y2="0" stroke="#fff" stroke-width="2"/>`;
    for (let q = -32; q <= 32; q++) {
      const p = q * 2.5;
      if (p === 0) continue;
      const ten = q % 4 === 0, five = q % 2 === 0;
      if (!(p >= -10 && p <= 30) && !ten) continue;
      const y = -p * PK, hw = ten ? 30 : five ? 16 : 8;
      s += `<line x1="${-hw}" y1="${y}" x2="${hw}" y2="${y}" stroke="#fff" stroke-width="2"/>`;
      if (ten) {
        for (const x of [-50, 50]) {
          s += `<text x="${x}" y="${y + 7}" fill="#fff" font-size="19" text-anchor="middle">${Math.abs(p)}</text>`;
        }
      }
    }
    // Pitch protection symbols: green = at 30 up / 15 down, amber x when lost.
    for (const [p, x] of [[30, 37], [-15, 23]]) {
      const y = -p * PK;
      for (const sx of [-x, x]) {
        s += `<g class="prot-ok" stroke="${COL.green}" stroke-width="2.4"><line x1="${sx - 5}" y1="${y - 3}" x2="${sx + 5}" y2="${y - 3}"/><line x1="${sx - 5}" y1="${y + 3}" x2="${sx + 5}" y2="${y + 3}"/></g>`
          + `<g class="prot-lost" stroke="${COL.amber}" stroke-width="2.4"><line x1="${sx - 5}" y1="${y - 5}" x2="${sx + 5}" y2="${y + 5}"/><line x1="${sx - 5}" y1="${y + 5}" x2="${sx + 5}" y2="${y - 5}"/></g>`;
      }
    }
    // Red arrowheads beyond 30°, pointing back to the horizon (positions illustrative).
    const chevron = (y, dir) => `<path d="M-26 ${y - 14 * dir} L0 ${y + 8 * dir} L26 ${y - 14 * dir} L26 ${y - 3 * dir} L0 ${y + 19 * dir} L-26 ${y - 3 * dir} Z" fill="#000" stroke="${COL.red}" stroke-width="3" stroke-linejoin="round"/>`;
    s += '<g class="arrows-up">';
    for (const p of [35, 45, 55, 65, 75]) s += chevron(-p * PK, 1);
    s += '</g><g class="arrows-down">';
    for (const p of [-35, -45, -55, -65, -75]) s += chevron(-p * PK, -1);
    s += '</g></svg>';
    return s;
  }

  function maskPath() {
    const h = Math.sqrt(135 * 135 - 117 * 117);
    return `M0 0H500V500H0Z M97 ${CY - h} A135 135 0 0 1 331 ${CY - h} L331 ${CY + h} A135 135 0 0 1 97 ${CY + h} Z`;
  }

  function staticSVG() {
    let s = `<svg viewBox="0 0 500 500" width="500" height="500">`
      + `<path d="${maskPath()}" fill="#000" fill-rule="evenodd"/>`;
    // FMA dividers: columns 1|2 and 2|3 cover lines 1-2 only; line 3 there is for special messages (FCOM DSC-22_30-80-20 P 1/36).
    // They go with the rest of the FMA when the PFD declutters (FCOM DSC-31-40 P 3/54).
    s += '<g class="dc">' + [[109, 44], [211, 44], [322, 66], [418, 66]].map(([x, y2]) => `<line x1="${x}" y1="4" x2="${x}" y2="${y2}" stroke="#fff" stroke-width="2"/>`).join('') + '</g>';
    // Roll scale, all white: a triangle at 0 and markers at 10, 20, 30 and 45 (FCOM DSC-31-40 P 3/54).
    for (const a of [-45, -30, -20, -10, 10, 20, 30, 45]) {
      const r2 = Math.abs(a) === 45 ? 152 : Math.abs(a) === 30 ? 150 : 146;
      const sx = Math.sin(a * DEG), cy = -Math.cos(a * DEG);
      s += `<line x1="${fmt(CX + 137 * sx, 1)}" y1="${fmt(CY + 137 * cy, 1)}" x2="${fmt(CX + r2 * sx, 1)}" y2="${fmt(CY + r2 * cy, 1)}" stroke="#fff" stroke-width="2.6"/>`;
    }
    s += `<path d="M205 92 L223 92 L214 106 Z" fill="#fff"/>`;
    // Bank angle protection symbols at 67° on the sphere edge.
    const yb = CY - 117 / Math.tan(67 * DEG);
    for (const x of [97, 331]) {
      const dir = x < CX ? -1 : 1;
      s += `<g class="prot-ok" stroke="${COL.green}" stroke-width="2.4" transform="translate(${x} ${fmt(yb, 1)}) rotate(${dir * 67})"><line x1="-6" y1="-3" x2="6" y2="-3"/><line x1="-6" y1="3" x2="6" y2="3"/></g>`
        + `<g class="prot-lost" stroke="${COL.amber}" stroke-width="2.4" transform="translate(${x} ${fmt(yb, 1)})"><line x1="-6" y1="-6" x2="6" y2="6"/><line x1="-6" y1="6" x2="6" y2="-6"/></g>`;
    }
    // Speed and altitude tape fields, heading field, V/S field.
    s += `<rect x="9" y="110" width="54" height="270" fill="${COL.tape}"/>`
      + `<line x1="9" y1="110" x2="72" y2="110" stroke="#fff" stroke-width="2"/><line x1="9" y1="380" x2="72" y2="380" stroke="#fff" stroke-width="2"/>`
      + `<rect x="383" y="110" width="62" height="270" fill="${COL.tape}"/>`
      + `<line x1="383" y1="110" x2="445" y2="110" stroke="#fff" stroke-width="2"/><line x1="383" y1="380" x2="445" y2="380" stroke="#fff" stroke-width="2"/>`
      + `<rect x="105" y="445" width="218" height="35" fill="${COL.tape}"/>`
      + `<path d="M465 92 L490 92 L498 120 L498 366 L490 394 L465 394 Z" fill="${COL.tape}"/>`;
    for (const [v, lab] of [[500, ''], [1000, '1'], [1500, ''], [2000, '2'], [6000, '6']]) {
      for (const sgn of [-1, 1]) {
        const y = CY + sgn * vsY(v);
        s += `<line x1="${lab ? 478 : 481}" y1="${fmt(y, 1)}" x2="487" y2="${fmt(y, 1)}" stroke="#fff" stroke-width="${lab ? 3 : 2}"/>`;
        if (lab) s += `<text x="472" y="${fmt(y + 6, 1)}" fill="#fff" font-size="17" text-anchor="middle">${lab}</text>`;
      }
    }
    s += `<line x1="470" y1="${CY}" x2="490" y2="${CY}" stroke="${COL.yellow}" stroke-width="3"/>`;
    // Aircraft symbol: black, outlined in yellow.
    s += `<g fill="#000" stroke="${COL.yellow}" stroke-width="2.6" stroke-linejoin="round">`
      + `<path d="M${CX - 112} ${CY - 4} H${CX - 56} V${CY + 18} H${CX - 64} V${CY + 4} H${CX - 112} Z"/>`
      + `<path d="M${CX + 112} ${CY - 4} H${CX + 56} V${CY + 18} H${CX + 64} V${CY + 4} H${CX + 112} Z"/>`
      + `<rect x="${CX - 5}" y="${CY - 5}" width="10" height="10"/></g>`;
    // Speed reference (yellow line and triangle), altitude reference, heading lubber line.
    s += `<line x1="0" y1="${CY}" x2="12" y2="${CY}" stroke="${COL.yellow}" stroke-width="3"/>`
      + `<line x1="52" y1="${CY}" x2="64" y2="${CY}" stroke="${COL.yellow}" stroke-width="3"/>`
      + `<path d="M63 ${CY} L76 ${CY - 7} L76 ${CY + 7} Z" fill="${COL.yellow}"/>`
      + `<line x1="338" y1="${CY}" x2="380" y2="${CY}" stroke="${COL.yellow}" stroke-width="3"/>`
      + `<line x1="${CX}" y1="436" x2="${CX}" y2="458" stroke="${COL.yellow}" stroke-width="3"/>`;
    return s + '</svg>';
  }

  function vsY(v) {                        // non-linear V/S scale, units from centre
    const a = Math.abs(v);
    const pts = [[0, 0], [1000, 84.5], [2000, 116.5], [6000, 151], [9000, 160]];
    for (let i = 1; i < pts.length; i++) {
      if (a <= pts[i][0]) {
        const [x0, y0] = pts[i - 1], [x1, y1] = pts[i];
        return y0 + (y1 - y0) * (a - x0) / (x1 - x0);
      }
    }
    return 160;
  }

  function rollSVG() {
    // Roll index (yellow triangle) and sideslip index (trapezoid) rotate with the horizon.
    return `<svg viewBox="0 0 300 300" width="300" height="300">`
      + `<path d="M150 15 L159 29 L141 29 Z" fill="${COL.yellow}"/>`
      + `<path class="slip" d="M141 31 L159 31 L163 38 L137 38 Z" fill="${COL.yellow}"/></svg>`;
  }

  function fpvSVG() {
    return `<svg viewBox="-30 -30 60 60" width="60" height="60" style="position:absolute;left:-30px;top:-30px">`
      + `<g stroke="${COL.green}" stroke-width="2.6" fill="none"><circle r="7"/><line x1="-23" y1="0" x2="-7" y2="0"/><line x1="7" y1="0" x2="23" y2="0"/><line x1="0" y1="-7" x2="0" y2="-16"/></g></svg>`;
  }

  function horizonTicksSVG() {
    let s = `<svg viewBox="-400 -10 800 20" width="800" height="20" style="position:absolute;left:-400px;top:-10px">`;
    for (let k = -8; k <= 8; k++) s += `<line x1="${k * 10 * PK}" y1="0" x2="${k * 10 * PK}" y2="9" stroke="#fff" stroke-width="2"/>`;
    return s + '</svg>';
  }

  function tapeSVG(kind, lo, hi) {
    let s = '';
    if (kind === 'spd') {
      const h = (hi - lo) * SK;
      s = `<svg width="63" height="${fmt(h)}" viewBox="0 0 63 ${fmt(h)}">`;
      for (let v = Math.ceil(lo / 10) * 10; v <= hi; v += 10) {
        const y = (hi - v) * SK;
        s += `<line x1="43" y1="${fmt(y, 1)}" x2="54" y2="${fmt(y, 1)}" stroke="#fff" stroke-width="2"/>`;
        if (v % 20 === 0 && v >= 30) s += `<text x="39" y="${fmt(y + 7, 1)}" fill="#fff" font-size="20" text-anchor="end">${v}</text>`;
      }
    } else if (kind === 'alt') {
      const h = (hi - lo) * AK;
      s = `<svg width="62" height="${fmt(h)}" viewBox="0 0 62 ${fmt(h)}">`;
      for (let a = Math.ceil(lo / 100) * 100; a <= hi; a += 100) {
        const y = (hi - a) * AK;
        s += `<line x1="50" y1="${fmt(y, 1)}" x2="62" y2="${fmt(y, 1)}" stroke="#fff" stroke-width="2"/>`;
        if (a % 500 === 0) s += `<text x="5" y="${fmt(y + 7, 1)}" fill="#fff" font-size="20">${a / 100}</text>`;
      }
    } else {
      const w = (hi - lo) * HK;
      s = `<svg width="${fmt(w)}" height="35" viewBox="0 0 ${fmt(w)} 35">`;
      for (let hh = Math.ceil(lo / 5) * 5; hh <= hi; hh += 5) {
        const x = (hh - lo) * HK, ten = hh % 10 === 0;
        s += `<line x1="${fmt(x, 1)}" y1="0" x2="${fmt(x, 1)}" y2="${ten ? 9 : 5}" stroke="#fff" stroke-width="2"/>`;
        if (ten) s += `<text x="${fmt(x, 1)}" y="29" fill="#fff" font-size="19" text-anchor="middle">${(((hh / 10) % 36) + 36) % 36}</text>`;
      }
    }
    return s + '</svg>';
  }

  function dynSVG() {
    const t = (cls, x, y, size, fill, anchor = 'middle', extra = '') => `<text class="${cls}" x="${x}" y="${y}" font-size="${size}" fill="${fill}" text-anchor="${anchor}" ${extra}></text>`;
    let s = `<svg viewBox="0 0 500 500" width="500" height="500"><defs>`
      + `<clipPath id="clip-spd"><rect x="0" y="110" width="84" height="270"/></clipPath>`
      + `<clipPath id="clip-vs"><rect x="465" y="88" width="35" height="310"/></clipPath>`
      + `<clipPath id="clip-drum"><rect x="437" y="219" width="20" height="48"/></clipPath>`
      + `<pattern id="pole-red" width="6" height="12" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="${COL.red}"/><rect y="6" width="6" height="6" fill="#000"/></pattern>`
      + `<pattern id="pole-amber" width="6" height="12" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="${COL.amber}"/><rect y="6" width="6" height="6" fill="#000"/></pattern>`
      + `</defs>`
      // FD bars, green (FCOM DSC-31-40 P 37/54); removed with the rest when the PFD declutters.
      + `<g class="fd dc" stroke="${COL.green}" stroke-width="3.2"><line class="fd-roll" x1="${CX}" y1="${CY - 64}" x2="${CX}" y2="${CY + 64}"/>`
      + `<line class="fd-pitch" x1="${CX - 64}" y1="${CY}" x2="${CX + 64}" y2="${CY}"/></g>`
      + `<g clip-path="url(#clip-spd)">`
      + `<rect class="s-vmax" x="57" width="6" fill="url(#pole-red)"/>`
      + `<rect class="s-vls" x="59" width="4" fill="${COL.amber}"/>`
      + `<rect class="s-vaprot" x="57" width="6" fill="url(#pole-amber)"/>`
      + `<rect class="s-vamax" x="57" width="6" fill="${COL.red}"/>`
      + `<rect class="s-vsw" x="57" width="6" fill="url(#pole-red)"/>`
      // Speed protection symbol, a green = at VMO + 6 kt / MMO + 0.01 (FCOM DSC-31-40 P 13/54; PDP high speed protection).
      + `<g class="s-hsp" stroke="${COL.green}" stroke-width="2.4"><line x1="46" x2="56" y1="-3" y2="-3"/><line x1="46" x2="56" y1="3" y2="3"/></g>`
      + `<circle class="s-gd" cx="72" r="5" fill="none" stroke="${COL.green}" stroke-width="2.4"/>`
      + t('s-sf', 74, 0, 18, COL.green, 'start')
      + `<path class="s-target dc" d="M64 0 L76 -8 L76 8 Z" fill="${COL.cyan}"/>`
      + `<g class="s-trend"><line class="s-trend-line" x1="50" x2="50" y1="${CY}" stroke="${COL.yellow}" stroke-width="3"/><path class="s-trend-head" fill="${COL.yellow}"/></g>`
      + `</g>`
      + t('s-target-num dc', 50, 0, 20, COL.cyan)
      + t('s-mach dc', 14, 432, 22, COL.green, 'start')
      // altitude window, drum and targets
      + t('a-target dc', 414, 0, 20, COL.cyan)
      + `<rect class="a-target-mark dc" x="383" width="9" height="16" fill="none" stroke="${COL.cyan}" stroke-width="2.4"/>`
      + `<path d="M383 229 H437 V219 H457 V267 H437 V257 H383 Z" fill="#000" stroke="${COL.yellow}" stroke-width="2.6"/>`
      + t('a-digits', 436, 252, 27, COL.green, 'end')
      + `<g clip-path="url(#clip-drum)"><g class="a-drum">`
      + [0, 1, 2, 3, 4].map(k => t(`a-drum-${k}`, 447, 0, 17, COL.green)).join('')
      + `</g></g>`
      + t('a-baro-label dc', 383, 436, 16, COL.white, 'start')
      + t('a-baro dc', 424, 436, 20, COL.cyan, 'start')
      // V/S needle and digits
      + `<g clip-path="url(#clip-vs)"><line class="v-needle" x1="560" y1="${CY}" x2="466" y2="${CY}" stroke="${COL.green}" stroke-width="3"/></g>`
      + `<g class="v-box"><rect x="466" width="34" height="20" fill="#000"/>${t('v-digits', 483, 0, 17, COL.green)}</g>`
      // heading: track diamond
      + `<path class="h-track dc" d="M0 447 L5 454 L0 461 L-5 454 Z" fill="none" stroke="${COL.green}" stroke-width="2.4"/>`
      // FMA. A.FLOOR and TOGA LK show in column 1, line 1, in a flashing amber box (FCOM DSC-22_30-80-20 P 4/36, P 34/36).
      + `<rect class="f-box dc" x="15" y="4" width="79" height="21" fill="none" stroke="${COL.amber}" stroke-width="2"/>`
      + [54.5, 160, 266.5, 370, 459].map((x, c) => [20, 40, 60].map((y, l) => t(`f-${c}-${l} dc`, x, y, 17, COL.green)).join('')).join('')
      + t('f-trim dc', 215.5, 60, 17, COL.amber)
      // messages
      // STALL STALL is two words, one either side of the centre (FCOM DSC-31-40 P 49/54).
      + `<g class="m-stall">${[-52, 52].map(dx => `<rect x="${CX + dx - 37}" y="172" width="74" height="26" fill="#000"/>`
        + t('', CX + dx, 193, 22, COL.red, 'middle', 'font-weight="600"').replace('></text>', '>STALL</text>')).join('')}</g>`
      // ILS raw data (FCOM DSC-31-40 P 40-41/54): white dots at one and two dots, magenta diamond indexes (half a
      // diamond at the end of the scale beyond two dots), the yellow localizer centre mark, the ILS ident, frequency
      // and DME bottom left, and the magenta course dagger on the heading scale. Removed when the PFD declutters.
      + `<g class="i-ils dc">`
      + [-2, -1, 1, 2].map(k => `<circle cx="${GSX}" cy="${CY + k * DOT}" r="3.2" fill="none" stroke="#fff" stroke-width="1.8"/>` + `<circle cx="${CX + k * DOT}" cy="${LOCY}" r="3.2" fill="none" stroke="#fff" stroke-width="1.8"/>`).join('')
      + `<line x1="${CX}" y1="${LOCY - 12}" x2="${CX}" y2="${LOCY + 12}" stroke="${COL.yellow}" stroke-width="3"/>`
      + `<path class="i-gs" fill="none" stroke="${COL.magenta}" stroke-width="2.4" stroke-linejoin="round"/>`
      + `<path class="i-loc" fill="none" stroke="${COL.magenta}" stroke-width="2.4" stroke-linejoin="round"/>`
      + t('i-id', 14, 422, 18, COL.magenta, 'start') + t('i-freq', 14, 444, 18, COL.magenta, 'start')
      + `<text class="i-dme" x="14" y="466" font-size="18" fill="${COL.magenta}"><tspan class="i-dme-v"></tspan><tspan fill="${COL.cyan}"> NM</tspan></text>`
      + `<path class="i-crs" d="M0 447 V479 M-6 470 H6" fill="none" stroke="${COL.magenta}" stroke-width="2.6"/>`
      + t('i-crs-num', 0, 474, 17, COL.magenta)
      + `</g>`
      // Radio height, green under the attitude sphere (FCOM DSC-31-40 P 32/54; position from P 40/54). A black outline
      // keeps the digits readable over the pitch scale's 15° nose-down marks.
      + t('i-ra dc', CX, 371, 24, COL.green, 'middle', 'stroke="#000" stroke-width="5" stroke-linejoin="round" paint-order="stroke"')
      + `<g class="m-bank"><rect x="140" y="312" width="148" height="26" fill="#000"/>${t('', CX, 333, 22, COL.red, 'middle', 'font-weight="600"').replace('></text>', '>BANK  BANK</text>')}</g>`
      + '</svg>';
    return s;
  }

  function el(tag, cls, html) {
    const e = doc.createElement(tag);
    if (cls) e.className = cls;
    if (html) e.innerHTML = html;
    return e;
  }

  function buildPFD(root) {
    root.innerHTML = '';
    const att = el('div', 'pfd-att', ladderSVG());
    const mark = el('div', 'pfd-mark');
    const ticks = el('div', 'dc', horizonTicksSVG());
    ticks.style.position = 'absolute';
    const fpv = el('div', 'dc', fpvSVG());
    fpv.style.position = 'absolute';
    mark.append(ticks, fpv);
    att.append(mark);
    const roll = el('div', 'pfd-roll', rollSVG());
    const stat = el('div', 'pfd-layer', staticSVG());
    const spdWin = el('div', 'pfd-win');
    Object.assign(spdWin.style, { left: '9px', top: '110px', width: '63px', height: '270px' });
    const spdTape = el('div', 'pfd-tape');
    spdWin.append(spdTape);
    const altWin = el('div', 'pfd-win');
    Object.assign(altWin.style, { left: '383px', top: '110px', width: '62px', height: '270px' });
    const altTape = el('div', 'pfd-tape');
    altWin.append(altTape);
    const hdgWin = el('div', 'pfd-win');
    Object.assign(hdgWin.style, { left: '105px', top: '445px', width: '218px', height: '35px' });
    const hdgTape = el('div', 'pfd-tape');
    hdgWin.append(hdgTape);
    const dyn = el('div', 'pfd-layer', dynSVG());
    root.append(att, roll, stat, spdWin, altWin, hdgWin, dyn);
    const q = sel => dyn.querySelector(sel);
    const P = {
      root, att, mark, ticks, fpv, roll, slip: roll.querySelector('.slip'), spdTape, altTape, hdgTape,
      vmax: q('.s-vmax'), vls: q('.s-vls'), vaprot: q('.s-vaprot'), vamax: q('.s-vamax'), vsw: q('.s-vsw'), hsp: q('.s-hsp'), fBox: q('.f-box'),
      gd: q('.s-gd'), sf: q('.s-sf'), target: q('.s-target'), targetNum: q('.s-target-num'), mach: q('.s-mach'),
      trend: q('.s-trend'), trendLine: q('.s-trend-line'), trendHead: q('.s-trend-head'),
      aTarget: q('.a-target'), aTargetMark: q('.a-target-mark'), aDigits: q('.a-digits'), aDrum: q('.a-drum'),
      drum: [0, 1, 2, 3, 4].map(k => q(`.a-drum-${k}`)), baroLabel: q('.a-baro-label'), baro: q('.a-baro'),
      needle: q('.v-needle'), vBox: q('.v-box'), vDigits: q('.v-digits'), track: q('.h-track'),
      fd: q('.fd'), fdRoll: q('.fd-roll'), fdPitch: q('.fd-pitch'),
      fma: [0, 1, 2, 3, 4].map(c => [0, 1, 2].map(l => q(`.f-${c}-${l}`))), fTrim: q('.f-trim'),
      mStall: q('.m-stall'), mBank: q('.m-bank'), ranges: null,
      ils: q('.i-ils'), iGs: q('.i-gs'), iLoc: q('.i-loc'), iId: q('.i-id'), iFreq: q('.i-freq'), iDme: q('.i-dme-v'),
      iCrs: q('.i-crs'), iCrsNum: q('.i-crs-num'), ra: q('.i-ra'),
    };
    return P;
  }

  const cache = new WeakMap();
  function setA(e, name, v) {
    let c = cache.get(e);
    if (!c) { c = {}; cache.set(e, c); }
    if (c[name] !== v) { c[name] = v; e.setAttribute(name, v); }
  }
  function setT(e, v) {
    let c = cache.get(e);
    if (!c) { c = {}; cache.set(e, c); }
    if (c.$t !== v) { c.$t = v; e.textContent = v; }
  }
  function show(e, on) {
    let c = cache.get(e);
    if (!c) { c = {}; cache.set(e, c); }
    if (c.$s !== on) { c.$s = on; e.style.display = on ? '' : 'none'; }
  }
  function setHidden(e, v) {
    let c = cache.get(e);
    if (!c) { c = {}; cache.set(e, c); }
    if (c.$h !== v) { c.$h = v; e.hidden = v; }
  }
  function setStyle(e, prop, v) {
    let c = cache.get(e);
    if (!c) { c = {}; cache.set(e, c); }
    const k = '$' + prop;
    if (c[k] !== v) { c[k] = v; e.style[prop] = v; }
  }

  // "g:ALT" -> green ALT; "c:" cyan, "w:" white, "a:" amber, "m:" magenta. A trailing [] draws the flashing amber box.
  function fmaText(spec) {
    if (!spec) return ['', COL.green, false];
    const boxed = spec.endsWith('[]');
    if (boxed) spec = spec.slice(0, -2);
    const m = /^([gcwarm]):(.*)$/.exec(spec);
    if (!m) return [spec, COL.green, boxed];
    return [m[2], { g: COL.green, c: COL.cyan, w: COL.white, a: COL.amber, r: COL.red, m: COL.magenta }[m[1]], boxed];
  }

  function prepareTapes(P, frames) {
    let sLo = 1e9, sHi = -1e9, aLo = 1e9, aHi = -1e9, hLo = 1e9, hHi = -1e9;
    for (const f of frames) {
      sLo = Math.min(sLo, f.ias); sHi = Math.max(sHi, f.ias);
      aLo = Math.min(aLo, f.alt); aHi = Math.max(aHi, f.alt);
      hLo = Math.min(hLo, f.hdg); hHi = Math.max(hHi, f.hdg);
    }
    const r = {
      sLo: Math.max(0, Math.floor((sLo - 60) / 20) * 20), sHi: Math.ceil((sHi + 60) / 20) * 20,
      aLo: Math.floor((aLo - 1000) / 500) * 500, aHi: Math.ceil((aHi + 1000) / 500) * 500,
      hLo: Math.floor((hLo - 40) / 10) * 10, hHi: Math.ceil((hHi + 40) / 10) * 10,
    };
    P.spdTape.innerHTML = tapeSVG('spd', r.sLo, r.sHi);
    P.altTape.innerHTML = tapeSVG('alt', r.aLo, r.aHi);
    P.hdgTape.innerHTML = tapeSVG('hdg', r.hLo, r.hHi);
    P.ranges = r;
  }

  function drawPFD(P, f) {
    const root = P.root, r = P.ranges;
    root.classList.toggle('law-normal', f.law === 'normal');
    root.classList.toggle('law-altn', f.law === 'altn');
    root.classList.toggle('law-direct', f.law === 'direct' || f.law === 'abnormal');
    root.classList.toggle('declutter', f.dc);
    root.classList.toggle('nose-up', f.pitch > 30);
    root.classList.toggle('nose-down', f.pitch < -30);
    setStyle(P.att, 'transform', `rotate(${fmt(-f.bank, 2)}deg) translate(0px, ${fmt(f.pitch * PK, 2)}px)`);
    setStyle(P.fpv, 'transform', `translate(${fmt(f.drift * PK, 2)}px, ${fmt(-f.gamma * PK, 2)}px)`);
    show(P.fpv, f.bird);
    show(P.fd, f.fd && !f.bird);
    setA(P.fdRoll, 'transform', `translate(${fmt(f.fdRoll * 48, 1)} 0)`);
    setA(P.fdPitch, 'transform', `translate(0 ${fmt(-f.fdPitch * 48, 1)})`);
    const hm = ((f.hdg % 10) + 10) % 10;
    setStyle(P.ticks, 'transform', `translate(${fmt(-hm * PK, 2)}px, 0px)`);
    setStyle(P.roll, 'transform', `rotate(${fmt(-f.bank, 2)}deg)`);
    setA(P.slip, 'transform', `translate(${fmt(Math.max(-40, Math.min(40, f.beta * 5)), 1)} 0)`);
    setA(P.slip, 'fill', f.btgt ? COL.cyan : COL.yellow);

    // speed scale
    setStyle(P.spdTape, 'transform', `translate(0px, ${fmt(133 - (r.sHi - f.ias) * SK, 2)}px)`);
    const ys = v => CY - (v - f.ias) * SK;
    const bar = (e, top, bottom) => {
      const a = Math.max(100, Math.min(390, top)), b = Math.max(100, Math.min(390, bottom));
      show(e, b - a > 0.5);
      setA(e, 'y', fmt(a, 1)); setA(e, 'height', fmt(Math.max(0, b - a), 1));
    };
    bar(P.vmax, 100, ys(f.vmax));
    if (f.law === 'normal') {
      show(P.vsw, false);
      bar(P.vls, ys(f.vls), ys(f.vaprot));
      bar(P.vaprot, ys(f.vaprot), ys(f.vamax));
      bar(P.vamax, ys(f.vamax), 390);
    } else {
      show(P.vaprot, false); show(P.vamax, false);
      bar(P.vls, ys(f.vls), ys(f.vsw));
      bar(P.vsw, ys(f.vsw), 390);
    }
    // High speed protection belongs to normal law (FCOM DSC-27-20-20 P 11/20: not available in alternate law).
    const yh = ys(f.vhsp);
    show(P.hsp, f.law === 'normal' && yh > 104 && yh < 386);
    if (f.law === 'normal') setA(P.hsp, 'transform', `translate(0 ${fmt(yh, 1)})`);
    if (f.greenDot) { show(P.gd, true); setA(P.gd, 'cy', fmt(ys(f.greenDot), 1)); } else show(P.gd, false);
    const sf = f.sSpeed ? ['S', f.sSpeed] : f.fSpeed ? ['F', f.fSpeed] : null;
    if (sf) { show(P.sf, true); setT(P.sf, sf[0]); setA(P.sf, 'y', fmt(ys(sf[1]) + 6, 1)); } else show(P.sf, false);
    if (f.spdTarget != null) {
      const y = ys(f.spdTarget);
      const on = y >= 112 && y <= 378;
      // Managed speed target magenta, selected cyan (FCOM DSC-31-40 P 12-16/54).
      const tc = f.spdManaged ? COL.magenta : COL.cyan;
      setA(P.target, 'fill', tc); setA(P.targetNum, 'fill', tc);
      show(P.target, on); show(P.targetNum, !on);
      if (on) setA(P.target, 'transform', `translate(0 ${fmt(y, 1)})`);
      else { setT(P.targetNum, String(Math.round(f.spdTarget))); setA(P.targetNum, 'y', y < 112 ? '102' : '400'); }
    } else { show(P.target, false); show(P.targetNum, false); }
    show(P.trend, f.showTrend);
    if (f.showTrend) {
      const ty = Math.max(104, Math.min(382, CY - f.trend * SK));
      setA(P.trendLine, 'y2', fmt(ty, 1));
      const d = ty < CY ? 1 : -1;
      setA(P.trendHead, 'd', `M44 ${fmt(ty + 9 * d, 1)} L50 ${fmt(ty, 1)} L56 ${fmt(ty + 9 * d, 1)} Z`);
    }
    show(P.mach, f.showMach);
    if (f.showMach) setT(P.mach, '.' + String(Math.round(f.mach * 1000)).padStart(3, '0'));

    // altitude
    setStyle(P.altTape, 'transform', `translate(0px, ${fmt(133 - (r.aHi - f.alt) * AK, 2)}px)`);
    setT(P.aDigits, String(Math.floor(f.alt / 100)));
    const base = Math.floor(f.alt / 20) * 20, frac = (f.alt - base) / 20;
    for (let k = 0; k < 5; k++) {
      const v = base + (2 - k) * 20;
      setT(P.drum[k], String(((v % 100) + 100) % 100).padStart(2, '0'));
      setA(P.drum[k], 'y', fmt(250 + (k - 2) * 19 + frac * 19, 1));
    }
    if (f.altTarget != null) {
      const d = f.altTarget - f.alt, y = CY - d * AK;
      const on = y >= 114 && y <= 376;
      show(P.aTargetMark, on); show(P.aTarget, !on);
      if (on) setA(P.aTargetMark, 'y', fmt(y - 8, 1));
      else { setT(P.aTarget, String(f.altTarget)); setA(P.aTarget, 'y', y < 114 ? '102' : '402'); }
    } else { show(P.aTarget, false); show(P.aTargetMark, false); }
    const std = f.baro === 'STD';
    setT(P.baroLabel, std ? '' : f.baro.split(' ')[0] || '');
    setT(P.baro, std ? 'STD' : (f.baro.split(' ')[1] || ''));

    // vertical speed
    const vy = CY - Math.sign(f.vs) * vsY(f.vs);
    const vsAmber = Math.abs(f.vs) > 6000;
    setA(P.needle, 'x2', '466'); setA(P.needle, 'y2', fmt(vy, 1));
    setA(P.needle, 'stroke', vsAmber ? COL.amber : COL.green);
    const showDigits = Math.abs(f.vs) >= 200;
    show(P.vBox, showDigits);
    if (showDigits) {
      const by = f.vs > 0 ? Math.max(70, vy - 24) : Math.min(410, vy + 4);
      setA(P.vBox, 'transform', `translate(0 ${fmt(by, 1)})`);
      setA(P.vDigits, 'y', '16');
      setA(P.vDigits, 'fill', vsAmber ? COL.amber : COL.green);
      setT(P.vDigits, String(Math.round(Math.abs(f.vs) / 100)));
    }

    // heading
    const hu = f.hdg;
    setStyle(P.hdgTape, 'transform', `translate(${fmt(109 - (hu - r.hLo) * HK, 2)}px, 0px)`);
    setA(P.track, 'transform', `translate(${fmt(CX + Math.max(-100, Math.min(100, f.drift * HK)), 1)} 0)`);

    // FMA
    const fma = f.fma || {};
    let boxed = false;
    for (let c = 0; c < 4; c++) {
      const col = fma['c' + (c + 1)] || [];
      for (let l = 0; l < 3; l++) {
        const [txt, color, box] = fmaText(col[l]);
        setT(P.fma[c][l], txt); setA(P.fma[c][l], 'fill', color);
        if (box && c === 0 && l === 0) boxed = true;
      }
    }
    show(P.fBox, boxed);
    const c5 = [f.ap ? f.ap : '', f.fd ? '1FD2' : '', f.athr === 'active' ? 'A/THR' : f.athr === 'armed' ? 'A/THR' : ''];
    for (let l = 0; l < 3; l++) {
      setT(P.fma[4][l], c5[l]);
      setA(P.fma[4][l], 'fill', l === 2 && f.athr === 'armed' ? COL.cyan : COL.white);
    }
    setT(P.fTrim, f.law === 'direct' || f.law === 'abnormal' ? 'USE MAN PITCH TRIM' : '');

    show(P.mStall, f.stall);
    show(P.mBank, f.bankBank);

    // ILS raw data. The glideslope diamond shows where the glideslope is: below the centre when the aircraft is above it.
    show(P.ils, !!f.ils);
    if (f.ils) {
      const gs = Math.max(-2, Math.min(2, f.ils.gs)), loc = Math.max(-2, Math.min(2, -f.ils.loc));
      setA(P.iGs, 'd', ilsIndex(f.ils.gs, false)); setA(P.iGs, 'transform', `translate(${GSX} ${fmt(CY + gs * DOT, 1)})`);
      setA(P.iLoc, 'd', ilsIndex(-f.ils.loc, true)); setA(P.iLoc, 'transform', `translate(${fmt(CX + loc * DOT, 1)} ${LOCY})`);
      setT(P.iId, f.ils.ident); setT(P.iFreq, f.ils.freq); setT(P.iDme, fmt(f.ils.dme, 1));
      // The course dagger, or the course in digits at the end of the heading scale when it is off the scale.
      const dc = ((((f.ils.crs - f.hdg) % 360) + 540) % 360) - 180, on = Math.abs(dc) <= 21;
      show(P.iCrs, on); show(P.iCrsNum, !on);
      if (on) setA(P.iCrs, 'transform', `translate(${fmt(CX + dc * HK, 1)} 0)`);
      else {
        setT(P.iCrsNum, String(Math.round(f.ils.crs)).padStart(3, '0'));
        setA(P.iCrsNum, 'x', dc < 0 ? '128' : '300');
      }
    }
    // Radio height: every 10 ft down to 50 ft, then every 5 ft down to 10 ft, then every foot; amber at 400 ft or
    // below when no decision height is entered (FCOM DSC-31-40 P 32/54).
    show(P.ra, f.ra != null);
    if (f.ra != null) {
      const st = f.ra > 50 ? 10 : f.ra > 10 ? 5 : 1;
      setT(P.ra, String(Math.max(0, Math.round(f.ra / st) * st)));
      setA(P.ra, 'fill', f.ra <= 400 ? COL.amber : COL.green);
    }
  }

  // A deviation index: a magenta diamond, long along its scale; beyond two dots only the inner half shows, at the end
  // of the scale (FCOM DSC-31-40 P 40/54). dev > 0 moves it down (glideslope) or right (localizer).
  function ilsIndex(dev, horiz) {
    const [a, b] = horiz ? [13, 9] : [9, 13];
    if (Math.abs(dev) <= 2) return `M0 ${-b} L${a} 0 L0 ${b} L${-a} 0 Z`;
    if (horiz) return dev > 0 ? `M0 ${-b} L${-a} 0 L0 ${b}` : `M0 ${-b} L${a} 0 L0 ${b}`;
    return dev > 0 ? `M${-a} 0 L0 ${-b} L${a} 0` : `M${-a} 0 L0 ${b} L${a} 0`;
  }

  // ------------------------------------------------------------ controls
  const ctl = {};
  function bindControls() {
    for (const who of ['capt', 'fo']) {
      const fig = doc.querySelector(`.ctl-stick[data-stick="${who}"]`);
      ctl[who] = { fig, knob: fig.querySelector('.stick-knob'), shaft: fig.querySelector('.stick-shaft'), pb: fig.querySelector('.stick-pb'), read: fig.querySelector('.ctl-read') };
    }
    ctl.levers = [...doc.querySelectorAll('.lever')];
    ctl.leverRead = doc.querySelector('[data-read="levers"]');
    ctl.trimWheel = doc.querySelector('.trim-marks');
    ctl.trimPointer = doc.querySelector('.trim-pointer');
    ctl.trimRead = doc.querySelector('[data-read="trim"]');
    ctl.rudder = doc.querySelector('.rudder-knob');
    ctl.rudderRead = doc.querySelector('[data-read="rudder"]');
    ctl.spdbrk = doc.querySelector('[data-read="spdbrk"]');
    ctl.flaps = doc.querySelector('[data-read="flaps"]');
    ctl.gear = doc.querySelector('[data-read="gear"]');
    ctl.mw = doc.querySelector('[data-lamp="mw"]');
    ctl.mc = doc.querySelector('[data-lamp="mc"]');
    ctl.law = doc.querySelector('[data-read="law"]');
    ctl.ecam = doc.querySelector('[data-read="ecam"]');
    ctl.aural = doc.querySelector('[data-read="aural"]');
    ctl.gload = doc.querySelector('[data-read="gload"]');
    ctl.buffet = doc.querySelector('[data-read="buffet"]');
  }

  function amount(v) { const a = Math.abs(v); return a >= 0.97 ? 'full' : `${Math.round(a * 100)}%`; }
  function stickText(x, y) {
    const parts = [];
    if (Math.abs(y) >= 0.03) parts.push(`${amount(y)} ${y < 0 ? 'forward' : 'aft'}`);
    if (Math.abs(x) >= 0.03) parts.push(`${amount(x)} ${x < 0 ? 'left' : 'right'}`);
    if (!parts.length) return 'Neutral';
    const s = parts.join(' · ');
    return s[0].toUpperCase() + s.slice(1);
  }
  function leverY(v) {
    v = Math.max(0, Math.min(2, v));
    if (v <= 1) return 104 - v * 50;
    if (v <= 1.5) return 54 - (v - 1) * 44;
    return 32 - (v - 1.5) * 36;
  }
  function leverName(v) {
    if (v < 0.03) return 'IDLE';
    if (Math.abs(v - 1) < 0.03) return 'CL';
    if (Math.abs(v - 1.5) < 0.03) return 'MCT';
    if (v > 1.97) return 'TOGA';
    return null;
  }
  // ADR 1+2 OFF gives alternate law with reduced protection (FCOM DSC-27-20-20 P 3/20). Without reduced
  // protection only follows an abnormal attitude law (P 18/20).
  const LAW_NAMES = { normal: 'Normal law', altn: 'Alternate law', direct: 'Direct law', abnormal: 'Abnormal attitude law' };
  const lawName = f => (f.law === 'altn' && f.noprot ? 'Alternate law (no protection)' : LAW_NAMES[f.law]);

  function drawControls(f, aural) {
    for (const who of ['capt', 'fo']) {
      const [x, y] = f[who], c = ctl[who];
      const kx = 60 + x * 45, ky = 60 + y * 45;
      setA(c.knob, 'cx', fmt(kx, 1)); setA(c.knob, 'cy', fmt(ky, 1));
      setA(c.shaft, 'x2', fmt(kx, 1)); setA(c.shaft, 'y2', fmt(ky, 1));
      setA(c.pb, 'cx', fmt(kx, 1)); setA(c.pb, 'cy', fmt(ky, 1));
      const pressed = f.pb === who;
      c.fig.classList.toggle('pb-on', pressed);
      setT(c.read, pressed ? 'Takeover pb' : stickText(x, y));
      c.fig.classList.toggle('active', f.active === who);
    }
    setA(ctl.levers[0], 'transform', `translate(0 ${fmt(leverY(f.tl1), 1)})`);
    setA(ctl.levers[1], 'transform', `translate(0 ${fmt(leverY(f.tl2), 1)})`);
    const n1 = f.n11 && f.n12 ? `N1 ${fmt(f.n11)} · ${fmt(f.n12)} %` : 'N1 –';
    const l1 = leverName(f.tl1), l2 = leverName(f.tl2);
    // Detent names only when both levers share one; the drawing shows split levers (one line on iPad).
    const pos = l1 && l1 === l2 ? `${l1} · ` : '';
    setT(ctl.leverRead, pos + n1);
    setA(ctl.trimWheel, 'transform', `rotate(${fmt(-f.trim * 40, 1)})`);
    setA(ctl.trimPointer, 'transform', `translate(0 ${fmt(12 + (13.5 - f.trim) / 17.5 * 96, 1)})`);
    setT(ctl.trimRead, `THS ${fmt(Math.abs(f.trim), 1)}° ${f.trim >= 0 ? 'UP' : 'DN'}`);
    setA(ctl.rudder, 'x', fmt(67 + f.rud * 55, 1));
    setT(ctl.rudderRead, Math.abs(f.rud) < 0.03 ? 'Neutral' : `${amount(f.rud)} ${f.rud < 0 ? 'left' : 'right'}`);
    const sb = f.spdbrk;
    setT(ctl.spdbrk, sb < 0.03 ? 'RET' : sb > 0.97 ? 'FULL' : Math.abs(sb - 0.5) < 0.04 ? '1/2' : `${Math.round(sb * 100)}%`);
    setT(ctl.flaps, f.flaps === '0' ? '0' : f.flaps);
    setT(ctl.gear, f.gear === 'down' ? 'DOWN' : 'UP');
    ctl.mw.classList.toggle('lit', !!f.mw);
    ctl.mc.classList.toggle('lit', !!f.mc);
    setT(ctl.law, lawName(f));
    setA(ctl.law, 'class', `status-chip law-${f.law}`);
    setHidden(ctl.ecam, !f.ecam);
    if (f.ecam) {
      setT(ctl.ecam, `${/memo$/.test(f.ecam.level) ? 'EWD' : 'ECAM'}: ${f.ecam.text}`);
      setA(ctl.ecam, 'class', `status-chip ecam ecam-${f.ecam.level}`);
    }
    setHidden(ctl.aural, !aural);
    if (aural) { setT(ctl.aural, `Aural: ${aural.text}`); ctl.aural.classList.toggle('red', !!aural.red); }
    setHidden(ctl.gload, !f.gload);
    if (f.gload) setT(ctl.gload, `SD: G LOAD ${fmt(f.n, 1)}`);
    setHidden(ctl.buffet, !f.buffet);
  }

  // ------------------------------------------------------------ sound
  const audio = (() => {
    let ctx = null, enabled = false, stallOn = false, stallTimer = 0;
    function context() {
      if (!ctx) {
        const AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) return null;
        ctx = new AC();
      }
      if (ctx.state === 'suspended') ctx.resume();
      return ctx;
    }
    function unlock() {
      try { if (navigator.audioSession) navigator.audioSession.type = 'playback'; } catch (e) { /* not supported */ }
      const c = context();
      if (!c) return;
      const b = c.createBuffer(1, 1, 22050), s = c.createBufferSource();
      s.buffer = b; s.connect(c.destination); s.start(0);
    }
    function tone(freq, at, dur, type = 'sine', gain = 0.25, attack = 0.005) {
      const c = ctx, o = c.createOscillator(), g = c.createGain();
      o.type = type; o.frequency.value = freq;
      g.gain.setValueAtTime(0, at);
      g.gain.linearRampToValueAtTime(gain, at + attack);
      g.gain.exponentialRampToValueAtTime(0.0001, at + dur);
      o.connect(g).connect(c.destination);
      o.start(at); o.stop(at + dur + 0.05);
    }
    function chime(at) { tone(1040, at, 0.6, 'sine', 0.22); tone(2080, at, 0.4, 'sine', 0.08); }
    function cricket(at) {           // rapid high-pitched chirps
      for (let k = 0; k < 3; k++) for (let j = 0; j < 6; j++) tone(4200, at + k * 0.32 + j * 0.035, 0.022, 'square', 0.05, 0.002);
    }
    function cavalry(at) {
      const notes = [392, 523, 659, 784, 659, 784];
      notes.forEach((f, i) => tone(f, at + i * 0.2, i === notes.length - 1 ? 0.5 : 0.18, 'sawtooth', 0.08, 0.01));
    }
    function say(text) {
      if (!('speechSynthesis' in window)) return;
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US'; u.rate = 1.05; u.pitch = 0.75;
      window.speechSynthesis.speak(u);
    }
    function stallLoop() {
      if (!stallOn || !enabled || !context()) return;
      say('Stall. Stall.');
      cricket(ctx.currentTime + 1.0);
      stallTimer = setTimeout(stallLoop, 2100);
    }
    // Continuous repetitive chime, for as long as the OVERSPEED warning lasts.
    let crcOn = false, crcTimer = 0;
    function crcLoop() {
      if (!crcOn || !enabled || !context()) return;
      chime(ctx.currentTime + 0.02);
      crcTimer = setTimeout(crcLoop, 700);
    }
    return {
      get enabled() { return enabled; },
      setEnabled(v) { enabled = v; if (v) unlock(); else this.stop(); },
      play(name) {
        if (!enabled || !context()) return;
        const at = ctx.currentTime + 0.02;
        if (name === 'bank') say('Bank. Bank.');
        else if (name === 'chime') chime(at);
        else if (name === 'cavalry') cavalry(at);
        else if (name === 'crc') { for (let k = 0; k < 4; k++) chime(at + k * 0.7); }
      },
      setStall(on) {
        if (on === stallOn) return;
        stallOn = on;
        clearTimeout(stallTimer);
        if (on) stallLoop();
      },
      setCrc(on) {
        if (on === crcOn) return;
        crcOn = on;
        clearTimeout(crcTimer);
        if (on) crcLoop();
      },
      stop() {
        stallOn = false; crcOn = false; clearTimeout(stallTimer); clearTimeout(crcTimer);
        if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      },
      unlock,
    };
  })();

  // ------------------------------------------------------------ player
  const $ = id => doc.getElementById(id);
  const state = { ex: null, part: null, frames: null, t: 0, playing: false, speed: 1, mirror: false, stepIdx: -1, lastFrame: -1 };
  let P = null, raf = 0, lastNow = 0;
  const compiled = new Map();

  function mirrorText(s) {
    const m = state.mirror;
    return s.replace(/\{(left|right|Left|Right|eng1|eng2)\}/g, (_, k) => ({
      left: m ? 'right' : 'left', right: m ? 'left' : 'right', Left: m ? 'Right' : 'Left', Right: m ? 'Left' : 'Right',
      eng1: m ? 'ENG 2' : 'ENG 1', eng2: m ? 'ENG 1' : 'ENG 2',
    })[k]);
  }
  function refLabel(id) {
    const s = SOURCES[id];
    if (!s) return id;
    if (s.book) return `${s.book} ${s.code}${s.page ? ' P ' + s.page : ''}, PDF ${s.pdf}`;
    if (id === 'FORM') return 'Topics form (photo)';
    if (id === 'USER') return 'Your decision';
    const m = /p\. (\d+) of/.exec(s.label);
    return m ? `Session guidance p. ${m[1]} (photo)` : s.label;
  }
  const ACTORS = { aircraft: 'Aircraft', instructor: 'Instructor · left seat', trainee: 'Trainee (PF) · right seat', ios: 'IOS' };

  function framesFor(ex, part) {
    const key = `${ex.row}/${part.id}/${state.mirror ? 1 : 0}`;
    if (!compiled.has(key)) compiled.set(key, compile(part, state.mirror));
    return compiled.get(key);
  }

  function selectRow(row, partId, t) {
    const ex = EXERCISES.find(e => e.row === row) || EXERCISES.find(e => e.parts.length);
    pause();
    state.ex = ex;
    $('row-select').value = String(ex.row);
    for (const s of doc.querySelectorAll('.sheet')) s.classList.toggle('current', Number(s.dataset.row) === ex.row);
    const tabs = $('part-tabs');
    tabs.innerHTML = '';
    if (ex.parts.length > 1) {
      for (const p of ex.parts) {
        const b = el('button', 'control', `Part ${p.id.toUpperCase()} · ${p.label}`);
        b.type = 'button'; b.setAttribute('role', 'tab'); b.dataset.part = p.id;
        b.addEventListener('click', () => selectPart(p.id, 0));
        tabs.append(b);
      }
    }
    const idx = EXERCISES.indexOf(ex);
    $('prev-row').disabled = idx <= 0;
    $('next-row').disabled = idx >= EXERCISES.length - 1;
    const animated = ex.parts.length > 0;
    $('stage').hidden = !animated;
    if (animated) selectPart(partId && ex.parts.some(p => p.id === partId) ? partId : ex.parts[0].id, t || 0);
    else { state.part = null; state.frames = null; syncURL(); }
  }

  function selectPart(id, t) {
    pause();
    const ex = state.ex, part = ex.parts.find(p => p.id === id);
    state.part = part;
    for (const b of $('part-tabs').children) b.setAttribute('aria-selected', String(b.dataset.part === id));
    state.frames = framesFor(ex, part);
    prepareTapes(P, state.frames);
    const scrub = $('scrub');
    scrub.max = String(part.duration);
    const ticks = $('scrub-ticks');
    ticks.innerHTML = '';
    for (const s of part.steps) {
      const m = el('span');
      m.style.left = `${(s.t / part.duration) * 100}%`;
      ticks.append(m);
    }
    $('illustrative').textContent = `Illustrative: ${part.illustrative}`;
    renderSteps();
    state.stepIdx = -2;
    seek(Math.max(0, Math.min(part.duration, t || 0)));
    syncURL();
  }

  function renderSteps() {
    const sheet = doc.querySelector(`.sheet[data-row="${state.ex.row}"]`);
    for (const ol of sheet.querySelectorAll('.steps')) {
      for (const b of ol.querySelectorAll('.step-seek')) {
        b.disabled = false;
        const step = state.ex.parts.find(p => p.id === b.dataset.part).steps.find(s => s.t === Number(b.dataset.t));
        const body = b.nextElementSibling;
        if (step && body) {
          const txt = body.querySelector('.step-text');
          if (txt) txt.textContent = mirrorText(step.text);
        }
      }
    }
  }

  function seek(t) {
    state.t = t;
    render(true);
  }

  function frameAt(t) { return state.frames[Math.max(0, Math.min(state.frames.length - 1, Math.round(t * HZ)))]; }

  function auralFor(t) {
    const f = frameAt(t);
    if (f.stall) return { text: 'STALL, STALL + cricket', red: true };
    if (f.overspeed) return { text: 'Continuous repetitive chime', red: true };
    // one-shot alerts stay listed for 1.5 s
    const i0 = Math.max(0, Math.round((t - 1.5) * HZ)), i1 = Math.round(t * HZ);
    for (let i = i1; i >= i0; i--) {
      const s = state.frames[i] && state.frames[i].sounds;
      if (s && s.length) {
        const name = s[s.length - 1];
        if (name === 'bank') return { text: 'BANK BANK' };
        if (name === 'cavalry') return { text: 'Cavalry charge' };
        if (name === 'chime') return { text: 'Single chime' };
        if (name === 'crc') return { text: 'Continuous repetitive chime', red: true };
      }
    }
    return null;
  }

  function render(force) {
    const f = frameAt(state.t);
    drawPFD(P, f);
    drawControls(f, auralFor(state.t));
    $('scrub').value = String(state.t);
    $('clock').textContent = `${fmt(state.t, 1)} / ${state.part.duration} s`;
    const steps = state.part.steps;
    let si = 0;
    for (let i = 0; i < steps.length; i++) if (steps[i].t <= state.t + 1e-6) si = i;
    if (si !== state.stepIdx || force) {
      state.stepIdx = si;
      showStep(steps[si]);
    }
  }

  function showStep(step) {
    const ex = state.ex;
    const actor = $('cap-actor');
    actor.textContent = ACTORS[step.actor];
    actor.className = `actor actor-${step.actor}`;
    const co = $('cap-callout');
    co.hidden = !step.callout;
    co.textContent = step.callout || '';
    $('cap-time').textContent = `${fmt(step.t, 1)} s`;
    $('cap-text').textContent = mirrorText(step.text);
    const g = step.g ? ex.guidance.find(x => x.id === step.g) : null;
    $('cap-quote').hidden = !g;
    if (g) {
      $('cap-quote-text').textContent = `“${g.text}”`;
      $('cap-quote-src').textContent = refLabel(g.source || ex.source);
    }
    $('cap-refs').textContent = step.refs.map(refLabel).join(' · ');
    const sheet = doc.querySelector(`.sheet[data-row="${ex.row}"]`);
    for (const li of sheet.querySelectorAll('.guidance li')) li.classList.toggle('now', !!g && li.dataset.g === g.id);
    for (const b of sheet.querySelectorAll('.step-seek')) {
      b.closest('li').classList.toggle('now', b.dataset.part === state.part.id && Number(b.dataset.t) === step.t);
    }
  }

  function play() {
    if (!state.part) return;
    if (state.t >= state.part.duration - 1e-6) seek(0);
    state.playing = true;
    $('player').classList.add('playing');
    lastNow = performance.now();
    state.lastFrame = Math.round(state.t * HZ);
    raf = requestAnimationFrame(tick);
  }
  function pause() {
    state.playing = false;
    cancelAnimationFrame(raf);
    $('player').classList.remove('playing');
    audio.setStall(false);
    audio.setCrc(false);
    if (state.part) syncURL();
  }
  function tick(now) {
    if (!state.playing) return;
    const dtReal = Math.min(0.1, (now - lastNow) / 1000);
    lastNow = now;
    state.t = Math.min(state.part.duration, state.t + dtReal * state.speed);
    const fi = Math.round(state.t * HZ);
    for (let i = state.lastFrame + 1; i <= fi; i++) for (const s of state.frames[i].sounds) if (s !== 'stall') audio.play(s);
    state.lastFrame = fi;
    render(false);
    audio.setStall(frameAt(state.t).stall);
    audio.setCrc(frameAt(state.t).overspeed);
    if (state.t >= state.part.duration - 1e-6) { pause(); return; }
    raf = requestAnimationFrame(tick);
  }

  // Safari allows 100 history updates per 10 s and throws past that, which dragging the scrubber or
  // tapping through steps can reach, so updates are coalesced and a refused one is skipped.
  let urlTimer = 0;
  function syncURL() {
    clearTimeout(urlTimer);
    urlTimer = setTimeout(writeURL, 300);
  }
  function writeURL() {
    const q = new URLSearchParams();
    q.set('row', String(state.ex.row));
    if (state.part && state.ex.parts.length > 1) q.set('part', state.part.id);
    if (state.part && state.t > 0) q.set('t', fmt(state.t, 1));
    if (state.mirror) q.set('mirror', '1');
    try { history.replaceState(null, '', `${location.pathname}?${q}`); } catch (e) { /* rate limited */ }
  }

  function stepJump(dir) {
    if (!state.part) return;
    pause();
    const steps = state.part.steps;
    let i = state.stepIdx + dir;
    if (dir < 0 && state.t - steps[state.stepIdx].t > 0.6) i = state.stepIdx;
    i = Math.max(0, Math.min(steps.length - 1, i));
    seek(steps[i].t);
  }

  function setMirror(on) {
    state.mirror = on;
    $('mirror').setAttribute('aria-pressed', String(on));
    if (state.part) {
      const t = state.t;
      selectPart(state.part.id, t);
    }
  }

  function fitPFD() {
    const w = $('pfd-wrap').clientWidth;
    if (w) $('pfd').style.transform = `scale(${w / 500})`;
  }

  function init() {
    doc.documentElement.classList.add('js');
    $('no-js-note').hidden = true;
    $('player').hidden = false;
    P = buildPFD($('pfd'));
    bindControls();
    fitPFD();
    if ('ResizeObserver' in window) new ResizeObserver(fitPFD).observe($('pfd-wrap'));
    else window.addEventListener('resize', fitPFD);
    // Step lists: make the text mirrorable.
    for (const li of doc.querySelectorAll('.steps li')) {
      const body = li.querySelector('.step-body');
      const refs = body.querySelector('.refs');
      const actor = body.querySelector('.step-actor');
      const callout = body.querySelector('.callout');
      const txt = el('span', 'step-text');
      body.textContent = '';
      body.append(actor, ' ');
      if (callout) body.append(callout, ' ');
      body.append(txt, ' ', refs);
    }
    for (const b of doc.querySelectorAll('.step-seek')) {
      b.addEventListener('click', () => {
        if (state.part && state.part.id !== b.dataset.part) selectPart(b.dataset.part, Number(b.dataset.t));
        else { pause(); seek(Number(b.dataset.t)); }
        $('stage').scrollIntoView({ block: 'nearest' });
      });
    }
    $('row-select').addEventListener('change', e => selectRow(Number(e.target.value), null, 0));
    $('prev-row').addEventListener('click', () => { const i = EXERCISES.indexOf(state.ex); if (i > 0) selectRow(EXERCISES[i - 1].row); });
    $('next-row').addEventListener('click', () => { const i = EXERCISES.indexOf(state.ex); if (i < EXERCISES.length - 1) selectRow(EXERCISES[i + 1].row); });
    $('play').addEventListener('click', () => {
      if (state.playing) { pause(); return; }
      if (audio.enabled) audio.unlock();
      play();
    });
    $('restart').addEventListener('click', () => { pause(); seek(0); });
    $('step-back').addEventListener('click', () => stepJump(-1));
    $('step-next').addEventListener('click', () => stepJump(1));
    $('scrub').addEventListener('input', e => { pause(); seek(Number(e.target.value)); });
    for (const b of doc.querySelectorAll('[data-speed]')) {
      b.addEventListener('click', () => {
        state.speed = Number(b.dataset.speed);
        for (const o of doc.querySelectorAll('[data-speed]')) o.setAttribute('aria-pressed', String(o === b));
      });
    }
    $('mirror').addEventListener('click', () => setMirror(!state.mirror));
    $('sound').addEventListener('click', () => {
      const on = !audio.enabled;
      audio.setEnabled(on);
      $('sound').setAttribute('aria-pressed', String(on));
      if (on && state.playing) { audio.setStall(frameAt(state.t).stall); audio.setCrc(frameAt(state.t).overspeed); }
    });
    const q = new URLSearchParams(location.search);
    state.mirror = q.get('mirror') === '1';
    $('mirror').setAttribute('aria-pressed', String(state.mirror));
    const row = Number(q.get('row')) || 13;
    selectRow(row, q.get('part'), Number(q.get('t')) || 0);

    // Hook for the browser checks (check_uprt.py).
    window.uprt = {
      rows: () => EXERCISES.filter(e => e.parts.length).map(e => ({ row: e.row, parts: e.parts.map(p => ({ id: p.id, duration: p.duration, abnormal: !!p.abnormal_attitude, steps: p.steps.map(s => s.t) })) })),
      select: (row, part, t) => selectRow(row, part, t || 0),
      seek: t => { pause(); seek(t); },
      frame: () => Object.assign({}, frameAt(state.t), { sounds: undefined }),
      frames: () => state.frames.map(f => ({ t: f.t, pitch: f.pitch, bank: f.bank, ias: f.ias, n: f.n, alpha: f.alpha, alt: f.alt, gamma: f.gamma, stall: f.stall, bankBank: f.bankBank, dc: f.dc, gload: f.gload, law: f.law, adc: f.adc, buffet: f.buffet, overspeed: f.overspeed, mach: f.mach, vls: f.vls, vsw: f.vsw, vaprot: f.vaprot, vamax: f.vamax, n11: f.n11 })),
      state: () => ({ row: state.ex.row, part: state.part && state.part.id, t: state.t, playing: state.playing, mirror: state.mirror }),
      play, pause, setMirror,
    };
  }

  init();
})();
