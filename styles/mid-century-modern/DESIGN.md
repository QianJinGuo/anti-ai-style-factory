---
version: 1.0.0
name: Mid-Century Modern (中世纪现代)
description: A design language rooted in the post-war American ethos of functionalism, characterized by organic geometry, warm natural materials, and an unpretentious integration of form and utility.
colors:
  primary:
    name: Mustard Yellow
    value: "#E3B448"
    description: A warm, saturated yellow derived from mustard seeds, providing energy without aggression.
  secondary:
    name: Olive Green
    value: "#556B2F"
    description: A deep, earthy green reflecting the organic connection to nature and landscape architecture.
  tertiary:
    name: Burnt Orange
    value: "#CC5500"
    description: A rich, reddish-orange used sparingly for accents, echoing terracotta and autumn leaves.
  neutral:
    name: Warm White
    value: "#FDFBF7"
    description: An off-white with a slight yellow undertone, avoiding the sterility of pure white.
    name: Charcoal
    value: "#333333"
    description: A soft black for text, softer than pure black to reduce eye strain and match paper tones.
  muted:
    name: Taupe
    value: "#B8A99A"
    description: A neutral brown-gray for borders and secondary backgrounds, bridging wood and stone.
typography:
  h1:
    fontFamily: "Clarendon, 'Courier New', monospace"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
    description: Heavy slab serif for strong, grounded headlines.
  h2:
    fontFamily: "Clarendon, 'Courier New', monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Clarendon, 'Courier New', monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0em"
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.01em"
    description: High-readability serif for long-form content, evoking print journalism.
  caption:
    fontFamily: "Courier New, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
    description: Monospaced typewriter style for metadata, labels, and technical details.
rounded:
  sm: "2px"
  md: "4px"
  lg: "0px"
  description: Minimal rounding. Rectangles dominate; slight rounding only for tactile elements like buttons.
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "48px"
  description: Generous whitespace to emphasize negative space and structural clarity.
components:
  button-primary:
    background: "#E3B448"
    color: "#333333"
    border: "1px solid #333333"
    borderRadius: "2px"
    padding: "10px 20px"
    fontFamily: "Courier New, monospace"
    fontWeight: 700
    textTransform: "uppercase"
    letterSpacing: "0.05em"
    description: Solid, block-like buttons with high contrast and typewriter aesthetics.
  card:
    background: "#FDFBF7"
    border: "1px solid #B8A99A"
    borderRadius: "0px"
    padding: "24px"
    boxShadow: "none"
    description: Flat cards with sharp edges, relying on borders and spacing for definition, not shadows.
  table:
    headerFont: "Courier New, monospace"
    headerBackground: "#F2EFE9"
    border: "1px solid #B8A99A"
    cellPadding: "12px 16px"
    description: Grid-based tables with clear horizontal rules, mimicking ledger paper.
---

# Mid-Century Modern Design System

## Overview
Mid-Century Modern (MCM) is not merely a visual style but a philosophy of "form follows function." Originating in the United States between 1945 and 1970, this design system rejects ornamentation in favor of clarity, warmth, and honesty of materials. In a digital context, this translates to high-contrast typography, ample whitespace, and a rejection of modern UI tropes like gradients and drop shadows. The interface should feel like a well-designed piece of furniture: sturdy, useful, and aesthetically integrated into its environment.

## Colors
The palette is derived from natural materials and post-war industrial pigments. It avoids cool blues and purples, favoring earth tones that ground the user.

- **Primary (Mustard Yellow #E3B448):** Used for primary actions and key highlights. It is warm and inviting but not aggressive.
- **Secondary (Olive Green #556B2F):** Used for secondary actions, success states, and organic accents.
- **Tertiary (Burnt Orange #CC5500):** Use sparingly for alerts or destructive actions, or as an accent in illustrations.
- **Neutral (Warm White #FDFBF7 & Charcoal #333333):** Backgrounds are never pure white; they carry a paper-like warmth. Text is soft charcoal to reduce glare.
- **Muted (Taupe #B8A99A):** Used for borders, dividers, and disabled states.

## Typography
Typography is the primary structural element. We avoid geometric sans-serifs (like Inter or Helvetica) in favor of typefaces that have humanist or industrial roots.

- **Headings (Clarendon/Courier New):** A heavy slab serif or typewriter monospace. This provides weight and authority. The tight letter-spacing in headings creates a block-like, architectural feel.
- **Body (Georgia/Times New Roman):** A traditional serif that ensures high readability for long-form content. It evokes the feeling of reading a quality magazine or book.
- **Captions/Metadata (Courier New):** Monospace fonts are used for technical data, timestamps, and labels, referencing the typewriter culture of the mid-century office.

## Layout
- **Grid:** Strict, asymmetric grids. Content is aligned to clear vertical and horizontal rules.
- **Whitespace:** Generous margins and padding. Negative space is not empty; it is a structural component that allows the content to breathe.
- **Flow:** Open layouts that guide the eye from top to bottom, mimicking the flow of a printed page. Avoid complex multi-column clutter.

## Elevation & Depth
**Flat Design Principle:**
Mid-Century Modern design does not use shadows to indicate hierarchy. Depth is achieved through:
1. **Color Contrast:** Using lighter backgrounds for cards against darker backgrounds.
2. **Borders:** Thin, crisp lines (1px solid) define boundaries.
3. **Layering:** Overlapping elements are rare; if used, they are distinct and sharp, not blurred.

**No Glassmorphism:**
Never use `backdrop-filter: blur`. Surfaces are opaque and solid, representing physical materials like wood, paper, and plastic.

## Shapes
- **Rectangles:** The dominant shape. Sharp corners are preferred.
- **Rounding:** Minimal. `0px` is the standard for containers. `2px` or `4px` may be used for small interactive elements (buttons, inputs) to suggest tactility, but never `12px` or more.
- **Organic Curves:** If curves are used, they should be large-radius arcs or circles, often used in decorative illustrations or iconography, not in UI containers.

## Components

### Buttons
- **Shape:** Rectangular with sharp or slightly rounded corners (`2px`).
- **Style:** Solid fill with high contrast. No gradients.
- **Text:** Uppercase, monospaced, bold.
- **Interaction:** No hover animations like scaling or shadow expansion. A simple color inversion or border thickening is sufficient.

### Cards
- **Structure:** Flat panels with a 1px border.
- **Content:** Title in slab serif, body in serif, metadata in monospace.
- **Spacing:** Internal padding should be generous (`24px` minimum).

### Tables
- **Style:** Minimalist grid. Horizontal lines separate rows. Vertical lines are optional or very faint.
- **Headers:** Monospaced, uppercase, aligned left.
- **Data:** Serif or sans-serif depending on readability needs, but aligned for easy scanning.

## Do's and Don'ts

### Do's
- **Do** use warm, earthy color palettes.
- **Do** prioritize readability with high-contrast serif text.
- **Do** use sharp, geometric shapes.
- **Do** embrace whitespace as a design element.
- **Do** use monospace fonts for technical details and metadata.

### Don'ts
- **Don't** use gradients, especially blue/purple ones.
- **Don't** use drop shadows or blurs for elevation.
- **Don't** use rounded corners (`>4px`) for major containers.
- **Don't** use generic sans-serif fonts (Inter, Roboto, Poppins).
- **Don't** use emoji as icons. Use simple line icons or typographic symbols.
- **Don't** use marketing buzzwords ("Seamless", "Next-Gen"). Use clear, descriptive language.