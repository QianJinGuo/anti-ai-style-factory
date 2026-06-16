```yaml
---
version: "1.0.0"
name: "Gothic Cathedral"
description: "A design system derived from High Gothic architecture, emphasizing verticality, structural honesty, and the interplay of light and shadow through stone and glass."
colors:
  primary:
    name: "Limestone"
    value: "#E8E4D9"
    description: "The base stone, warm and textured, providing a neutral canvas for structural elements."
  secondary:
    name: "Deep Lapis"
    value: "#1A2B4C"
    description: "Inspired by the cobalt blue in medieval stained glass, used for primary actions and headings."
  tertiary:
    name: "Gold Leaf"
    value: "#C5A059"
    description: "Gilded accents for borders, icons, and highlights, representing divine light."
  neutral:
    name: "Charcoal Mortar"
    value: "#2C2C2C"
    description: "Dark grout and shadow, used for body text and high-contrast elements."
  muted:
    name: "Faded Fresco"
    value: "#9A958A"
    description: "Weathered stone and dust, used for secondary text and disabled states."
typography:
  h1:
    fontFamily: '"UnifrakturMaguntia", "Old English Text MT", serif'
    fontSize: 3.5rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: '"UnifrakturMaguntia", "Old English Text MT", serif'
    fontSize: 2.5rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: '"Cinzel", serif'
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.05em
  body-md:
    fontFamily: '"Libre Baskerville", serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: '"Cinzel", serif'
    fontSize: 0.75rem
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.1em
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
    style: "solid fill with gold border, uppercase serif text"
  card:
    style: "bordered panel with header accent line, no shadow"
  table:
    style: "grid lines, alternating muted backgrounds, serif headers"
```

# Gothic Cathedral Design System

## Overview

This design system is not merely aesthetic; it is architectural. It draws directly from the **High Gothic** period (1140–1500), prioritizing **verticality** to draw the eye upward, **structural transparency** where support is visible, and **light as substance**. Unlike modern interfaces that float in void space, this system grounds content in a heavy, stone-like hierarchy. It rejects the ephemeral and the flat in favor of weight, texture, and historical gravity.

## Colors

The palette is derived from the materials of the cathedral itself: stone, lead, gold leaf, and stained glass.

*   **Primary (Limestone `#E8E4D9`)**: The background. Not pure white, but warm, imperfect stone. It reduces eye strain and mimics the ambient light filtering through the nave.
*   **Secondary (Deep Lapis `#1A2B4C`)**: The dominant text and action color. Derived from the deep blues of the Virgin Mary’s robes in 13th-century iconography. High contrast against limestone.
*   **Tertiary (Gold Leaf `#C5A059`)**: Used sparingly for borders, active states, and critical highlights. It represents the divine light entering the structure. Avoid flat yellow; use metallic, desaturated gold.
*   **Neutral (Charcoal Mortar `#2C2C2C`)**: Body text. Dark enough to be legible on stone, but softer than pure black to maintain the aged parchment feel.
*   **Muted (Faded Fresco `#9A958A`)**: Secondary information, captions, and disabled states. Represents weathered stone and dust.

## Typography

We reject sans-serif uniformity. The typography must evoke the hand of the scribe and the chisel of the mason.

*   **Headings**: Use **Blackletter** (Fraktur) styles for H1/H2. This is not for readability alone, but for visual weight and historical signifier. The font should feel carved.
*   **Subheadings**: Use **Cinzel** or similar Roman-inspired serif caps. This represents the classical influence creeping into Gothic architecture (Transitional Gothic).
*   **Body**: Use **Libre Baskerville** or **EB Garamond**. High-contrast serifs that mimic the vertical strokes of blackletter but remain legible for long-form reading.
*   **Captions**: Small caps with wide tracking (`letter-spacing: 0.1em`) to mimic inscriptions on stone plinths.

**Anti-AI Rule**: Never use Inter, Roboto, or Helvetica. The interface must feel ancient, not contemporary.

## Layout

The layout is **hierarchical** and **vertical**.

*   **Grid**: Use a strict 12-column grid, but treat columns like pillars. They are structural supports, not just containers.
*   **Verticality**: Content should feel tall. Use generous top margins. The eye should travel down the page like a gaze moving down a nave toward the altar.
*   **Centering**: Major content blocks are often centered, reflecting the axial symmetry of cathedral plans.
*   **Borders**: Use double borders or triple lines to mimic tracery. A single thin line is insufficient; it lacks the weight of stone.

## Elevation & Depth

We do not use soft shadows (`box-shadow: 0 4px 12px rgba(0,0,0,0.1)`). Shadows are too modern and digital.

*   **Hard Shadows**: Use `box-shadow: 4px 4px 0px #2C2C2C` to create a hard, offset shadow. This mimics the physical depth of carved stone blocks.
*   **Borders as Depth**: Depth is created by thick borders and inset lines, not blur.
*   **No Floating**: Elements should feel anchored. Cards do not hover; they sit on the page like a lectern.

## Shapes

*   **Pointed Arches**: The primary shape motif. Use SVG masks or CSS `clip-path` to create pointed arches for images and cards.
*   **Rose Windows**: Use circular patterns with radial symmetry for decorative dividers or loading states.
*   **Rectangular Rigidity**: Despite the arches, the overall container is a rigid rectangle, reflecting the structural reality of the building.
*   **Border-Radius**: Use `0px` for most elements. Use `2px` or `4px` only for small interactive elements (buttons) to suggest chiseled edges, not rounded plastic.

## Components

### Button Primary
*   **Shape**: Rectangular with a pointed top (arched) or sharp corners.
*   **Style**: Solid Deep Lapis background. Gold border (2px). Gold text.
*   **Hover**: Invert colors (Gold background, Lapis text). Add a hard offset shadow.
*   **Text**: Uppercase, Cinzel, wide tracking.

### Card
*   **Structure**: No border-radius. Thick border (2px) in Charcoal Mortar.
*   **Header**: A gold accent line at the top.
*   **Image**: Masked into a pointed arch shape.
*   **Content**: Left-aligned, generous padding.

### Table
*   **Style**: Grid lines only (top and bottom borders of rows). No vertical lines.
*   **Header**: Uppercase, Gold text, Lapis background.
*   **Rows**: Alternating Limestone and slightly darker stone (`#E0DCD1`) for readability.

### Navigation
*   **Style**: Horizontal bar with a gold bottom border.
*   **Active State**: Vertical gold line above the active item, mimicking a pillar.

## Do's and Don'ts

### Do:
*   **Do** use high-contrast serif fonts.
*   **Do** emphasize vertical lines and upward movement.
*   **Do** use gold sparingly for hierarchy.
*   **Do** embrace the "stone" aesthetic with hard edges and offsets.
*   **Do** use historical color names in documentation.

### Don't:
*   **Don't** use soft, blurred shadows.
*   **Don't** use sans-serif fonts for headings.
*   **Don't** use rounded corners on major containers.
*   **Don't** use bright, saturated primary colors (red, blue, green) outside of the specific Lapis/Gold/Limestone palette.
*   **Don't** use emoji as icons. Use SVG line icons inspired by medieval manuscripts (quills, shields, crosses, stars).
*   **Don't** use marketing jargon. Use terms like "Nave," "Tracery," "Pillar," "Altar."