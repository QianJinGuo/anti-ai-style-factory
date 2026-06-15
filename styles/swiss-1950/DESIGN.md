---
version: alpha
name: Swiss 1950
description: Grid as law. Helvetica as voice. White space as structure. Mathematical precision meets editorial clarity.
colors:
  primary: "#000000"
  secondary: "#E20613"
  tertiary: "#0047AB"
  neutral: "#FFFFFF"
  neutral-warm: "#F5F5F0"
  muted: "#888888"
  border: "#CCCCCC"
typography:
  h1:
    fontFamily: "Helvetica Neue"
    fontSize: "4rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.04em"
  h2:
    fontFamily: "Helvetica Neue"
    fontSize: "2rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  h3:
    fontFamily: "Helvetica Neue"
    fontSize: "1rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.02em"
  body-md:
    fontFamily: "Helvetica Neue"
    fontSize: "0.875rem"
    fontWeight: 300
    lineHeight: 1.7
    letterSpacing: "0em"
  caption:
    fontFamily: "Helvetica Neue"
    fontSize: "0.6875rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.12em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  xs: 4px
  sm: 8px
  md: 24px
  lg: 48px
  xl: 72px
  gutter: 24px
  column: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    fontWeight: 700
    letterSpacing: "0.08em"
    textTransform: uppercase
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral}"
  section-divider:
    height: "1px"
    backgroundColor: "{colors.border}"
    margin: "{spacing.lg} 0"
  grid-12col:
    display: grid
    gridTemplateColumns: "repeat(12, {spacing.column})"
    gap: "{spacing.gutter}"
---

## Overview

Swiss International Typographic Style (1950-1970). Muller-Brockmann's grid is not a suggestion — it is law. Every element exists within a mathematically defined structure. The grid creates order; the type creates voice; the white space creates meaning.

Anti-AI principle: **AI default is organic, flexible, and visually forgiving.** Swiss style is rigid, mathematical, and unforgiving. Where AI places elements by feel, Swiss places them by coordinate.

## Colors

Black, white, one red. The palette is austere by design — Josef Muller-Brockmann used color sparingly because the grid and type carry the message. Blue is permitted for data differentiation only.

- **Primary (#000000):** Absolute black. Text, borders, structure.
- **Secondary (#E20613):** Signal red. The single accent. Use once per page.
- **Tertiary (#0047AB):** Royal blue. Data charts only.
- **Neutral (#FFFFFF):** Pure white. The primary surface.
- **Neutral-warm (#F5F5F0):** Warm white for alternate sections.

## Typography

One family. Helvetica Neue in all weights from 300 to 700. The weight contrast carries hierarchy — no serif/sans mixing, no display faces, no decorative alternatives.

Font substitution: Use **Helvetica Neue** if available. Fallback to **Arial**. Last resort: **Inter** — but ONLY as a system fallback, never as a design choice.

**Critical rule:** letter-spacing is negative for headlines (-0.03 to -0.04em) and positive for labels/captions (0.08 to 0.12em). This is the Swiss signature — tight headlines, loose labels.

## Layout

The 12-column grid is mandatory. Content widths must be multiples of columns (2, 3, 4, 6, 8, 12). No "almost aligned" — elements snap to grid lines or they are wrong.

- Full-width: 12 columns (headline, hero)
- Two-column: 6+6 (text + sidebar)
- Three-column: 4+4+4 (cards, features)
- Asymmetric: 8+4 or 9+3 (content + nav)

Gutter: 24px. Column width: 64px. Total content width: 12*64 + 11*24 = 1032px.

## Elevation & Depth

No shadows. No blur. No transparency. Depth is expressed through:
- **White space** — more space = more importance
- **Weight** — bolder = higher hierarchy
- **Color** — red on white = emphasis

## Shapes

Zero radius. A rectangle aligned to the grid is the only shape. Circles are permitted only for:
- Data visualization (pie charts, bubble plots)
- Image masking (circular portraits)

## Components

### Section Divider

1px gray line. Separates content blocks. The line IS the component — no decorative lines, no ornamental borders.

### Button

Black rectangle, white uppercase text. Tight letter-spacing (0.08em). On hover: red. No transitions — states are instant.

### Table

Clean lines, no heavy borders. Header in bold 300-weight. Data in regular weight. Generous row padding (16px vertical).

## Do's and Don'ts

**Do:**
- Align everything to the grid
- Use negative letter-spacing on headlines
- Use positive letter-spacing on labels
- Leave generous white space between sections
- Use weight contrast (700 headline, 300 body) for hierarchy

**Don't:**
- Use any border-radius > 0px
- Use any box-shadow
- Use any gradient (even white-to-white)
- Use more than one accent color per page
- Center text (except in data tables)
- Use decorative elements that don't serve the content
