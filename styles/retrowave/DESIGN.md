---
version: 1.0.0
name: 复古波 (Retrowave)
description: A digital aesthetic rooted in 1980s synth-pop nostalgia, characterized by high-contrast neon gradients, perspective grids, and monospaced terminal typography.
colors:
  primary:
    name: "Neon Magenta"
    hex: "#ff00ff"
  secondary:
    name: "Electric Cyan"
    hex: "#00ffff"
  tertiary:
    name: "Solar Yellow"
    hex: "#ffff00"
  neutral:
    name: "Void Black"
    hex: "#050510"
  muted:
    name: "Deep Purple"
    hex: "#2d004d"
    hex_light: "#4b0082"
typography:
  h1:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: 64
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -2
  h2:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: 48
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -1
  h3:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: 32
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Share Tech Mono', 'IBM Plex Mono', monospace"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.5
  caption:
    fontFamily: "'Share Tech Mono', 'IBM Plex Mono', monospace"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1
rounded:
  sm: 0
  md: 0
  lg: 0
spacing:
  sm: 8
  md: 16
  lg: 32
  xl: 64
components:
  button-primary:
    style: "solid neon border, no radius, hover glow"
    padding: "12px 24px"
    background: "transparent"
    border: "2px solid #00ffff"
    color: "#00ffff"
    hoverBackground: "#00ffff"
    hoverColor: "#050510"
  card:
    style: "grid background, neon border"
    background: "rgba(5, 5, 16, 0.8)"
    border: "1px solid #ff00ff"
    boxShadow: "0 0 10px rgba(255, 0, 255, 0.3)"
  table:
    style: "terminal style, monospaced, no borders"
    background: "transparent"
    borderColor: "#2d004d"
---

# 复古波 (Retrowave) Design Specification

## Overview

Retrowave is not merely a color palette; it is a digital time capsule. It rejects the soft, friendly, and approachable aesthetics of modern "corporate Memphis" or "glassmorphism" in favor of sharp, angular, and high-contrast visuals. It draws directly from the VHS tape era, arcade cabinets, and early computer terminals. The design philosophy is one of **digital nostalgia**: cold, precise, yet emotionally warm through the lens of memory. Every element should feel like it was rendered in 1985, optimized for CRT monitors with scanlines and chromatic aberration.

## Colors

The palette is built on the subtractive color model of light (RGB) against a void-like darkness. We avoid soft pastels or muted earth tones. Colors must be saturated, electric, and high-contrast.

| Token | Name | Hex | Usage |
|-------|------|-----|-------|
| `--color-primary` | Neon Magenta | `#ff00ff` | Primary actions, accents, glowing lines |
| `--color-secondary` | Electric Cyan | `#00ffff` | Secondary actions, links, data visualization |
| `--color-tertiary` | Solar Yellow | `#ffff00` | Warnings, highlights, sun gradients |
| `--color-neutral` | Void Black | `#050510` | Backgrounds, text base |
| `--color-muted` | Deep Purple | `#2d004d` | Subtle backgrounds, grid lines |
| `--color-muted-light` | Purple Haze | `#4b0082` | Hover states, secondary borders |

**Gradient Rule:** The signature "Sunset Gradient" is mandatory for hero sections and major backgrounds. It must flow vertically from Void Black (`#050510`) at the top, through Deep Purple (`#2d004d`), to Neon Magenta (`#ff00ff`) and Solar Yellow (`#ffff00`) at the bottom horizon.

## Typography

We strictly use **monospaced fonts**. Proportional fonts are forbidden as they break the "terminal" illusion. The text should feel like code, data streams, or retro computer output.

1.  **Headings:** `VT323` or `Courier New`. These fonts have a blocky, pixelated feel that mimics early LCD displays.
2.  **Body/Caption:** `Share Tech Mono` or `IBM Plex Mono`. These are legible but retain the technical, utilitarian aesthetic.

**Text Effects:**
-   Use `text-shadow` to create a "glow" effect on headings.