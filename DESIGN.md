---
name: A320 SIM syllabus
description: A precise, calm briefing matrix for comparing Trainee A and Trainee B.
colors:
  canvas: '#fff'
  surface: '#f1f4f8'
  page: '#f7f9fc'
  ink: '#1b2735'
  muted: '#526171'
  line: '#dce2e8'
  blue: '#175cd3'
  blue-hover: '#10459f'
  blue-soft: '#edf3ff'
  navy: '#19364b'
  trainee-a: '#155e55'
  trainee-b: '#264ea5'
  difference: '#edf3ff'
  conditional: '#79520b'
  failure: '#9a3c08'
  failure-soft: '#fff3e7'
  failure-line: '#ca8750'
  header: '#e8eef6'
  trainee-a-soft: '#e6f3ef'
  control-selected-line: '#c3d5f7'
  tab-selected-line: '#c6d5ec'
  warning: '#b42318'
  warning-soft: '#fdeceb'
  condition-rule: '#d9b56a'
  leader: '#9aa7b4'
  timeline-rail: '#c5d0dc'
  checklist-band: '#f3f6fa'
  option-border: '#b9c5d3'
  summary-link-underline: '#9db8ec'
  brief-row-hover: '#ffe9d4'
typography:
  headline:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.025em
  title:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1.25rem
    fontWeight: 700
    lineHeight: 1.3
  heading-small:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1rem
    fontWeight: 700
    lineHeight: 1.35
  site-title:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1.125rem
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: -0.015em
  link-title:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1.125rem
    fontWeight: 700
    lineHeight: 1.35
  body:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.35
  field-label:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1rem
    fontWeight: 500
    lineHeight: 1.35
  label:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1rem
    fontWeight: 600
    lineHeight: 1.35
  key-limit:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1.125rem
    fontWeight: 700
    lineHeight: 1.35
    fontFeature: '"tnum"'
rounded:
  badge: 4px
  tab: 5px
  control: 6px
  container: 8px
  dialog: 12px
spacing:
  '2': 2px
  '4': 4px
  '5': 5px
  '6': 6px
  '8': 8px
  '10': 10px
  '12': 12px
  '14': 14px
  '16': 16px
  '20': 20px
  '24': 24px
  '32': 32px
  '40': 40px
  '48': 48px
