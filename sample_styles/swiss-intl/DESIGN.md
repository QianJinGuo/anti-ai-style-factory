version: 1.0.0
name: Swiss International Style
description: A rational, objective design system rooted in grid-based structure, mathematical typography, and universal legibility, prioritizing clarity over decoration.
colors:
  primary:
    name: International Orange
    hex: "#FF3B30"
    usage: "Critical actions, alerts, primary highlights"
  secondary:
    name: International Blue
    hex: "#0055A4"
    usage: "Secondary actions, links, secondary highlights"
  tertiary:
    name: Swiss Black
    hex: "#000000"
    usage: "Headings, body text, structural lines"
  neutral:
    name: Paper White
    hex: "#FFFFFF"
    usage: "Backgrounds, card surfaces, negative space"
  muted:
    name: Concrete Gray
    hex: "#8E8E93"
    usage: "Placeholder text, disabled states, secondary labels"
typography:
  h1:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 24
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
rounded:
  sm: 0
  md: 0
  lg: 0
spacing:
  sm: 8
  md: 16
  lg: 24
  xl: 32
components:
  button-primary:
    background: "#000000"
    color: "#FFFFFF"
    border: "1px solid #000000"
    borderRadius: 0
    padding: "12px 24px"
    fontWeight: 700
    fontSize: 14
    textTransform: uppercase
    letterSpacing: 0.05em
  card:
    background: "#FFFFFF"
    border: "1px solid #E5E5E5"
    borderRadius: 0
    padding: 24px
    boxShadow: "none"
  table:
    headerBackground: "#F5F5F5"
    rowHover: "#FAFAFA"
    border: "1px solid #E5E5E5"
    borderRadius: 0
```

# Swiss International Style Design Specification

## Overview

The Swiss International Style (Swiss Style) is a graphic design style characterized by cleanliness, readability, and objectivity. Originating in Switzerland in the 1950s, it is defined by the use of a mathematical grid system, sans-serif typography (specifically Helvetica), asymmetric layouts, and flush-left, ragged-right text. The design philosophy posits that design should be neutral, universal, and functional, removing all unnecessary decoration to let the content speak through structure.

## Colors

The palette is strictly limited to ensure high contrast and legibility. Colors are used functionally, not decoratively.

*   **Primary (#FF3B30):** A bold, industrial red. Used sparingly to draw attention to critical data points or primary actions.
*   **Secondary (#0055A4):** A deep, authoritative blue. Used for secondary navigation or informational links.
*   **Tertiary (#000000):** Pure black. The standard for text and structural lines. No dark grays for text.
*   **Neutral (#FFFFFF):** Pure white. The canvas. No off-whites or warm tones.
*   **Muted (#8E8E93):** Medium gray. Used exclusively for non-essential metadata, placeholders, or disabled states.

## Typography

Typography is the primary visual element. There is no emphasis through italics or color changes; emphasis is achieved through weight, size, and grid placement.

*   **Font Family:** `Helvetica Neue`, `Helvetica`, `Arial`, `sans-serif`.
*   **Hierarchy:** Strictly defined by size and weight.
    *   **H1:** 48px, Bold (700). Used for page titles.
    *   **H2:** 32px, Bold (700). Used for section headers.
    *   **H3:** 24px, Semibold (600). Used for sub-sections.
    *   **Body:** 16px, Regular (400). Line height set to 1.5 for optimal readability.
    *   **Caption:** 12px, Regular (400). Small caps or uppercase for labels.
*   **Alignment:** Left-aligned (flush left, ragged right). Justified text is discouraged as it creates uneven word spacing.
*   **Kerning/Letter-spacing:** Tight tracking for headings (-0.02em) to create a solid block of text; neutral tracking for body text.

## Layout

*   **Grid System:** All elements must align to a 12-column or 16-column modular grid. Margins and gutters are consistent across all breakpoints.
*   **Whitespace:** Whitespace is an active design element, not empty space. Margins should be generous (minimum 24px) to separate content blocks clearly.
*   **Asymmetry:** Avoid centering. Use asymmetric balance to create visual interest through structural contrast rather than decorative elements.
*   **Lines:** Thin, precise lines (1px) are used to separate content, not shadows or borders.

## Elevation & Depth

*   **No Shadows:** Drop shadows, blurs, and gradients are strictly prohibited. Depth is conveyed through color contrast and grid placement.
*   **Flat Design:** All surfaces are flat. No textures, no patterns, no illustrations.

## Shapes

*   **Rectilinear:** All shapes are rectangles. No rounded corners (border-radius: 0).
*   **Borders:** Use 1px solid borders in light gray (#E5E5E5) to define containers, not shadows.

## Components

### Button
*   **Shape:** Sharp rectangle.
*   **Style:** High contrast. Black background, white text, or white background, black border.
*   **Text:** Uppercase, bold, wide letter-spacing.
*   **No Icons:** Buttons rely on text labels only.

### Card
*   **Structure:** Defined by borders and spacing, not elevation.
*   **Padding:** Consistent internal padding (24px).
*   **Content:** Image (if any) is cropped to exact grid dimensions. No overlays.

### Table
*   **Style:** Minimalist. Thin horizontal lines only (no vertical lines).
*   **Header:** Light gray background (#F5F5F5) to distinguish from body.
*   **Hover:** Subtle background color change (#FAFAFA) for interactivity.

## Do's and Don'ts

**Do:**
*   Use a strict modular grid for all layouts.
*   Prioritize legibility and hierarchy through typography.
*   Use high-contrast black and white as the base.
*   Align elements precisely to grid lines.
*   Use ample whitespace to separate content.

**Don't:**
*   Use rounded corners or drop shadows.
*   Use decorative fonts or serif typefaces.
*   Use gradients, patterns, or textures.
*   Center-align text blocks.
*   Use colored backgrounds for cards or containers (use borders instead).
*   Add unnecessary icons or illustrations.