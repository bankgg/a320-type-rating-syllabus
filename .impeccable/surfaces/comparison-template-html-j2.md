---
version: 1
slug: "comparison-template-html-j2"
primary_target: "comparison_template.html.j2"
related_targets: ["index.html","build_comparison.py"]
---

# Syllabus comparison

Mode: Read. Scope: the generated comparison webpage and its Jinja2 renderer. Primary scene: trainee preparation on an 11-inch iPad in landscape, in normal daylight.

## Direction contract

THESIS: A compact briefing matrix makes the complete course easy to navigate, prioritizes exercise comparison and ordered topics, presents one-time flight setup in a complete modal, and opens source-cited failure procedure briefs (PF/PM swimlane first) in the same modal pattern.

OWN-WORLD: White tables on a cool daylight canvas, charcoal system type, blue selection and setup controls, navy grouping bands, teal A / blue B labels, fine dividers and drawn SVG icons. Orange is reserved for failure-related exercises and recovery; pale blue and explicit text mark A/B differences.

STORY: Choose a numbered session or Previous/Next, scan its combined A/B failure-only summary separated by bullet dots and compact airport/runway strip, compare both trainees equally in Exercises or Schedule, and open complete Setup & conditions when needed. In sessions with briefs (MFTD/FBS 8), tap an orange failure row or a failure name in the summary to read its procedure brief.

FIRST VIEWPORT: Compact toolbar and grouped numbered session buttons; session title and summary; one airport/runway strip and setup button; two touch-sized detail tabs; dense category-grouped exercise rows. The primary 1194×834 MFTD/FBS 5 view shows at least eight exercise rows. Shared facts appear once. Complete setup, departure and arrival weather appear side by side in a modal, with full routes below and no scrolling at landscape iPad sizes. Phones wrap navigation, stack modal sections and allow modal scrolling.

FORM: User-approved refinement of the existing Briefing matrix, implemented directly in the existing static Python/Jinja2 tooling. The prior generated mockup is historical evidence, not a reproduction target. Session selection and detail tabs use buttons and query-string history, without internal anchor jumps. A native dialog contains the one-time setup task.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

Preserve source content, identifiers, sequence, conditional branches and unspecified values. User-approved session descriptions combine actual failure/emergency subjects across both trainees, with bullet-dot separators and no attribution; descriptions omit ordinary exercises and repetitive recovery variants. All Schedule topic copy uses dark ink, avoiding the previous unexplained routine-gray distinction. Failure/recovery rows have visible one-pixel orange borders along the top, bottom and outside edges, forming boxes rather than underlines. Remove exercise-count captions; retain source-backed repeated assignment notation. Remove redundant Both labels from Schedule and omit the status column when neither trainee has unique or mixed entries (FFS 8 and FFS 10). Keep course overview as the default, preserve the chosen detail tab between sessions, and support bookmarks, browser history, keyboard access and complete no-JavaScript reading. The visible Schedule tab retains view=topics in URLs for compatibility. Existing hash bookmarks migrate to query-string selection without scrolling to internal sections. The builder produces only the webpage. Procedure briefs: native dialog shared with setup; alert chips (red warning uses the warning token; amber uses failure tokens) always carry text; key limits strip; PF/PM swimlane with phase column, PF and PM lanes in neutral navy (never trainee colours), shared rows spanning both lanes, amber condition labels with a 1px rule; verbatim ECAM/STATUS/QRH blocks with navy bands and dotted leaders; secondary material in <details>; deep link ?brief=<slug>; Back closes; no-JS renders all briefs in order. Recovery rows without an ECAM/QRH procedure stay plain. The rehearsal-PDF workflow under sessions/ remains deferred.
