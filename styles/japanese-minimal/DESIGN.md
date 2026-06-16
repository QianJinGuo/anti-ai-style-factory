```yaml
version: 1.0.0
name: 日式极简 (Wabi-Sabi Minimalism)
description: A design philosophy rooted in the acceptance of transience and imperfection, utilizing negative space as an active element and muted earth tones to foster calm and focus.
colors:
  primary:
    name: Ink Black
    hex: "#2B2B2B"
    usage: "Primary text, strong structural lines"
  secondary:
    name: Washi White
    hex: "#F7F5F0"
    usage: "Backgrounds, negative space filler"
  tertiary:
    name: Moss Green
    hex: "#5C6B5C"
    usage: "Secondary accents, nature-inspired highlights"
  neutral:
    name: Stone Grey
    hex: "#9E9E9E"
    usage: "Borders, disabled states, subtle dividers"
  muted:
    name: Dust Beige
    hex: "#D4CFC7"
    usage: "Subtle backgrounds, hover states"
typography:
  h1:
    fontFamily: "Yu Gothic, Yu Gothic UI, Meiryo, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Yu Gothic, Yu Gothic UI, Meiryo, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Yu Gothic, Yu Gothic UI, Meiryo, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0em"
  body-md:
    fontFamily: "Yu Gothic, Yu Gothic UI, Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: "0.05em"
  caption:
    fontFamily: "Yu Gothic, Yu Gothic UI, Meiryo, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.08em"
rounded:
  sm: 2px
  md: 4px
  lg: 8px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    background: "#2B2B2B"
    color: "#F7F5F0"
    border: "1px solid #2B2B2B"
    borderRadius: "2px"
    padding: "12px 24px"
    fontWeight: 500
  card:
    background: "#FFFFFF"
    border: "1px solid #EAEAEA"
    borderRadius: "4px"
    padding: "24px"
    boxShadow: "none"
  table:
    headerBackground: "#F7F5F0"
    rowHoverBackground: "#FAFAFA"
    borderColor: "#EAEAEA"
    borderWidth: "1px"
    cellPadding: "12px 16px"
```

# 日式极简 (Wabi-Sabi Minimalism)

## Overview
This design system is inspired by the Japanese aesthetic of *Ma* (negative space) and *Wabi-Sabi* (beauty in imperfection). It prioritizes content clarity over decorative flourish, using low-contrast palettes and generous whitespace to create a sense of calm and order. The interface feels tactile and grounded, avoiding digital sterility in favor of warmth and subtlety.

## Colors
The palette is derived from natural materials: ink, washi paper, stone, and moss. High-saturation colors are avoided to reduce visual noise.

- **Ink Black (`#2B2B2B`)**: Used for primary text and critical UI elements. It is softer than pure black (#000000) to reduce eye strain.
- **Washi White (`#F7F5F0`)**: The dominant background color. It mimics the texture of traditional paper, providing a warm, neutral canvas.
- **Moss Green (`#5C6B5C`)**: A muted, earthy accent for interactive elements or secondary information.
- **Stone Grey (`#9E9E9E`)**: Used for borders and dividers to maintain structure without dominance.
- **Dust Beige (`#D4CFC7`)**: A subtle hover state or inactive background, blending into the Washi White.

## Typography
Typography is the primary voice. We use **Yu Gothic** as the primary font stack, ensuring readability and cultural alignment. The type scale is tight, with subtle letter-spacing to enhance legibility in Japanese and Latin scripts.

- **Headings**: Bold, dark, and compact. They anchor the layout without shouting.
- **Body**: Lighter weight, larger line-height (1.8), and slight letter-spacing. This creates "breathing room" between lines, reflecting the *Ma* principle.
- **Captions**: Small, widely spaced text for metadata, emphasizing hierarchy through spacing rather than size alone.

## Layout
- **Grid**: Asymmetric grids are preferred to create dynamic but balanced compositions.
- **Negative Space**: Margins and padding are generous. Empty space is not "empty"; it is an active design element that guides focus.
- **Alignment**: Left-aligned text for readability. Centered elements are used sparingly for emphasis or ceremonial importance.

## Elevation & Depth
Depth is achieved through **color and opacity**, not shadow.
- **No Drop Shadows**: To avoid the "card" aesthetic common in Western UI.
- **Layering**: Overlapping elements are distinguished by subtle changes in background color (e.g., a slightly darker beige on hover) or crisp, thin borders.
- **Opacity**: Translucent overlays use a high-opacity neutral color to maintain legibility.

## Shapes
- **Edges**: Minimal rounding. Buttons and cards have slight rounding (2px-4px) to soften the rigid grid without losing structural integrity.
- **Lines**: Thin, precise lines (1px) define structure. Thick borders are avoided.

## Components

### Button (Primary)
- **Style**: Solid Ink Black background with Washi White text.
- **Border**: 1px solid Ink Black.
- **Radius**: 2px.
- **Effect**: No hover shadow. Hover state inverts colors (Washi White background, Ink Black text) or adds a subtle underline.

### Card
- **Style**: No shadow. Defined by a 1px Stone Grey border.
- **Background**: Pure white or very light beige to contrast with the Washi White page background.
- **Padding**: Generous internal padding to let content breathe.

### Table
- **Style**: Clean, grid-like. Header row has a Washi White background.
- **Borders**: Only horizontal dividers between rows, using Stone Grey. Vertical borders are omitted to reduce visual clutter.
- **Hover**: Row background changes to a very light beige.

## Do's and Don'ts

### Do
- **Embrace Whitespace**: Let elements exist in isolation. Do not crowd the interface.
- **Use Natural Colors**: Stick to earth tones, blacks, and whites.
- **Prioritize Readability**: Ensure high legibility with appropriate line-heights and font weights.
- **Be Subtle**: Use opacity and color shifts for interactivity rather than animations or shadows.

### Don't
- **Avoid Gradients**: Flat colors only.
- **No Drop Shadows**: Depth is not achieved through blur.
- **Don't Overuse Color**: Limit accent colors to one per view.
- **Avoid Standard Web Fonts**: Do not use Inter, Roboto, or Helvetica. Use Yu Gothic or similar sans-serif fonts that respect Japanese typographic norms.
- **No Fluffy UI**: Avoid rounded corners > 8px. Keep shapes crisp and intentional.