---
version: alpha
name: Brutalist Web
description: Raw HTML. Exposed structure. Monospace everything. No decoration, no pretense. What you see is what the machine sees.
colors:
  primary: "#000000"
  secondary: "#FF0000"
  neutral: "#FFFFFF"
  neutral-dark: "#F0F0F0"
  code-bg: "#1A1A1A"
  code-text: "#00FF00"
  link: "#0000EE"
  visited: "#551A8B"
typography:
  h1:
    fontFamily: "Courier New"
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0em"
  h2:
    fontFamily: "Courier New"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0em"
  body-md:
    fontFamily: "Courier New"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: "0em"
  caption:
    fontFamily: "Courier New"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0em"
  code:
    fontFamily: "Courier New"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    border: "2px solid {colors.primary}"
    fontWeight: 700
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral}"
    border: "2px solid {colors.secondary}"
  link:
    color: "{colors.link}"
    textDecoration: underline
  link-visited:
    color: "{colors.visited}"
  border-raw:
    border: "3px solid {colors.primary}"
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.code-text}"
    padding: "{spacing.lg}"
---

## Overview

Brutalist Web (2016-now). Named after Brutalist architecture — exposed concrete, no facade, no ornament. The HTML itself is the design. A `<table>` is displayed as a table, not restyled into cards. A form uses native elements. The browser default is the style system.

Anti-AI principle: **AI default is to beautify — to smooth, round, gradient, and polish.** Brutalism rejects all of that. The rawness IS the aesthetic. An AI cannot be "casually raw" — it either generates raw HTML by instruction or it defaults to polish.

## Colors

Black, white, red. Period. Blue for links (browser default). Green for terminal code blocks. No other colors. No tints. No pastels.

- **Primary (#000000):** Black. Everything structural.
- **Secondary (#FF0000):** Pure red. Alerts only. Used exactly once per page.
- **Code-bg (#1A1A1A):** Near-black for code blocks.
- **Code-text (#00FF00):** Terminal green. Code content only.

## Typography

One face: Courier New. The system monospace. It is ugly and that is the point. Every character occupies the same width — code, headings, body text, everything. Weight contrast is the only hierarchy tool.

No web fonts. No Google Fonts. No CDN requests. The page loads from system fonts only.

## Layout

No grid. No flexbox. Content flows vertically. Headers are full-width `<h1>`. Data is in `<table>`. Navigation is a horizontal list. The layout is what HTML does by default — plus borders.

Tables have thick borders (3px solid black). This is not "table styling" — it IS the table.

## Elevation & Depth

No shadows. No blur. Depth is expressed through:
- **Thick borders** (3px solid black) — structural grouping
- **Background contrast** (black on white) — emphasis
- **Literal stacking** — elements above/below, not layered

## Shapes

Zero radius. Elements are rectangles. No circles. No curves. A button is a bordered rectangle. An input is a bordered rectangle. Everything is a rectangle.

## Components

### Button

Black border, black text, white background. Thick border (2px). On hover: black fill, white text. No animation.

### Table

3px solid black border. Visible cell borders. This is a data table — the borders ARE the design. No alternating row colors, no rounded corners, no hover states.

### Link

Browser default blue. Underlined. Visited: purple. No hover color change.

### Code Block

Black background, green text. Padding. Monospace. This is a terminal inside a web page.

## Do's and Don'ts

**Do:**
- Use `<table>` for tabular data with visible borders
- Use system fonts only (Courier New)
- Use thick borders for grouping
- Leave HTML semantics visible (headers look like headers, lists look like lists)
- Use monospace for ALL text — headings, body, labels

**Don't:**
- Use any border-radius > 0px
- Use any box-shadow
- Use any gradient
- Use any web font
- Use any CSS framework (Tailwind, Bootstrap)
- Use any decoration that doesn't come from HTML itself
- Use SVG icons — use text characters instead (> for arrow, [x] for close)
