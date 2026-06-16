---
version: 1.0.0
name: Streamline Modern (流线型现代)
description: A design language derived from 1930s aerodynamic industrial design, prioritizing horizontal velocity, polished metal surfaces, and boat-tail silhouettes to convey speed and efficiency in static interfaces.
colors:
  primary:
    name: "Chromium Silver"
    hex: "#E0E0E0"
    usage: "Primary surfaces, metallic highlights, active states"
  secondary:
    name: "Gunmetal"
    hex: "#2C3E50"
    usage: "Primary text, heavy structural elements, contrast borders"
  tertiary:
    name: "Oxblood Red"
    hex: "#8B0000"
    usage: "Call-to-action accents, error states, focal points"
  neutral:
    name: "Aluminum White"
    hex: "#F5F5F5"
    usage: "Backgrounds, card surfaces, disabled states"
  muted:
    name: "Oxidized Brass"
    hex: "#B5A642"
    usage: "Secondary text, borders, hover states"
typography:
  h1:
    fontFamily: "'DIN Alternate', 'Futura', 'Century Gothic', sans-serif"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "'DIN Alternate', 'Futura', 'Century Gothic', sans-serif"
    fontSize: "36px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "'DIN Alternate', 'Futura', 'Century Gothic', sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: "1.3"
    letterSpacing: "0.02em"
  body-md:
    fontFamily: "'DIN Alternate', 'Futura', 'Century Gothic', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.6"
    letterSpacing: "0.01em"
  caption:
    fontFamily: "'DIN Alternate', 'Futura', 'Century Gothic', sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: "1.4"
    letterSpacing: "0.05em"
    textTransform: "uppercase"
rounded:
  sm: "2px"
  md: "4px"
  lg: "0px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
components:
  button-primary:
    style: "Horizontal pill shape, metallic gradient background (silver to dark gray), sharp right edge, text in uppercase, bold. No shadow."
  card:
    style: "Rectangular with extreme left-right elongation. Subtle 1px solid border in Gunmetal. Background is Aluminum White. No border radius on top/bottom, slight radius on left/right only if mimicking a tail."
  table:
    style: "Striped rows with alternating Aluminum White and very light gray. Borders are thin 1px lines. Headers are uppercase, tracked out, aligned left."
  input:
    style: "Underline only (bottom border). No box. Text aligns with the line. Focus state is a solid Oxblood Red underline."
---

# Streamline Modern Design System

## Overview
Streamline Modern is an interface philosophy rooted in the Aerodynamic Age of the 1930s and 40s. It rejects the boxy rigidity of early digital design in favor of horizontal momentum. The aesthetic mimics the fuselage of streamlined trains, ships, and automobiles. Interfaces should feel like they are moving forward, even when static. The visual language relies on polished metals, sharp geometric precision, and a distinct lack of decorative fluff. Every element must serve the illusion of speed and industrial efficiency.

## Colors
The palette is strictly metallic and industrial. We avoid vibrant, digital colors.

- **Chromium Silver (#E0E0E0)**: The primary surface color. It represents polished steel and aluminum. Use for buttons, active tabs, and metallic accents.
- **Gunmetal (#2C3E50)**: The text color. It provides high contrast against silver and white, mimicking the dark recesses of machinery.
- **Oxblood Red (#8B0000)**: The accent color. Used sparingly for critical actions or warnings, referencing the paint colors of luxury streamlined vehicles.
- **Aluminum White (#F5F5F5)**: The background. It is not pure white, but a slightly warm, matte metal finish to reduce glare and enhance the metallic feel.
- **Oxidized Brass (#B5A642)**: Used for secondary information or borders, adding a touch of vintage industrial warmth without breaking the monochromatic metal theme.

## Typography
We reject soft, humanist sans-serifs. The typography must be geometric, mechanical, and authoritative.

- **Font Family**: `'DIN Alternate'` is the primary choice. If unavailable, use `'Futura'` or `'Century Gothic'`. These fonts are based on geometric circles and straight lines, reflecting the engineering precision of the era.
- **Headings**: Tight letter-spacing (`-0.02em`) to create a solid, block-like appearance.
- **Body Text**: Slightly loose letter-spacing (`0.01em`) for readability.
- **Captions**: Uppercase and widely tracked (`0.05em`) to mimic engraved metal labels or technical schematics.

## Layout
The layout must emphasize horizontal lines.

- **Horizontal Flow**: Content should flow from left to right with clear visual pathways.
- **Elongated Containers**: Cards and sections should be wider than they are tall. Avoid square blocks.
- **Grid**: A strict 12-column grid, but elements should span multiple columns to create long, horizontal bands.
- **Alignment**: Left-aligned text. Right-aligned numerical data.

## Elevation & Depth
We do not use soft, colored shadows. Depth is achieved through:

- **Contrast**: Using darker shades of gray/silver for lower layers.
- **Borders**: Thin, 1px solid lines in Gunmetal to define edges.
- **Gradient**: Subtle linear gradients on metallic surfaces to simulate light reflecting off curved metal. The gradient should be vertical (top to bottom) to simulate overhead lighting.

## Shapes
- **No Circular Corners**: Avoid rounded corners on cards and containers. Use sharp 90-degree angles or extreme horizontal rounding (pill shapes) only for buttons.
- **Streamlined Curves**: Use subtle curves on the right edge of containers to mimic the "boat-tail" rear of a streamlined vehicle.
- **Lines**: Use horizontal rules extensively to separate content, reinforcing the sense of horizontal movement.

## Components

### Button-Primary
- **Shape**: Horizontal pill shape.
- **Background**: Linear gradient from Chromium Silver (top) to Gunmetal (bottom).
- **Text**: Uppercase, bold, Gunmetal color.
- **Border**: 1px solid Gunmetal.
- **Hover**: Gradient reverses (Gunmetal top, Silver bottom) to simulate a change in light angle.

### Card
- **Shape**: Rectangle with sharp corners.
- **Background**: Aluminum White.
- **Border**: 1px solid Gunmetal.
- **Shadow**: None. Use a 1px inner shadow for depth if necessary.
- **Content**: Headings in Chromium Silver, body in Gunmetal.

### Table
- **Headers**: Uppercase, tracked out, Oxblood Red background, White text.
- **Rows**: Alternating Aluminum White and very light gray.
- **Borders**: 1px solid Gunmetal lines between rows.
- **Data**: Right-aligned for numbers, left-aligned for text.

### Input
- **Style**: Underline only. No box.
- **Border**: 1px solid Gunmetal.
- **Focus**: 2px solid Oxblood Red underline.
- **Placeholder**: Muted Brass color, italicized.

## Do's and Don'ts

### Do
- Use horizontal lines to guide the eye.
- Emphasize metallic textures and gradients.
- Use geometric, sans-serif fonts.
- Keep the interface clean and uncluttered.
- Use Oxblood Red sparingly for focus.

### Don't
- Use rounded corners on cards or containers.
- Use soft, blurred shadows.
- Use vibrant, non-metallic colors (e.g., bright blue, green, purple).
- Use serif fonts.
- Use emoji or decorative icons.
- Use marketing jargon. Keep text technical and precise.