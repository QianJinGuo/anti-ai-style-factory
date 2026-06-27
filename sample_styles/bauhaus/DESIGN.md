---
version: 1.0.0
name: Bauhaus
description: A radical synthesis of art, craft, and technology where form follows function, utilizing pure geometry, primary colors, and industrial rationality to eliminate ornamentation.
colors:
  primary: "#D92B2B"       # Pure Red (Mondrian/Itten influence)
  secondary: "#003898"     # Deep Blue (Kandinsky/Albers influence)
  tertiary: "#F4D03F"      # Bright Yellow (Klee/Albers influence)
  neutral: "#1A1A1A"       # Near Black (Ink/Steel)
  muted: "#8C8C8C"         # Concrete Grey
  background: "#F2F2F2"    # Raw Canvas/Paper
  surface: "#FFFFFF"       # White Plaster
typography:
  h1:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: "48px"
    fontWeight: 800
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "1.2"
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: "1.3"
    letterSpacing: "0"
  body-md:
    fontFamily: "Roboto, Helvetica, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.6"
    letterSpacing: "0.01em"
  caption:
    fontFamily: "Roboto, Helvetica, Arial, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: "1.4"
    letterSpacing: "0.05em"
    textTransform: "uppercase"
rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
components:
  button-primary:
    backgroundColor: "#1A1A1A"
    color: "#FFFFFF"
    borderRadius: "0px"
    padding: "12px 24px"
    fontWeight: 700
    textTransform: "uppercase"
    letterSpacing: "0.1em"
    border: "2px solid #1A1A1A"
    boxShadow: "4px 4px 0px #D92B2B"
  card:
    backgroundColor: "#FFFFFF"
    border: "1px solid #1A1A1A"
    borderRadius: "0px"
    padding: "0px"
    boxShadow: "none"
    display: "flex"
    flexDirection: "column"
  table:
    borderCollapse: "collapse"
    width: "100%"
    borderColor: "#1A1A1A"
    borderWidth: "1px"
  input:
    backgroundColor: "#FFFFFF"
    border: "2px solid #1A1A1A"
    borderRadius: "0px"
    padding: "12px"
    focusBorderColor: "#003898"
    focusBoxShadow: "none"
---

# Bauhaus Design System

## Overview

The Bauhaus design system is an exercise in radical reduction. It rejects the decorative excesses of the 19th century in favor of industrial honesty. Every element must have a purpose; if a curve does not serve a function, it is deleted. The interface is a machine for reading, constructed from a strict grid of primary colors and geometric forms. It is not "friendly"; it is efficient.

## Colors

The palette is derived from Johannes Itten’s color theory and the primary color triad (Red, Blue, Yellow) combined with the neutrality of black and white.