components:
  control:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.label}'
    rounded: '{rounded.control}'
    padding: '8px 12px'
  control-primary:
    backgroundColor: '{colors.blue}'
    textColor: '{colors.canvas}'
    typography: '{typography.label}'
    rounded: '{rounded.control}'
    padding: '8px 12px'
  control-primary-hover:
    backgroundColor: '{colors.blue-hover}'
    textColor: '{colors.canvas}'
  session-button:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.muted}'
    typography: '{typography.label}'
    rounded: '{rounded.control}'
    width: '44px'
  session-button-selected:
    backgroundColor: '{colors.blue}'
    textColor: '{colors.canvas}'
  detail-tab:
    backgroundColor: 'transparent'
    textColor: '{colors.muted}'
    typography: '{typography.body}'
    rounded: '{rounded.tab}'
    padding: '8px 14px'
  detail-tab-selected:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.blue}'
    typography: '{typography.label}'
    rounded: '{rounded.tab}'
    padding: '8px 14px'
  overview-row:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '12px'
  brief-strip:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    rounded: '{rounded.container}'
    padding: '4px 12px'
  exercise-row:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '6px 10px'
  comparison-row-different:
    backgroundColor: '{colors.difference}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '5px 8px'
  failure-row:
    backgroundColor: '{colors.failure-soft}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '6px 10px'
  setup-dialog:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    rounded: '{rounded.dialog}'
    padding: '20px'
  conditional-panel:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '12px'
  summary-link:
    backgroundColor: 'transparent'
    textColor: '{colors.blue}'
    typography: '{typography.field-label}'
    padding: '4px 0'
  summary-link-hover:
    textColor: '{colors.blue-hover}'
  brief-open:
    backgroundColor: 'transparent'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '6px 10px'
    height: '44px'
    width: '100%'
  brief-open-hover:
    backgroundColor: '{colors.brief-row-hover}'
  brief-cue:
    textColor: '{colors.blue}'
    typography: '{typography.label}'
  alert-chip-warning:
    backgroundColor: '{colors.warning-soft}'
    textColor: '{colors.warning}'
    typography: '{typography.label}'
    rounded: '{rounded.badge}'
    padding: '2px 8px'
  alert-chip-caution:
    backgroundColor: '{colors.failure-soft}'
    textColor: '{colors.failure}'
    typography: '{typography.label}'
    rounded: '{rounded.badge}'
    padding: '2px 8px'
  alert-chip-qrh:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.navy}'
    typography: '{typography.label}'
    rounded: '{rounded.badge}'
    padding: '2px 8px'
  alert-chip-memory:
    backgroundColor: '{colors.header}'
    textColor: '{colors.ink}'
    typography: '{typography.label}'
    rounded: '{rounded.badge}'
    padding: '2px 8px'
  branch-chip:
    backgroundColor: '{colors.header}'
    textColor: '{colors.navy}'
    typography: '{typography.label}'
    rounded: '{rounded.badge}'
    padding: '0 6px'
  key-limits:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.key-limit}'
    rounded: '{rounded.container}'
    padding: '8px 12px'
  swimlane-header:
    backgroundColor: '{colors.header}'
    textColor: '{colors.muted}'
    typography: '{typography.label}'
    padding: '6px 10px'
  swimlane-phase:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.navy}'
    typography: '{typography.heading-small}'
    padding: '8px 10px'
    width: '9.5rem'
  swimlane-lane:
    backgroundColor: '{colors.canvas}'
    textColor: '{colors.ink}'
    typography: '{typography.body}'
    padding: '8px 10px'
  verbatim-block-title:
    backgroundColor: '{colors.navy}'
    textColor: '{colors.canvas}'
    typography: '{typography.heading-small}'
    padding: '8px 10px'
  brief-disclosure:
    backgroundColor: 'transparent'
    textColor: '{colors.ink}'
    typography: '{typography.label}'
    padding: '0 10px'
    height: '44px'
---
# Design System: A320 SIM syllabus

## Overview

**Creative North Star: "Briefing matrix"**

The Briefing matrix presents training information as a precise, calm document for comprehension in normal daylight. White tables on a cool daylight canvas, charcoal native system type, aligned columns and fine rules make dense comparisons comfortable to scan. Density comes from compact rows and clear hierarchy while reading text stays at 16px.

Blue identifies actions, selection and A/B difference fields. Teal Trainee A and blue Trainee B labels carry equal emphasis. Orange identifies failure-related exercises and recovery across categories and ordered topics; amber text retains conditional qualifiers. Red appears only for ECAM red warnings. Briefing planes remain flat, while one native modal dialog, shared by Setup & conditions and the failure-procedure briefs, uses a single diffuse shadow and a dim backdrop to establish its temporary layer.

**Key Characteristics:**

- White tables, cool daylight canvas and navy grouping bands.
- Native system typography with a distinct title, heading and reading hierarchy.
- Equal trainee emphasis and explicit text or notation for applicability.
- Fine ruled rows, compact comparisons and generous touch targets.
- Landscape iPad first, with stacked reading groups and a scrolling setup dialog on phones.
- Failure procedures open from their matrix rows into the shared dialog as a ruled briefing: alert chips, key limits, a neutral PF/PM swimlane and verbatim ECAM/QRH text.

This approved extension is extracted from `comparison_template.html.j2`, mirrored by `index.html`. The historical mockup remains critique evidence. The shipping page uses drawn SVG icons and no bitmap assets. Surface composition and session-specific behavior are also recorded in `.impeccable/surfaces/comparison-template-html-j2.md`.

## Colors

The palette combines a cool daylight field, white reading planes, navy organization and restrained semantic accents. Exact normative values live in the frontmatter; the existing CSS token names remain intact.

### Primary

