---
version: 1.0.0
name: Memphis Design System
description: A rejection of minimalist austerity through chaotic geometry, primary color collisions, and postmodern irony, prioritizing expressive visual noise over functional silence.
colors:
  primary: "#FF4500" # Orange Red
  secondary: "#00FFFF" # Cyan
  tertiary: "#FFD700" # Gold
  neutral: "#FFFFFF" # White
  muted: "#000000" # Black
typography:
  h1:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  h2:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0px
  h3:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0px
  body-md:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "Courier New, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
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
    background: "#FF4500"
    border: "3px solid #000000"
    color: "#FFFFFF"
    font-weight: 700
    border-radius: 0px
    box-shadow: "4px 4px 0px #000000"
  card:
    background: "#FFFFFF"
    border: "3px solid #000000"
    border-radius: 0px
    box-shadow: "6px 6px 0px #000000"
  table:
    border: "3px solid #000000"
    border-collapse: separate
    border-spacing: 0
    header-bg: "#00FFFF"
    row-alt-bg: "#FFD700"
    cell-border: "1px solid #000000"
---

# Memphis Design System

## Overview

The Memphis design language is a deliberate assault on the "International Style" of modernism. Originating from the Milan-based studio led by Ettore Sottsass, this system rejects the notion that design must be purely functional, neutral, or subtle. Instead, it embraces asymmetry, arbitrary geometric shapes (dots, squiggles, triangles), and clashing primary colors to create interfaces that are playful, ironic, and visually aggressive. It is not about clarity; it is about expression.

## Colors

The palette is strictly limited to high-contrast primary and secondary colors against stark white and black. No gradients. No opacity variations. Colors must be solid, flat, and loud.

- **Primary (Orange Red)**: `#FF4500` - Used for primary actions and dominant visual anchors.
- **Secondary (Cyan)**: `#00FFFF` - Used for backgrounds, highlights, and secondary structural elements.
- **Tertiary (Gold)**: `#FFD700` - Used for accents, warnings, or tertiary data visualization.
- **Neutral (White)**: `#FFFFFF` - The canvas. Do not use gray.
- **Muted (Black)**: `#000000` - Used for all strokes, borders, and text. Never use dark gray.

**Pattern Colors**: When using the characteristic "Arca" or "Wavy" patterns, restrict usage to these exact hex codes to maintain historical fidelity.

## Typography

Typography in Memphis design is typically utilitarian or retro-modern, never elegant or humanist. It serves as a grid against which the chaotic graphics rebel.

- **Headings**: `Futura` or `Century Gothic`. Geometric sans-serifs that feel cold and architectural.
- **Body**: `Helvetica` or `Arial`. Neutral, invisible text to contrast with the decorative elements.
- **Captions/Code**: `Courier New`. Monospace fonts add a layer of bureaucratic irony.

**Usage Rule**: Headings should be uppercase. Body text should be left-aligned. Never justify text.

## Layout

Layouts are asymmetric and grid-breaking.

- **Asymmetry**: Content blocks should not be centered. Offset them to create tension.
- **Overlap**: Elements should overlap each other. Text can sit on top of geometric shapes. Borders can intersect.
- **Whitespace**: Use generous white space, but treat it as a negative space to be filled by shapes, not just empty room.
- **Borders**: All major containers must have a thick, black border (3px minimum). This is the defining structural element of the style.

## Elevation & Depth

Memphis design does not use soft shadows or gradients to denote depth. It uses **hard, offset shadows**.

- **Shadow Style**: Solid black box-shadow with no blur.
- **Offset**: Typically `4px` to `6px` on the X and Y axes.
- **Application**: Apply to buttons, cards, and floating panels to create a "pop-art" sticker effect.
- **No Blur**: `box-shadow: 4px 4px 0px #000000;` is the only valid shadow syntax.

## Shapes

Geometric primitives are the core vocabulary. Decorative elements must be derived from these shapes.

- **Squiggles**: Wavy black lines used as dividers or background textures.
- **Dots**: Solid black circles of varying sizes, often arranged in grids or scattered randomly.
- **Triangles**: Right-angled or equilateral triangles, often filled with primary colors.
- **Arches**: Semi-circles used as frames or decorative headers.
- **Stripes**: Horizontal or vertical black lines, sometimes broken or dashed.

**Implementation**: Use SVG paths or CSS `clip-path` for these shapes. Do not use images.

## Components

### Button (Primary)

A rectangular block with a hard black border and offset shadow. The color must be one of the primary palette colors. Text is white and bold.