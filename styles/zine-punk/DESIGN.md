---
version: 1.0.0
name: 朋克志 (Punk Zine)
description: A raw, anti-establishment visual language rooted in 1970s DIY ethics, utilizing photocopy aesthetics, jagged typography, and collage techniques to reject corporate polish.
colors:
  primary: "#FF0000"
  secondary: "#000000"
  tertiary: "#FFFFFF"
  neutral: "#333333"
  muted: "#888888"
typography:
  h1:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "48px"
    fontWeight: 900
    lineHeight: "0.9"
    letterSpacing: "-2px"
  h2:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "32px"
    fontWeight: 900
    lineHeight: "1"
    letterSpacing: "-1px"
  h3:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: "1.1"
    letterSpacing: "0px"
  body-md:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: "1.4"
    letterSpacing: "0px"
  caption:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "10px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "1px"
rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
spacing:
  sm: "4px"
  md: "8px"
  lg: "16px"
  xl: "32px"
components:
  button-primary:
    background: "#000000"
    color: "#FFFFFF"
    border: "2px solid #000000"
    padding: "8px 16px"
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "14px"
    fontWeight: 700
    textTransform: "uppercase"
    cursor: "pointer"
    transition: "none"
    box-shadow: "4px 4px 0px #FF0000"
  card:
    background: "#FFFFFF"
    border: "3px solid #000000"
    padding: "16px"
    box-shadow: "none"
    position: "relative"
  table:
    border-collapse: "collapse"
    width: "100%"
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: "12px"
  image:
    filter: "grayscale(100%) contrast(150%) brightness(90%)"
    mix-blend-mode: "multiply"
---

# 朋克志 (Punk Zine) Design System

## Overview
"朋克志" is not a UI kit; it is a visual act of rebellion. Inspired by the cut-and-paste ethos of early punk fanzines (like *Sniffin' Glue* or *Sideburns*), this design system rejects the smoothness, symmetry, and predictability of modern digital interfaces. It embraces the glitch, the photocopy artifact, and the aggressive juxtaposition of text and image. The goal is to make the user feel the texture of the paper and the urgency of the message.

## Colors
The palette is limited to high-contrast, reproducible colors. It mimics the output of a cheap Xerox machine with limited toner.

- **Primary (`#FF0000`)**: Danger, alarm, passion. Used for highlights, underlines, and critical actions.
- **Secondary (`#000000`)**: The ink. Used for borders, text, and structural elements.
- **Tertiary (`#FFFFFF`)**: The paper. The background canvas.
- **Neutral (`#333333`)**: Faded ink. Used for secondary text or disabled states.
- **Muted (`#888888`)**: Photocopy noise. Used for subtle dividers or background texture.

**Rule:** Never use gradients. Never use soft shadows. If it looks "designed," break it.

## Typography
Typography is the voice of the zine. It is loud, jagged, and utilitarian.

- **Font Family**: `'Courier New', Courier, monospace`. This is the font of typewriters and newsprint. It is not elegant; it is honest.
- **Hierarchy**: 
  - **H1**: Massive, tight leading, often overlapping with images.
  - **H2**: Bold, all-caps, often rotated or skewed.
  - **Body**: Readable but raw. Leave generous margins to mimic column layouts.
  - **Caption**: Small, uppercase, tracking wide. Used for credits or disclaimers.

**Rule:** Do not use web fonts that look "clean." If you must use a web font, use a pixel font or a heavily distressed typeface.

## Layout
The layout is grid-based but intentionally broken.

- **Columns**: Use a strict 12-column grid, but allow content to spill over.
- **Margins**: Wide margins to mimic the white space of printed zines.
- **Alignment**: Left-aligned text. Ragged right edges.
- **Overlap**: Allow images to overlap text. Allow cards to overlap each other.
- **Rotation**: Subtle rotation (1-3 degrees) on elements to simulate hand-cut placement.

**Rule:** Symmetry is boring. Asymmetry is truth.

## Elevation & Depth
Depth is achieved through hard shadows and borders, not blur.

- **Shadows**: Hard, solid, offset shadows (e.g., `box-shadow: 4px 4px 0px #000000`). No blur.
- **Borders**: Thick, black borders (2-4px).
- **Layering**: Use `z-index` to create physical stacking effects. Elements should look like they are taped to the page.

**Rule:** No `backdrop-filter`. No transparency. Everything is opaque and physical.

## Shapes
- **Borders**: Sharp, 90-degree angles. No rounded corners.
- **Cutouts**: Use `clip-path` to create jagged, torn-paper edges on images and cards.
- **Icons**: Hand-drawn or pixelated. No SVG icons with smooth curves. Use ASCII art or simple geometric shapes.

**Rule:** If it has a curve, it's suspect. Make it straight or jagged.

## Components

### Button (Primary)
A block of black ink with red warning.
- **Background**: `#000000`
- **Color**: `#FFFFFF`
- **Border**: 2px solid `#000000`
- **Shadow**: `4px 4px 0px #FF0000`
- **Hover**: Invert colors. Background `#FF0000`, Color `#000000`. No transition.

### Card
A cut-out piece of paper.
- **Background**: `#FFFFFF`
- **Border**: 3px solid `#000000`
- **Padding**: 16px
- **Shadow**: `none`
- **Effect**: Add a subtle noise texture overlay to simulate photocopy grain.

### Table
A ledger of facts.
- **Border**: 1px solid `#000000`
- **Header**: Bold, underlined, background `#000000`, color `#FFFFFF`.
- **Rows**: Alternating background colors (`#FFFFFF` and `#F0F0F0`).

### Image
A pasted photograph.
- **Filter**: `grayscale(100%) contrast(150%)`
- **Border**: 2px solid `#000000`
- **Placement**: Often rotated slightly.

## Do's and Don'ts

### Do
- **Embrace Imperfection**: Use CSS filters to add noise, grain, or distortion.
- **Use High Contrast**: Black on white, red on black.
- **Hand-Cut Aesthetics**: Use `clip-path` to create irregular shapes.
- **Typewriter Feel**: Stick to monospace fonts for headings and body text.
- **Tape Effects**: Use pseudo-elements (`::before`, `::after`) to simulate masking tape holding elements in place.

### Don't
- **Don't Use Smooth Curves**: Avoid `border-radius` and smooth SVG paths.
- **Don't Use Soft Shadows**: No `box-shadow` with `blur > 0`.
- **Don't Use Elegant Fonts**: No serif fonts like Garamond or sans-serifs like Helvetica.
- **Don't Over-Decorate**: Less is more. The message is the design.
- **Don't Use Gradients**: Flat colors only.
- **Don't Use Emoji**: They are too polished. Use text symbols (e.g., `*`, `!`, `?`, `#`).