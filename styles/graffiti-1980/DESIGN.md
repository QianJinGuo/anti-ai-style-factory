---
version: 1.0.0
name: Graffiti / 涂鸦
description: A raw, unauthorized aesthetic that treats the interface as a public wall, prioritizing aggressive expression, illegible speed, and chemical permanence over readability and order.
colors:
  primary: "#00FF00" # Neon Lime Spray
  secondary: "#FF00FF" # Magenta Highlighter
  tertiary: "#00FFFF" # Cyan Underpaint
  neutral: "#1A1A1A" # Asphalt Black
  muted: "#333333" # Dry Wall Grey
typography:
  h1:
    fontFamily: "'Permanent Marker', 'Marker Felt', cursive"
    fontSize: 48
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -1
  h2:
    fontFamily: "'Permanent Marker', 'Marker Felt', cursive"
    fontSize: 36
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5
  h3:
    fontFamily: "'Permanent Marker', 'Marker Felt', cursive"
    fontSize: 24
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  body-md:
    fontFamily: "'Comic Sans MS', 'Chalkboard SE', cursive"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5
  caption:
    fontFamily: "'Comic Sans MS', 'Chalkboard SE', cursive"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1
rounded:
  sm: 2px # Chipped paint edge
  md: 0px # No rounding, straight cuts
  lg: 0px # Aggressive rectilinear
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    style: "Solid neon fill, thick black stroke, no border radius, text-transform: uppercase, slight rotation"
  card:
    style: "Asphalt background, visible border texture, overlapping elements, drop-shadow with high contrast"
  table:
    style: "Hand-drawn borders, irregular row heights, monospaced typewriter font for data"
```

# DESIGN.md: 涂鸦 (Graffiti)

## Overview

The **涂鸦** style rejects the sanitized, corporate neutrality of modern UI. It is not about "user experience" in the traditional sense; it is about **visibility** and **claiming space**. Inspired by the street art movements of the 1970s through to contemporary digital glitch art, this design system treats the screen as a brick wall. It embraces chaos, illegibility, and the visceral impact of chemical spray. It is anti-design because it prioritizes the *gesture* of creation over the *result* of polish.

## Colors

The palette is derived from aerosol cans and highlighters. Colors are not blended; they are layered. High contrast is mandatory to ensure the "tag" pops against the urban decay of the background.

- **Primary (`#00FF00`)**: Acid Green. Used for primary actions and critical alerts. It screams.
- **Secondary (`#FF00FF`)**: Hot Pink. Used for secondary actions, hover states, and decorative tags.
- **Tertiary (`#00FFFF`)**: Electric Cyan. Used for outlines, strokes, and underlines.
- **Neutral (`#1A1A1A`)**: Wet Asphalt. The base canvas. Not pure black, but the dark grey of a rainy city street.
- **Muted (`#333333`)**: Dried Concrete. Used for disabled states or background textures.

**Rule:** Never use opacity to fade colors. If it needs to recede, make it smaller or cover it with another layer.

## Typography

Typography is the voice of the street. It is loud, unrefined, and often difficult to read. We avoid system sans-serifs entirely.

- **Headers**: Use `Permanent Marker` or `Marker Felt`. The text should look like it was written in haste with a thick felt tip. Tight letter-spacing (-1px) creates a claustrophobic, urgent feel.
- **Body**: Use `Comic Sans MS` or `Chalkboard SE`. This is not a joke; it is a reference to elementary school walls and informal notes. It signals that the content is raw and unedited.
- **Captions**: Small, widely spaced, often rotated or scribbled.

**Rule:** Do not justify text. Let it hang unevenly. If a word doesn't fit, let it overflow or break awkwardly.

## Layout

The layout is **asymmetric and overlapping**. There is no grid. Elements collide.

- **Overlap**: Cards, buttons, and text blocks should physically overlap each other. This creates depth through conflict, not shadow.
- **Rotation**: Apply slight random rotations (-2deg to 2deg) to containers to simulate the imperfection of hand-painted signs.
- **Whitespace**: Minimize whitespace. The wall should be covered. If there is empty space, fill it with a scribble, a tag, or a texture.

## Elevation & Depth

We do not use soft shadows (0 4px 6px rgba(0,0,0,0.1)). That is "AI taste."

- **Hard Shadows**: Use `box-shadow: 4px 4px 0px #000000`. Solid, hard, offset shadows. No blur.
- **Layering**: Depth is achieved by stacking elements. A button sits on top of a card. The card sits on top of the background. The hierarchy is visual, not atmospheric.
- **Texture**: Apply a subtle noise or grain overlay to the background to simulate concrete or brick.

## Shapes

- **Borders**: Thick, irregular black strokes (`2px solid #000000`). Borders should look hand-drawn, not vector-perfect.
- **Radius**: `0px`. Sharp corners. The aesthetic is aggressive and rectangular. If a curve is needed, it should be a rough, hand-sketched circle, not a CSS `border-radius`.
- **Icons**: No emoji. Use simple, bold, black-outlined symbols that look like stickers or stencils.

## Components

### Button (Primary)
- **Shape**: Rectangular, no border radius.
- **Style**: Solid `#00FF00` background. `2px solid #000000` border.
- **Text**: Uppercase, `Permanent Marker`, `#000000`.
- **Interaction**: On hover, shift the button `4px` down and `4px` right, removing the shadow to simulate pressing into the wall.
- **State**: Active state is indistinguishable from hover.

### Card
- **Shape**: `#1A1A1A` background.
- **Border**: `2px solid #00FF00`.
- **Content**: Text should overlap the border slightly. Images should have a hard `#000000` border and a `4px` offset shadow.
- **Decoration**: Include a "tag" in the top-right corner, rotated 15 degrees, with the date or version number.

### Table
- **Style**: No grid lines. Rows are separated by thick horizontal black lines.
- **Text**: `Comic Sans MS`, `#FFFFFF`.
- **Header**: `#FF00FF` background, `#000000` text, uppercase.
- **Row Hover**: Invert colors. `#000000` background, `#00FF00` text.

## Do's and Don'ts

### Do
- **Do** embrace illegibility. If it's too easy to read, it's not graffiti.
- **Do** use high-contrast neon colors against dark backgrounds.
- **Do** allow elements to overlap and collide.
- **Do** use hand-drawn fonts and textures.
- **Do** keep shadows hard and solid.

### Don't
- **Don't** use Inter, Roboto, or Helvetica.
- **Don't** use glassmorphism or blur effects.
- **Don't** center-align everything. Asymmetry is key.
- **Don't** use soft, blurred box-shadows.
- **Don't** smooth out the edges of shapes. Keep them rough.
- **Don't** use marketing language. Use street slang or raw declarations.
