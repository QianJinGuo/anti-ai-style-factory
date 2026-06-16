---
version: 1.0.0
name: 活版印刷 (Letterpress)
description: 一种致敬145年凸版印刷工艺的视觉语言，强调物理压痕、油墨渗透与纸张纤维的原始触感，摒弃数字界面的平滑与完美，拥抱手工制作的温度与不完美。
colors:
  primary: "#2C2C2C"
  secondary: "#8B4513"
  tertiary: "#556B2F"
  neutral: "#F5F5DC"
  muted: "#A9A9A9"
typography:
  h1:
    fontFamily: "Playfair Display"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02
  h2:
    fontFamily: "Playfair Display"
    fontSize: 32
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01
  h3:
    fontFamily: "Playfair Display"
    fontSize: 24
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "EB Garamond"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0.01
  caption:
    fontFamily: "EB Garamond"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.05
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
    variant: "inked-plate"
    style: "solid-border, no-radius, serif-font"
  card:
    variant: "paper-sheet"
    style: "high-texture-bg, deep-shadow, no-radius"
  table:
    variant: "ledger"
    style: "single-line-divider, monospaced-numeric, high-contrast"
---

# 活版印刷 (Letterpress) Design Specification

## Overview

The **活版印刷** (Letterpress) design style is a digital interpretation of the tactile experience of letterpress printing. It rejects the sterile, frictionless nature of modern UI in favor of materiality, weight, and history. Every element should feel as if it were pressed onto heavy, textured cotton paper with oil-based ink. The aesthetic is defined by **imperfect registration**, **ink bleed**, **deep embossing**, and **organic paper textures**. It is not about decoration; it is about the honest representation of the printing process.

## Colors

The palette is derived from traditional oil-based inks and unbleached cotton rag paper. Colors are muted, earthy, and high-contrast. Avoid pure blacks or pure whites; everything is grounded in the paper's natural tone.

- **Primary (`#2C2C2C`)**: *Charcoal Ink*. Not pure black, but a deep, rich charcoal that simulates oil-based ink absorption.
- **Secondary (`#8B4513`)**: *Raw Umber*. A deep, earthy brown used for accents, links, or secondary text, reminiscent of aged leather bindings.
- **Tertiary (`#556B2F`)**: *Forest Green*. A muted, natural green for success states or historical references, inspired by early botanical prints.
- **Neutral (`#F5F5DC`)**: *Cotton Rag*. The base background color. Warm, off-white, with visible fiber texture. Never pure white (`#FFFFFF`).
- **Muted (`#A9A9A9`)**: *Faded Ink*. Used for disabled states, placeholders, or secondary metadata, simulating ink that has worn away over time.

## Typography

Typography is the soul of this style. We use high-contrast serif fonts that mimic the sharp edges and thick/thin strokes of metal type. No sans-serifs. No rounded edges.

- **Headings**: `Playfair Display`. A high-contrast Didone serif. Use it for titles and large statements. The contrast between thick and thin strokes should be exaggerated.
- **Body**: `EB Garamond`. A classic, readable serif based on 16th-century models. It provides excellent legibility at small sizes while maintaining historical authenticity.
- **Captions/Metadata**: `EB Garamond` with increased letter-spacing (`0.05em`) to simulate the tight justification of justified text blocks.

**Rules:**
- Do not use font weights lighter than 400 for body text; thin strokes may not render well on low-res screens.
- Use `text-transform: uppercase` sparingly, only for small caps or labels, mimicking metal type headers.

## Layout

Layouts should feel structured yet organic. Avoid rigid grids where possible; instead, use a **modular grid** that allows for slight irregularities.

- **Margins**: Generous margins to simulate the "white space" of a printed page. Minimum 48px on desktop, 24px on mobile.
- **Alignment**: Justified text is encouraged for body paragraphs, but hyphenation must be enabled to prevent uneven word spacing (rivers of white).
- **Grid**: Use a 12-column grid, but allow content to span uneven columns (e.g., 5/7 or 7/5) to break monotony.

## Elevation & Depth

Depth is achieved not through shadows, but through **embossing** and **debossing**.

- **Embossed Text**: Use `text-shadow` with a very subtle offset to simulate raised type.