- **Blue** identifies setup actions, session selection, selected detail tabs and keyboard focus.
- **Blue hover** deepens the primary setup button on hover.
- **Blue soft** provides secondary-control hover and selected fields, overview-row hover and Trainee B badge fields.
- **Summary-link underline** is the pale blue 1px underline of procedure links in session summaries; on hover the underline takes the full link color.
- Blue also carries the dotted underline on exercise titles and schedule topics that open a brief.
- **Navy** gives course-group and setup-section bands their strong grouping hierarchy; exercise-category bands use navy text on Surface.

### Secondary

- **Trainee A** is the teal of A labels, ordered-topic headings and trainee-specific status text, paired with **Trainee A soft** fields.
- **Trainee B** is the equivalent blue of B labels, ordered-topic headings and status text. Their weights, sizes and geometry match.

### Tertiary

- **Difference** is the pale blue row field for differing setup/weather values and unique or mixed ordered topics.
- **Failure**, **Failure soft** and **Failure line** are the orange warning mark, pale orange row field and orange rectangular row outline for failure-related exercises and recovery. Each isolated row has top and bottom rules plus outside left and right edges; there are no added internal vertical dividers. Adjacent failure rows share one divider rather than doubling the stroke. This treatment crosses categories and follows linked ordered topics. Failure tint takes precedence over a difference tint; explicit A/B status still communicates the difference.
- **Conditional** is the darker amber text for conditional exercise qualifiers and the `If` assignment label. Inside procedure briefs it also colors bold condition labels (ECAM/QRH "IF" lines and swimlane branches).
- **Condition rule** is the 1px amber rule that indents nested swimlane steps beneath a condition.
- **Brief-row hover** is the slightly deeper orange field of a failure row whose title opens a procedure; on hover the title's dotted Blue underline turns solid Blue hover.
- **Warning** and **Warning soft** are the ECAM red-warning text and pale red field. They appear only on the red-warning alert chip and the red LAND ASAP chip, always with a text label. The amber caution and amber LAND ASAP chips use Failure on Failure soft, and verbatim CAUTION labels use Failure text.

### Neutral

- **Page** is the cool daylight page background.
- **Canvas** is the white table, toolbar, control, briefing strip and dialog plane.
- **Surface** is the cool gray session-navigation field, exercise-category field and conditional panel.
- **Header** is the stronger cool gray table-header and tab-rail field, now also a named CSS variable (`--header`). It fills the swimlane header row, memory-items chips, aircraft-branch chips and phone lane tags.
- **Ink** is the primary reading color and assignment notation.
- **Muted** carries summaries, field labels, session progress, shared setup labels and unassigned notation.
- **Line** supplies fine document dividers. **Control selected line** and **Tab selected line** are the quiet strokes of selected secondary controls and tabs.
- **Leader** is the 1px dotted leader drawn between an ECAM item and its setting.

### Named Rules

**The Equal Emphasis Rule.** Give Trainee A and Trainee B matching type, parallel labels and equal assignment-column widths. Their colors identify the trainee without establishing a visual ranking.

**The Meaning Before Color Rule.** Pair color with labels, assignment notation or explanatory text. A difference, failure or conditional branch must remain understandable without its tint.

**The Reserved Alarm Rule.** Orange stays reserved for failure marking: failure rows, their warning icons and entry hover, and the amber caution chips and CAUTION labels of failure procedures. Red is used only for ECAM red warnings and red LAND ASAP chips. Amber text marks procedure conditions, consistent with Conditional's meaning. None of these hues decorates anything else.

**The Neutral Lanes Rule.** PF/PM swimlanes are neutral navy, header gray and white. They never borrow the Trainee A teal or Trainee B blue, because pilot roles are not trainees.

## Typography

**Display and Body Font:** the native system stack recorded in the frontmatter. The same approved stack serves headings, labels, data and controls.

**Character:** direct and familiar, with measured weight changes and compact heading leading. Tables, counts and session numbers use tabular numerals. The body uses compact leading while preserving the established reading size.

### Hierarchy

