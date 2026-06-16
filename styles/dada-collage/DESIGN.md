---
version: 1.0.0
name: Dada Collage
description: A visual manifesto of anti-rationality, utilizing random juxtaposition, ready-made artifacts, and typographic violence to dismantle bourgeois aesthetic order.
colors:
  primary:
    name: "Newspaper Ink"
    value: "#1a1a1a"
    hex: "#1a1a1a"
  secondary:
    name: "Clipping Paste"
    value: "#f4f1ea"
    hex: "#f4f1ea"
  tertiary:
    name: "Ultramarine Blue"
    value: "#002e5d"
    hex: "#002e5d"
  neutral:
    name: "Cardboard Brown"
    value: "#8c7b6b"
    hex: "#8c7b6b"
  muted:
    name: "Faded Chlorine"
    value: "#d3d9c8"
    hex: "#d3d9c8"
typography:
  h1:
    fontFamily: "Impact, 'Arial Black', sans-serif"
    fontSize: 48
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -2
  h2:
    fontFamily: "Courier New, monospace"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1
  h3:
    fontFamily: "'Times New Roman', serif"
    fontSize: 24
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "'Georgia', serif"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Courier New, monospace"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1
rounded:
  sm: 0
  md: 0
  lg: 0
spacing:
  sm: 4
  md: 8
  lg: 16
  xl: 32
components:
  button-primary:
    variant: "cutout"
    background: "#1a1a1a"
    color: "#f4f1ea"
    border: "2px solid #000"
    borderRadius: 0
    shadow: "none"
    hover:
      background: "#002e5d"
  card:
    variant: "scrap"
    background: "#f4f1ea"
    border: "1px dashed #1a1a1a"
    borderRadius: 0
    shadow: "4px 4px 0px #1a1a1a"
  table:
    variant: "ledger"
    background: "#fff"
    border: "1px solid #1a1a1a"
    cellPadding: 8
    headerBackground: "#1a1a1a"
    headerColor: "#fff"
---

# Dada Collage Design System

## Overview

This design system rejects the harmony, symmetry, and utility of modernist grids. It is built upon the principles of **Dadaism** (1916-1924), specifically the collage techniques pioneered in Zurich and Berlin. The interface is not a window into a digital space, but a physical assembly of torn paper, newspaper clippings, and typewriter text. It embraces **chaos**, **irony**, and **absurdity**. The user experience is intentionally disorienting, forcing the viewer to confront the randomness of information.

## Colors

The palette is derived from the materials available to early 20th-century artists: cheap newsprint, ink, and binding agents.

- **Primary (#1a1a1a)**: Heavy, industrial ink. Used for main text and structural lines. It should feel permanent and oppressive.
- **Secondary (#f4f1ea)**: Unbleached newsprint. Slightly yellowed, representing the passage of time and the ephemeral nature of news.
- **Tertiary (#002e5d)**: Ultramarine blue. A stark, artificial color often found in vintage advertising clippings. Used for high-contrast accents.
- **Neutral (#8c7b6b)**: Cardboard brown. Represents the raw material of the collage.
- **Muted (#d3d9c8)**: Faded chlorine. The color of old photographs left in the sun.

*Note: Avoid pure white (#ffffff). The background should always be the "paper" color (#f4f1ea) or a dark ink color (#1a1a1a). Pure white feels sterile and corporate.*

## Typography

Typography is not for readability; it is for impact. We mix typefaces aggressively to create visual tension.

- **Headings (H1)**: Use **Impact** or **Arial Black**. Thick, bold, and impersonal. It mimics the headline of a sensationalist newspaper.
- **Subheadings (H2)**: Use **Courier New**. Monospaced, mechanical, and bureaucratic. It represents the machine age.
- **Body Text (H3/Body)**: Use **Georgia** or **Times New Roman**. The traditional serif of printed literature, juxtaposed against the modern sans-serif headers.
- **Captions**: Use **Courier New** again, but smaller. Like a typist's note on the margin of a document.

**Rules:**
- Never use a sans-serif font for body text.
- Never justify text. Left-aligned ragged edges mimic torn paper.
- Allow text to overlap images and other text blocks.
- Use all-caps for emphasis, not italics.

## Layout

The layout is a **non-grid**. Elements are positioned based on visual weight and randomness, not mathematical alignment.

- **Asymmetry**: Balance is achieved through chaos, not symmetry. A large block of text might be balanced by a small, bright image cutout.
- **Overlap**: Elements should intersect. Text should run over images. Images should cover other images.
- **Rotation**: Rotate elements by small angles (3-7 degrees) to simulate hand-placed cutouts.
- **Borders**: Use dashed lines, solid black lines, or no borders. Never use soft shadows or gradients.

## Elevation & Depth

Depth is achieved through **layering** and **shadows**, mimicking physical paper.

- **Shadows**: Hard, black shadows with no blur (`box-shadow: 4px 4px 0px #000`). This creates a stark, graphic effect, as if the paper is casting a shadow on the layer below.
- **Layering**: Use `z-index` to create a sense of physical stacking. The top layer is always the most important or the most absurd.
- **No Blurs**: Never use `backdrop-filter: blur`. The transparency should be solid color or pattern.

## Shapes

- **Rectangles**: All shapes are rectangular. Circles and rounded corners are rejected as bourgeois decadence.
- **Borders**: Use solid black borders (`2px solid #000`) or dashed borders (`1px dashed #000`) to mimic cutting lines.
- **Clipping Masks**: Images should appear to be cut out with scissors. Irregular edges are preferred, but hard rectangular cuts are acceptable if they contrast with the organic content.

## Components

### Button: Primary
A button that looks like a piece of paper pinned to a board.
- **Background**: `#1a1a1a` (Ink)
- **Color**: `#f4f1ea` (Paper)
- **Border**: `2px solid #000`
- **Shadow**: `4px 4px 0px #000`
- **Hover**: Background changes to `#002e5d` (Blue). Text remains white.
- **Text**: All caps, Impact font.

### Card: Scrap
A container that looks like a newspaper clipping taped to a wall.
- **Background**: `#f4f1ea`
- **Border**: `1px dashed #1a1a1a`
- **Shadow**: `4px 4px 0px #1a1a1a`
- **Padding**: 16px
- **Content**: Mix of serif and monospace text. Include a small, low-resolution image.

### Table: Ledger
A table that looks like a financial record from 1920.
- **Background**: `#fff` (or `#f4f1ea`)
- **Border**: `1px solid #1a1a1a`
- **Header**: `#1a1a1a` background, `#fff` text, Courier New font.
- **Cells**: Left-aligned, Georgia font.
- **Rows**: Alternating row colors are prohibited. Instead, use a solid line under each row.

## Do's and Don'ts

### Do
- **Do** use mixed fonts. Contrast serif and sans-serif, or serif and monospace.
- **Do** embrace asymmetry. Let elements overlap and intersect.
- **Do** use hard, black shadows. No blurs.
- **Do** use historical colors: ink, paper, blue, brown.
- **Do** make the interface feel physical and tactile.

### Don't
- **Don't** use rounded corners. Everything is sharp and cut.
- **Don't** use gradients or glassmorphism. It is too modern and clean.
- **Don't** use emojis. Use typographic symbols (e.g., *, +, #, §) instead.
- **Don't** use smooth animations. Use instant, jarring transitions.
- **Don't** prioritize readability over impact. If it's hard to read, it's more Dada.