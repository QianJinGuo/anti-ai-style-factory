---
version: 1.0.0
name: African Wax Print (Ankara/Kente)
description: A high-contrast, narrative-driven visual system rooted in West African textile traditions, prioritizing bold geometric repetition and cultural storytelling over minimalist uniformity.
colors:
  primary: "#D94F28" # Deep Ochre/Red (Earth, Heat, Vitality)
  secondary: "#F4D03F" # Saffron Yellow (Gold, Wealth, Sun)
  tertiary: "#2E8B57" # Forest Green (Growth, Prosperity)
  neutral: "#1A1A1A" # Charcoal Black (Grounding, Contrast)
  muted: "#E8E4D9" # Raw Cotton/Off-White (Canvas, Texture)
typography:
  h1:
    fontFamily: "Oswald"
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "Oswald"
    fontSize: 2.25rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "Oswald"
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "Source Sans 3"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: "Source Sans 3"
    fontSize: 0.875rem
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.05em
    textTransform: uppercase
rounded:
  sm: 2px
  md: 4px
  lg: 0px # Deliberately sharp corners to mimic fabric cuts and hard edges
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    background: "#D94F28"
    color: "#FFFFFF"
    border: "2px solid #1A1A1A"
    borderRadius: "0px"
    padding: "12px 24px"
    fontWeight: 700
    letterSpacing: 0.05em
    textTransform: uppercase
    boxShadow: "4px 4px 0px #1A1A1A" # Hard, offset shadow mimicking print layering
  card:
    background: "#FFFFFF"
    border: "3px solid #1A1A1A"
    borderRadius: "0px"
    boxShadow: "6px 6px 0px #1A1A1A"
    padding: 0
  table:
    headerBackground: "#F4D03F"
    headerColor: "#1A1A1A"
    rowBorder: "1px solid #1A1A1A"
    cellPadding: "12px 16px"
---

# Design System: African Wax Print

## Overview

This design system translates the visceral energy of West African wax-resist dyeing (Ankara, Vlisco, Kente) into a digital interface language. It rejects the sterile neutrality of modernist minimalism in favor of **narrative density** and **bold chromatic contrast**. 

The philosophy is grounded in the concept of "Pattern as Language." Just as traditional wax prints convey proverbs, social status, or historical events through geometric repetition, this UI uses structured repetition and high-contrast borders to create visual hierarchy without relying on subtle gradients or soft shadows. The interface feels tactile, printed, and culturally anchored.

## Colors

The palette is derived from natural dyes and industrial pigments used in traditional textile production. It relies on high saturation and strong contrast against black and off-white.

- **Primary (#D94F28):** Used for primary actions and key focal points. Represents earth and vitality.
- **Secondary (#F4D03F):** Used for highlights, accents, and warning states. Represents gold and abundance.
- **Tertiary (#2E8B57):** Used for success states and secondary navigation. Represents growth.
- **Neutral (#1A1A1A):** The structural anchor. Used for borders, text, and hard shadows. Never gray; always deep black for maximum contrast.
- **Muted (#E8E4D9):** The background canvas. Mimics raw cotton or unbleached fabric.

**Rule:** Avoid using primary, secondary, and tertiary colors in the same small area. Use them in distinct blocks or patterns to maintain legibility.

## Typography

Typography is chosen for its geometric clarity and ability to withstand heavy weight without losing legibility, mimicking the bold strokes of block-printed text.

- **Headings: Oswald**
  - A tall, condensed sans-serif that echoes the verticality of woven strips and traditional signage.
  - Used in uppercase or Title Case with tight letter-spacing for headers.
- **Body: Source Sans 3**
  - A humanist sans-serif that provides readability while maintaining a slight warmth compared to mechanical grotesques.
  - High x-height for clarity at small sizes.

**Rule:** Never use serif fonts for UI elements. Never use rounded or decorative display fonts. The text must be functional but bold.

## Layout

Layouts are grid-based but allow for modular "patchwork" arrangements.

- **Modular Grid:** Use a 12-column grid, but treat columns as "strips" of fabric.
- **Asymmetry:** Encourage asymmetric balance where a large block of primary color might be offset by a column of patterned background.
- **Full-Width Sections:** Backgrounds should often span the full width to create a sense of immersion, similar to a draped cloth.

## Elevation & Depth

Depth is achieved not through blur or transparency, but through **hard offset shadows** and **layered borders**.

- **Hard Shadows:** Use `box-shadow: 4px 4px 0px #1A1A1A;` instead of diffuse shadows. This mimics the layering of stencils in the wax-resist process.
- **Borders:** All interactive elements and cards must have a solid 2px-3px black border. This defines the "cut" of the element.
- **No Blur:** Never use `backdrop-filter: blur()`. The interface should feel solid and printed, not glass-like.

## Shapes

- **Rectilinear:** All shapes are rectangles with sharp 0px corners.
- **Diagonal Accents:** Use diagonal lines or triangular accents (derived from Kente weaving patterns) to break up horizontal/vertical rigidity.
- **Geometric Patterns:** Backgrounds can feature subtle, low-opacity geometric repeats (zig-zags, diamonds) to add texture without affecting readability.

## Components

### Button (Primary)
A solid block of color with a thick black border and a hard offset shadow.
- **State:** On hover, the shadow disappears (`box-shadow: none;`) and the button moves 4px down and right, simulating physical pressure.
- **Icon:** Use simple, geometric SVG icons (no gradients).

### Card
A white container with a thick black border and a significant hard shadow.
- **Header:** Can feature a background color (Primary/Secondary) with black text.
- **Content:** Clean white space.
- **Footer:** A thin black line separator.

### Table
- **Headers:** Yellow background (#F4D03F) with black text.
- **Rows:** Alternating white and off-white (#E8E4D9) backgrounds.
- **Borders:** Black lines between all cells.

### Navigation
- **Style:** Top-level navigation should be a solid bar (Primary or Black) with white or yellow text.
- **Active State:** A thick black underline or a left-border accent (3px wide) in the Secondary color.

## Do's and Don'ts

### Do
- **Use High Contrast:** Black text on yellow, white text on red. Ensure WCAG AA compliance through luminance difference, not just opacity.
- **Embrace Repetition:** Use geometric patterns as background textures, but keep them at <10% opacity so they don't distract from content.
- **Keep Corners Sharp:** Avoid border-radius. The aesthetic is about structure and cut, not softness.
- **Tell a Story:** Use icons and imagery that reflect cultural motifs (geometric, organic, symbolic) rather than generic corporate stock photos.

### Don't
- **No Glassmorphism:** Do not use blurred backgrounds or translucent layers.
- **No Soft Shadows:** Do not use large, diffuse box-shadows (e.g., `blur: 20px`).
- **No Pastels:** Do not use low-saturation colors. The aesthetic is bold and loud.
- **No Rounded Buttons:** Do not use pill-shaped buttons. They contradict the textile/cut aesthetic.
- **No Minimalist Whitespace:** Do not leave excessive empty space. Fill the canvas with structure, pattern, or color blocks.