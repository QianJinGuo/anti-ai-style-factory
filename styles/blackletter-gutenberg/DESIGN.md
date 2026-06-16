---
version: 1.0.0
name: Gothic Movable Type (哥特活字)
description: A typographic system rooted in the tactile imperfection and dense density of 15th-century German printing, prioritizing the weight of ink over the clarity of white space.
colors:
  primary: '#1a1a1a'
  secondary: '#8b0000'
  tertiary: '#5c4033'
  neutral: '#f4e4bc'
  muted: '#d4c5a3'
typography:
  h1:
    fontFamily: 'UnifrakturMaguntia, "Fraktur", "Old English Text MT", serif'
    fontSize: '3.5rem'
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: '-0.02em'
  h2:
    fontFamily: 'UnifrakturMaguntia, "Fraktur", "Old English Text MT", serif'
    fontSize: '2.5rem'
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: '-0.01em'
  h3:
    fontFamily: 'UnifrakturMaguntia, "Fraktur", "Old English Text MT", serif'
    fontSize: '1.75rem'
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: '0em'
  body-md:
    fontFamily: '"Libertinus Serif", "Palatino Linotype", "Book Antiqua", Palatino, serif'
    fontSize: '1rem'
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0.01em'
  caption:
    fontFamily: '"Libertinus Mono", "Courier New", Courier, monospace'
    fontSize: '0.85rem'
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0.05em'
rounded:
  sm: '0px'
  md: '0px'
  lg: '0px'
spacing:
  sm: '0.25rem'
  md: '0.5rem'
  lg: '1rem'
  xl: '2rem'
components:
  button-primary:
    background: '#1a1a1a'
    color: '#f4e4bc'
    border: '1px solid #1a1a1a'
    padding: '0.5rem 1rem'
    font-family: 'UnifrakturMaguntia, serif'
    font-size: '1.1rem'
    text-transform: 'uppercase'
    letter-spacing: '0.05em'
  card:
    background: '#f4e4bc'
    border: '1px solid #5c4033'
    padding: '1.5rem'
    box-shadow: '2px 2px 0px #1a1a1a'
  table:
    border-collapse: 'collapse'
    width: '100%'
    font-family: '"Libertinus Serif", serif'
  input:
    background: '#f4e4bc'
    border: '1px solid #5c4033'
    padding: '0.5rem'
    font-family: '"Libertinus Serif", serif'
    color: '#1a1a1a'
---

# Gothic Movable Type Design System

## Overview

This design language rejects the sterile uniformity of modern digital interfaces in favor of the historical authenticity of early German printing (c. 1450–1600). It is not designed for "user engagement" but for the solemn transmission of knowledge. The interface mimics the physical constraints of movable type: ink bleed, paper texture, and the rigid geometry of Fraktur script. White space is not a luxury; it is the parchment itself.

## Colors

The palette is derived from the materials of the press: iron gall ink, linen rag paper, and blood-red rubrics.

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#1a1a1a` | Iron Gall Ink. Used for body text, borders, and dominant structural elements. Should appear slightly uneven. |
| `secondary` | `#8b0000` | Rubrication. Reserved for drop caps, section dividers, and critical alerts. |
| `tertiary` | `#5c4033` | Binding Leather. Used for subtle borders, inactive states, and secondary dividers. |
| `neutral` | `#f4e4bc` | Parchment. The default background. Must have a noise texture applied to simulate rag paper grain. |
| `muted` | `#d4c5a3` | Faded Ink. Used for captions, timestamps, and disabled text. |

## Typography

Typography is the primary visual layer. There are no sans-serif fonts. Clarity is achieved through hierarchy, not legibility optimization.

### Primary Typeface: Fraktur
**Font:** `UnifrakturMaguntia` (Google Fonts) or fallback to generic `Fraktur`.
**Usage:** Headings (H1-H3), Button Labels, Navigation Headers.
**Philosophy:** The angular, broken strokes of Fraktur create a dense visual rhythm. It demands respect and slows reading speed intentionally.

### Secondary Typeface: Serif
**Font:** `Libertinus Serif` or `Palatino`.
**Usage:** Body copy, paragraphs, long-form text.
**Philosophy:** A transitional serif that echoes the roman typefaces of the late 15th century. It must be set tightly.

### Tertiary Typeface: Monospace
**Font:** `Libertinus Mono` or `Courier New`.
**Usage:** Footnotes, citations, code blocks, metadata.
**Philosophy:** Represents the mechanical nature of the printing press.

### Typographic Rules
1.  **Drop Caps:** The first letter of every new section must be a `secondary` colored, large-scale Fraktur initial, dropping 3 lines deep.
2.  **Justification:** Text must be fully justified with hyphenation enabled. Ragged right edges are unacceptable.
3.  **Letter Spacing:** Headings should have slight negative letter-spacing (`-0.02em`) to mimic the compression of ink on paper. Body text should have neutral spacing.

## Layout

Layout is grid-based but rigid. Margins are generous to frame the content like a page in a codex.

-   **Grid:** 12-column grid, but often treated as a single column of text with wide margins.
-   **Margins:** Minimum 2rem on all sides.
-   **Vertical Rhythm:** Line height is fixed at 1.5 for body text. Headings have tight line heights (1.1-1.2).
-   **No Scroll-Inducing Whitespace:** Content should feel dense. Avoid padding that feels "empty."

## Elevation & Depth

Depth is achieved through hard shadows, not blur.

-   **Shadows:** `box-shadow: 2px 2px 0px #1a1a1a;`
-   **Application:** Applied to cards, modals, and buttons.
-   **Philosophy:** This mimics the layered impression of a woodblock or the physical stacking of paper. No blur, no diffusion.

## Shapes

-   **Border Radius:** `0px` for all elements.
-   **Borders:** 1px solid lines using `tertiary` or `primary`.
-   **Dividers:** Double horizontal lines (`border-top: 1px solid #1a1a1a; border-bottom: 1px solid #1a1a1a;`) to separate sections.

## Components

### Buttons
-   **Style:** Square edges, high contrast.
-   **Hover:** Invert colors (`background: #f4e4bc; color: #1a1a1a;`).
-   **Font:** Fraktur, uppercase.
-   **Effect:** Hard shadow persists on hover.

### Cards
-   **Style:** Parchment background, single solid border.
-   **Content:** Dense text. No icons.
-   **Header:** H3 with a top border separator.

### Tables
-   **Style:** Minimalist. Only bottom borders on headers and rows.
-   **Font:** Serif for data, Monospace for labels.
-   **Alternating Rows:** Optional, using `muted` background for even rows to simulate ruled paper.

### Inputs
-   **Style:** Underline only or single border.
-   **Focus:** Change border color to `secondary`.
-   **Placeholder:** Italicized, `muted` color.

## Do's and Don'ts

### Do
-   Use `UnifrakturMaguntia` for all headings.
-   Apply a subtle noise overlay to the `neutral` background.
-   Use `secondary` color for the first letter of paragraphs (drop cap).
-   Keep borders sharp and unblurred.
-   Justify all body text.

### Don't
-   **NEVER** use sans-serif fonts (Inter, Roboto, Helvetica).
-   **NEVER** use rounded corners.
-   **NEVER** use soft, blurred box-shadows.
-   **NEVER** use purple, blue, or vibrant gradient colors.
-   **NEVER** use emoji as icons. Use text-based symbols (e.g., `*`, `†`, `§`) or Fraktur characters if necessary.
-   **NEVER** use marketing buzzwords. Use archaic or formal language.