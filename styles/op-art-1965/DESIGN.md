```yaml
---
version: 1.0.0
name: Op-Art / Kinetic Geometric
description: A rigorous, high-contrast visual system derived from 1960s Op Art, prioritizing optical vibration, geometric precision, and the dynamic tension of black and white over decorative color.
colors:
  primary: "#000000"
  secondary: "#FFFFFF"
  tertiary: "#808080"
  neutral: "#F5F5F5"
  muted: "#CCCCCC"
typography:
  h1:
    fontFamily: "Bodoni Moda, Didot, serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "Bodoni Moda, Didot, serif"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 18
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.05em
  body-md:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 12
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.1em
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 4px
  md: 8px
  lg: 16px
  xl: 32px
components:
  button-primary:
    background: "#000000"
    color: "#FFFFFF"
    border: "1px solid #000000"
    borderRadius: 0px
    padding: "12px 24px"
    fontWeight: 700
    letterSpacing: 0.1em
    textTransform: uppercase
    hover:
      background: "#FFFFFF"
      color: "#000000"
      border: "1px solid #000000"
  card:
    background: "#FFFFFF"
    border: "2px solid #000000"
    borderRadius: 0px
    padding: 0px
    boxShadow: "none"
  table:
    border: "1px solid #000000"
    borderRadius: 0px
    header:
      background: "#000000"
      color: "#FFFFFF"
    cell:
      border: "1px solid #000000"
      padding: "12px 16px"
```

# Op-Art / Kinetic Geometric Design System

## Overview
This design system is rooted in the **Op Art** (Optical Art) movement of the 1960s and 70s, championed by figures like Bridget Riley and Victor Vasarely. It rejects softness, warmth, and subtle gradients in favor of **high-contrast geometry**, **visual vibration**, and **mathematical precision**. The interface should feel like a living, breathing optical illusion—static yet dynamic. Content is not "presented"; it is constructed through the interplay of black, white, and strict grid systems.

## Colors
The palette is strictly binary. Color is not used for hierarchy but for **contrast**.

*   **Primary (`#000000`)**: Absolute black. Used for text, borders, and dominant shapes.
*   **Secondary (`#FFFFFF`)**: Absolute white. Used for backgrounds and negative space.
*   **Tertiary (`#808080`)**: Neutral gray. Used sparingly for secondary borders or inactive states, but never for primary content.
*   **Muted (`#CCCCCC`)**: Light gray. Only for subtle grid lines or disabled elements.

**Rule**: Never use color for emphasis. Use weight (boldness) or position.

## Typography
Typography is split between **Editorial Elegance** (Serif) for headlines and **Swiss Modernism** (Sans-Serif) for data.

*   **Headlines (Serif)**: Use `Bodoni Moda` or `Didot`. High contrast between thick and thin strokes creates a sense of rhythm and tension.
*   **Body/UI (Sans-Serif)**: Use `Helvetica` or `Arial`. Neutral, functional, and legible. No rounded corners in fonts.
*   **Caps**: All UI labels and buttons must be UPPERCASE with wide letter-spacing (`0.1em`) to enhance readability and geometric feel.

## Layout
*   **Grid**: Strict, visible grids. Borders are structural, not decorative.
*   **Alignment**: Left-aligned or justified. Never centered for body text.
*   **Whitespace**: Generous but controlled. White space is an active element, not just empty space.
*   **Borders**: All containers must have visible borders (1px or 2px solid black). No floating cards without borders.

## Elevation & Depth
**Flat is mandatory.**
*   **No shadows**.
*   **No gradients**.
*   **No blur**.
*   Depth is achieved through **overlap** and **border weight**. A black border on white creates a "cut-out" effect. A white border on black creates a "highlight" effect.

## Shapes
*   **Rectangles**: The only shape. No circles, no rounded corners.
*   **Lines**: Horizontal and vertical lines are primary design elements.
*   **Patterns**: Subtle geometric patterns (stripes, dots, waves) can be used as backgrounds, but must be low-contrast (e.g., 5% black on white).

## Components

### Button Primary
*   **Shape**: Sharp rectangle.
*   **Style**: Black background, white text, black border.
*   **Hover**: Invert colors (White background, black text, black border).
*   **Effect**: Creates a "negative" state.

### Card
*   **Structure**: White background, 2px black border.
*   **Content**: No padding inside the card itself; padding is part of the content block within.
*   **Divider**: A 1px black line separates sections.

### Table
*   **Header**: Black background, white text, bold.
*   **Rows**: White background, black text, 1px black border on all sides.
*   **Hover**: Row background becomes light gray (`#F5F5F5`).

### Form Input
*   **Style**: White background, 1px black border.
*   **Focus**: 2px black border.
*   **Label**: Uppercase, small font, left-aligned, black.

## Do's and Don'ts

### DO
*   **DO** use high-contrast black and white.
*   **DO** use sharp, geometric shapes.
*   **DO** use serif fonts for headlines to create elegance and tension.
*   **DO** use visible borders and grids.
*   **DO** align everything to a strict grid.

### DON'T
*   **DON'T** use rounded corners (`border-radius > 0`).
*   **DON'T** use drop shadows or blur effects.
*   **DON'T** use pastel colors or gradients.
*   **DON'T** use playful or handwritten fonts.
*   **DON'T** hide borders or make them subtle.
*   **DON'T** use emoji as icons. Use simple geometric symbols (lines, squares, arrows) if icons are needed.