- **Headline:** bold session and course headings, compact leading and slight negative tracking.
- **Title:** bold section headings with a 1.3 line height.
- **Heading small:** bold phase, trainee, category and conditional-panel headings.
- **Site title:** bold toolbar identity with slight negative tracking; it uses the reading size at the compact breakpoint.
- **Link title:** bold session titles within course overview button rows.
- **Body:** regular reading text, values and notes. Overview prose is limited to 70ch, session summaries to 85ch and exercise notes to 75ch.
- **Field label:** medium-weight comparison row labels and trainee-specific status text.
- **Label:** semibold table headings, controls, selected tabs, trainee badges, alert and branch chips, swimlane header cells and disclosure summaries. Labels retain natural case; verbatim ECAM/QRH wording keeps its source capitalization.
- **Key limit:** bold, slightly enlarged tabular values in the procedure key-limits strip, with balanced wrapping on values and their muted labels.

Procedure briefs reuse these roles: the dialog heading is a Title with the session name in medium-weight Muted (nowrap); a brief title within a multi-brief group uses the Link title size; phase names, navy block titles and block subheadings use the reading size. PF/PM callouts are bold with curly quotation marks; swimlane notes are Muted. Brief summaries are limited to 75ch and disclosure bodies to 85ch.

### Named Rules

**The Reading First Rule.** Keep body copy, notes, table values and control labels at 16px or larger. Use the title and heading roles to establish hierarchy instead of shrinking supporting facts.

**The Sequential Heading Rule.** Heading levels follow structure, not size. A procedure group title is h3; brief titles, phase names and block titles are h4 when the group holds one brief and h5 when it holds several, with block subheadings one level deeper.

## Layout

A centered document container uses a maximum outer width of 1224px and 24px horizontal padding. The main document uses 16px top and 40px bottom padding. The sticky toolbar has a 60px minimum inner height and safe-area-aware top padding. The grouped session navigation sits immediately below it on wide screens. There are no authored internal anchor jumps or anchor-offset rules.

The observed spacing scale is in the frontmatter. Default table rows use 6px vertical and 10px horizontal padding; category bands use 5px vertical padding. Setup/weather cells use 5px by 8px; route cells use 6px by 8px. Compact rhythm increases visible content without reducing reading type.

The exercise matrix allocates 76% to the exercise and 12% to each equal assignment column. Related ordered-topic tables, conditional panels and overview rows use two equal columns with a 16px gap. Setup comparison field columns use 42%; topic number and optional status columns use 34px and 76px. Shared setup/weather values appear once, with an explicit Both label where one value spans A/B columns.

The setup dialog uses a maximum width of 1200px, a viewport gutter of 16px on each side, 20px internal padding and a maximum height of the viewport minus 32px. Its setup, departure-weather and arrival-weather sections use a 1.1fr / 1fr / 1fr grid with 16px gaps. Full routes span the width below. The complete content fits without scrolling at the verified 1194×834 and 1112×834 landscape iPad sizes. Smaller viewports and enlarged text retain complete content through stacking and dialog scrolling.

The failure-procedure dialog shares the setup dialog's dimensions, gutters and padding. Its content runs in a fixed order: sticky heading, optional brief switcher, alert chips with "Practised by" trainee badges, summary, key-limits strip, PF/PM swimlane, verbatim ECAM/QRH and STATUS blocks, optional numeric tables, disclosures and a muted footnote. The key-limits strip is an auto-fit grid of columns at least 170px wide. The swimlane uses a 9.5rem phase column followed by two equal lanes; items shared by both pilots span both lanes. Verbatim procedure and STATUS/QRH blocks sit in two equal columns with a 16px gap, or a single column capped at 760px when only the procedure exists. ECAM lines indent 1.25rem per condition level. Numeric tables scroll horizontally within their own container.

