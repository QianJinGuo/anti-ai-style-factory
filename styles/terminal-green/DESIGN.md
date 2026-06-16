---
version: 1.0.0
name: 终端绿 (Terminal Green)
description: A utilitarian aesthetic rooted in monochrome CRT phosphor displays, prioritizing raw data density and command-line efficiency over graphical embellishment.
colors:
  primary:
    name: "Phosphor Green"
    hex: "#00FF00"
    description: "The standard high-intensity green of early monochrome monitors."
  secondary:
    name: "Dim Green"
    hex: "#008F00"
    description: "Used for secondary text, inactive states, and borders to reduce eye strain."
  tertiary:
    name: "Phosphor White"
    hex: "#E0E0E0"
    description: "Reserved for critical system alerts or active cursor indicators."
  neutral:
    name: "Monitor Black"
    hex: "#050505"
    description: "The deep black of an unlit CRT screen, serving as the primary background."
  muted:
    name: "Scanline Grey"
    hex: "#1A1A1A"
    description: "Subtle background for hover states or disabled elements."
typography:
  h1:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: "32px"
    fontWeight: "400"
    lineHeight: "1.2"
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: "24px"
    fontWeight: "400"
    lineHeight: "1.3"
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: "18px"
    fontWeight: "700"
    lineHeight: "1.4"
    letterSpacing: "0em"
  body-md:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: "16px"
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0em"
  caption:
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: "12px"
    fontWeight: "400"
    lineHeight: "1.4"
    letterSpacing: "0.05em"
rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
spacing:
  sm: "4px"
  md: "8px"
  lg: "16px"
  xl: "32px"
components:
  button-primary:
    background: "#000000"
    border: "1px solid #00FF00"
    color: "#00FF00"
    padding: "8px 16px"
    borderRadius: "0px"
    fontFamily: "'VT323', 'Courier New', monospace"
    fontSize: "16px"
    fontWeight: "700"
    letterSpacing: "0.1em"
    textTransform: "uppercase"
    cursor: "pointer"
    transition: "none"
    hover:
      background: "#00FF00"
      color: "#000000"
      border: "1px solid #00FF00"
  card:
    background: "#050505"
    border: "1px solid #008F00"
    padding: "16px"
    borderRadius: "0px"
    boxShadow: "none"
    margin: "0"
  table:
    border: "1px solid #008F00"
    borderCollapse: "collapse"
    width: "100%"
    td:
      border: "1px solid #008F00"
      padding: "8px"
      color: "#00FF00"
      fontFamily: "'VT323', 'Courier New', monospace"
    th:
      border: "1px solid #00FF00"
      padding: "8px"
      color: "#E0E0E0"
      backgroundColor: "#002200"
      fontFamily: "'VT323', 'Courier New', monospace"
      fontWeight: "700"
      textTransform: "uppercase"
---

# 终端绿 (Terminal Green) Design Specification

## Overview

This design system is a direct translation of the 1970s–1990s monochrome CRT (Cathode Ray Tube) computing environment. It rejects modern skeuomorphism and flat design trends in favor of raw, functional typography and high-contrast monochrome signaling. The philosophy is "Data First, Interface Invisible." Every pixel serves to convey information or command input; decoration is considered noise. The aesthetic is grounded in the physical limitations and characteristics of early green-phosphor monitors, including scanlines, slight glow, and strict grid alignment.

## Colors

The palette is strictly limited to variations of green and black to mimic the phosphor emission of a CRT monitor.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| `primary` | `#00FF00` | Active text, primary buttons, links, focus states. |
| `secondary` | `#008F00` | Inactive text, borders, secondary data, disabled states. |
| `tertiary` | `#E0E0E0` | Critical warnings, system errors, cursor block. |
| `neutral` | `#050505` | Background (Monitor Black). |
| `muted` | `#1A1A1A` | Hover backgrounds, subtle dividers, disabled containers. |

**Note:** No gradients, no shadows, no transparency. Opacity is achieved by using the secondary color (`#008F00`) instead of the primary (`#00FF00`).

## Typography

Typography is the only visual element. It must be monospaced to ensure alignment and readability in fixed-width contexts.

*   **Primary Font:** `'VT323'` (Google Fonts) or `'Courier New'` as fallback.
*   **Weight:** Only `400` (Regular) and `700` (Bold). No italic, no light weights.
*   **Sizing:** Strictly integer-based sizes (12px, 14px, 16px, 24px, 32px).
*   **Spacing:** Zero margin/padding on headings. Line height is tight (1.2–1.4) to maximize data density.
*   **Case:** Headings are UPPERCASE. Body text is sentence case.

## Layout

*   **Grid:** 8px baseline grid. All spacing must be a multiple of 4px.
*   **Alignment:** Left-aligned for all text. Justified text is prohibited (creates uneven spacing in monospace).
*   **Whitespace:** Minimal. Content should feel dense and compact, reflecting the limited screen real estate of early terminals.
*   **Borders:** Solid 1px lines. No rounded corners. All containers are sharp rectangles.

## Elevation & Depth

*   **No Shadows:** Drop shadows are prohibited. Depth is implied through color contrast and border thickness.
*   **Layering:** Use background color changes (`#000000` vs `#002200`) to indicate active states or selected items.
*   **Scanlines:** Optional CSS overlay to simulate CRT scanlines (1px black line every 2px) for authenticity, but must be toggleable for accessibility.

## Shapes

*   **Corners:** All elements are `0px` border-radius. Sharp, angular, and utilitarian.
*   **Icons:** No vector icons. Use ASCII art characters (e.g., `[X]`, `>` , `|`, `-`, `+`) or Unicode block elements (`█`, `▓`, `░`) for visual separation.
*   **Dividers:** Use `────────────────────────` (underscore or box-drawing characters) instead of `<hr>` with borders.

## Components

### Button (Primary)
A rectangular block with a solid border. No hover animations other than color inversion.