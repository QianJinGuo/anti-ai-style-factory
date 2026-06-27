---
version: 1.0.0
name: Art Deco
description: A synthesis of industrial modernity and ornamental luxury, defined by strict geometry, verticality, and metallic precision.
colors:
  primary:
    name: "Gatsby Gold"
    hex: "#D4AF37"
    usage: "Accents, borders, icons, active states"
  secondary:
    name: "Midnight Onyx"
    hex: "#0A0A0A"
    usage: "Primary text, dark backgrounds, headers"
  tertiary:
    name: "Sunset Copper"
    hex: "#B87333"
    usage: "Secondary accents, hover states, subtle highlights"
  neutral:
    name: "Pearl Cream"
    hex: "#F5F5DC"
    usage: "Light backgrounds, card surfaces, paper texture"
  muted:
    name: "Charcoal Slate"
    hex: "#36454F"
    usage: "Secondary text, disabled states, subtle dividers"
typography:
  h1:
    fontFamily: "'Bodoni Moda', 'Didot', 'Playfair Display', serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "'Bodoni Moda', 'Didot', 'Playfair Display', serif"
    fontSize: 36
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "'Bodoni Moda', 'Didot', 'Playfair Display', serif"
    fontSize: 24
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Futura', 'Century Gothic', 'Avant Garde', sans-serif"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.04em
  caption:
    fontFamily: "'Futura', 'Century Gothic', 'Avant Garde', sans-serif"
    fontSize: 12
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
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
    background: "#0A0A0A"
    color: "#D4AF37"
    border: "1px solid #D4AF37"
    borderRadius: 0px
    padding: "12px 24px"
    fontWeight: 600
    letterSpacing: 0.1em
    textTransform: "uppercase"
    hover:
      background: "#D4AF37"
      color: "#0A0A0A"
  card:
    background: "#F5F5DC"
    border: "1px solid #D4AF37"
    borderRadius: 0px
    boxShadow: "none"
    padding: 24px
  table:
    headerBg: "#0A0A0A"
    headerColor: "#D4AF37"
    rowBg: "#F5F5DC"
    border: "1px solid #36454F"
    cellPadding: "12px 16px"
---

# Art Deco Design System

## Overview

This design system is rooted in the **Art Deco** movement (c. 1925–1940), characterized by a rejection of organic curves in favor of sharp, machine-age geometry. It balances the opulence of pre-war luxury with the efficiency of modern industrial production. The aesthetic is not "friendly" or "soft"; it is authoritative, elegant, and precise. Visual hierarchy is established through contrast (gold on black) and structural rigidity, not through playful shadows or rounded corners.

## Colors

The palette is high-contrast and metallic. It relies on the interplay between deep, absorbing darks and reflective, luminous metallics.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| `primary` | `#D4AF37` | **Gatsby Gold**. Use for borders, thin lines, icons, and primary interactive states. Never use as a large background fill. |
| `secondary` | `#0A0A0A` | **Midnight Onyx**. The primary canvas for dark mode or high-contrast headers. |
| `tertiary` | `#B87333` | **Sunset Copper**. A subtle accent for secondary information or hover states where gold is too aggressive. |
| `neutral` | `#F5F5DC` | **Pearl Cream**. The primary background for light mode. It should mimic the texture of aged paper or ivory. |
| `muted` | `#36454F` | **Charcoal Slate**. For body text on cream backgrounds or secondary UI elements. |

**Rule:** Never blend these colors. Art Deco relies on flat, solid blocks of color. Gradients are forbidden unless they simulate a metallic sheen via linear gradients with sharp stops.

## Typography

Typography is the primary vehicle for decoration. We reject neutral sans-serifs (like Inter or Roboto) in favor of fonts with historical weight and geometric precision.

### Headings
*   **Font:** `Bodoni Moda`, `Didot`, or `Playfair Display`
*   **Style:** High-contrast serif. Thick vertical stems and hairline horizontals.
*   **Treatment:** Uppercase for navigation and major section headers. Tight letter-spacing (`-0.02em`) to create a solid block of text.

### Body & UI
*   **Font:** `Futura`, `Century Gothic`, or `Avant Garde`
*   **Style:** Geometric sans-serif. Perfect circles and straight lines.
*   **Treatment:** Wide letter-spacing (`0.04em` to `0.1em`) to enhance readability and lend an air of architectural spacing. Uppercase for labels and captions.

## Layout

The layout must be **symmetrical** and **grid-based**.

1.  **Verticality:** Emphasize vertical lines. Use tall, narrow containers for images or key data points.
2.  **Symmetry:** Center-aligned content is preferred for hero sections. Left-aligned content is acceptable for body text but must respect a rigid column structure.
3.  **Zig-Zags and Sunbursts:** Use these geometric motifs sparingly as dividers or background patterns, not as primary structural elements.
4.  **Whitespace:** Use whitespace as a framing device, not just padding. Margins should be generous (`64px`+) to create a sense of luxury and exclusivity.

## Elevation & Depth

Art Deco does not use soft drop shadows (`box-shadow` with blur) to indicate depth. Depth is achieved through:

1.  **Layering:** Overlapping flat shapes with distinct borders.
2.  **Border Weight:** Thicker borders indicate foreground elements; thinner borders indicate background structure.
3.  **Metallic Borders:** A 1px or 2px solid border in `#D4AF37` creates a "frame" effect, separating content from the background without softness.

**Rule:** `box-shadow` is strictly prohibited. If elevation is needed, use a solid offset block of color (e.g., a 4px offset of `#0A0A0A` behind a `#F5F5DC` card).

## Shapes

*   **Corners:** `0px`. All elements must have sharp, 90-degree angles.
*   **Borders:** Solid, single-pixel lines. No dashed or dotted lines.
*   **Icons:** Linear, geometric icons. Use simple shapes (circles, triangles, chevrons) with consistent stroke width (1.5px or 2px). No filled icons unless they are solid geometric blocks.

## Components

### Buttons
Buttons are rectangular plaques. They should look like engraved metal plates.

*   **Shape:** Rectangle (`border-radius: 0`).
*   **Border:** 1px solid `#D4AF37`.
*   **Text:** Uppercase, wide spacing.
*   **Interaction:** On hover, invert colors (Gold background, Black text). No transition animation; the change should be instant or fade, not slide.

### Cards
Cards are framed panels.

*   **Structure:** A solid border (`#D4AF37`) surrounding the content.
*   **Header:** A horizontal line (`border-bottom: 1px solid #D4AF37`) separating the title from the body.
*   **Background:** Flat `#F5F5DC`. No gradients.

### Tables
Tables should resemble ledgers or schedules.

*   **Headers:** Black background (`#0A0A0A`) with Gold text (`#D4AF37`).
*   **Rows:** Cream background with Charcoal text.
*   **Grid:** Visible borders on all cells (`1px solid #36454F`) to emphasize the tabular structure.

## Do's and Don'ts

| Do | Don't |
| :--- | :--- |
| **DO** use high-contrast black and gold. | **DON'T** use purple, blue, or pastel gradients. |
| **DO** use serif fonts for headings to convey elegance. | **DON'T** use rounded corners (`border-radius > 0px`). |
| **DO** align elements symmetrically or on a strict grid. | **DON'T** use soft, blurred shadows (`box-shadow` with blur). |
| **DO** use uppercase text with wide letter-spacing for UI labels. | **DON'T** use emoji or organic, hand-drawn icons. |
| **DO** use sharp, geometric dividers. | **DON'T** use marketing buzzwords ("seamless", "future"). |
| **DO** treat borders as structural elements. | **DON'T** use glassmorphism or translucent backgrounds. |