- **At 1160px and below:** numbered session groups occupy separate rows; group labels reserve 96px.
- **At 760px and below:** navigation becomes static beneath the sticky toolbar, all reading and setup grids become one column, the airport/runway strip stacks with a full-width setup button, and main padding becomes 16px at the top and safe-area-aware sides with 32px at the bottom. Assignment widths become 68% / 16% / 16%. Previous/Next become icon buttons. Visible trainee labels abbreviate to A/B. Dialog gutters reduce to 8px, padding to 14px and maximum height to the viewport minus 16px. The swimlane becomes one column: the header row hides, PF, PM and PF + PM tags appear on each lane, and empty lanes are hidden. Verbatim blocks stack.
- **At 520px and below:** the toolbar can wrap, the session heading and progress stack, both tabs share the available width, cells use 6px horizontal padding and topic status columns become 68px. Dialog heading type becomes 18px. Key-limit columns narrow to a 140px minimum and procedure entry rows use 6px horizontal padding.

Without JavaScript, all 18 sessions, exercises, setup/weather values, full routes and ordered topics remain readable in course order. Successive sessions use 48px separation, a divider and 24px top padding. Every failure brief (11 in the current build) also renders in document order under a "Failure procedures" heading after each session's panels, with entry buttons left disabled. The enhanced view shows one selected session and its selected reading panel, and opens briefs in the dialog. No runtime Node or server dependency is required.

Verified in Chromium at 1194×834 and 390×844: no horizontal overflow, text of at least 16px and targets of at least 44px. Safari has not been verified.

## Elevation & Depth

White tables, cool header fields, navy bands, semantic row fields and fine dividers establish depth on the document. The toolbar and numbered navigation use stacking order and bottom rules. The shared modal dialog (Setup & conditions and failure procedures) alone uses a diffuse modal shadow (`0 16px 64px #142c4540`) and a dim backdrop (`#142c4573`). Those extension tokens live in the sidecar.

### Named Rules

**The Ruled Plane Rule.** Separate briefing information with fine dividers and semantic bands. Keep document surfaces flat; reserve the diffuse shadow and dim backdrop for the shared modal dialog.

## Shapes

Tables, category bands, overview rows and conditional panels keep square, ruled silhouettes. The actual radius scale is recorded in the frontmatter: small trainee badges, slightly curved tab buttons, control corners, broader strip/tab-rail/overview-container corners and the setup-dialog corners. Borders remain single-pixel rules. Exercise and Schedule tables use separate borders with zero spacing so a preceding gray rule cannot hide the orange top edge. Consecutive failure rows suppress the following top border and share a single orange divider. Inline SVG line icons carry actions and warnings; included assignments use drawn checkmarks rather than text glyph icons.

Procedure briefs keep the same language. Alert, branch and lane-tag chips use the badge radius. The key-limits strip is a single bordered container with the container radius and 1px internal column rules. Swimlanes, verbatim blocks and disclosures stay square and ruled. ECAM leaders are drawn 1px dotted rules rather than typed dots, and the disclosure chevron is a drawn SVG that rotates 90° when open.

**The Hairline Edge Rule.** No colored side stripe is thicker than 1px. Failure-row edges and the amber condition rule are hairlines like every other divider.

## Components

### Buttons

The primary Setup & conditions button uses Blue with white text; hover uses Blue hover. Overview, Previous/Next and close controls use white planes with a fine line, Blue soft hover and Blue text/stroke. Numbered session buttons are 44px wide with a 44px minimum height; selected buttons use Blue and white. Other controls also retain a 44px minimum height. Disabled boundary navigation uses Muted at 0.55 opacity.

All interactive elements use a 3px Blue focus outline with a 3px offset. Controls, numbered session buttons and tabs transition background, color and border for 160ms with ease-out only when reduced motion is not requested. Selection and tap feedback use the existing pale blue field; scrollbar details live in the sidecar.