- **Primary (#D92B2B)**: Used for primary actions, critical alerts, and structural accents. It commands attention without decoration.
- **Secondary (#003898)**: Used for secondary information, links, and depth. It provides intellectual weight.
- **Tertiary (#F4D03F)**: Used sparingly for highlights, icons, or warning states. It provides energy.
- **Neutral (#1A1A1A)**: The ink. Used for text, borders, and primary structural lines.
- **Muted (#8C8C8C)**: Used for placeholders, disabled states, and secondary metadata.
- **Background (#F2F2F2)**: The raw material. Not pure white, but the color of industrial paper or concrete.
- **Surface (#FFFFFF)**: The canvas for content.

**Rule**: Never mix gradients. Colors must be flat, solid, and opaque.

## Typography

Typography is the voice of the system. It must be legible, geometric, and authoritative.

- **Headings**: `Futura` or `Century Gothic`. These geometric sans-serif fonts reflect the industrial era. They are bold, stark, and unapologetic.
- **Body**: `Roboto` or `Helvetica`. Neutral, readable, and invisible. The text should not call attention to itself; it should call attention to the meaning.
- **Captions**: Uppercase, wide letter-spacing. Used for labels, tags, and metadata to create a rhythmic structural grid.

**Rule**: Avoid serif fonts entirely. Avoid soft, rounded typefaces. Hierarchy is established through weight and size, not color or italics.

## Layout

The layout is a rigid grid. It is based on the principles of the International Typographic Style (Swiss Style), which evolved from Bauhaus.

- **Grid System**: 12-column grid with 16px gutters.
- **Alignment**: Left-aligned text. Justified text is discouraged as it creates uneven spacing.
- **Whitespace**: Whitespace is not empty space; it is an active design element. Use it to separate content blocks clearly.
- **Asymmetry**: While the grid is symmetric, content can be arranged asymmetrically to create dynamic tension, provided the balance is maintained.

## Elevation & Depth

Depth is not achieved through soft shadows or blur. It is achieved through **hard edges** and **layering**.

- **Shadows**: `box-shadow: 4px 4px 0px #1A1A1A;` or `box-shadow: 2px 2px 0px #D92B2B;`.
- **Style**: No blur. The shadow is a solid block of color offset by 2-4px. This mimics the physical layering of paper or the sharp contrast of industrial materials.
- **Borders**: Use 1px or 2px solid borders to define areas. Borders are structural, not decorative.

## Shapes

- **Corners**: Always `0px` border-radius. Squares and rectangles only. Circles are used only for icons or data visualization, never for containers.
- **Lines**: Horizontal and vertical lines only. Diagonals are used sparingly for dynamic accents or dividers.
- **Icons**: Geometric, line-based icons. No filled icons. No gradients. No skeuomorphism.

## Components

### Button-Primary
A rectangular block of color. No rounded corners. High contrast.
```css
.button-primary {
  background-color: #1A1A1A;
  color: #FFFFFF;
  border: 2px solid #1A1A1A;
  border-radius: 0px;
  padding: 12px 24px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  box-shadow: 4px 4px 0px #D92B2B; /* Hard shadow */
  transition: transform 0.1s ease;
}
.button-primary:active {
  transform: translate(2px, 2px);
  box-shadow: 2px 2px 0px #D92B2B;
}
```

### Card
A white rectangle with a black border. Content is left-aligned. No internal padding beyond structural spacing.
```css
.card {
  background-color: #FFFFFF;
  border: 1px solid #1A1A1A;
  border-radius: 0px;
  padding: 0;
  box-shadow: none;
}
.card-header {
  border-bottom: 2px solid #1A1A1A;
  padding: 16px;
  font-weight: 700;
  text-transform: uppercase;
}
.card-body {
  padding: 16px;
}
```

### Input
A rectangular field with a thick black border. Focus state changes border color to Secondary Blue.
```css
.input {
  background-color: #FFFFFF;
  border: 2px solid #1A1A1A;
  border-radius: 0px;
  padding: 12px;
  font-family: "Roboto", sans-serif;
}
.input:focus {
  border-color: #003898;
  outline: none;
  box-shadow: none;
}
```

### Table
Clean, grid-based table. Borders on all cells. Header row has a black background with white text.
```css
.table {
  border-collapse: collapse;
  width: 100%;
}
.table th, .table td {
  border: 1px solid #1A1A1A;
  padding: 12px;
  text-align: left;
}
.table th {
  background-color: #1A1A1A;
  color: #FFFFFF;
  text-transform: uppercase;
  font-size: 12px;
  letter-spacing: 0.05em;
}
```

## Do's and Don'ts

### Do
- **Use primary colors** to create visual hierarchy.
- **Align everything** to the grid.
- **Use hard shadows** to indicate depth.
- **Keep it simple**. If it can be removed, it should be.
- **Use geometric shapes** for all UI elements.

### Don't
- **Don't use gradients**. They are decorative and unnecessary.
- **Don't use rounded corners**. They soften the industrial aesthetic.
- **Don't use drop shadows with blur**. They are soft and imprecise.
- **Don't use serif fonts**. They are traditional and ornate.
- **Don't use decorative icons**. Use geometric symbols only.
- **Don't justify text**. It creates uneven spacing and reduces readability.