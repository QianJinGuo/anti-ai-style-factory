---
version: 1.0.0
name: "Signboard Script"
description: "A utilitarian, high-contrast typographic system rooted in the hand-painted commercial signage of the 20th century, prioritizing immediate legibility and local cultural context over universal standardization."
colors:
  primary: "#D40000"  # Vermilion Red (High visibility, traditional ink)
  secondary: "#0033A0" # Prussian Blue (Contrast, authority)
  tertiary: "#FFB800" # Ochre Yellow (Highlight, warmth)
  neutral: "#1A1A1A"  # Charcoal (Text base, softer than black)
  muted: "#F4F1EA"    # Aged Paper (Background, warm off-white)
typography:
  h1:
    fontFamily: "'Noto Serif Display', 'Songti SC', 'SimSun', serif"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "'Noto Serif Display', 'Songti SC', 'SimSun', serif"
    fontSize: "2rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "'Noto Serif Display', 'Songti SC', 'SimSun', serif"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "0.01em"
  body-md:
    fontFamily: "'Noto Sans', 'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.02em"
  caption:
    fontFamily: "'Courier New', 'Menlo', monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    background: "#D40000"
    color: "#F4F1EA"
    border: "2px solid #1A1A1A"
    borderRadius: 0
    padding: "12px 24px"
    fontWeight: 700
    textTransform: "none"
  card:
    background: "#FFFFFF"
    border: "1px solid #1A1A1A"
    borderRadius: 0
    boxShadow: "4px 4px 0px #1A1A1A"
  table:
    headerBackground: "#0033A0"
    headerColor: "#FFFFFF"
    rowAlternating: "#F4F1EA"
    border: "1px solid #1A1A1A"
---

# Signboard Script Design System

## Overview
This design system draws inspiration from the global history of hand-painted commercial signage (1900–1980). It rejects the homogenized, digital-first aesthetic of modern UI in favor of a tactile, grounded approach. The system emphasizes **localization** (using region-appropriate serif/sans-serif pairings), **functionality** (high contrast for street-level readability), and **human touch** (imperfections in spacing and alignment). It is not "friendly"; it is authoritative and legible.

## Colors
The palette is derived from traditional oil-based inks and painted wood. Colors are flat, opaque, and highly saturated to cut through visual noise.

- **Primary (Vermilion Red `#D40000`)**: Used for primary actions and key headlines. Historically associated with good fortune and visibility in East Asian signage, and urgency in Western contexts.
- **Secondary (Prussian Blue `#0033A0`)**: Used for secondary information and footers. Provides a cool contrast to the warm primary.
- **Tertiary (Ochre Yellow `#FFB800`)**: Used for highlights, warnings, or accents. Highly visible against both dark and light backgrounds.
- **Neutral (Charcoal `#1A1A1A`)**: Never use pure black (`#000000`). Charcoal mimics the slight bleed of ink on paper.
- **Muted (Aged Paper `#F4F1EA`)**: The background color. Avoid pure white (`#FFFFFF`) for large surfaces to reduce eye strain and mimic physical materials.

## Typography
Typography is the hero. We do not use uniform geometric sans-serifs (like Inter or Roboto). We use typefaces that have character, history, and regional relevance.

- **Headings**: Use **Serif** typefaces that mimic brush strokes or chiseled stone. In CJK contexts, this is `SimSun` or `Songti`; in Latin contexts, `Georgia` or `Times New Roman`. The goal is weight and presence.
- **Body**: Use a **Sans-Serif** that is clean but not sterile. `Microsoft YaHei` or `PingFang SC` for CJK; `Arial` or `Helvetica` (if forced) for Latin. Avoid rounded sans-serifs.
- **Captions/Metadata**: Use **Monospace** (`Courier New`). This references the typewritten labels often found on physical signage or shipping manifests.

**Key Principle**: Do not justify text. Left-align or ragged-right to maintain the natural flow of hand-painted lettering.

## Layout
- **Grid**: Rigid, rectangular blocks. No curved containers.
- **Alignment**: Strictly left-aligned or centered. Avoid justified text.
- **Whitespace**: Generous but structured. Spacing is measured in 8px increments but often broken by the natural width of characters.
- **Borders**: Use 1px or 2px solid lines. No gradients. No soft shadows.

## Elevation & Depth
Depth is achieved through **hard shadows** and **borders**, not blur.

- **Shadows**: `box-shadow: 4px 4px 0px #1A1A1A;` (No blur radius).
- **Borders**: Use borders to define hierarchy. A thick border on a primary element, a thin border on secondary.
- **Layering**: Elements sit on top of each other with clear, hard edges. No overlapping transparency.

## Shapes
- **Corners**: Always **0px**. Square corners reflect the brush strokes of straight lines and the physical constraints of wood/metal signs.
- **Icons**: Line icons with uniform stroke width (2px). No filled icons. No gradients. No rounded icon containers.

## Components

### Button Primary
- **Shape**: Square, hard edges.
- **Style**: Solid primary color background, bold text, hard border.
- **Interaction**: On hover, shift the button 2px right and 2px down, and move the shadow to `2px 2px 0px #1A1A1A` to simulate a physical press.

### Card
- **Shape**: Rectangular.
- **Style**: White background, 1px black border, hard offset shadow.
- **Content**: Header with h2, body with p, footer with caption. No images inside the card unless they are framed by a border.

### Table
- **Style**: Grid lines visible.
- **Header**: Dark blue background, white text, uppercase.
- **Rows**: Alternating background colors (White / Aged Paper).
- **Borders**: 1px solid black lines between all cells.

## Do's and Don'ts

### Do
- **DO** use high-contrast color combinations (Red/White, Blue/Yellow).
- **DO** use serif fonts for headings to convey authority and tradition.
- **DO** use hard, offset shadows to create depth.
- **DO** use square corners for all interactive elements.
- **DO** ensure text is left-aligned for natural reading flow.

### Don't
- **DON'T** use rounded corners (`border-radius > 0`).
- **DON'T** use blur effects (`backdrop-filter`, `box-shadow` with blur).
- **DON'T** use purple/blue gradients.
- **DON'T** use Inter, Roboto, Poppins, or Helvetica Neue as primary fonts.
- **DON'T** use emoji as icons.
- **DON'T** use marketing buzzwords ("Seamless", "Revolutionary"). Use clear, descriptive language.