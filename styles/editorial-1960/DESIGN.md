```yaml
---
version: 1.0.0
name: editorial-classic
description: A typographic system rooted in mid-century print journalism, prioritizing hierarchical clarity, grid-based structure, and the inherent authority of serif typefaces over decorative UI elements.
colors:
  primary: "#1a1a1a"       # Rich Black (Print standard)
  secondary: "#4a4a4a"     # Dark Gray (Text body)
  tertiary: "#8c7b70"      # Sepia/Umber (Accents, borders)
  neutral: "#f4f1ea"       # Warm Off-White (Paper background)
  muted: "#a8a29e"         # Light Gray (Disabled states, subtle lines)
typography:
  h1:
    fontFamily: "Playfair Display, Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Playfair Display, Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Playfair Display, Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.01em"
  body-md:
    fontFamily: "Charter, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.01em"
  caption:
    fontFamily: "Charter, 'Iowan Old Style', 'Palatino Linotype', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.03em"
    textTransform: "uppercase"
rounded:
  sm: 2px
  md: 4px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    style: "border: 1px solid #1a1a1a; background: #1a1a1a; color: #f4f1ea; font-family: 'Charter', serif; text-transform: uppercase; letter-spacing: 0.05em; padding: 12px 24px; transition: background 0.2s ease;"
  card:
    style: "background: #fff; border: 1px solid #e5e5e5; box-shadow: none; padding: 24px; margin-bottom: 32px;"
  table:
    style: "width: 100%; border-collapse: collapse; font-family: 'Charter', serif; font-size: 16px;"
    header: "border-bottom: 2px solid #1a1a1a; padding: 12px 8px; text-align: left; font-weight: 700;"
    row: "border-bottom: 1px solid #e5e5e5; padding: 12px 8px;"
---

# Editorial Classic Design System

## Overview

This design system is built on the principles of mid-20th century American and British magazine publishing (1945–1980). It rejects the ephemeral, screen-native trends of modern web design in favor of permanence, hierarchy, and readability. The interface is treated as a page, not a canvas. Content is king; UI elements are merely the structural scaffolding (columns, rules, margins) that organizes the text. The aesthetic is authoritative, calm, and intellectually rigorous.

## Colors

The palette is derived from ink on paper. It avoids digital vibrancy in favor of print realism.

*   **Backgrounds**: Use warm, off-white tones (`#f4f1ea`) to simulate high-quality newsprint or magazine stock. Pure white (`#ffffff`) is reserved for specific card surfaces to create subtle contrast against the page background.
*   **Text**: Rich Black (`#1a1a1a`) is used for headings and primary actions. Dark Gray (`#4a4a4a`) is used for body text to reduce eye strain compared to pure black.
*   **Accents**: Muted earth tones (Sepia `#8c7b70`) are used for borders, dividers, and secondary information. No bright blues, greens, or purples.
*   **Borders**: Always use thin, solid lines (`1px` or `2px`). Never use soft shadows or gradients to indicate separation.

## Typography

Typography is the primary visual element. We rely on high-contrast Serifs for headings to establish authority and humanist Serifs for body text for long-form readability.

### Typefaces

*   **Headings**: `Playfair Display` or `Georgia`. These fonts have high x-heights and strong contrast, mimicking headline fonts like *The New York Times* or *Vogue* of the era.
*   **Body**: `Charter` (preferred) or `Palatino Linotype`. Charter was designed specifically for screen legibility while maintaining the warmth of print type. It is more readable at small sizes than Garamond or Baskerville.

### Hierarchy

*   **H1**: Large, tight tracking, high contrast. Used for article titles.
*   **H2**: Section headers, separated by horizontal rules.
*   **Body**: Generous line-height (1.6) and optimal line length (60-75 characters).
*   **Captions**: Uppercase, wide tracking, small size. Used for image credits, dates, and labels.

## Layout

The layout is strictly grid-based, inspired by the "column grid" of newspaper design.

*   **Columns**: Content is divided into 2, 3, or 4 columns depending on viewport width. On desktop, a 2-column layout is standard for articles, with a sidebar for metadata.
*   **Margins**: Wide margins are essential. Content should never touch the edge of the screen. Padding should be at least `32px` on all sides.
*   **Alignment**: Left-aligned text (ragged right) is preferred for body copy. Center-aligned text is reserved for short pull-quotes or titles.
*   **Whitespace**: Use whitespace to create hierarchy, not color. A large gap between sections is more effective than a colored background change.

## Elevation & Depth

**Flat is mandatory.**

*   **No Shadows**: Drop shadows are excluded. Depth is achieved through:
    1.  **Color Contrast**: Dark text on light paper.
    2.  **Borders**: Thin lines (`1px solid #e5e5e5`) separate cards from the background.
    3.  **Spacing**: Margins and padding define the boundaries of elements.
*   **No Gradients**: All backgrounds are solid colors.

## Shapes

*   **Borders**: Minimal rounding. `sm` (2px) for small tags, `md` (4px) for buttons. `lg` (0px) for cards and images. Sharp corners convey seriousness and precision.
*   **Images**: Rectangular, sharp corners. Images are treated as figures within the text, often with a thin border or caption below.

## Components

### Buttons

Buttons are understated and typographic. They should look like links that have been boxed.

*   **Style**: Uppercase, wide letter-spacing, solid background.
*   **Hover**: Invert colors (black bg to white text) or add a subtle underline.
*   **No Icons**: Use text labels only.

### Cards

Cards are not floating containers. They are sections of the page.

*   **Style**: White background, thin border, no shadow.
*   **Content**: Image on top, headline in H2, excerpt in body-md, metadata in caption.
*   **Separator**: Use a horizontal rule (`<hr>`) below the card content.

### Tables

Tables are grid-based and clean.

*   **Style**: No vertical lines. Only horizontal rules.
*   **Header**: Bold, uppercase, bottom border.
*   **Rows**: Light gray bottom border, ample vertical padding.

### Navigation

*   **Style**: Simple list of links. Underline on hover.
*   **Position**: Sticky top or fixed header with a solid background color (not transparent).
*   **Logo**: Text-based logo using the H1 font family.

## Do's and Don'ts

### Do
*   Use serif fonts for all text.
*   Maintain a strict grid structure.
*   Use thin lines to separate content.
*   Prioritize readability and hierarchy.
*   Use warm, paper-like backgrounds.
*   Keep UI elements minimal and functional.

### Don't
*   **Never** use sans-serif fonts for body text (no Inter, Roboto, Helvetica).
*   **Never** use drop shadows or glassmorphism.
*   **Never** use bright, neon, or gradient colors.
*   **Never** use rounded corners > 4px.
*   **Never** use emoji as icons.
*   **Never** hide content behind complex interactions; show it directly.
*   **Never** use marketing buzzwords in labels. Use clear, descriptive text.
```