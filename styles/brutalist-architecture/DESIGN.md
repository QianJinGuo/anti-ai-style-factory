# DESIGN.md

```yaml
version: 1.0.0
name: Brutalism Architecture
description: A raw, unadorned design language prioritizing material honesty, structural clarity, and monumental scale over aesthetic comfort.
colors:
  primary:
    name: Raw Concrete
    hex: "#8A8D8E"
    usage: Primary surfaces, cards, structural elements
  secondary:
    name: Exposed Rebar
    hex: "#A0522D"
    usage: Accents, active states, warning indicators
  tertiary:
    name: Concrete Aggregate
    hex: "#D3D3D3"
    usage: Secondary backgrounds, disabled states, subtle dividers
  neutral:
    name: Slate Grey
    hex: "#333333"
    usage: Primary text, headings, high-contrast borders
  muted:
    name: Dust
    hex: "#666666"
    usage: Secondary text, captions, placeholders
typography:
  h1:
    fontFamily: "Arial Black, Impact, sans-serif"
    fontSize: "3.5rem"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Arial Black, Impact, sans-serif"
    fontSize: "2.5rem"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Arial Black, Impact, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0em"
  body-md:
    fontFamily: "Courier New, Courier, monospace"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
  caption:
    fontFamily: "Courier New, Courier, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
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
    background: "#333333"
    color: "#FFFFFF"
    border: "2px solid #333333"
    padding: "12px 24px"
    font-weight: 700
    text-transform: "uppercase"
    border-radius: "0px"
    hover:
      background: "#8A8D8E"
      color: "#FFFFFF"
      border-color: "#8A8D8E"
  card:
    background: "#8A8D8E"
    border: "1px solid #333333"
    padding: "24px"
    border-radius: "0px"
    box-shadow: "4px 4px 0px #333333"
  table:
    border-collapse: "collapse"
    width: "100%"
    border: "2px solid #333333"
    th:
      background: "#333333"
      color: "#FFFFFF"
      padding: "12px"
      text-align: "left"
      font-weight: 700
    td:
      border-top: "1px solid #666666"
      padding: "12px"
      background: "#D3D3D3"
```

## Overview

Brutalism Architecture (1950–1980) rejects the decorative veneer of modernism in favor of raw material honesty. It celebrates the structural truth of the building, exposing the bones rather than hiding them behind facades. In digital design, this translates to high-contrast layouts, monospaced or heavy sans-serif typography, rigid grids, and a rejection of soft shadows or rounded corners. The interface should feel like a concrete slab: heavy, permanent, and unapologetically functional.

## Colors

The palette is derived from the natural hues of raw concrete, steel, and shadow.

- **Primary (Raw Concrete `#8A8D8E`)**: The dominant surface color. It is not white; it is the color of the material itself. It provides a neutral but textured backdrop that feels industrial.
- **Secondary (Exposed Rebar `#A0522D`)**: A rusted iron orange used sparingly for critical actions or warnings. It mimics the oxidation of structural steel.
- **Tertiary (Concrete Aggregate `#D3D3D3`)**: Lighter grey for secondary surfaces or inactive elements, representing the lighter side of concrete mix.
- **Neutral (Slate Grey `#333333`)**: Near-black used for text and borders. It provides maximum contrast against the grey backgrounds, ensuring legibility without relying on pure black which can be too harsh against grey.
- **Muted (Dust `#666666`)**: Used for secondary information, captions, and placeholders. It recedes visually, mimicking the dust and weathering on concrete surfaces.

## Typography

Typography must be utilitarian and legible. No serif fonts. No elegant script.

- **Headings (Arial Black / Impact)**: Heavy, bold, and blocky. The type should feel carved into stone. Tight letter-spacing creates a solid block of text.
- **Body (Courier New / Monospace)**: Monospaced fonts reflect the technical, blueprint-like nature of architectural plans. They are not "friendly"; they are informational. The fixed width reinforces the grid system.
- **Captions (Courier New)**: Small, uppercase, with wide letter-spacing to mimic stencil labels on construction materials.

## Layout

- **Grid System**: Rigid, visible grids. Borders should be explicit.
- **Whitespace**: Negative space is treated as "void" rather than padding. It is structural, not decorative.
- **Alignment**: Strict left or justified alignment. Centered content is avoided unless it represents a monument.
- **Scale**: Use exaggerated scale differences. Headings should be massive; body text should be compact.

## Elevation & Depth

- **No Blur**: `backdrop-filter: blur()` is strictly prohibited.
- **Hard Shadows**: Shadows are solid, offset, and have no blur. They represent physical projection, not atmospheric depth.
  - Example: `box-shadow: 4px 4px 0px #333333;`
- **Borders**: Thick, solid borders (1px–2px) define elements. They are structural lines, not subtle separators.

## Shapes

- **Zero Border Radius**: All elements are rectangular. `border-radius: 0px` is mandatory.
- **Rectangular Blocks**: Components are built from stacked rectangles. No circles, no pills, no rounded corners.
- **Asymmetry**: While the grid is rigid, content placement can be asymmetrical to create dynamic tension, reflecting the sculptural nature of brutalist architecture.

## Components

### Button (Primary)
- **Shape**: Sharp rectangle.
- **Style**: Solid fill with thick border.
- **Interaction**: On hover, invert colors or shift to a lighter grey. No smooth transitions; use instant state changes or a 0.1s linear transition.
- **Text**: Uppercase, bold, monospaced or heavy sans-serif.

### Card
- **Structure**: A solid block of primary color with a hard shadow.
- **Border**: 1px solid neutral border.
- **Content**: No padding inside the card unless necessary for readability. Content should feel embedded in the block.

### Table
- **Style**: Grid-like, with visible borders for every cell.
- **Header**: Dark background with light text.
- **Rows**: Alternating background colors (Primary vs. Tertiary) to enhance readability without softness.

### Input Field
- **Style**: No border radius. Thick border.
- **Focus State**: Highlight the entire border with the secondary color (Rust Orange).
- **Placeholder**: Muted grey, monospaced.

## Do's and Don'ts

### Do
- **DO** use raw, unpolished colors.
- **DO** expose the structure (borders, grids, shadows).
- **DO** use heavy, bold typography for headings.
- **DO** maintain a rigid, grid-based layout.
- **DO** use monospaced fonts for data and technical content.
- **DO** keep corners sharp (0px radius).

### Don't
- **DON'T** use gradients, glassmorphism, or soft shadows.
- **DON'T** use rounded corners or pill-shaped buttons.
- **DON'T** use elegant serif or thin sans-serif fonts.
- **DON'T** use pastel colors or vibrant, saturated hues.
- **DON'T** add decorative icons or emojis.
- **DON'T** smooth out transitions; keep them abrupt or linear.
- **DON'T** hide structural elements behind layers of UI.