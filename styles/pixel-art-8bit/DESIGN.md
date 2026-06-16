version: 1.0.0
name: 像素艺术 (Pixel Art)
description: A rigid, grid-bound aesthetic that celebrates the technical limitations of early CRT displays through exact integer-based positioning and a constrained, historically accurate color palette.
colors:
  primary: "#00FF00" # Terminal Green
  secondary: "#FF00FF" # Magenta (Atari/Commodore accent)
  tertiary: "#FFFF00" # Yellow (Warning/High contrast)
  neutral: "#000000" # Pure Black
  muted: "#555555" # Dark Gray (Scanline depth)
  background: "#111111" # Off-black for CRT phosphor feel
  surface: "#222222" # Dark gray for UI containers
  text: "#FFFFFF" # Pure White
  text-muted: "#AAAAAA" # Dimmed white
  border: "#444444" # Hard edge separator
  success: "#00FF00"
  warning: "#FFFF00"
  error: "#FF0000"
typography:
  h1:
    fontFamily: "'Press Start 2P', 'Courier New', monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: -1px
  h2:
    fontFamily: "'Press Start 2P', 'Courier New', monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: -0.5px
  h3:
    fontFamily: "'Press Start 2P', 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  body-md:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.5px
  caption:
    fontFamily: "'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 4px
  md: 8px
  lg: 16px
  xl: 32px
components:
  button-primary:
    background: "#000000"
    border: "2px solid #00FF00"
    color: "#00FF00"
    padding: "8px 16px"
    font-family: "'Press Start 2P', monospace"
    font-size: 12px
    text-transform: uppercase
    cursor: pointer
    transition: none
    active:
      background: "#00FF00"
      color: "#000000"
      transform: translateY(2px)
  card:
    background: "#111111"
    border: "2px solid #444444"
    padding: 0
    box-shadow: "4px 4px 0px #000000"
  table:
    border-collapse: collapse
    width: 100%
    font-family: "'VT323', monospace"
    font-size: 16px
  input:
    background: "#000000"
    border: "2px solid #444444"
    color: "#00FF00"
    font-family: "'VT323', monospace"
    padding: "8px"
    caret-color: "#00FF00"
    outline: none
    focus:
      border-color: "#00FF00"
  checkbox:
    width: 16px
    height: 16px
    border: "2px solid #00FF00"
    background: "#000000"
    appearance: none
    cursor: pointer
    position: relative
    checked:
      background: "#00FF00"
      content: "✓"
      color: "#000000"
      font-weight: bold
      display: flex
      align-items: center
      justify-content: center
      font-size: 12px
```

# 像素艺术 (Pixel Art) Design Specification

## Overview
This design system is rooted in the constraints of 8-bit and 16-bit computing (1977-1995). It rejects modern fluidity, anti-aliasing, and soft shadows in favor of hard edges, integer-based geometry, and a strictly limited color palette. The interface should feel like a terminal command line or a retro game HUD. Every pixel must have a purpose; decoration is forbidden. The aesthetic is functional, nostalgic, and brutally honest about its digital nature.

## Colors
The palette is derived from the NTSC/PAL color limits and early VGA/EGA displays. We use a maximum of 8 distinct colors for any single element to maintain the "8-color board" principle.

- **Primary (`#00FF00`)**: Terminal Green. Used for active states, primary actions, and success indicators. High contrast against black.
- **Secondary (`#FF00FF`)**: Magenta. Used for secondary actions or highlights. Historically accurate to Commodore 64 and Atari.
- **Tertiary (`#FFFF00`)**: Yellow. Used for warnings or high-priority text.
- **Neutral (`#000000`)**: Pure Black. The default background and text color for white-mode themes.
- **Muted (`#555555`)**: Dark Gray. Used for disabled states or secondary borders.
- **Surface (`#222222`)**: Off-black. Used for container backgrounds to create depth without blur.
- **Text (`#FFFFFF`)**: Pure White. For high-readability text on dark backgrounds.

