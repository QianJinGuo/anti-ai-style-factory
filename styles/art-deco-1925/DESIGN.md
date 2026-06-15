---
version: 1.0.0
name: Art Deco System
description: A design system rooted in the geometric rigor, verticality, and luxurious minimalism of the 1925 Paris Exposition, prioritizing symmetry and metallic contrast over organic warmth.
colors:
  primary:
    name: "Onyx"
    value: "#1A1A1A"
    usage: "Primary text, structural lines, background depth"
  secondary:
    name: "Champagne Gold"
    value: "#D4AF37"
    usage: "Accents, borders, active states, icons"
  tertiary:
    name: "Deep Emerald"
    value: "#0B3D2C"
    usage: "Secondary backgrounds, link states, subtle contrast"
  neutral:
    name: "Ivory"
    value: "#F5F5F0"
    usage: "Page background, card surfaces"
  muted:
    name: "Charcoal"
    value: "#4A4A4A"
    usage: "Secondary text, disabled states, subtle borders"

typography:
  h1:
    fontFamily: "'Cinzel', 'Playfair Display', serif"
    fontSize: "3.5rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.05em"
    textTransform: "uppercase"
  h2:
    fontFamily: "'Cinzel', 'Playfair Display', serif"
    fontSize: "2.5rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.03em"
    textTransform: "uppercase"
  h3:
    fontFamily: "'Cinzel', 'Playfair Display', serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.02em"
    textTransform: "uppercase"
  body-md:
    fontFamily: "'Montserrat', 'Lato', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.01em"
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.1em"
    textTransform: "uppercase"

rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"

spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"

components:
  button-primary:
    background: "#1A1A1A"
    color: "#D4AF37"
    border: "1px solid #D4AF37"
    padding: "12px 24px"
    borderRadius: "0px"
    fontWeight: 600
    letterSpacing: "0.15em"
    textTransform: "uppercase"
    hover:
      background: "#D4AF37"
      color: "#1A1A1A"
  card:
    background: "#F5F5F0"
    border: "1px solid #D4AF37"
    boxShadow: "0 2px 4px rgba(26, 26, 26, 0.1)"
    padding: "24px"
    borderRadius: "0px"
  table:
    border: "1px solid #D4AF37"
    cellPadding: "12px"
    headerBackground: "#1A1A1A"
    headerColor: "#D4AF37"
    rowHover: "#E8E8E0"
---

# Art Deco Design System Specification

## Overview

Art Deco (Les Années Folles) is not merely decorative; it is an architecture of order. This system rejects the soft, organic curves of the preceding Arts & Crafts movement and the chaotic abstraction of Dadaism in favor of **symmetry, geometric precision, and verticality**. 

The design language draws from the 1925 Paris Exposition Internationale des Arts Décoratifs et Industriels Modernes. It values the juxtaposition of luxurious materials (gold, onyx) with industrial efficiency. The interface should feel constructed, like a skyscraper or a luxury liner, rather than grown like a plant.

## Colors

The palette is high-contrast and deliberate. It relies on the interplay between deep, absorbing darks and reflective, metallic lights.

