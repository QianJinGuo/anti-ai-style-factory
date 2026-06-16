```yaml
version: 1.0.0
name: Tufte Data-Ink Ratio
description: A minimalist data visualization style that strips all non-essential graphical elements to maximize the density of information per unit of ink, prioritizing clarity, precision, and intellectual honesty over decoration.
colors:
  primary:
    hex: "#1a1a1a"
    name: "Data Black"
    usage: "Primary text, data lines, axes"
  secondary:
    hex: "#4d4d4d"
    name: "Subtle Grey"
    usage: "Secondary text, gridlines (if necessary), labels"
  tertiary:
    hex: "#b0b0b0"
    name: "Light Grey"
    usage: "Backgrounds for sparklines, faint separators"
  neutral:
    hex: "#ffffff"
    name: "Paper White"
    usage: "Canvas background"
  muted:
    hex: "#e8e8e8"
    name: "Off-White"
    usage: "Inactive states, disabled elements"
typography:
  h1:
    fontFamily: "IBM Plex Serif"
    fontSize: 24
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.5
  h2:
    fontFamily: "IBM Plex Serif"
    fontSize: 20
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.4
  h3:
    fontFamily: "IBM Plex Serif"
    fontSize: 16
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.3
  body-md:
    fontFamily: "IBM Plex Sans"
    fontSize: 14
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.1
  caption:
    fontFamily: "IBM Plex Mono"
    fontSize: 11
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2
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
    style: "Borderless, text-only, underline on hover"
    background: "transparent"
    border: "none"
    color: "primary"
  card:
    style: "No border, no shadow, defined by whitespace"
    background: "neutral"
    border: "none"
    shadow: "none"
  table:
    style: "Minimal headers, bottom border only, aligned right for numbers"
    background: "neutral"
    border: "none"
    shadow: "none"
```

# Tufte Data-Ink Ratio Design System

## Overview

This design system is built on the philosophy of **Edward Tufte's "The Visual Display of Quantitative Information"**. The core tenet is the **Data-Ink Ratio**: the proportion of non-erased ink used to present data. Every pixel, line, and color must serve to communicate information directly. If it does not add to the understanding of the data, it is clutter and must be removed. This style rejects the "chart junk" of modern dashboards (grids, shadows, gradients) in favor of a clean, academic, and high-fidelity aesthetic.

## Colors

The palette is strictly monochromatic with high contrast. Color is used sparingly, only to distinguish distinct data series or highlight specific anomalies, never for decoration.

- **Data Black (`#1a1a1a`)**: The primary color for all text and primary data lines. It should appear crisp against the white background.
- **Subtle Grey (`#4d4d4d`)**: Used for axis labels, legends, and secondary annotations. It must be legible but visually subordinate to the data.
- **Light Grey (`#b0b0b0`)**: Reserved for background elements that are not part of the data, such as sparkline backgrounds or very faint separators.
- **Paper White (`#ffffff`)**: The canvas. No gray backgrounds for cards. The white space is part of the design.
- **Off-White (`#e8e8e8`)**: Used for disabled states or very low-priority UI elements that do not interact with the data.

**Rule:** Never use saturated colors unless the data itself is categorical and requires distinct hues. Even then, use muted, desaturated tones (e.g., `#2c7bb6` for blue, `#d7191c` for red) rather than vibrant UI colors.

## Typography

Typography is the primary vehicle for information. We use a serif font for headings to evoke academic rigor and a sans-serif for body text for readability. Monospace is used for data values to ensure alignment and precision.

- **Headings (`IBM Plex Serif`)**: Bold, tight line height. The serif font adds authority and historical context, distinguishing headers from the data itself.
- **Body (`IBM Plex Sans`)**: Clean, neutral, highly legible at small sizes.
- **Data/Captions (`IBM Plex Mono`)**: Essential for numbers. The monospaced font ensures that digits align vertically, facilitating easy comparison of values in tables and labels.

**Rule:** Avoid decorative fonts. Use font weight (light, regular, bold) and size to establish hierarchy, not color.

## Layout

Layout is driven by content density and proximity.

- **No Grids**: Do not use background grid lines. If you need alignment, use whitespace or subtle vertical rules.
- **Proximity**: Related data points and their labels should be placed immediately adjacent to each other. Avoid legends that require the eye to jump back and forth.
- **Sparklines**: Integrate sparklines directly into the text flow or table cells to show trend context without taking up vertical space.
- **Whitespace**: Use whitespace as an active design element. It separates data series and reduces cognitive load.

**Rule:** The layout should feel like a page from a high-end scientific journal, not a web dashboard.

## Elevation & Depth

**Zero Elevation.**

- **No Shadows**: Drop shadows imply physical layers, which is irrelevant to data.
- **No Borders**: Cards should not have borders. Separation is achieved through spacing.
- **Flat Design**: The interface is completely flat. Depth is conveyed through contrast and position, not elevation.

**Rule:** If it doesn't cast a shadow in the real world, it shouldn't cast a shadow in the UI.

## Shapes

**Zero Rounded Corners.**

- **Sharp Edges**: All elements (buttons, inputs, containers) have `0px` border radius. This reinforces the precision and technical nature of the data.
- **Lines**: Use thin, crisp lines (`1px`) for axes and separators.

**Rule:** Roundness implies softness and friendliness. We are presenting hard facts.

## Components

### Button (Primary)
- **Style**: Text-only. No background fill.
- **Interaction**: Underline on hover.
- **Rationale**: Buttons are actions, not data. They should be unobtrusive until needed.

### Card
- **Style**: No border, no shadow, no background color change.
- **Rationale**: A "card" is a conceptual container, not a physical object. In data visualization, containers are defined by proximity and spacing.

### Table
- **Style**:
  - Headers: Bold, uppercase, small font size.
  - Rows: Alternating row colors are **forbidden**. Use a single horizontal line under the header.
  - Alignment: Text left-aligned, numbers right-aligned.
  - Borders: No vertical borders. Only a bottom border on the header row.
- **Rationale**: Tables are for precise reading. Visual noise must be eliminated.

### Chart
- **Style**:
  - Axes: Thin, black lines. No tick marks unless necessary for precision.
  - Labels: Placed directly on the data line or point, not in a legend.
  - Lines: Use thin strokes (`1px` or `2px`).
  - Fill: Avoid area fills unless comparing magnitude between two series.
- **Rationale**: The line is the data. The axis is the reference. Everything else is clutter.

## Do's and Don'ts

### Do's
- **Do** use whitespace to separate data series.
- **Do** align numbers to the right in tables.
- **Do** use serif fonts for titles to establish authority.
- **Do** integrate sparklines into text.
- **Do** label data directly instead of using legends.

### Don'ts
- **Don't** use drop shadows or gradients.
- **Don't** use rounded corners.
- **Don't** use bright, saturated colors for decorative elements.
- **Don't** add grid lines unless they are essential for reading values.
- **Don't** use emojis or icons to represent data.
- **Don't** use "marketing" language in labels. Be precise.