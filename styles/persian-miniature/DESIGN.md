```yaml
version: 1.0.0
name: Persian Miniature
description: A design system rooted in the meticulous, flat-plane aesthetics of 14th–16th century Iranian manuscript illumination, prioritizing decorative density, intricate geometric borders, and narrative clarity over Western perspective.
colors:
  primary: "#B8860B" # Dark Goldenrod - representing gold leaf application
  secondary: "#005F73" # Deep Teal - derived from lapis lazuli pigments
  tertiary: "#9E2A2B" # Vermilion Red - traditional cinnabar/minium for accents
  neutral: "#F5F1E8" # Parchment White - base tone for aged paper
  muted: "#8C7B70" # Sepia - for secondary text and subdued details
typography:
  h1:
    fontFamily: "'Noto Nastaliq Urdu', 'Urdu Typesetting', serif"
    fontSize: 2.5rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: -0.02em
  h2:
    fontFamily: "'Noto Nastaliq Urdu', 'Urdu Typesetting', serif"
    fontSize: 2rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.01em
  h3:
    fontFamily: "'Noto Nastaliq Urdu', 'Urdu Typesetting', serif"
    fontSize: 1.5rem
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0em
  body-md:
    fontFamily: "'Amiri', 'Noto Naskh Arabic', serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Amiri', 'Noto Naskh Arabic', serif"
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
rounded:
  sm: 2px
  md: 4px
  lg: 0px
spacing:
  sm: 4px
  md: 8px
  lg: 16px
  xl: 32px
components:
  button-primary:
    background: "#B8860B"
    color: "#F5F1E8"
    border: "2px solid #9E2A2B"
    padding: "8px 16px"
    font-size: 1rem
    border-radius: 0px
    text-transform: uppercase
    letter-spacing: 0.05em
  card:
    background: "#F5F1E8"
    border: "1px solid #B8860B"
    padding: 16px
    box-shadow: "none"
    border-radius: 0px
    position: relative
  table:
    header-bg: "#005F73"
    header-color: "#F5F1E8"
    row-alt-bg: "#EFEAD9"
    border-color: "#B8860B"
    padding: 8px
    font-size: 0.9rem
```

# Persian Miniature Design System

## Overview

This design system draws directly from the **Persian Miniature** tradition (c. 1300–1600), a style defined by its rejection of linear perspective in favor of a flattened, decorative space where every inch is filled with meaningful detail. It prioritizes **precision** (each line intentional), **planar decoration** (no shadows or gradients, only solid color fields), and **narrative framing** (content is always contained within ornate, geometric borders).

The aesthetic is not minimalist; it is **dense**. It treats whitespace as "parchment" to be adorned, not left empty. The interface should feel like a illuminated manuscript: hierarchical, ornate, and deeply textual.

## Colors

The palette is derived from natural mineral and vegetable pigments used in historical manuscripts.

*   **Primary (`#B8860B`)**: Gold. Used for borders, headings, and key interactive elements. Represents the gold leaf gilding.
*   **Secondary (`#005F73`)**: Lapis Lazuli. A deep, resonant blue used for backgrounds of text blocks, headers, and primary content areas.
*   **Tertiary (`#9E2A2B`)**: Cinnabar Red. Used for accents, active states, and decorative motifs. High contrast against gold and blue.
*   **Neutral (`#F5F1E8`)**: Parchment. The base canvas. Slightly warm, off-white to simulate aged paper. No pure white (`#FFFFFF`) is used.
*   **Muted (`#8C7B70`)**: Sepia. Used for secondary text, captions, and inactive states.

**Rule:** Never use pure black (`#000000`) or pure white (`#FFFFFF`). Text should always be the deep sepia or the dark blue.

## Typography

Typography is the central pillar. The system relies on **Nastaliq** and **Naskh** styles, which are inherently vertical and flowing, contrasting with the horizontal rigidity of Western grids.

