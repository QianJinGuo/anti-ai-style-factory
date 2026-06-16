---
version: 1.0.0
name: PopArt
description: A high-contrast, mass-media-inspired aesthetic that treats digital interfaces as comic book panels, utilizing bold outlines, primary colors, and Ben-Day dot textures to celebrate consumer culture.
colors:
  primary: '#FF0000'
  secondary: '#0055FF'
  tertiary: '#FFD700'
  neutral: '#FFFFFF'
  muted: '#000000'
typography:
  h1:
    fontFamily: "'Bangers', 'Impact', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 1px
  h2:
    fontFamily: "'Bangers', 'Impact', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  h3:
    fontFamily: "'Bangers', 'Impact', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0px
  body-md:
    fontFamily: "'Comic Sans MS', 'Chalkboard SE', 'Marker Felt', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "'Courier New', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: -0.5px
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    background: '#FF0000'
    border: 3px solid #000000
    color: '#FFFFFF'
    padding: 12px 24px
    borderRadius: 0px
    boxShadow: 4px 4px 0px #000000
  card:
    background: '#FFFFFF'
    border: 3px solid #000000
    padding: 16px
    borderRadius: 0px
    boxShadow: 6px 6px 0px #000000
  table:
    headerBackground: '#0055FF'
    headerColor: '#FFFFFF'
    rowBackground: '#FFFFFF'
    border: 2px solid #000000
    cellPadding: 12px
---

# PopArt Design System

## Overview
PopArt rejects the subtle gradients and soft shadows of modern minimalism in favor of the visual language of American and British consumer culture from 1958 to 1970. This system is built on the premise that digital interfaces are not clean canvases, but printed pages. It embraces the artificiality of mass production, using hard edges, thick black outlines, and primary colors to create a sense of immediate, loud impact. It is anti-pretentious, loud, and unapologetically graphic.

## Colors
The palette is strictly limited to primary colors and black/white to mimic newsprint and comic book inking. No gradients. No transparency.

- **Primary (Red):** `#FF0000` - Used for call-to-action buttons and critical alerts.
- **Secondary (Blue):** `#0055FF` - Used for secondary actions and headers.
- **Tertiary (Yellow):** `#FFD700` - Used for highlights and badges.
- **Neutral (White):** `#FFFFFF` - Backgrounds and text on dark colors.
- **Muted (Black):** `#000000` - Outlines, text, and hard shadows.

**Texture Overlay:**
All solid color blocks should optionally support a 10% opacity black Ben-Day dot pattern overlay to simulate printing techniques.

## Typography
Typography must feel hand-drawn or stamped. We avoid geometric sans-serifs entirely.

- **Headings:** `Bangers` or `Impact`. These fonts are condensed, bold, and evoke comic book sound effects or headline news.
- **Body:** `Comic Sans MS` or `Chalkboard SE`. The choice is intentionally informal and accessible, referencing handwritten notes or school supplies.
- **Captions/Code:** `Courier New`. Monospace fonts reinforce the idea of typed manuscripts or mechanical reproduction.

**Hierarchy:**
Headings are never italicized. They are always uppercase or title case, with tight letter spacing. Body text is left-aligned, never justified.

## Layout
Layouts are grid-based but rigid. Think of a comic book page or a Warhol soup can print.

- **Grid:** Strict 12-column grid.
- **Gutters:** Wide gutters (24px) to separate distinct "panels."
- **Alignment:** Left-aligned content blocks.
- **Panels:** Content is contained within distinct rectangular blocks with thick black borders.

## Elevation & Depth
Depth is achieved through **hard shadows**, not blur.

- **Shadow Style:** Solid black offset shadow.
- **Offset:** 4px to 6px down and right.
- **Blur:** 0px.
- **Purpose:** This creates a "cut-out" paper effect, reinforcing the idea that the UI elements are physical objects pasted onto the page.

## Shapes
- **Borders:** All interactive elements and containers must have a 2px to 3px solid black border.
- **Corners:** Zero rounding. `border-radius: 0px`. Sharp corners reflect the industrial and mechanical nature of mass production.
- **Dividers:** Thick black lines (3px) separate sections, mimicking panel gutters in comics.

## Components

### Button (Primary)
- **Shape:** Rectangle.
- **Background:** Primary Red (`#FF0000`).
- **Text:** White, Bold, Uppercase.
- **Border:** 3px solid Black.
- **Shadow:** 4px 4px 0px Black.
- **Hover State:** Move shadow to 2px 2px 0px Black (simulate pressing down).

### Card
- **Shape:** Rectangle.
- **Background:** White.
- **Border:** 3px solid Black.
- **Shadow:** 6px 6px 0px Black.
- **Header:** Black background, White text, 3px black border.
- **Content:** Left-aligned, generous padding.

### Table
- **Header:** Blue background, White text, Bold, Uppercase.
- **Rows:** White background, alternating with light yellow (`#FFF9C4`) for readability.
- **Borders:** All cells have 2px black borders.
- **Font:** Monospace for data, Comic Sans for labels.

### Badge/Tag
- **Shape:** Small rectangle.
- **Background:** Tertiary Yellow.
- **Border:** 2px solid Black.
- **Text:** Black, Bold, Small Caps.

## Do's and Don'ts

### Do
- **Do** use thick black outlines for all UI elements.
- **Do** use high-contrast primary colors.
- **Do** use hard, solid shadows (no blur).
- **Do** use comic-book style fonts for headings.
- **Do** treat the screen as a printed page.

### Don't
- **Don't** use gradients or translucent backgrounds.
- **Don't** use rounded corners.
- **Don't** use subtle gray shadows or blurs.
- **Don't** use modern sans-serif fonts (Inter, Roboto, etc.).
- **Don't** use minimalist iconography; use bold, outlined icons or text-based indicators.