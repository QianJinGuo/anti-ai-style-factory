---
version: 1.0.0
name: Terminal (CRT Monochrome)
description: A utilitarian interface rooted in the raw, unadorned text rendering of early cathode-ray tube monitors, prioritizing data density and system feedback over aesthetic decoration.
colors:
  primary: "#00FF41"
  secondary: "#008F11"
  tertiary: "#003B00"
  neutral: "#000000"
  muted: "#004D00"
typography:
  h1:
    fontFamily: '"VT323", "Courier New", monospace'
    fontSize: 48
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  h2:
    fontFamily: '"VT323", "Courier New", monospace'
    fontSize: 32
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  h3:
    fontFamily: '"VT323", "Courier New", monospace'
    fontSize: 24
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: '"VT323", "Courier New", monospace'
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: '"VT323", "Courier New", monospace'
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
rounded:
  sm: 0
  md: 0
  lg: 0
spacing:
  sm: 4
  md: 8
  lg: 16
  xl: 32
components:
  button-primary:
    background: "#00FF41"
    color: "#000000"
    border: "1px solid #00FF41"
    padding: "2px 8px"
    cursor: pointer
    hover:
      background: "#000000"
      color: "#00FF41"
      border: "1px solid #00FF41"
  card:
    background: "#000000"
    border: "1px solid #00FF41"
    padding: 0
    box-shadow: none
  table:
    border-collapse: collapse
    width: 100%
    borderColor: "#00FF41"
    header:
      borderBottom: "1px solid #00FF41"
      fontWeight: bold
    row:
      borderBottom: "1px dotted #004D00"
---

# Terminal Design System

## Overview

The **Terminal** design style is a strict adherence to the aesthetic and functional constraints of 1970s–1990s computer terminals. It rejects modern UI trends in favor of raw data representation. The interface is purely textual, utilizing a phosphor-green on black color scheme to mimic monochrome CRT displays. There are no icons, no gradients, and no rounded corners. The goal is maximum information density with zero visual noise. This style is appropriate for developer tools, system logs, configuration interfaces, and data-heavy dashboards where clarity and speed of reading are paramount.

## Colors

The palette is derived from the physical limitations of early phosphor screens.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| `primary` | `#00FF41` | Active text, borders, primary actions, cursors. The standard "phosphor green." |
| `secondary` | `#008F11` | Inactive text, secondary data, disabled states. |
| `tertiary` | `#003B00` | Background highlights, subtle dividers, low-contrast borders. |
| `neutral` | `#000000` | Background canvas. Pure black to simulate the dark glass of a CRT. |
| `muted` | `#004D00` | Placeholders, hints, non-essential metadata. |

**Note:** Do not use white (`#FFFFFF`) for text. It causes excessive glare on black backgrounds and deviates from the CRT standard. Use `#00FF41` for all high-contrast text.

## Typography

Typography is the only visual hierarchy tool available. We rely exclusively on monospaced fonts to ensure alignment and readability of tabular data.

- **Font Family:** `VT323` (preferred for authentic pixel-perfect rendering), `Courier New` (fallback), or `monospace`.
- **Weight:** All text remains at `400` (normal). Bold is achieved by increasing size or using full brightness `#00FF41` rather than font-weight changes, though `bold` is acceptable for headers if the font supports it cleanly.
- **Sizing:**
  - `h1`: 48px (System Title)
  - `h2`: 32px (Section Header)
  - `h3`: 24px (Subsection)
  - `body-md`: 16px (Standard content)
  - `caption`: 12px (Metadata, timestamps)
- **Letter Spacing:** `0`. Monospaced fonts do not require tracking adjustments.

## Layout

- **Grid:** Fixed-width character grid. Content should align to the baseline of the monospace font.
- **Whitespace:** Minimal. Use spacing tokens only for logical grouping. `sm` (4px) for tight lists, `xl` (32px) for major section breaks.
- **Alignment:** Left-aligned for all text. Center alignment is discouraged as it breaks the columnar structure of terminal output.
- **Containers:** No padding inside containers unless necessary for readability. The "card" is essentially a bordered block of text.

## Elevation & Depth

- **Shadows:** None. `box-shadow` is set to `none`.
- **Depth:** Depth is conveyed solely through borders and contrast.
  - Active elements: Bright green (`#00FF41`) with black background.
  - Inactive elements: Darker green (`#008F11`) or black background with dark green border.
  - No overlapping elements with blur or opacity.

## Shapes

- **Corners:** All border-radius values are `0`. Sharp, square edges are mandatory.
- **Borders:** Solid lines only. Dotted lines (`1px dotted #004D00`) may be used for internal table row separators.
- **Icons:** None. Use ASCII characters or Unicode box-drawing characters (e.g., `┌`, `─`, `┐`, `│`, `└`, `┘`) for structural elements if necessary, but prefer text labels.

## Components

### Button Primary
A rectangular block with a solid background.
- **Default:** Black background, Green border, Green text.
- **Hover:** Black background, Green border, Black text, Green background (inverted).
- **Focus:** Dashed green border.
- **Text:** UPPERCASE or Title Case. No icons.

### Card
A bordered rectangle containing text data.
- **Border:** 1px solid `#00FF41`.
- **Background:** `#000000`.
- **Padding:** 0. Content sits directly against the border or uses `sm` spacing.
- **Header:** Text in `h3` size, bolded via brightness.

### Table
- **Structure:** HTML `<table>` with `border-collapse: collapse`.
- **Borders:** Header row has a solid bottom border (`1px solid #00FF41`). Data rows have a dotted bottom border (`1px dotted #004D00`).
- **Text:** Left-aligned, `body-md` size.
- **Selection:** Selected rows have a black background and green text.

### Input Field
- **Border:** 1px solid `#008F11` (default), 1px solid `#00FF41` (focus).
- **Background:** `#000000`.
- **Text:** Green (`#00FF41`).
- **Cursor:** Blinking block cursor (simulated via CSS animation or caret color).
- **Placeholder:** Muted green (`#004D00`).

### Alert/Notification
- **Success:** Green text on black background. Prefix with `[OK]`.
- **Error:** Green text on black background. Prefix with `[ERR]`. (Note: Red is avoided to maintain CRT authenticity, but can be introduced as `#FF0040` if strictly necessary for critical errors, though pure green is preferred for consistency).
- **Warning:** Muted green text. Prefix with `[WARN]`.

## Do's and Don'ts

### Do
- **DO** use monospaced fonts exclusively.
- **DO** maintain high contrast between text and background.
- **DO** use ASCII/Unicode characters for structural decoration.
- **DO** keep interactions immediate and text-based.
- **DO** prioritize data density and alignment.

### Don't
- **DON'T** use rounded corners.
- **DON'T** use gradients or shadows.
- **DON'T** use sans-serif fonts (Inter, Roboto, Helvetica).
- **DON'T** use emojis or SVG icons.
- **DON'T** use white text on black backgrounds (glare).
- **DON'T** use marketing language or decorative fluff.
- **DON'T** use colored backgrounds for buttons (only green/black).