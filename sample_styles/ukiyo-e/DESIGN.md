version: 1.0.0
name: Ukiyo-e
description: A design system rooted in the "Floating World," prioritizing flat planes of color, distinct outlines, and the expressive use of negative space over Western perspective or volumetric shading.
colors:
  primary:
    name: Aka (Red)
    hex: "#C9302C"
    description: Traditional cinnabar or vermillion, used for emphasis, seals, and focal points.
  secondary:
    name: Ai (Blue)
    hex: "#2B4C7E"
    description: Indigo derived from Prussian blue (Prussian blue was later introduced, but indigo is the historical root), used for backgrounds and structural elements.
  tertiary:
    name: Kin (Gold)
    hex: "#D4AF37"
    description: Metallic gold leaf, used sparingly for highlights, borders, or premium accents.
  neutral:
    name: Washi (Paper)
    hex: "#F4F1EA"
    description: The color of traditional handmade paper, serving as the primary canvas.
  muted:
    name: Sumi (Ink)
    hex: "#2C2C2C"
    description: Deep carbon black, used for outlines, text, and defining shapes.
typography:
  h1:
    fontFamily: "'Noto Serif JP', 'Yu Mincho', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  h2:
    fontFamily: "'Noto Serif JP', 'Yu Mincho', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  h3:
    fontFamily: "'Noto Serif JP', 'Yu Mincho', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0px
  body-md:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.2px
  caption:
    fontFamily: "'Noto Sans JP', 'Hiragino Kaku Gothic ProN', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
rounded:
  sm: 2px
  md: 4px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    background: "Kin (Gold)"
    border: "2px solid Sumi (Ink)"
    color: "Sumi (Ink)"
    padding: "8px 24px"
    borderRadius: "0px"
    fontWeight: 700
    textTransform: "none"
  card:
    background: "Washi (Paper)"
    border: "1px solid Sumi (Ink)"
    padding: "24px"
    borderRadius: "0px"
    boxShadow: "none"
  table:
    headerBackground: "Ai (Blue)"
    headerColor: "Washi (Paper)"
    rowBorder: "1px solid Muted (Ink)"
    cellPadding: "12px 16px"
```

# Ukiyo-e Design System

## Overview

The Ukiyo-e design system translates the aesthetic principles of 17th–19th century Japanese woodblock prints into a modern digital interface. It rejects Western chiaroscuro (light/shadow modeling) and linear perspective in favor of **flat color fields**, **bold contour lines**, and **asymmetrical composition**. The interface should feel like a printed artifact: tactile, grounded, and honest about its two-dimensionality.

## Colors

The palette is derived from natural pigments used in woodblock printing. Colors are flat and saturated, avoiding gradients or transparency effects that simulate depth.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Primary (Aka)** | `#C9302C` | Calls to action, active states, seals, critical alerts. |
| **Secondary (Ai)** | `#2B4C7E` | Headers, footers, background sections, structural dividers. |
| **Tertiary (Kin)** | `#D4AF37` | Premium accents, borders, icon highlights. Use sparingly. |
| **Neutral (Washi)** | `#F4F1EA` | Primary background. Simulates textured paper. |
| **Muted (Sumi)** | `#2C2C2C` | Text, outlines, icons, borders. High contrast against Washi. |

**Rules:**
- Never use `rgba` for color mixing. Opacity should be achieved by swapping to a lighter/darker solid color if necessary, but prefer solid blocks.
- Do not use pure black (`#000000`). Use `Sumi` (`#2C2C2C`) to soften the harshness of digital black.
- Do not use pure white (`#FFFFFF`) for backgrounds. Use `Washi` (`#F4F1EA`) to maintain the paper aesthetic.

## Typography

Typography mimics the contrast between hand-carved serif kanji and clean sans-serif modernization.

- **Headings**: Use a high-contrast Serif font (e.g., *Noto Serif JP*, *Yu Mincho*). This reflects the calligraphic roots of the movement.
- **Body**: Use a clean, legible Sans-serif font (e.g., *Noto Sans JP*, *Hiragino Kaku Gothic*). This ensures readability on screens while maintaining a modern utility.
- **Vertical Rhythm**: Align text to a strict grid. Japanese typography often relies on vertical alignment; in horizontal layouts, ensure generous line height to let characters breathe.

## Layout

The layout is defined by **Ma (留白)** – the purposeful use of empty space.

1.  **Asymmetry**: Avoid centered symmetry. Place elements off-center to create dynamic tension.
2.  **Negative Space**: Do not fill every pixel. Allow large areas of `Washi` background to separate content blocks.
3.  **Grid**: Use a modular grid but break it intentionally. Elements should feel "carved" into the layout, not floating.
4.  **No Perspective**: All elements exist on the same Z-plane. Do not use drop shadows to indicate elevation.

## Elevation & Depth

**Flatness is a feature, not a limitation.**

- **No Shadows**: Do not use `box-shadow` with blur. Depth is achieved through color contrast and overlapping shapes.
- **Outlines**: Use `Sumi` borders to define boundaries between elements instead of shadows.
- **Layering**: If layering is required, use solid color blocks with distinct borders. A secondary element can overlap a primary one, separated by a 1px `Sumi` stroke.

## Shapes

- **Rectilinear**: Prefer sharp corners. Rounded corners are minimal.
- **Borders**: Borders are structural. They define the "block" of content, similar to the woodblock carving.
- **Radii**:
  - `sm`: 2px (Subtle softening for small interactive elements)
  - `md`: 4px (Standard for cards/inputs)
  - `lg`: 0px (Buttons, major sections, images)

## Components

### Button Primary
- **Style**: Solid `Kin` background with `Sumi` border.
- **Text**: `Sumi` color, bold serif or sans-serif.
- **Hover**: Invert colors (Background becomes `Sumi`, Text becomes `Kin`).
- **Shape**: Sharp rectangle (0px radius).

### Card
- **Style**: `Washi` background, 1px `Sumi` border.
- **Padding**: Generous padding (24px) to utilize negative space.
- **Image**: Images should be framed with a `Sumi` border. No rounded corners on images.

### Table
- **Header**: `Ai` background, `Washi` text.
- **Rows**: Alternating rows are discouraged; instead, use 1px `Sumi` bottom borders for each row to maintain the "carved line" aesthetic.
- **Borders**: Vertical borders are optional; if used, they should be thin and light gray, not `Sumi`.

## Do's and Don'ts

| Do | Don't |
| :--- | :--- |
| Use flat, solid color blocks. | Use gradients or glassmorphism. |
| Embrace large areas of empty space. | Fill every corner with content or icons. |
| Use bold, distinct outlines. | Use subtle, blurry drop shadows. |
| Align text to a strict, visible grid. | Use floating, unanchored layouts. |
| Use historical color names (Aka, Ai, Kin). | Use generic names (Primary, Secondary, Accent). |
| Keep borders sharp and rectangular. | Use uniform rounded corners everywhere. |