# DESIGN.md

```yaml
version: 1.0.0
name: Wabi-Sabi
description: A design philosophy embracing the beauty of imperfection, impermanence, and incompleteness, prioritizing natural materials and quietude over polished perfection.
colors:
  primary:
    name: Sumi Ink
    hex: '#2C2825'
    description: Deep, charcoal black derived from traditional ink sticks, allowing for high contrast without harsh digital sterility.
  secondary:
    name: Unbleached Linen
    hex: '#E8E4DD'
    description: Warm, organic off-white resembling raw paper or cotton, providing a soft, non-reflective background.
  tertiary:
    name: Moss Green
    hex: '#5A6B5C'
    description: Muted, earthy green found in aged foliage, used sparingly for subtle emphasis.
  neutral:
    name: Kintsugi Gold
    hex: '#C5A059'
    description: A subdued, oxidized gold tone used for accents, representing the repair of breaks rather than hiding them.
  muted:
    name: Weathered Stone
    hex: '#8C857B'
    description: Desaturated grey-brown for secondary text and borders, avoiding pure grey which feels artificial.

typography:
  h1:
    fontFamily: 'Noto Serif JP, serif'
    fontSize: 2.5rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.02em
    description: Large, authoritative but calm. Serifs evoke traditional calligraphy brushes.
  h2:
    fontFamily: 'Noto Serif JP, serif'
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.01em
    description: Secondary headings maintain the serif tradition but with reduced weight.
  h3:
    fontFamily: 'Noto Serif JP, serif'
    fontSize: 1.25rem
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    description: Subheadings that breathe, avoiding boldness that screams for attention.
  body-md:
    fontFamily: 'Noto Serif JP, serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0.02em
    description: High x-height and loose line-height mimic the rhythm of reading classical text.
  caption:
    fontFamily: 'Noto Serif JP, serif'
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.05em
    description: Small text with increased tracking to simulate carved stone or stamped seal impressions.

rounded:
  sm: 2px
  md: 4px
  lg: 8px
  description: Borders are rarely fully rounded; slight rounding suggests hand-carved edges or worn stone, never machine-perfect circles.

spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  description: Generous whitespace (Ma) is critical. Content should feel sparse, allowing elements to exist in silence.

components:
  button-primary:
    background: '#2C2825'
    color: '#E8E4DD'
    border: 1px solid '#2C2825'
    borderRadius: 2px
    padding: '12px 24px'
    hover:
      background: '#3D3835'
      border: 1px solid '#3D3835'
    description: Rectangular, sharp edges. No shadows. Interaction is subtle, indicated only by slight darkening, mimicking the weight of a brush touching paper.
  card:
    background: '#FFFFFF'
    border: 1px solid '#E8E4DD'
    borderRadius: 4px
    padding: 24px
    boxShadow: 'none'
    description: Cards do not float. They sit flat on the page, outlined by a thin, almost invisible line, resembling a framed scroll or a piece of textured paper.
  table:
    headerBg: '#E8E4DD'
    rowHover: '#F5F2ED'
    border: 1px solid '#E8E4DD'
    description: Minimalist tables. No grid lines unless necessary. Borders are thin and warm.
```

## Overview

Wabi-Sabi design rejects the digital obsession with clarity, symmetry, and gloss. It embraces the rough, the worn, and the incomplete. In a UI context, this translates to a rejection of high-contrast neon, heavy shadows, and rounded "friendly" buttons. Instead, we prioritize texture, asymmetry, and a sense of quiet history. The interface should feel like an old library or a tea house—grounded, material, and timeless.

## Colors

The palette is derived from natural materials: ink, paper, stone, and wood.

