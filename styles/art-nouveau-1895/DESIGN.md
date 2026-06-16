```yaml
version: 1.0.0
name: Art Nouveau
description: "A design system rooted in the late 19th-century rejection of industrial uniformity, prioritizing organic asymmetry, hand-crafted elegance, and the rhythmic flow of natural forms."
colors:
  primary: "#2E5C48"
  secondary: "#B8860B"
  tertiary: "#D4AF37"
  neutral: "#F5F5DC"
  muted: "#8F9E8A"
typography:
  h1:
    fontFamily: "Didot"
    fontSize: 48
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5
  h2:
    fontFamily: "Didot"
    fontSize: 36
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25
  h3:
    fontFamily: "Bodoni MT"
    fontSize: 24
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Baskerville"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.2
  caption:
    fontFamily: "Bodoni MT"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1.2
rounded:
  sm: 2
  md: 8
  lg: 24
spacing:
  sm: 8
  md: 16
  lg: 24
  xl: 48
components:
  button-primary:
    variant: "outline"
    borderStyle: "solid"
    borderRadius: 24
  card:
    variant: "minimal"
    borderRadius: 4
  table:
    variant: "striped"
    headerBackground: "#F5F5DC"
```

# Art Nouveau Design System

## Overview

Art Nouveau (New Art) emerged in the late 19th century as a total work of art (*Gesamtkunstwerk*), rejecting the rigid rectilinearity of the Industrial Revolution in favor of the fluid, asymmetrical lines found in nature. This design system is not merely aesthetic; it is a structural philosophy where UI elements behave like growing vines—organic, interconnected, and purposeful. The interface should feel hand-forged yet mathematically precise, echoing the architectural integrity of Hector Guimard and the graphic mastery of Alphonse Mucha.

## Colors

The palette is derived from natural pigments used in stained glass, oil paints, and early printing processes. It avoids the synthetic vibrancy of digital-native palettes in favor of muted, earthy tones that age gracefully.

- **Primary (`#2E5C48`)**: *Forest Green*. Represents the leaf, the stem, and the organic foundation. Used for primary actions and structural headers.
- **Secondary (`#B8860B`)**: *Antique Gold*. Represents the gilding in metalwork and the center of the flower. Used for accents, icons, and secondary emphasis.
- **Tertiary (`#D4AF37`)**: *Bright Gold*. A higher contrast gold for hover states and active selections, mimicking polished brass.
- **Neutral (`#F5F5DC`)**: *Beige*. A warm, parchment-like background that reduces eye strain and mimics aged paper.
- **Muted (`#8F9E8A`)**: *Sage Grey*. Used for disabled states, borders, and non-essential text.

## Typography

Typography in Art Nouveau is characterized by high contrast between thick and thin strokes, reflecting the influence of 18th-century engraving and calligraphy. Serifs are sharp and elegant, never rounded or soft.

- **Headings (`Didot`, `Bodoni MT`)**: High-contrast Didones. The extreme thick-thin transition mimics the varying thickness of a pen nib. Used for hierarchy.
- **Body (`Baskerville`)**: Transitional serif. Highly legible but retains the humanist touch of the hand. Preferred for long-form reading.
- **Captions/Labels (`Bodoni MT`)**: Small caps or tracked-out uppercase in Bodoni to create a sense of architectural rigidity against the organic curves.

## Layout

The layout rejects the strict grid in favor of **asymmetrical balance**. Content should flow like a vine, with whitespace acting as the "air" through which the design breathes.

- **Margins**: Generous. Whitespace is not empty; it is part of the composition.
- **Alignment**: Left-aligned text blocks with ragged right edges, mimicking justified paragraphs in books but with a softer, more natural termination.
- **Structure**: Use of "whiplash" curves to separate sections rather than straight horizontal lines.

## Elevation & Depth

Depth is achieved not through shadows (which imply a light source from above, a modern UI trope) but through **layering and opacity**.

- **Shadows**: None.
- **Layering**: Overlapping elements with slight opacity variations to create a stained-glass effect.
- **Borders**: Thin, precise lines (1px) in Gold or Green to define boundaries without obscuring content.

## Shapes

- **Curves**: All interactive elements should feature subtle curvature. Buttons are pill-shaped or irregular ovals. Cards have slightly softened corners but retain a sense of structure.
- **Ornaments**: Decorative dividers should be floral or geometric (honeycomb) patterns, not simple lines.
- **Icons**: Line-art icons with varying stroke widths, inspired by Art Nouveau posters.

## Components

### Button Primary
- **Shape**: Pill-shaped (`border-radius: 24px`).
- **Style**: Outlined in `#2E5C48` with `#F5F5DC` background.
- **Hover**: Fill with `#2E5C48`, text turns `#F5F5DC`. Add a subtle gold border.
- **Typography**: Uppercase, tracked out, `Bodoni MT`.

### Card
- **Shape**: Rectangular with `border-radius: 4px` (subtle, not rounded).
- **Style**: Minimal border in `#8F9E8A`. No shadow.
- **Content**: Image header with a floral overlay or decorative divider below the title.

### Table
- **Style**: Striped rows with `#F5F5DC` and a slightly darker beige.
- **Headers**: `#2E5C48` background with `#D4AF37` text.
- **Borders**: Thin gold lines between columns.

### Input Field
- **Shape**: Rectangular with `border-radius: 2px`.
- **Style**: Underline only (no box) in `#8F9E8A`. Focus state changes underline to `#B8860B`.
- **Placeholder**: `#8F9E8A`, italicized.

## Do's and Don'ts

### Do's
- **Do** use high-contrast serif fonts for headings.
- **Do** incorporate organic, flowing lines as dividers or background elements.
- **Do** use warm, earthy neutrals for backgrounds.
- **Do** prioritize legibility through generous spacing and clear hierarchy.
- **Do** use gold accents sparingly to highlight key interactive elements.

### Don'ts
- **Don't** use sans-serif fonts (Inter, Roboto, Helvetica) as they contradict the movement's rejection of industrial uniformity.
- **Don't** use drop shadows or blur effects (`backdrop-filter`) which create a "glass" aesthetic alien to the hand-crafted ethos.
- **Don't** use bright, neon, or synthetic colors (cyan, magenta, electric blue).
- **Don't** use uniform 12px or 16px border-radius everywhere; vary shapes to reflect organic irregularity.
- **Don't** use emoji as icons; use line-art illustrations or custom SVGs.
- **Don't** use marketing buzzwords in placeholder text or labels.