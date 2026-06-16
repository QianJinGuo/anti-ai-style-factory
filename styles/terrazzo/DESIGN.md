version: 1.0.0
name: Terrazzo
description: A design system rooted in the 16th-century Venetian tradition of repurposing marble waste into durable, speckled surfaces, emphasizing organic randomness and polished materiality.
colors:
  primary:
    name: "Marble Base"
    value: "#F5F2EB"
    description: "A warm, off-white limestone tone serving as the neutral canvas."
  secondary:
    name: "Aggregates"
    value: "#8C7B6C"
    description: "A muted, earthy taupe representing the stone chips."
  tertiary:
    name: "Veins"
    value: "#4A4036"
    description: "Deep charcoal-brown for high-contrast structural lines and text."
  neutral:
    name: "Polished Finish"
    value: "#E8E4DB"
    description: "Slightly darker than base, used for secondary backgrounds or hover states."
  muted:
    name: "Dust"
    value: "#D1C7B7"
    description: "Low contrast gray-beige for disabled states or subtle dividers."
typography:
  h1:
    fontFamily: "Playfair Display"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "Playfair Display"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "DM Serif Display"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Liberation Serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: "IBM Plex Mono"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
rounded:
  sm: 2px
  md: 4px
  lg: 8px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    variant: "solid"
    background: "#4A4036"
    color: "#F5F2EB"
    border: "1px solid #4A4036"
    borderRadius: "2px"
    padding: "12px 24px"
    fontWeight: 500
  card:
    background: "#F5F2EB"
    border: "1px solid #E8E4DB"
    borderRadius: "4px"
    shadow: "none"
    padding: "24px"
  table:
    headerBg: "#E8E4DB"
    rowHover: "#F0ECE3"
    border: "1px solid #D1C7B7"
```

# Terrazzo Design System

## Overview

Terrazzo is a design philosophy derived from the Venetian technique of embedding marble chips into concrete or epoxy, then polishing the surface to a smooth, monolithic finish. It rejects the sterile uniformity of digital minimalism in favor of organic texture, historical depth, and material honesty. The system prioritizes readability and structure while allowing for controlled visual "noise" that mimics natural stone. It is not about decoration; it is about the integrity of the material.

## Colors

The palette is strictly earth-bound, avoiding artificial hues. Colors are chosen to simulate the interaction of light on polished stone surfaces.

- **Base (#F5F2EB)**: The dominant background. It is not pure white (#FFFFFF) but a warm, raw limestone. Pure white is reserved only for text on dark aggregates.
- **Aggregates (#8C7B6C)**: Used for secondary text, icons, and borders. This taupe provides sufficient contrast without the harshness of black.
- **Veins (#4A4036)**: The darkest tone. Used for primary headings, active states, and critical data points. It anchors the design.
- **Polished Finish (#E8E4DB)**: A subtle tonal shift for cards, sections, or hover states. It creates depth without shadow.
- **Dust (#D1C7B7)**: For dividers, disabled states, and placeholders. It blends into the background, receding visually.

**Rule**: Do not use pure black (#000000) or pure white (#FFFFFF) as primary UI colors. They break the illusion of material continuity.

## Typography

Typography must reflect the tension between the rough aggregate (serif) and the smooth matrix (sans/monospace).

- **Headings (Playfair Display, DM Serif Display)**: High-contrast geometric serifs. They evoke the chiseled inscriptions found on historical Venetian facades. Use tight letter-spacing for impact.
- **Body (Liberation Serif)**: A robust, legible serif. It ensures that long-form reading feels grounded and traditional, not airy and disposable.
- **Data/Captions (IBM Plex Mono)**: Used sparingly for metadata, dates, or technical specifications. It provides a structural counterpoint to the organic serifs, representing the precise engineering of the polish.

**Rule**: Never mix sans-serif headings with serif body text. The aesthetic relies on the consistency of the "stone" metaphor.

## Layout

Layouts are grid-based but content-driven. Margins are generous to allow the "material" to breathe.

- **Grid**: 12-column grid with a 24px gutter.
- **Padding**: Minimum 40px horizontal padding on desktop. Content should never touch the screen edge.
- **Alignment**: Left-aligned text. Justified text is discouraged as it creates uneven spacing (rivers) that disrupts the smooth "polished" reading experience.

## Elevation & Depth

Terrazzo has no elevation in the Material Design sense. It is a single, flat, polished plane. Depth is achieved through:

1. **Color Contrast**: Using the "Vein" vs. "Base" contrast to distinguish hierarchy.
2. **Borders**: Thin, 1px solid borders in `#E8E4DB` or `#D1C7B7` to define containers.
3. **Texture**: Optional subtle SVG noise overlays at 2% opacity on backgrounds to simulate stone grain.

**Rule**: Do not use drop shadows (`box-shadow`). Shadows imply floating elements; Terrazzo is a solid, grounded surface.

## Shapes

- **Borders**: Minimal rounding. `sm` (2px) for small elements, `md` (4px) for cards. Avoid `lg` (8px+) as it softens the material too much, resembling plastic rather than stone.
- **Dividers**: Solid lines, 1px thick. No dotted or dashed lines.

## Components

### Button (Primary)
- **Shape**: Sharp or slightly rounded (2px).
- **Style**: Solid fill with `#4A4036` background and `#F5F2EB` text.
- **Hover**: Invert colors (Background becomes `#F5F2EB`, Text becomes `#4A4036`) with a 1px border appearing. No scaling or shadow effects.
- **Focus**: Outer outline using `#8C7B6C`.

### Card
- **Structure**: Minimal border (`1px solid #E8E4DB`). No shadow.
- **Content**: Headings in Playfair Display, Body in Liberation Serif.
- **Background**: `#F5F2EB`.

### Table
- **Header**: Background `#E8E4DB`, text `#4A4036`.
- **Rows**: Alternating subtle background shifts (`#F5F2EB` vs `#F0ECE3`) to aid readability without grid lines.
- **Borders**: 1px solid `#D1C7B7` between cells.

### Input Field
- **Style**: Underline only. No box.
- **Border**: 1px solid `#D1C7B7` on bottom only.
- **Focus**: Border color shifts to `#4A4036`.
- **Label**: Small, uppercase, monospace (`IBM Plex Mono`), positioned above the input.

## Do's and Don'ts

### Do
- **Use Serif Fonts**: Embrace the historical weight of serif typefaces.
- **Embrace Warmth**: Stick to beige, taupe, brown, and cream tones.
- **Keep it Flat**: Use borders and color contrast for structure, not shadows.
- **Be Precise**: Use monospace fonts for data and metadata to highlight the engineering aspect of the material.

### Don't
- **Use Gradients**: Terrazzo is a solid material. Gradients imply digital gloss.
- **Use Glassmorphism**: Blur effects destroy the clarity of the stone metaphor.
- **Use Rounded Corners Excessively**: Keep corners sharp to maintain structural integrity.
- **Use Sans-Serif for Body Text**: It breaks the historical consistency of the system.
- **Use Pure Black/White**: They are too stark and digital for this organic palette.