- **Sumi Ink (#2C2825)**: Used for primary text and key interactive elements. It is never pure black (#000000), which feels too harsh and digital.
- **Unbleached Linen (#E8E4DD)**: The primary background. It simulates the warmth of raw washi paper.
- **Moss Green (#5A6B5C)**: A muted accent for success states or natural elements.
- **Kintsugi Gold (#C5A059)**: Used sparingly for critical highlights or borders that need to draw the eye without shouting.
- **Weathered Stone (#8C857B)**: For disabled states, borders, and secondary text.

Avoid saturated colors. If a color feels "loud," it is incorrect.

## Typography

Typography is the voice of the interface. In Wabi-Sabi, the voice should be calm and measured.

- **Font Family**: `Noto Serif JP` or similar high-quality serif fonts. Sans-serif fonts are generally avoided as they feel too corporate and sterile. If a sans-serif is absolutely necessary for data density, use a grotesque with humanist tendencies (e.g., Optima), but serif is preferred.
- **Weight**: Regular (400) is the default. Bold is used rarely, only for structural hierarchy, never for emphasis through volume.
- **Line Height**: Generous (1.6 to 1.8). Text should breathe. Crowded text feels anxious; spacious text feels contemplative.
- **Letter Spacing**: Slight positive tracking (0.02em - 0.05em) for body text and captions to improve legibility on textured backgrounds and mimic the spacing of printed kanji.

## Layout

Layout is governed by the concept of *Ma* (negative space).

- **Asymmetry**: Perfect grid alignment is secondary to visual balance. Elements may be offset to create dynamic tension.
- **Whitespace**: Margins and padding are large. Empty space is not wasted space; it is an active design element that defines the content.
- **Grid**: Use a flexible grid, but allow content to break out of strict columns if it enhances the narrative flow.

## Elevation & Depth

Depth is achieved through color and texture, not shadow.

- **No Drop Shadows**: Avoid `box-shadow` with blur. Shadows imply a digital layer floating above the screen, which contradicts the tactile nature of Wabi-Sabi.
- **Layering**: Use opacity and border colors to suggest depth. A card might sit on the background with a subtle border, but no shadow.
- **Texture**: Subtle noise or paper texture overlays can be used on backgrounds to break up the flatness of digital screens, but must be extremely low opacity (2-5%) to avoid distraction.

## Shapes

Shapes should feel organic and hand-crafted.

- **Rounded Corners**: Minimal rounding (2px - 8px). Avoid fully rounded corners (pill shapes) which feel playful or tech-startup-esque.
- **Borders**: Thin, solid lines. Borders should feel like the edge of a stone or a piece of paper.
- **Icons**: Use line-art icons with varying stroke weights. Avoid filled icons. Icons should look sketched, not vector-perfect.

## Components

### Buttons

Buttons are functional markers, not interactive toys.

- **Shape**: Rectangular with slight rounding (2px).
- **Style**: Flat, no shadows.
- **Interaction**: On hover, the background darkens slightly. No scale transforms. No bounce.
- **Text**: Uppercase with wide letter-spacing or standard case with high line-height. Avoid all-caps if it feels too aggressive; standard case is often more elegant.

### Cards

Cards are containers for content, not floating panels.

- **Style**: Flat background with a thin border (1px).
- **Content**: Minimal. Headlines, body text, and perhaps one image.
- **Images**: Images should be desaturated or have a slight sepia tone to match the overall palette. They should look like photographs taken on film, not digital captures.

### Tables

Tables are for data, not decoration.

- **Style**: Minimal borders. Only horizontal lines between rows, or no lines at all, relying on whitespace for separation.
- **Header**: Light background color, distinct from body rows.
- **Data**: Aligned left for text, right for numbers.

## Do's and Don'ts

### Do
- Use natural, earthy colors.
- Prioritize whitespace and breathing room.
- Use serif fonts for a human, historical feel.
- Embrace asymmetry and organic shapes.
- Keep interactions subtle and respectful of the user's attention.

### Don't
- Use pure black (#000000) or pure white (#FFFFFF).
- Use gradients (especially blue/purple).
- Use glassmorphism or heavy drop shadows.
- Use emojis as icons.
- Use marketing buzzwords ("innovative," "seamless").
- Force symmetry where it doesn't belong.