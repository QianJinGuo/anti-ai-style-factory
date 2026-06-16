```yaml
---
version: 1.0.0
name: Bauhaus Dessau
description: "A rigorous system of industrial geometry where form follows function, stripping away ornament to reveal the truth of material and structure."
colors:
  primary: "#D22B2B" # Bauhaus Red
  secondary: "#0055A4" # Industrial Blue
  tertiary: "#F4C430" # Prismatic Yellow
  neutral: "#F5F5F0" # Unbleached Canvas
  muted: "#8C8C8C" # Concrete Grey
  dark: "#1A1A1A" # Ink Black
typography:
  h1:
    fontFamily: "Univers 75 Black, Helvetica Neue, Arial"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Univers 65 Bold, Helvetica Neue, Arial"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Univers 55 Roman, Helvetica Neue, Arial"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0em"
  body-md:
    fontFamily: "Univers 45 Light, Helvetica Neue, Arial"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: "0.01em"
  caption:
    fontFamily: "Univers 55 Roman, Helvetica Neue, Arial"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
    textTransform: "uppercase"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    backgroundColor: "#D22B2B"
    color: "#F5F5F0"
    border: "1px solid #1A1A1A"
    borderRadius: 0px
    padding: "12px 24px"
    fontWeight: 700
    textTransform: "uppercase"
    letterSpacing: "0.05em"
    transition: "none"
  card:
    backgroundColor: "#FFFFFF"
    border: "1px solid #1A1A1A"
    borderRadius: 0px
    padding: "0px"
    boxShadow: "none"
  table:
    borderCollapse: "collapse"
    borderColor: "#1A1A1A"
    borderWidth: "1px"
    headerBackground: "#0055A4"
    headerColor: "#FFFFFF"
    rowHoverBackground: "#F5F5F0"
```

# Bauhaus Dessau Design System

## Overview

This design language is rooted in the Dessau period of the Bauhaus school (1925–1932), a time when the movement shifted from expressionist craft to industrial standardization. The aesthetic is characterized by the rejection of historical ornamentation in favor of geometric purity, functional clarity, and universal legibility. It treats digital interfaces as architectural structures: grids are visible, typography is utilitarian, and color is used structurally rather than decoratively. The goal is not to "delight" the user, but to inform them with maximum efficiency and minimum friction.

## Colors

The palette is derived from the primary triad taught at the Bauhaus workshop, combined with industrial neutrals. Colors are flat, saturated, and opaque. No gradients. No transparency effects.

*   **Bauhaus Red (`#D22B2B`)**: Used for primary actions, critical alerts, and structural anchors. It commands attention without ambiguity.
*   **Industrial Blue (`#0055A4`)**: Used for secondary information, links, and data visualization. It provides stability and depth without the softness of pastel blues.
*   **Prismatic Yellow (`#F4C430`)**: Used sparingly for highlights, warnings, or to draw the eye to specific data points. It serves as a visual accent against the monochrome base.
*   **Unbleached Canvas (`#F5F5F0`)**: The primary background color. It mimics the texture of raw paper or canvas, reducing eye strain compared to pure white and grounding the interface in material reality.
*   **Concrete Grey (`#8C8C8C`)**: Used for disabled states, secondary text, and grid lines.
*   **Ink Black (`#1A1A1A`)**: Used for primary text and borders. It is never pure black (`#000000`) to allow for slight visual breathing room while maintaining high contrast.

## Typography

Typography is the voice of the interface. We reject decorative typefaces in favor of **Univers** (or closest web-safe alternatives like Helvetica Neue/Arial). The type system is modular, relying on weight and size rather than italics or underlines for emphasis.

*   **Hierarchy**: Established strictly through scale and weight.
*   **H1**: `Univers 75 Black`. Massive, imposing, and structural. Used for page titles only.
*   **H2**: `Univers 65 Bold`. Used for section headers.
*   **Body**: `Univers 45 Light`. High readability, generous line height.
*   **Caption**: `Univers 55 Roman` in uppercase. Used for metadata, labels, and dates.
*   **Alignment**: Left-aligned for body text. Justified text is prohibited as it creates uneven word spacing that disrupts the grid.

## Layout

The layout is governed by a strict **8px baseline grid** and a **12-column modular grid**.

*   **Visibility**: Grid lines should be implied by the alignment of elements, but can be made visible using thin `1px` lines in `#8C8C8C` for design prototypes to emphasize structural integrity.
*   **Whitespace**: Whitespace is not empty space; it is an active design element. Margins are generous (minimum 32px) to allow content to breathe.
*   **Asymmetry**: While the grid is symmetric, content distribution may be asymmetric to create dynamic tension, provided balance is maintained.

## Elevation & Depth

Depth is achieved through **layering** and **bordering**, not shadows.

*   **No Shadows**: `box-shadow` with blur is strictly prohibited. It introduces ambiguity about what is flat and what is elevated.
*   **Borders**: All interactive elements and containers have a `1px solid #1A1A1A` border. This clearly defines the boundary of an element against the background.
*   **Overlaps**: When elements overlap, the one "on top" is defined by its background color covering the element below, or by a distinct border.

## Shapes

*   **Rectangles**: All components are rectangular.
*   **Zero Radius**: `border-radius: 0px`. Rounded corners soften the visual language and hide the underlying structure. Sharp corners emphasize precision and industrial manufacturing.
*   **Lines**: Horizontal and vertical lines are used extensively to separate content areas. Diagonal lines are used only in abstract graphic elements or data visualization.

## Components

### Button Primary
*   **Shape**: Sharp rectangle.
*   **Style**: Solid `#D22B2B` background, `#F5F5F0` text.
*   **Border**: `1px solid #1A1A1A`.
*   **Interaction**: On hover, invert colors (White background, Red text). No fade transitions. Instant change.
*   **Text**: Uppercase, bold, spaced out (`letter-spacing: 0.05em`).

### Card
*   **Structure**: A container with a white background and a black border.
*   **Padding**: Content inside is padded with `24px`.
*   **Header**: If the card has a header, it is separated by a `1px` black line.
*   **No Elevation**: The card sits flat on the canvas.

### Table
*   **Headers**: Solid `#0055A4` background, white text, uppercase.
*   **Rows**: Alternating row colors are prohibited. Use a `1px` bottom border for each row.
*   **Hover**: On hover, the row background turns `#F5F5F0`.
*   **Alignment**: Numbers right-aligned; text left-aligned.

### Form Input
*   **Style**: Transparent background, `1px solid #8C8C8C` border.
*   **Focus**: On focus, border turns `#D22B2B`. No glow.
*   **Label**: Positioned above the input, uppercase, small size, `#1A1A1A` color.

## Do's and Don'ts

### Do
*   **Do** use the grid to align every element.
*   **Do** use primary colors to indicate function (Red = Action, Blue = Info).
*   **Do** keep typography simple and legible.
*   **Do** use high contrast between text and background.
*   **Do** treat whitespace as a structural element.

### Don't
*   **Don't** use rounded corners.
*   **Don't** use drop shadows or blur effects.
*   **Don't** use gradients.
*   **Don't** use decorative fonts (serifs, script, display fonts).
*   **Don't** use emojis or icon-only buttons.
*   **Don't** use marketing buzzwords in microcopy. Be direct and factual.