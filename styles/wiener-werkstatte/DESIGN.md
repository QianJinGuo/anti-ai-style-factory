---
version: 1.0.0
name: Vienna Workshop
description: A rigorous application of Koloman Moser’s geometric rationalism, where ornament is reduced to the square and function dictates form, eliminating the distinction between art and craft.
colors:
  primary: "#C5A059"
  secondary: "#1A1A1A"
  tertiary: "#F2F0E9"
  neutral: "#8C8C8C"
  muted: "#E6E4DB"
typography:
  h1:
    fontFamily: "Bodoni Moda"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Bodoni Moda"
    fontSize: "32px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Bodoni Moda"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0em"
  body-md:
    fontFamily: "Libre Baskerville"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
  caption:
    fontFamily: "Libre Baskerville"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
    textTransform: "uppercase"
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
    backgroundColor: "#1A1A1A"
    color: "#C5A059"
    border: "1px solid #C5A059"
    borderRadius: "0px"
    padding: "12px 24px"
    textTransform: "uppercase"
    letterSpacing: "0.1em"
  card:
    backgroundColor: "#F2F0E9"
    border: "1px solid #E6E4DB"
    borderRadius: "0px"
    padding: "24px"
    boxShadow: "none"
  table:
    headerBackground: "#1A1A1A"
    headerColor: "#C5A059"
    rowBackground: "#F2F0E9"
    rowBorderColor: "#E6E4DB"
    cellPadding: "12px 16px"
---

# Overview

The **Vienna Workshop** design style is derived from the architectural and decorative philosophy of the Wiener Werkstätte (1903–1932). It rejects the organic curves of Art Nouveau in favor of Koloman Moser’s "square principle." This style is defined by extreme geometric restraint, high-contrast monochrome palettes with metallic accents, and the belief that every object, from a chair to a web interface, should possess equal aesthetic and functional dignity.

# Colors

The palette is historically grounded in the materials of early 20th-century Viennese luxury: gold leaf, black lacquer, and raw linen.

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#C5A059` | **Gold Leaf.** Used sparingly for borders, active states, and key highlights. Never as a background fill. |
| `secondary` | `#1A1A1A` | **Lacquer Black.** The primary text color and button backgrounds. Provides maximum contrast against neutral backgrounds. |
| `tertiary` | `#F2F0E9` | **Raw Linen.** The primary background color. Warm, off-white, mimicking unbleached paper or fabric. |
| `neutral` | `#8C8C8C` | **Graphite.** For secondary text, icons, and disabled states. |
| `muted` | `#E6E4DB` | **Parchment.** For subtle dividers, borders, and inactive form elements. |

# Typography

Typography must reflect the elegance of Viennese printing presses. Serifs are mandatory; sans-serifs are forbidden as they lack the historical lineage of the movement.

*   **Headings:** `Bodoni Moda`. High-contrast serifs that mimic the sharpness of geometric ornamentation. Tight tracking for impact.
*   **Body:** `Libre Baskerville`. Highly legible, traditional serif that maintains readability while adhering to the era's aesthetic.
*   **Captions/Labels:** Uppercase, wide letter-spacing. These act as structural grid markers rather than mere labels.

# Layout

The layout is governed by the **Grid**.

1.  **Square Geometry:** Content containers should favor square or rectangular proportions. Circular elements are prohibited unless they serve a strict mechanical function (e.g., a gauge).
2.  **Modular System:** Use a strict 8px or 16px baseline grid. Margins are not whitespace; they are structural divisions.
3.  **Asymmetrical Balance:** Avoid centered symmetry. Align content to the left or right, creating tension through offset geometric blocks.

# Elevation & Depth

**Flatness is preferred.** Depth is achieved through color contrast and border lines, not shadows.

*   **No Box Shadows:** Drop shadows are considered "cheap" decoration.
*   **Borders as Separators:** Use 1px solid borders (`#E6E4DB` or `#1A1A1A`) to define hierarchy.
*   **Layering:** Layering is indicated by overlapping geometric shapes with contrasting fills (e.g., a black square over a linen background).

# Shapes

*   **Corners:** `0px` radius. All elements are rectangular.
*   **Ornaments:** If decorative elements are used, they must be reduced to the square, the circle, and the straight line. No floral patterns, no curves.
*   **Icons:** Geometric line icons. Stroke width should be consistent (1.5px or 2px).

# Components

## Button (Primary)
*   **Shape:** Sharp rectangle.
*   **Style:** Black background, gold text, gold border.
*   **Hover:** Invert colors (Gold background, Black text). No scale transform.

## Card
*   **Structure:** A linen-colored rectangle with a 1px black border.
*   **Content:** Title in Bodoni Moda, body in Libre Baskerville.
*   **Divider:** A gold horizontal line (`#C5A059`) below the title to separate metadata.

## Table
*   **Header:** Black background, gold uppercase text.
*   **Rows:** Linen background, black text.
*   **Borders:** 1px `#E6E4DB` between rows.
*   **Alignment:** Left-aligned text for readability; numbers right-aligned.

## Form Inputs
*   **Style:** Underline only. No box.
*   **Focus State:** The underline turns from `#E6E4DB` to `#C5A059` (gold).
*   **Label:** Small, uppercase, placed above the input.

# Do's and Don'ts

| Do | Don't |
|----|-------|
| Use sharp, rectangular grids. | Use rounded corners or soft shadows. |
| Contrast black text against warm white. | Use white text on black backgrounds (except for footers). |
| Use serif fonts for all text. | Use sans-serif fonts (Inter, Roboto, etc.). |
| Limit gold to accents and borders. | Use gold as a primary background color. |
| Justify text alignment in headers. | Center-align long paragraphs. |
| Reduce ornamentation to geometric primitives. | Use organic, floral, or curvy patterns. |
| Maintain high contrast ratios. | Use pastel or muted colors for primary actions. |