Procedure entry points exist only where a brief exists. In session summaries, failure subjects with a brief become inline link-style buttons: Blue, medium weight, a 1px pale blue underline offset 3px, deepening to Blue hover with a full-color underline. In the Exercises and Schedule tables, an orange failure row with a brief turns its title cell into a full-width button (44px minimum height, 6px by 10px padding) holding the warning mark and the title; there is no chevron or "Procedure" word. The one cue, identical in both tables, is a 1.5px dotted Blue underline under the title, offset 5px with skip-ink off. On hover the row deepens to Brief-row hover and the underline turns solid Blue hover with Blue hover text. Each table's key ends with the same cue — "Dotted underline opens its procedure" in Exercises, "…topics with a dotted underline open their procedure" in the Schedule caption — the phrase "dotted underline" drawn in the cue's own style, rendered only for sessions with briefs and revealed by JavaScript. Orange rows without a brief, such as recovery manoeuvres, stay plain and never take the dotted underline. All entry buttons ship disabled, without the underline, until JavaScript enables them. Background and color transitions use 160ms ease-out only when reduced motion is not requested.

### Chips

Trainee badges use matching padding, semibold reading type and the badge radius. A pairs teal text with its pale teal field; B pairs blue text with Blue soft. Setup/weather column headers always display compact A/B badges.

Procedure alert chips use the badge radius, 2px by 8px padding, semibold reading type and no wrapping: Red warning on Warning soft, Amber caution on Failure soft, QRH procedure as Navy on Surface, and Memory items as Ink on Header. LAND ASAP appears as its own chip reading "LAND ASAP (red)" or "LAND ASAP (amber)" in the matching palette. Aircraft-branch chips (for example HS-TXP..TXU) are semibold Navy on Header with 0 by 6px padding.

### Cards / Containers

The compact airport/runway strip uses a white bordered plane, the container radius, 4px vertical padding and 10px vertical margins, with a flex row that stacks on phones. Overview emphasis uses the same radius and fine border; overview session buttons remain square ruled rows with Blue titles and muted summaries. Session and overview-entry summaries combine actual A/B failure and emergency subjects with bullet-dot separators and no trainee attribution. Ordinary exercises and recovery variants remain in the complete reading panels; sessions without failure subjects display `No failure exercises.` Conditional panels use Surface and 12px internal padding. These document containers cast no shadow.

### Navigation

Grouped MFTD/FBS and FFS numbered buttons provide direct session selection. Overview and Previous/Next remain in the toolbar, and changing sessions preserves the chosen Exercises or Schedule tab. The two detail tabs sit within a cool gray rounded rail with a 10px lower margin; selection is a white outlined tab with Blue semibold text. Tabs expose selection and panel relationships, support left/right arrows and Home/End, and use 44px minimum targets.

The visible Schedule tab and Session schedule heading retain the internal `topics` view identifier for bookmark compatibility. Session and view selection use query-string bookmarks and browser history. Legacy hash bookmarks migrate once to query selection, including setup-dialog or ordered-topic destinations. Navigation uses buttons and preserves source IDs without adding internal anchor links. Changing sessions moves focus to the selected heading and returns the document to the top.

### Comparison Tables

Shared values appear once. Blue difference rows retain explicit A/B column labels and top-aligned values; long identifiers and routes wrap within their cells. The complete setup dialog presents flight setup and departure/arrival weather together with full routes below. It contains focus and supports Escape, its close control and a genuine backdrop click. Closing restores opener focus and document scroll. A sticky heading retains the close control during phone scrolling. Enlarged text can scroll rather than clip content.

### Assignment Matrix

The signature matrix combines an exercise description with equal centered A/B assignment columns. Category rows use navy text on cool gray. All exercise-count captions are omitted; repeat notation such as ×2 and Session X of 18 progress remain. Included assignments use SVG checkmarks, repeats show counts, unassigned cells use a labeled dash, and conditional assignments show `If` with the qualifier in the exercise row. Orange fields, rectangular row outlines and drawn warning icons identify failure and recovery across all exercise categories. Notes retain the reading size.

### Session Schedule

Parallel trainee tables preserve each published sequence. All schedule topic copy, including routine entries, uses dark Ink; number and other metadata retain their semantic muted treatment. Pale blue identifies unique or mixed rows, with explicit `A only`, `B only`, `A adds` or `B adds` status. Shared schedule rows have no redundant Both text. If every row is shared, the A/B status column is omitted entirely on both trainee tables, as in FFS 8 and FFS 10; both full source sequences remain separate. Linked failure/recovery rows use the orange field and rectangular outline while retaining any applicable unique/mixed A/B status. Trainee colors identify headings and statuses with equal emphasis. Tables stack on phones without combining their sequences.

