---
version: 1.0.0
name: Islamic Geometric
description: A design system rooted in the mathematical precision of Tawhid, utilizing infinite repetition and strict symmetry to evoke spiritual order without figuration.
colors:
  primary: "#00695C" # Deep Turquoise (Firoza) - representing paradise and water
  secondary: "#C5A059" # Muted Gold (Zahab) - representing light and divinity
  tertiary: "#1A232E" # Deep Indigo/Black - representing the infinite void/night sky
  neutral: "#F7F5F0" # Raw Cotton/Plaster - representing purity and canvas
  muted: "#8C9E9C" # Faded Stone - representing history and structure

typography:
  h1:
    fontFamily: "Amiri, Noto Naskh Arabic"
    fontSize: "3.5rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Amiri, Noto Naskh Arabic"
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Amiri, Noto Naskh Arabic"
    fontSize: "1.75rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.01em"
  body-md:
    fontFamily: "Amiri, Noto Naskh Arabic"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: "0.02em"
  caption:
    fontFamily: "Amiri, Noto Naskh Arabic"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0.05em"
    textTransform: "uppercase"

rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"

spacing:
  sm: "0.5rem"
  md: "1rem"
  lg: "2rem"
  xl: "4rem"

components:
  button-primary:
    background: "#00695C"
    color: "#F7F5F0"
    border: "1px solid #C5A059"
    borderRadius: "0px"
    padding: "0.75rem 1.5rem"
    letterSpacing: "0.05em"
    fontWeight: 600
    textTransform: "uppercase"
    transition: "background 0.2s ease"
  card:
    background: "#FFFFFF"
    border: "1px solid #E0E0E0"
    borderRadius: "0px"
    padding: "2rem"
    boxShadow: "none"
  table:
    borderCollapse: "collapse"
    width: "100%"
    borderColor: "#C5A059"
    borderWidth: "1px"
---

# Islamic Geometric Design System

## Overview

This design system is built upon the principles of Islamic geometry: **Tawhid** (unity), **Infinity**, and **Balance**. It rejects arbitrary decoration in favor of structural integrity derived from mathematical patterns. The aesthetic is characterized by sharp angles, intricate interlacing lines, and a restrained palette that emphasizes texture and light over color saturation. There are no rounded corners, no soft shadows, and no figural imagery. The interface should feel like a page from a medieval manuscript or the floor of a grand mosque—precise, enduring, and meditative.

## Colors

The palette is derived from natural pigments and architectural materials of the Islamic Golden Age.

- **Primary (#00695C)**: Deep Turquoise. Used for primary actions and key structural elements. It evokes the tile work of Isfahan.
- **Secondary (#C5A059)**: Muted Gold. Used for borders, icons, and accents. It represents the gold leaf in illumination.
- **Tertiary (#1A232E)**: Deep Indigo. Used for headings and high-contrast text. It represents the night sky and depth.
- **Neutral (#F7F5F0)**: Raw Cotton. The background color. It simulates the texture of unbleached paper or plaster, providing warmth without the sterility of pure white.
- **Muted (#8C9E9C)**: Faded Stone. Used for disabled states, secondary borders, and subtle dividers.

## Typography

Type is treated as geometry. We use serif typefaces with high contrast between thick and thin strokes, mimicking the variation in calligraphic pens.

- **Font Family**: `Amiri` or `Noto Naskh Arabic`. These fonts have the historical lineage of Thuluth and Naskh scripts.
- **Hierarchy**: Headings are tight and authoritative. Body text is generous with wide line-heights (1.8) to facilitate slow, contemplative reading.
- **Letter Spacing**: Uppercase captions have significant letter spacing to create rhythm, mirroring the spacing in geometric star patterns.

## Layout

- **Grid**: The layout follows a modular grid based on the octagon and the square. Content blocks should align to strict vertical and horizontal axes.
- **Whitespace**: Whitespace is not empty; it is "negative space" that defines the positive shapes. Use ample padding to allow the eye to rest between complex patterns.
- **Symmetry**: Whenever possible, content should be centered or perfectly balanced. Asymmetry is used only to create dynamic tension, not chaos.

## Elevation & Depth

- **No Shadows**: Elevation is achieved through **borders** and **color contrast**, not blur.
- **Borders**: Use 1px or 2px solid borders in Gold or Stone to define containers.
- **Layering**: Layers are distinguished by background color shifts (e.g., White on Raw Cotton) rather than drop shadows.

## Shapes

- **No Border Radius**: All elements are square or rectangular. `border-radius: 0` is mandatory.
- **Patterns**: Use SVG backgrounds for geometric motifs (Arabesque, Girih). These patterns should be subtle (opacity 0.05 - 0.1) and serve as texture, not distraction.
- **Icons**: Icons must be linear, geometric, and monoline. Avoid filled icons. Use simple geometric shapes (circles, squares, triangles) combined to form abstract symbols.

## Components

### Buttons
Buttons are sharp rectangles with a gold border. The primary button is filled with Turquoise. On hover, the background darkens slightly, or the border thickens. No rounded corners.