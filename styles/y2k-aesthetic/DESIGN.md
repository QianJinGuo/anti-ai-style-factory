version: 1.0.0
name: 千禧虫美学 (Y2K Bug Aesthetic)
description: A digital optimistic, silver-future style characterized by transparent plastics, monospaced code aesthetics, and bubbling organic forms, reflecting the raw, unpolished optimism of the late 90s web.
colors:
  primary: "#00FF00" # Terminal Green
  secondary: "#C0C0C0" # Silver Chrome
  tertiary: "#00FFFF" # Cyan Laser
  neutral: "#1A1A1A" # Deep Void
  muted: "#4A4A4A" # Rusty Wire
typography:
  h1:
    fontFamily: "'Space Mono', 'Courier New', monospace"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: "1.1"
    letterSpacing: "-0.05em"
  h2:
    fontFamily: "'Space Mono', 'Courier New', monospace"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.03em"
  h3:
    fontFamily: "'Space Mono', 'Courier New', monospace"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: "1.3"
    letterSpacing: "0"
  body-md:
    fontFamily: "'Space Mono', 'Courier New', monospace"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.6"
    letterSpacing: "0.02em"
  caption:
    fontFamily: "'Space Mono', 'Courier New', monospace"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "1.4"
    letterSpacing: "0.05em"
rounded:
  sm: "2px"
  md: "12px"
  lg: "24px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
components:
  button-primary:
    background: "#00FF00"
    color: "#000000"
    border: "2px solid #000000"
    borderRadius: "sm"
    fontWeight: 700
    padding: "12px 24px"
    fontFamily: "'Space Mono', 'Courier New', monospace"
  card:
    background: "rgba(192, 192, 192, 0.1)"
    border: "1px solid #C0C0C0"
    borderRadius: "md"
    backdropFilter: "blur(4px)"
    padding: "24px"
  table:
    border: "1px solid #C0C0C0"
    borderRadius: "sm"
    fontFamily: "'Space Mono', 'Courier New', monospace"
```

# 千禧虫美学 (Y2K Bug Aesthetic) Design Specification

## Overview

This design language captures the transitional anxiety and digital optimism of 1996–2003. It is not about sleek minimalism, but about the raw materiality of early digital existence: the hum of CRT monitors, the transparency of cheap plastic packaging, and the glitchy, organic feel of early 3D renders. The aesthetic is "anti-design" in the sense that it embraces the limitations of the era—monospaced text, harsh contrasts, and transparent layers—as features, not bugs. It is silver, it is green, it is transparent, and it is alive.

## Colors

The palette is derived from the hardware limitations and marketing materials of the late 90s.

*   **Primary (`#00FF00`)**: Terminal Green. The color of the command line, success, and green screen. Used for primary actions and highlights.
*   **Secondary (`#C0C0C0`)**: Silver Chrome. The color of Apple iMac G3 translucent plastic and Windows 95 borders. Used for structural elements and borders.
*   **Tertiary (`#00FFFF`)**: Cyan Laser. Used sparingly for hover states or secondary data points.
*   **Neutral (`#1A1A1A`)**: Deep Void. Not pure black, but the dark gray of a powered-off monitor. Used for text.
*   **Muted (`#4A4A4A`)**: Rusty Wire. Used for disabled states and secondary text.

**Rule**: Never use gradients unless they are metallic or chrome. Avoid pure white (`#FFFFFF`) for backgrounds; use `#F0F0F0` or transparent layers over dark backgrounds.

## Typography

Typography is the backbone of this aesthetic. We reject proportional sans-serifs. The web was monospaced, and so is our design.

*   **Font Family**: `'Space Mono'`, `'Courier New'`, monospace.
*   **Rationale**: Monospaced fonts reflect the code-based nature of the internet at the time. They are legible, utilitarian, and carry a sense of technical authority.
*   **Hierarchy**: Use weight and size only. Do not use color to distinguish hierarchy unless it is for error/highlight purposes.
*   **Letter Spacing**: Tighten headings (`-0.05em`) to mimic the cramped feel of early web layouts. Widen captions (`0.05em`) to mimic terminal output.

## Layout

Layouts are grid-based but rigid. Think of a spreadsheet or a terminal window.

*   **Grid**: 12-column grid, but with visible gutters.
*   **Alignment**: Left-aligned text. Centered titles only if they are short.
*   **Whitespace**: Generous but functional. Use spacing to separate logical blocks, not to create "breathing room."
*   **Containers**: Content should feel contained within "windows" or "panels."

## Elevation & Depth

Depth is achieved through transparency and borders, not shadows.

*   **No Drop Shadows**: Avoid fluffy, blurred shadows. They are too modern.
*   **Borders**: Use `1px` or `2px` solid borders in Silver Chrome (`#C0C0C0`) to define layers.
*   **Transparency**: Use `rgba(192, 192, 192, 0.1)` for card backgrounds. This creates a "glass" effect, but it is cold, hard glass, not soft, blurry glassmorphism.
*   **Z-Index**: Keep z-indexes low and explicit. Layers should be clearly defined, not overlapping chaotically.

## Shapes

Shapes are a mix of the geometric and the organic.

*   **Buttons**: Rectangular with slight rounding (`sm: 2px`). They should look like physical buttons on a machine.
*   **Cards**: Rounded corners (`md: 12px`). This references the rounded edges of early 3D models and plastic casings.
*   **Icons**: Use simple, geometric shapes or ASCII art. No emoji. No filled icons. Use outline icons with `2px` stroke.
*   **Decorative Elements**: Use "bubbles" or "blobs" in the background. These should be low-opacity, silver or cyan, and slightly distorted to mimic early 3D rendering artifacts.

## Components

### Button (Primary)

*   **Style**: Solid Terminal Green (`#00FF00`) background, Black (`#000000`) text.
*   **Border**: `2px` solid Black.
*   **Hover**: Invert colors (Black background, Green text).
*   **Rationale**: High contrast, tactile, reminiscent of a physical switch.

### Card

*   **Style**: Transparent Silver (`rgba(192, 192, 192, 0.1)`) background.
*   **Border**: `1px` solid Silver Chrome (`#C0C0C0`).
*   **Padding**: `24px`.
*   **Rationale**: Represents a window into the digital space. The transparency allows the background to show through, creating depth.

### Table

*   **Style**: Silver borders (`#C0C0C0`).
*   **Header**: Silver Chrome background (`#C0C0C0`), Black text.
*   **Rows**: Alternating subtle transparency or no alternation.
*   **Font**: Monospace.
*   **Rationale**: Data should be presented with the clarity of a spreadsheet.

### Input Field

*   **Style**: Transparent background, Silver border (`#C0C0C0`).
*   **Focus**: Terminal Green border (`#00FF00`).
*   **Rationale**: Mimics the active cursor in a terminal.

## Do's and Don'ts

### Do's
*   **DO** use monospaced fonts for all text.
*   **DO** use high-contrast colors (Green on Black, Silver on Dark Gray).
*   **DO** use borders to define structure.
*   **DO** incorporate subtle transparency to create layers.
*   **DO** use geometric, simple icons.

### Don'ts
*   **DON'T** use rounded corners everywhere (`12px` max).
*   **DON'T** use gradients unless they are metallic/chrome.
*   **DON'T** use drop shadows with blur.
*   **DON'T** use emojis as icons.
*   **DON'T** use marketing language like "seamless" or "revolutionary." Use technical, precise language.
*   **DON'T** use Inter, Roboto, or any proportional sans-serif font.
