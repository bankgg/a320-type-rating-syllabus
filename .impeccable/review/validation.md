# Web comparison validation

The default Python build produces HTML only. No PDF generation dependency is imported.

Reviewed JSON and supplied source files are unchanged. DOM checks matched all 18 session summaries, 311 exercise groups and identifiers, assignment counts and conditional qualifiers, full setup and weather values, 361 Trainee A topics and 355 Trainee B topics with source order and statuses, and the FFS 5 conditional alternative.

Interaction checks covered all sessions and all three tabs, default Course overview, direct links to exercises/setup/weather/topics/conditional alternatives, browser back/forward, arrow/Home/End tab keys and no-JavaScript reading. All passed without page errors.

Eight viewport sizes were checked: 1194×834, 1112×834, 834×1194, 390×844, 320×640, 844×390, 1440×900 and 2560×1440. No horizontal overflow; reading text at least 16px; tested interactive controls at least 44px tall. FFS 3's long route was additionally checked at 320px.

Sampled text contrast was at least 5.81:1. In the primary iPad view, the first exercise row begins at 756px, within the 834px viewport. Sticky-toolbar offsets use its measured height. Anchor position at document bottom is constrained by the remaining scroll distance.

Safari remains unverified: the local Linux WebKit browser cannot reliably create a page. Chromium checks verify responsive behavior but do not substitute for a physical iPad Safari check.

One detector pass produced two findings: hierarchy below 1.25× (h3 raised from 18px to 20px) and semantic em-dash saturation (unassigned matrix cells and original missing values). The latter is retained for clarity and source fidelity. All generated mockup prompt metadata passed the provenance scan. The page itself ships no bitmap asset.