### Primary: Onyx (#1A1A1A)
Used for structural elements. It provides a heavy, stable foundation. Unlike pure black (#000000), Onyx offers slight warmth and depth, mimicking polished stone or lacquer.

### Secondary: Champagne Gold (#D4AF37)
The accent of prestige. Used sparingly for borders, active states, and key typography. It must never be yellow; it must be metallic. In digital contexts, this is achieved through precise hex values, avoiding gradients unless simulating light reflection on metal.

### Tertiary: Deep Emerald (#0B3D2C)
A nod to the natural motifs (sunrise, vegetation) stylized into geometry. Used for secondary information or link states to provide a rich, cool contrast to the warm gold.

### Neutral: Ivory (#F5F5F0)
The canvas. Pure white is too harsh for the era's aesthetic of luxury. Ivory mimics aged paper, bone, or ivory, providing a soft but clear background that allows the Onyx and Gold to pop.

### Muted: Charcoal (#4A4A4A)
For secondary text and disabled states. It maintains legibility without competing with the primary hierarchy.

## Typography

Typefaces must convey authority and elegance. The system pairs a classical serif for headings with a geometric sans-serif for body text, reflecting the fusion of tradition and modernity.

### Headings: Cinzel / Playfair Display
*   **Philosophy:** Serifs evoke the Roman inscriptions and classical influences central to Art Deco.
*   **Usage:** All headings (H1-H3) are **UPPERCASE**. This creates a monumental, architectural feel.
*   **Tracking:** Wide letter-spacing (`0.05em`+) is critical. It creates breathing room and emphasizes the geometric structure of the letters.

### Body: Montserrat / Lato
*   **Philosophy:** Geometric sans-serifs reflect the machine age, industrialization, and streamlined forms of the 1930s.
*   **Usage:** High legibility for content.
*   **Contrast:** The stark difference between the serif headings and sans-serif body creates a visual rhythm that is distinctively Deco.

### Caption: Montserrat (Uppercase)
*   Small, wide-tracked text for labels, dates, and metadata. It acts as a structural grid marker.

## Layout

### Symmetry & Grid
Art Deco is inherently symmetrical. Layouts should adhere to a strict 12-column grid. Content blocks are often centered or mirrored. Asymmetry is allowed only if it is balanced geometrically, not organically.

### Verticality
Lines should be vertical. Borders, separators, and column dividers should emphasize height. This mimics the skyscrapers of New York and Chicago.

### Negative Space
Space is a luxury. Do not crowd elements. Generous padding around key content areas signifies importance and refinement.

## Elevation & Depth

Depth is achieved through **layering and contrast**, not drop shadows.

*   **No Blurred Shadows:** Avoid `box-shadow: 0 10px 20px rgba(...)`.
*   **Hard Edges:** Use `box-shadow: 0 2px 4px rgba(0,0,0,0.1)` only if necessary for z-index context, but prefer hard borders.
*   **Layering:** Create depth by placing Ivory cards on a slightly darker background, or by using thin Gold borders to separate planes.

## Shapes

### Sharp Angles
All `border-radius` values must be `0px`. Circles and rounded corners are antithetical to the style. Corners should be sharp, precise, and 90-degree.

### Geometric Motifs
When decorative elements are needed, use:
*   **Sunbursts:** Radiating lines from a center point.
*   **Chevrons:** V-shaped patterns.
*   **Zigzags:** Stylized lightning or mountain forms.
*   **Steps:** Stepped forms reminiscent of ziggurats.

These should be implemented as SVG backgrounds or precise CSS borders, not as decorative boxes.

## Components

### Buttons
Buttons are not pills. They are rectangular plates.
*   **Style:** Flat background (Onyx) with a thin Gold border.
*   **Text:** Uppercase, wide tracking, Gold text.
*   **Interaction:** Invert colors on hover (Gold background, Onyx text). No transitions that ease; use instant or linear transitions to feel mechanical.

### Cards
Cards are framed windows, not floating islands.
*   **Structure:** Ivory background with a 1px Gold border.
*   **Content:** Headings in Uppercase Serif. Body in Sans-Serif.
*   **Separators:** Use a thin Gold line below the header to separate title from content.

### Tables
Tables are ledgers.
*   **Headers:** Onyx background, Gold text, Uppercase.
*   **Borders:** 1px Gold borders around all cells.
*   **Zebra Striping:** Avoid. Use alternating Ivory and slightly darker Ivory (or very light Gold tint) if needed, but solid is preferred.

### Forms
Inputs are precise fields.
*   **Style:** No border by default, or a thin 1px Charcoal border.
*   **Focus:** A 2px Gold border on focus.
*   **Labels:** Uppercase, small, wide tracking, placed above the input.

## Do's and Don'ts

### Do
*   Use uppercase for all headings and labels.
*   Maintain strict symmetry in layout structures.
*   Use Gold sparingly as an accent, not a background.
*   Employ sharp, geometric shapes (triangles, trapezoids, rectangles).
*   Use wide letter-spacing to create elegance.

### Don't
*   **Do not** use rounded corners (`border-radius > 0`).
*   **Do not** use drop shadows with blur (`blur >= 4px`).
*   **Do not** use gradients (except for subtle metallic simulation in SVGs).
*   **Do not** use organic, flowing, or hand-drawn lines.
*   **Do not** use sans-serif for headings (unless it is a very specific geometric font like Futura, but Serif is preferred for hierarchy).
*   **Do not** use bright, saturated colors (neon, primary red/blue). Stick to the muted, luxurious palette.