### Setup Dialog

A native modal dialog provides the one-time setup task, with complete facts and no shortened routes. Its shadow/backdrop are limited to this temporary layer, which the failure-procedure briefs share. Opening (setup and procedure briefs share the dialog): the sheet rises 12px and settles from 99% scale over 260ms with `cubic-bezier(.16, 1, .3, 1)`, reaching full opacity within the first 35% so text never ghosts over the page; the backdrop dims over 220ms. Closing is shorter: 160ms, a 6px drop with a late fade and the backdrop clearing, after which the dialog closes and focus returns to the opener; a new open or second close finishes it immediately. With reduced motion requested, both directions are opacity-only fades (140ms / 120ms). Without JavaScript the same setup content remains in document order.

### Procedure Dialog

Failure-procedure briefs reuse the native setup dialog through one shared open/close path: the same shadow, backdrop, focus containment, opener-focus restoration and scroll lock. The sticky heading carries the brief or group title, a medium-weight Muted "· session name" that does not wrap, and the close control. A group with several briefs adds a switcher that reuses the detail-tab rail, each tab carrying its trainee badges. Switching tabs keeps the dialog open.

The brief opens with a **header plate**: a Surface field with an 8px radius and 16px padding (12px on phones) holding the alert chips, the "Practised by" badges (on Canvas fields so both trainee colours stay visible), a 75ch summary at 1.45 leading, and the key-limits strip, a ruled definition list on Canvas. Each column has a Muted label, an optional branch chip and a Key limit value.

The rest of the brief is divided into **titled sections**: Handling flow, From the manuals, Reference tables (only when the brief has tables) and More detail. Each section starts 28px below the previous one, after a 1px Line rule and 20px of space, with a 1.25rem bold title led by a drawn icon (Navy on Header, 6px radius) and a Muted note on the same baseline describing its contents. Section titles are real headings one level below the brief title.

Verbatim ECAM/QRH and STATUS blocks are bordered 8px-radius boxes on Canvas that open with a navy band heading; STATUS and QRH sub-labels (Limitations, APPR PROC, CRUISE…) are bold Navy bands on Surface, and a ruled Muted reference line closes each procedure. Each action line draws a dotted Leader between item and bold right-aligned setting. Conditions are bold Conditional labels indented by level, and reference lines and notes are Muted. Optional numeric tables use the same boxed block and scroll horizontally. More detail groups its disclosures in one bordered 8px-radius panel of ruled `details` rows with 48px semibold summaries, Blue hover, a Surface field on open summaries and a rotating Muted chevron: What it is, FCTM technique, Related procedures, HS-TX differences (rendered only when the HS-TX registrations actually differ), Gaps and omissions, and Sources. A Muted disclaimer footnote closes the brief.

**Brief switcher.** A group with several briefs shows a muted lead line ("2 procedures in this group — choose one") above a grid of option cards (auto-fit, min 230px, 10px gap). Each card is a real button: 1px #b9c5d3 border, 8px radius, a faint 1px shadow, 64px minimum height, a 12px alert-type marker (warning red, failure orange, Navy for QRH procedures), the brief name in bold over its alert type in Muted, compact A/B trainee badges (letter only), and a chevron. Hover uses a Blue border. The selected card has a Blue double-weight border, a Blue soft field, a Blue-hover name and a drawn check in place of the chevron. Cards keep tab semantics, with arrow and Home/End keys.

**Jump bar and pinned flow header.** On iPad and wider, the sticky heading carries a compact Header-gray segmented jump bar (Flow · Manuals · Detail; 44px targets). It scrolls the dialog to the section title, clearing the heading, and moves focus there. The jump bar is hidden at ≤520px. The swimlane's Phase / PF / PM header row stays pinned directly below the dialog heading while the flow scrolls, using a measured `--dialog-head` offset; the flow container uses `overflow: clip` so sticky positioning still works. Both dialogs carry their top padding inside the sticky heading, so content never shows above it.

