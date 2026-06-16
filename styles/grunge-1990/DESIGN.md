# GRUNGE-90s DESIGN SYSTEM

## Overview

The **Grunge-90s** design style is an anti-design system born from the Seattle music scene between 1990 and 1996. It rejects the clean, vector-based precision of modern UI in favor of tactile imperfection, photocopied degradation, and structural chaos. This system is not about aesthetics; it is about attitude. It assumes the user is tired of corporate polish and wants something raw, honest, and slightly broken.

Key tenets:
- **Texture over Color**: Use noise, grain, and paper textures to convey depth.
- **Imperfection as Truth**: Misaligned elements, torn edges, and ink bleeds are features, not bugs.
- **Anti-Commercial**: Avoid gradients, drop shadows with blur, and rounded corners.
- **Manual Aesthetic**: Mimic hand-drawn elements, typewriters, and photocopies.

## Colors

The palette is derived from cheap printing inks, urban decay, and neon lights in dark rooms.

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#39ff14` | Toxic Green. Use for hover states, active links, or glitch effects. |
| `secondary` | `#808080` | Concrete Gray. Backgrounds for secondary cards or disabled states. |
| `tertiary` | `#8a0303` | Blood Rust. Warnings, errors, or high-priority alerts. |
| `neutral` | `#0a0a0a` | Ink Black. Primary text, borders, and structural lines. |
| `muted` | `#e8e4d9` | Paper White. Main background. Off-white, warm, slightly dirty. |

**Rules:**
- Never use pure white (`#ffffff`) for backgrounds; it feels too digital.
- Never use pure black (`#000000`) for text; it’s too harsh. Use `#0a0a0a`.
- Contrast must be high. Grunge is not subtle.

## Typography

Typography is the primary vehicle for emotion. We avoid standard sans-serifs (Inter, Roboto) and serif bodies (Georgia). Instead, we use fonts that imply manual creation or mechanical reproduction.

### Type Scale

- **Headings (H1, H2)**: Use `Impact`, `Arial Black`, or `Dingbat` fonts. They are bold, compressed, and aggressive.
- **Body & Captions**: Use `Courier New` or `Courier` (monospace). This mimics typewriters, zines, and code.

### Implementation Details

- **H1**: 56px, 900 weight, tight leading. Often stretched vertically (`transform: scaleY(1.2)`).
- **H2**: 32px, 700 weight, monospace. May have underlines or strikethroughs.
- **Body**: 16px, 400 weight, monospace. Line height 1.5.
- **Caption**: 12px, 700 weight, sans-serif (Helvetica/Arial). Uppercase.

**Rules:**
- Never use smooth font rendering (`antialiased`). Use `pixelated` or `none` to mimic low-res screens.
- Mix fonts intentionally. A heading in `Impact` next to body in `Courier` creates tension.
- Allow text to overflow containers. Let it break.

## Layout

Layouts are asymmetric, grid-less, and chaotic.

- **No Symmetry**: Avoid centered layouts. Push content to the left or right margins.
- **Overlapping**: Allow elements to overlap. Cards may sit on top of images. Text may run over borders.
- **Cramped**: Minimize whitespace. Pack information densely.
- **Borders**: Use thick, solid borders (`2px` or `3px`). Never use hairlines.

**Grid System**: None. Use absolute positioning or flexbox with `margin` adjustments to create misalignment.

## Elevation & Depth

Depth is achieved through hard shadows, not blur.

- **Shadows**: `box-shadow: 4px 4px 0px #0a0a0a;`
- **No Blur**: `0px` blur radius. Shadows are solid blocks of color.
- **Offset**: Shadows are offset to the bottom-right to mimic a photocopy misalignment.

**Rules:**
- Never use `box-shadow: 0 10px 15px -3px rgba(...)`.
- Use multiple layers of hard shadows for complex elements.

## Shapes

- **Corners**: Always `0px`. Squares and rectangles only.
- **Borders**: Solid, thick, black.
- **Textures**: Apply noise or grain overlays to all containers.

**Rules:**
- Never use `border-radius`.
- Never use gradients. Use solid colors or textures.

## Components

### Button Primary

A hard, blocky button with an offset shadow.