**Rule**: Do not use gradients. Do not use opacity for blending. If you need a lighter shade, use a lighter hex code from the palette, not `rgba()`.

## Typography
Typography must be monospaced. Proportional fonts are rejected as they break the grid alignment essential to pixel art.

- **Headings**: Use `'Press Start 2P'` or similar high-readability pixel font. Large sizes (32px+) for H1, smaller for H2/H3.
- **Body**: Use `'VT323'` or `'Courier New'`. This font mimics the dot-matrix printer style of early terminals. It is readable at small sizes but retains the pixelated character.
- **Captions/Metadata**: Use `'Courier New'` or `'Consolas'`. Standard monospace for code snippets or system logs.

**Rule**: Do not use `font-smoothing: antialiased`. We want jagged edges. Use `text-rendering: optimizeSpeed` or `crisp-edges` to ensure pixels remain sharp.

## Layout
Layouts are grid-based. Use a `4px` or `8px` baseline grid. All margins, padding, and widths must be multiples of 4.

- **No Fluidity**: Avoid `vw` or `vh` for core layout dimensions. Use fixed pixels or percentages that snap to the grid.
- **Alignment**: Left-aligned text. Center-aligned titles only if they fit the grid width exactly.
- **Whitespace**: Use generous whitespace to separate distinct UI blocks, but keep internal padding tight (4px-8px).

## Elevation & Depth
Depth is achieved through hard shadows, not blur.

- **Shadows**: Use `box-shadow` with `0px` blur radius.
  - Example: `box-shadow: 4px 4px 0px #000000;`
- **Borders**: Use 2px solid borders to define elements. 1px is too thin for retro displays; 4px is too thick for text areas.
- **No Blur**: Absolutely no `backdrop-filter: blur()`. No `rgba(255,255,255,0.1)` overlays.

## Shapes
All shapes are rectangular.

- **No Rounded Corners**: `border-radius: 0px` for all elements.
- **Borders**: Hard, solid lines. Dashed borders can be used for "inactive" or "placeholder" states.
- **Icons**: Use SVG icons with `shape-rendering="crispEdges"`. Do not use emoji. Do not use feather icons or FontAwesome (too smooth). Create custom pixel-art SVGs or use a library like `pixel-art-icons`.

## Components

### Buttons
- **Style**: Flat, with a hard right/bottom shadow.
- **Hover**: Invert colors (black background, green text) or shift the shadow.
- **Active**: Shift the button `2px` down and right to simulate a physical press.

### Cards/Containers
- **Style**: Dark background (`#111111`), 2px border (`#444444`), hard shadow (`4px 4px 0px #000000`).
- **Header**: Distinct background color (`#222222`) with a bottom border.
- **Content**: Padding of `16px`.

### Tables
- **Style**: No alternating row colors. Use borders between all cells.
- **Header**: Bold, uppercase, left-aligned.
- **Data**: Monospace font. Align numbers to the right.

### Inputs
- **Style**: Black background, green border.
- **Focus**: Green border, green caret.
- **Placeholder**: Dark gray text.

### Checkboxes/Radios
- **Style**: Custom styled `div`s or `input`s with 2px borders.
- **Checked**: Fill with primary color, add a checkmark character (`✓`) in the center.

## Do's and Don'ts

### Do
- Use `box-shadow` with `0px` blur for depth.
- Use monospace fonts for all text.
- Keep colors flat and solid.
- Align elements to a 4px or 8px grid.
- Use uppercase for labels and buttons.
- Use hard borders to define structure.

### Don't
- Do not use `border-radius`.
- Do not use `backdrop-filter` or `blur`.
- Do not use gradients or transparency.
- Do not use proportional fonts (Helvetica, Roboto, etc.).
- Do not use emoji as icons.
- Do not use marketing jargon ("seamless", "next-gen").
- Do not use `font-smoothing: antialiased`.