*   **Headings (`Noto Nastaliq Urdu`)**: The Nastaliq script is elegant, slanted, and connected. It should be used for titles and significant UI labels. It is not a "sans-serif" substitute; it is a calligraphic display font.
*   **Body (`Amiri`)**: A Naskh-style serif font designed for high legibility in Arabic/Persian scripts. It has a traditional book feel with clear ascenders and descenders.
*   **Sizing**: Headings are large but not bold-heavy. The weight is uniform (400). The emphasis comes from the script's natural variation, not font-weight changes.
*   **Line Height**: Generous line height (1.8 for body) to accommodate the verticality of the script and allow space for marginalia or decorative elements between lines.

**Rule:** Do not use sans-serif fonts for body text. Do not use bold weights for headings; use size and color instead.

## Layout

Layout is **modular** and **framed**.

*   **Borders are Structural**: Every major content block must be enclosed in a border. The border is not just a line; it is a decorative element (see Components).
*   **No Perspective**: All elements are placed on a flat plane. No drop shadows, no 3D transforms, no parallax. Depth is suggested through color contrast and layering of patterns, not lighting.
*   **Symmetry**: Layouts should be centered and symmetrical. Asymmetry is reserved for specific decorative motifs, not structural grid breaks.
*   **Density**: Avoid large gaps. Content should feel "packed" but organized. Use small spacing (4px–8px) between related elements.

## Elevation & Depth

**There is no elevation.**

*   **No Shadows**: `box-shadow` is forbidden.
*   **No Gradients**: `background: linear-gradient()` is forbidden.
*   **Depth via Color**: A "layered" effect is achieved by using a slightly darker shade of the neutral background for nested containers, or by using a contrasting border color.
*   **Flat Design**: All surfaces are matte and uniform.

## Shapes

*   **Rectilinear**: All containers are sharp rectangles (`border-radius: 0px`).
*   **Geometric Patterns**: Decorative elements (icons, dividers) should be based on Islamic geometric patterns (8-pointed stars, interlocking circles, arabesques), not organic shapes or rounded corners.
*   **Ornamentation**: Use thin, intricate lines for decorative dividers between sections.

## Components

### Button Primary
*   **Shape**: Sharp rectangle.
*   **Style**: Gold background (`#B8860B`) with a thin red border (`#9E2A2B`).
*   **Text**: White Parchment (`#F5F1E8`) in a serif font.
*   **Hover**: Background shifts to a slightly darker gold (`#A0740A`). No shadow.
*   **Focus**: Inner red border thickens.

### Card
*   **Structure**: A rectangular block with a double border.
    *   Outer border: 1px solid Gold (`#B8860B`).
    *   Inner border: 1px solid Muted Sepia (`#8C7B70`), inset 4px.
*   **Background**: Parchment (`#F5F1E8`).
*   **Content**: Title in Nastaliq, body in Amiri.
*   **No Shadow**: Flat appearance.

### Table
*   **Header**: Deep Teal (`#005F73`) background, White Parchment text.
*   **Rows**: Alternating rows of Parchment (`#F5F1E8`) and slightly darker Parchment (`#EFEAD9`).
*   **Borders**: All cells separated by 1px Gold (`#B8860B`) lines.
*   **Padding**: Generous vertical padding (12px) to accommodate script height.

### Navigation
*   **Style**: A horizontal bar with a thick Gold top border.
*   **Items**: Text links in Sepia, turning Red (`#9E2A2B`) on hover.
*   **Active State**: Underlined with a thick Gold line.

## Do's and Don'ts

| Do | Don't |
| :--- | :--- |
| Use gold and lapis lazuli for primary visual hierarchy. | Use blue-purple gradients or neon colors. |
| Use Nastaliq/Naskh fonts for headings and body. | Use Inter, Roboto, or Helvetica. |
| Frame content with intricate geometric borders. | Use rounded corners (border-radius > 0). |
| Keep backgrounds flat and matte. | Use glassmorphism, blur effects, or drop shadows. |
| Allow content density; fill space with meaningful detail. | Use excessive whitespace or minimalism. |
| Use serif fonts for all text. | Use sans-serif fonts for body text. |
| Use red for active states and accents. | Use green or orange for primary actions. |
| Ensure text is highly legible against parchment. | Use pure white backgrounds. |