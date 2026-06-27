---
version: 1.0.0
name: Pop Art
description: "A visual language derived from 1960s mass culture, characterized by high-contrast primary colors, bold outlines, and mechanical reproduction aesthetics."
colors:
  primary: "#FF0000"
  secondary: "#0000FF"
  tertiary: "#FFFF00"
  neutral: "#FFFFFF"
  muted: "#F0F0F0"
  accent: "#000000"
typography:
  h1:
    fontFamily: "'Bebas Neue', 'Impact', sans-serif"
    fontSize: 64
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.02
  h2:
    fontFamily: "'Bebas Neue', 'Impact', sans-serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.02
  h3:
    fontFamily: "'Arial Black', 'Impact', sans-serif"
    fontSize: 32
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0.01
  body-md:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Courier New', 'Lucida Console', monospace"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05
rounded:
  sm: 0
  md: 0
  lg: 0
spacing:
  sm: 8
  md: 16
  lg: 24
  xl: 48
components:
  button-primary:
    backgroundColor: "#FF0000"
    color: "#FFFFFF"
    border: "3px solid #000000"
    borderRadius: 0
    fontWeight: 900
    textTransform: uppercase
    padding: "12px 24px"
    letterSpacing: 0.1
  card:
    backgroundColor: "#FFFFFF"
    border: "4px solid #000000"
    borderRadius: 0
    boxShadow: "8px 8px 0px #000000"
    padding: 24
  table:
    headerBackground: "#0000FF"
    headerColor: "#FFFFFF"
    rowAlternating: "#F0F0F0"
    border: "2px solid #000000"
    fontFamily: "'Courier New', monospace"
---

# Pop Art Design System

## Overview

This design system is built upon the principles of Pop Art, a movement that emerged in the late 1950s and flourished in the 1960s. It rejects the subtlety of modernism in favor of the bold, ironic, and commercial imagery of mass culture. The aesthetic is defined by its rejection of "high art" pretension, embracing instead the visual noise of advertising, comic books, and consumer goods. It is loud, mechanical, and unapologetically graphic.

## Colors

The palette is strictly limited to primary colors and black/white to mimic the limitations of 4-color printing processes. No gradients. No subtle tints. Colors are flat and opaque.

- **Primary (Red)**: `#FF0000` - Used for calls to action and emphasis.
- **Secondary (Blue)**: `#0000FF` - Used for structural elements and headers.
- **Tertiary (Yellow)**: `#FFFF00` - Used for highlights and background accents.
- **Neutral (White)**: `#FFFFFF` - The canvas.
- **Muted (Off-White)**: `#F0F0F0` - Used only for alternating table rows or subtle background shifts.
- **Accent (Black)**: `#000000` - The most important color. Used for outlines, text, and shadows.

## Typography

Typography must feel mechanical, stamped, or printed. We avoid organic or humanist sans-serifs.

- **Headings**: Use `Bebas Neue` or `Impact`. These fonts are tall, condensed, and aggressive. They mimic newspaper headlines and comic book sound effects.
- **Body Text**: Use `Courier New` or `Lucida Console`. Monospace fonts reference typewriters, receipts, and mechanical reproduction.
- **Constraints**: Never italicize headings. Never use soft kerning. Text should feel like it was stamped onto the page.

## Layout

Layouts are grid-based but often broken by asymmetry. Think of a comic strip panel or a newspaper collage.

- **Grid**: Strict 12-column grid for structural alignment.
- **Alignment**: Left-aligned text is mandatory. Centered text is only used for isolated headlines.
- **Whitespace**: Minimal. The design should feel crowded and energetic, not airy.

## Elevation & Depth

Depth is achieved through **hard shadows**, not blurs.

- **Shadow Style**: Solid black offset shadow.
- **Shadow Values**: `8px 8px 0px #000000`.
- **Philosophy**: There is no atmospheric perspective. Objects are either on the page or they are not. The shadow is a graphic element, not a simulation of light.

## Shapes

- **Corners**: `0px` border radius. Everything is rectangular. Sharp edges convey industrial production.
- **Patterns**: Use **Ben-Day dots** (halftone patterns) as background textures for cards or buttons to reference comic book printing techniques.

## Components

### Button Primary

A rectangular block with a thick black border and a hard shadow.

- **Background**: Primary Red (`#FF0000`)
- **Text**: White (`#FFFFFF`), Uppercase, Bold
- **Border**: 3px Solid Black
- **Shadow**: 4px 4px 0px Black
- **Hover State**: Shadow disappears, button moves down 4px.

### Card

A white rectangle with a heavy black border and a hard shadow.

- **Background**: White
- **Border**: 4px Solid Black
- **Shadow**: 8px 8px 0px Black
- **Padding**: 24px
- **Header**: Blue background, White text, Uppercase.

### Table

A rigid, grid-like structure.

- **Headers**: Blue background, White text, Bold.
- **Borders**: 2px Solid Black between all cells.
- **Rows**: Alternating White and Off-White backgrounds.

## Do's and Don'ts

### Do:
- Use thick, black outlines on all interactive elements.
- Employ high-contrast color combinations (e.g., Yellow on Blue).
- Use Ben-Day dot patterns sparingly as texture.
- Keep typography bold and uppercase for headings.
- Embrace asymmetry and collage-like compositions.

### Don't:
- **Never** use drop shadows with blur (`box-shadow: 0 4px 12px rgba(0,0,0,0.1)`).
- **Never** use rounded corners (`border-radius: 8px`).
- **Never** use gradients.
- **Never** use soft, pastel colors.
- **Never** use elegant serif fonts like Garamond or Playfair Display.
- **Never** use minimalist whitespace-heavy layouts.