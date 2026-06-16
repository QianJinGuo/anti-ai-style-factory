---
version: 1.0.0
name: Constructivism
description: "A utilitarian, anti-decorative design system rooted in industrial production, political utility, and dynamic geometric tension."
colors:
  primary: '#D91E18' # Revolutionary Red
  secondary: '#111111' # Industrial Black
  tertiary: '#F2F0E6' # Unbleached Paper / Newsprint
  neutral: '#E5E5E5' # Steel Gray
  muted: '#999999' # Concrete Dust
typography:
  h1:
    fontFamily: '"Akzidenz-Grotesk", "Helvetica", "Arial", sans-serif'
    fontSize: 64px
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -2px
  h2:
    fontFamily: '"Akzidenz-Grotesk", "Helvetica", "Arial", sans-serif'
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1px
  h3:
    fontFamily: '"Akzidenz-Grotesk", "Helvetica", "Arial", sans-serif'
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0px
  body-md:
    fontFamily: '"Courier New", "Consolas", monospace' # Typewriter aesthetic
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
  caption:
    fontFamily: '"Courier New", "Consolas", monospace'
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
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
    background: '#D91E18'
    color: '#FFFFFF'
    border: 2px solid #111111
    borderRadius: 0px
    padding: '12px 24px'
    fontWeight: 700
    textTransform: uppercase
    letterSpacing: 1px
    boxShadow: '4px 4px 0px #111111'
  card:
    background: '#FFFFFF'
    border: 2px solid #111111
    borderRadius: 0px
    boxShadow: 'none'
    padding: 0
  table:
    borderCollapse: collapse
    width: 100%
    borderColor: '#111111'
    borderWidth: 2px
    borderStyle: solid
  nav:
    background: '#111111'
    color: '#FFFFFF'
    borderLeft: '12px solid #D91E18'
    padding: '16px 0'
---

# 构成主义 (Constructivism) Design Specification

## Overview

Constructivism rejects the concept of art for art's sake, asserting instead that art should be a practice for social purposes. In digital design, this translates to **radical functionality**, **typographic hierarchy over illustration**, and **structural honesty**. There is no decoration; every pixel serves a structural or informational purpose. The interface is not a window but a machine part.

## Colors

The palette is strictly limited to three colors plus white. This reduction is ideological: it mirrors the industrial raw materials and the stark contrast of propaganda posters.

- **Revolutionary Red (#D91E18)**: Used exclusively for action, emphasis, and primary navigation anchors. It is the active element.
- **Industrial Black (#111111)**: Used for text, borders, and structural lines. It provides the heavy foundation.
- **Unbleached Paper (#F2F0E6)**: Used for backgrounds to simulate newsprint and reduce eye strain, avoiding the sterility of pure white.
- **Steel Gray (#E5E5E5)**: Used sparingly for grid lines or secondary structural elements.

**Rule**: Never use gradients. Never use opacity for emphasis. Use weight and position.

## Typography

Typography is the primary visual element. There are no custom icons; the letterforms themselves are the graphics.

- **Headings**: Use heavy, condensed grotesque sans-serifs. They should feel cast in metal. Tight kerning and leading create a block-like density.
- **Body**: Use monospaced fonts (Courier, Consolas) to evoke the typewriter, the telegram, and the factory ledger. This reinforces the idea of data as raw material.
- **Hierarchy**: Established through size, weight, and rotation, not color.

**Rule**: Never use curved fonts. Never use decorative serifs.

## Layout

The layout is dynamic, based on the **diagonal** and the **asymmetrical grid**.

- **Diagonal Composition**: Break the static horizontal/vertical axis. Use diagonal lines or rotated text blocks to create tension and movement.
- **Staircase Typography**: Align text blocks in a cascading, step-like formation to guide the eye diagonally across the screen.
- **Grid**: Use a visible, rigid grid. Lines should be visible (2px solid black) to show the structure of the page.
- **Whitespace**: Use whitespace aggressively to separate distinct functional units. Whitespace is not empty; it is negative space defining the object.

## Elevation & Depth

Constructivism rejects soft shadows and blurs. Depth is created through **overlap** and **hard offset**.

- **Hard Shadows**: If an element must appear raised, use a solid black box-shadow with no blur (`4px 4px 0px #000`).
- **Layering**: Stack elements with high contrast borders.
- **No Blur**: `backdrop-filter` is forbidden. Transparency is only achieved through solid color blocks overlapping.

## Shapes

- **Rectangles**: The fundamental unit.
- **Circles**: Rarely used, only if representing mechanical gears or targets.
- **Lines**: Thick, bold lines are structural elements, not separators.

**Rule**: All borders are `0px` radius. Curves are mechanical, not organic.

## Components

### Button (Primary)
A rectangular block with a thick black border and a hard shadow. The text is uppercase, bold, and left-aligned.