**Shared briefs and session notes.** A brief is one shared document: the same pop-up content appears in every session that maps it. Inside the header plate, an optional **session note** follows the summary: a Canvas field with a 1px Line border and 6px radius, max 75ch, led by a bold Navy "In <session name>". It carries that session's scenario context, so the shared brief stays session-neutral. A **Technique** alert chip (Navy on Canvas with a 1px Line ring; Navy tab marker) marks briefs built from FCTM/PDP technique with no ECAM or QRH procedure. These include companion briefs, such as the drift-down strategy, that sit as an extra tab in a session's group.

A brief is addressable as `?brief=<slug>` and pushes a history entry; Back, Escape and the close control all close it with focus restored to the opener. When focus moves to a dialog heading programmatically, its focus ring is suppressed; all other focus rings remain.

### PF/PM Swimlane

This ruled grid on Canvas, bordered with an 8px radius, sets out who does what in each phase. A Header-gray header row names the Phase, PF and PM columns in Muted semibold type. Each phase row starts with an 11rem phase cell on Surface: a 26px Navy number node with white tabular numerals, then the phase name in Navy. A 2px Timeline rail (#c5d0dc) joins the nodes from the first phase to the last; the sequence carries meaning, so the numbering is earned. Each phase is an ordered list of **turns**: one crewmember's consecutive actions, in time order. A turn spans the full row with its content in the PF or PM column (a centred 1px Line rule keeps both columns legible when one side is empty), led by a Muted tabular step number such as 3.2. Dashed Line rules separate turns; solid rules separate phases. Exchanges therefore read top to bottom across the columns (PF "CONTINUE ECAM" → PM reads STATUS → PF "REMOVE STATUS"). Shared PF + PM turns span both columns on a faint field after a bold Navy "PF + PM" tag. Turn bodies use 10px × 14px padding and 8px item rhythm. Callouts are bold Navy in curly quotes, led by a drawn speech-mark icon. ECAM items sit on a pale checklist band (#f3f6fa, 4px radius) with the dotted leader, and consecutive bands stack 2px apart. Notes are Muted, and nested steps indent 12px behind the 1px Condition rule. On phones the rail is hidden; each phase becomes a numbered header above its stacked turns, each tagged PF, PM or PF + PM beside its step number, with PM turns on a faint field. Branch chips mark aircraft-specific items. Empty lanes stay empty.

## Do's and Don'ts

### Do:

- Do use the existing semantic color names and assignments from the frontmatter.
- Do keep both trainees equally prominent and label shared values explicitly when they span an A/B comparison.
- Do preserve 16px reading text, touch controls of at least 44px and a visible keyboard focus outline.
- Do use fine rules, cool gray fields and navy grouping bands to organize dense information.
- Do stack related reading groups on phones while retaining clear trainee headings and assignment columns.
- Do preserve explicit qualifiers, source terminology and unspecified values when they affect the comparison.
- Do keep setup complete, restore opener focus and preserve document scroll when the dialog closes.
- Do open failure procedures in the shared dialog from their orange rows and summary subjects, and render every brief in document order without JavaScript.
- Do pair every red, amber caution, QRH or memory-items chip with its text label.
- Do keep verbatim ECAM/QRH wording and its source capitalization, with drawn leaders and amber condition labels indented by level.

### Don't:
- Don't add screen-reader-only text, visually hidden labels or skip buttons; the users don't use screen readers.
- Don't use trainee colors as a substitute for text labels or accessible assignment meaning.
- Don't use orange or amber as general decoration; retain their failure/recovery and conditional meanings.
- Don't add shadows, imagery or ornamental backgrounds to the briefing planes.
- Don't replace the approved native system font stack without an approved design-system change.
- Don't turn ruled comparison rows into an ornamental card grid or add decorative labels above headings.
- Don't use red for anything other than ECAM red warnings and red LAND ASAP, or orange for anything other than failure marking.
- Don't color PF/PM lanes with the trainee teal or blue.
- Don't add colored side stripes thicker than 1px.
- Don't make rows without a brief look actionable.
