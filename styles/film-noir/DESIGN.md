---
version: 1.0.0
name: Noir
description: A monochromatic, high-contrast aesthetic rooted in the chiaroscuro lighting and psychological tension of 1940s American cinema.
colors:
  primary: "#000000"
  secondary: "#1A1A1A"
  tertiary: "#808080"
  neutral: "#FFFFFF"
  muted: "#B3B3B3"
typography:
  h1:
    fontFamily: "Playfair Display"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02
  h2:
    fontFamily: "Playfair Display"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01
  h3:
    fontFamily: "Playfair Display"
    fontSize: 24
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Source Serif Pro"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01
  caption:
    fontFamily: "IBM Plex Mono"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05
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
    backgroundColor: "#000000"
    color: "#FFFFFF"
    border: "1px solid #000000"
    borderRadius: 0px
    padding: "12px 24px"
    fontFamily: "IBM Plex Mono"
    fontSize: 14
    fontWeight: 500
    letterSpacing: 0.1
    textTransform: uppercase
  card:
    backgroundColor: "#FFFFFF"
    border: "1px solid #E0E0E0"
    borderRadius: 0px
    boxShadow: "none"
    padding: 24px
  table:
    backgroundColor: "#FFFFFF"
    border: "1px solid #000000"
    borderRadius: 0px
    headerBg: "#000000"
    headerColor: "#FFFFFF"
    rowHoverBg: "#F5F5F5"
---

# Noir Design System

## Overview

Noir is not a decoration; it is an atmosphere. Inspired by the American film noir movement of the 1940s and 50s, this design system prioritizes stark contrast, dramatic shadows, and typographic authority. It rejects the softness of modern UI trends in favor of hard lines, deep blacks, and the tension between light and dark. The interface should feel like a detective's case file: organized, serious, and slightly ominous.

## Colors

The palette is strictly monochromatic. Color is irrelevant; value is everything.

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#000000` | Absolute black. Used for text, primary buttons, and deep shadows. |
| `secondary` | `#1A1A1A` | Off-black. Used for backgrounds where pure black would cause eye strain. |
| `tertiary` | `#808080` | Mid-gray. Used for borders, disabled states, and secondary text. |
| `neutral` | `#FFFFFF` | Pure white. Used for primary text on dark backgrounds and card surfaces. |
| `muted` | `#B3B3B3` | Light gray. Used for captions, placeholders, and subtle dividers. |

**Shadows:**
We do not use colored or blurred shadows. We use hard-edged box shadows to simulate the physical presence of objects under a single light source.
- `shadow-sm`: `2px 2px 0px #000000`
- `shadow-md`: `4px 4px 0px #000000`
- `shadow-lg`: `8px 8px 0px #000000`

## Typography

Type is the primary visual element. We use a combination of a high-contrast serif for headings (evoking newspaper headlines and movie posters) and a monospaced font for data (evoking typewriters and police reports).

- **Headings:** `Playfair Display`. High contrast between thick and thin strokes. It commands attention and feels editorial.
- **Body:** `Source Serif Pro`. A readable, traditional serif that maintains the literary quality of the interface.
- **UI/Data:** `IBM Plex Mono`. Used for buttons, labels, and metadata. It introduces a mechanical, bureaucratic feel.

**Rules:**
- Never mix sans-serif fonts.
- Always use uppercase for UI labels (buttons, tabs) with wide letter-spacing.
- Headings should be large and heavy.
- Body text should have generous line height (1.6) to ensure readability in low-light contexts.

## Layout

- **Grid:** Strict 12-column grid.
- **Alignment:** Left-aligned text. Justified text creates uneven spacing that feels messy and unprofessional in this style.
- **Whitespace:** Use whitespace to create "negative space" that feels like darkness. Do not fill every pixel.
- **Borders:** Use 1px solid black lines to separate sections. No padding-based separation; use hard lines.

## Elevation & Depth

Depth is achieved through **hard shadows** and **layering**, not blur.

- **Base Layer:** White background (`#FFFFFF`).
- **Floating Layer:** White card with `box-shadow: 4px 4px 0px #000000`. This creates a crisp, offset shadow that looks like a physical paper document placed on a desk.
- **Overlay Layer:** Semi-transparent black (`rgba(0,0,0,0.8)`) for modals.

## Shapes

- **Border Radius:** `0px` everywhere. No rounded corners. Sharp corners convey seriousness and danger.
- **Icons:** Use simple, geometric SVG icons. No filled icons; use outlined icons with 2px stroke width.
- **Buttons:** Rectangular with hard edges.

## Components

### Button (Primary)
- Background: `#000000`
- Text: `#FFFFFF`
- Border: `1px solid #000000`
- Font: `IBM Plex Mono`, uppercase, 14px
- Hover: Background `#333333`, Text `#FFFFFF`

### Card
- Background: `#FFFFFF`
- Border: `1px solid #000000`
- Shadow: `4px 4px 0px #000000`
- Padding: `24px`
- Header: Bold, `Playfair Display`, 24px

### Table
- Header: `#000000` background, `#FFFFFF` text, `IBM Plex Mono`
- Rows: `#FFFFFF` background, `Source Serif Pro` text
- Borders: `1px solid #E0E0E0` between rows
- Hover: `#F5F5F5` background

### Input Field
- Border: `1px solid #000000`
- Focus: `2px solid #000000` with `0px` offset shadow
- Placeholder: `#B3B3B3`
- Font: `IBM Plex Mono`, 14px

## Do's and Don'ts

### Do
- **Do** use high contrast. If it’s not black and white, it’s not Noir.
- **Do** use serif fonts for headings.
- **Do** use hard, unblurred shadows.
- **Do** use uppercase labels with wide letter-spacing.
- **Do** let the content breathe with ample negative space.

### Don't
- **Don't** use rounded corners.
- **Don't** use gradients.
- **Don't** use colored accents.
- **Don't** use sans-serif fonts like Inter or Roboto.
- **Don't** use soft, blurred shadows.
- **Don't** use emojis.
- **Don't** use marketing buzzwords. Keep the tone dry, factual, and slightly cynical.