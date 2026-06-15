---
version: alpha
name: Bauhaus 1919
description: Form follows function. Primary colors on cream. Geometric composition. Hard shadows, zero radius, no gradients.
colors:
  primary: "#1A1A1A"
  secondary: "#C43838"
  tertiary: "#2859A6"
  quaternary: "#D4A017"
  neutral: "#F4F1EA"
  neutral-dark: "#E8E4D8"
  ink: "#1A1A1A"
  muted: "#666666"
typography:
  h1:
    fontFamily: "Akzidenz Grotesk"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.03em"
  h2:
    fontFamily: "Akzidenz Grotesk"
    fontSize: "1.75rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  h3:
    fontFamily: "Akzidenz Grotesk"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.02em"
  body-md:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
  caption:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.1em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 48px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: "14px 28px"
    fontWeight: 700
    letterSpacing: "0.05em"
    textTransform: uppercase
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
  card:
    backgroundColor: "{colors.neutral}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  card-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  table:
    border: "2px solid {colors.primary}"
    borderRadius: "{rounded.sm}"
  table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    fontWeight: 700
    textTransform: uppercase
    letterSpacing: "0.05em"
    fontSize: "0.75rem"
  shadow-hard:
    boxShadow: "6px 6px 0 {colors.secondary}"
---

## Overview

Bauhaus Weimar (1919-1933). The school that dissolved the boundary between art and industry. Every visual element must justify its existence through function — if it doesn't serve the content, it doesn't exist.

Anti-AI principle: **Inter + glassmorphism + purple gradient is the exact opposite of Bauhaus.** Where AI default is soft, blurred, and indistinct, Bauhaus is hard-edged, geometric, and unambiguous.

## Colors

Three primaries + black + cream. No tints, no shades between, no gradients. The palette is deliberately limited — this is not a limitation but a design discipline.

- **Primary (#1A1A1A):** Ink black. The structural element. Borders, text, anchors.
- **Secondary (#C43838):** Bauhaus red. The sole accent for emphasis. Buttons, highlights, warnings.
- **Tertiary (#2859A6):** Bauhaus blue. Secondary accent for data differentiation only.
- **Quaternary (#D4A017):** Bauhaus yellow. Tertiary accent — use sparingly.
- **Neutral (#F4F1EA):** Unbleached paper cream. The background of everything.
- **Neutral-dark (#E8E4D8):** Aged paper. Alternate row backgrounds.

## Typography

Two faces only. Akzidenz Grotesk for structure (headings, labels, buttons). IBM Plex Mono for data (body text, tables, metadata). The monospace body is a deliberate choice — data in monospace has a mechanical honesty that proportional fonts lack.

Font substitution: If Akzidenz Grotesk is unavailable, use **Be Vietnam Pro** (geometric, similar x-height). If IBM Plex Mono is unavailable, use **JetBrains Mono**.

## Layout

No centering. Left-align everything. Content starts at the left margin and flows right and down. Use a strict grid — 12 columns with 16px gutters. Headlines are full-width. Data is tabular. Navigation is horizontal top bar, no sidebar.

## Elevation & Depth

No soft shadows. No blur. Depth is expressed through:
- **Hard offset shadows** (6px 6px 0 #C43838) — for interactive elements
- **Borders** (2px solid #1A1A1A) — for structural grouping
- **Background contrast** (#1A1A1A on #F4F1EA) — for emphasis

## Shapes

Zero radius on everything. A rectangle is honest. Rounded corners soften and obscure — the opposite of Bauhaus intent. Circles are allowed only as geometric elements (not as border-radius), e.g., a red circle as a bullet marker.

## Components

### Button

Primary: black rectangle, cream text, hard red shadow. On hover: red rectangle. No transition animation — states are immediate, not gradual.

### Table

The primary data display. Heavy borders, alternating cream/aged-paper rows, uppercase monospace headers. Data density is a virtue, not a vice.

### Card

Borders define cards, not shadows or backgrounds. A card with a red left border is an alert. A card with all-border is a container. No subtle gray backgrounds.

## Do's and Don'ts

**Do:**
- Use hard edges, geometric shapes, and primary colors
- Let content density speak — don't pad to make it "breathe"
- Use uppercase monospace for metadata and labels
- Use the hard shadow for interactive elements
- Differentiate with color and shape, not with opacity or blur

**Don't:**
- Use any border-radius > 0px
- Use any box-shadow with blur > 0
- Use any linear-gradient
- Use Inter, Roboto, or Helvetica Neue
- Use any emoji as icons
- Use marketing language ("seamless", "innovative", "future")
- Use semi-transparent backgrounds (rgba with alpha < 1)
