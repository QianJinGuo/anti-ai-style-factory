version: 1.0.0
name: Memphis
description: A chaotic, anti-design manifesto that rejects functionalist minimalism through the aggressive collision of primary colors, geometric irregularity, and postmodern irony.
colors:
  primary: "#FF3366"
  secondary: "#00FFFF"
  tertiary: "#FFD700"
  neutral: "#FFFFFF"
  muted: "#333333"
typography:
  h1:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "Futura, 'Century Gothic', sans-serif"
    fontSize: 24
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Courier New, Courier, monospace"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.05em
  caption:
    fontFamily: "Courier New, Courier, monospace"
    fontSize: 12
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.1em
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
    borderRadius: 0px
    borderWidth: 3px
    borderColor: "#000000"
    padding: "12px 24px"
    backgroundColor: "#FF3366"
    hoverBackgroundColor: "#FFD700"
    boxShadow: "4px 4px 0px #000000"
  card:
    borderRadius: 0px
    borderWidth: 2px
    borderColor: "#000000"
    backgroundColor: "#FFFFFF"
    boxShadow: "6px 6px 0px #000000"
  table:
    borderWidth: 2px
    borderColor: "#000000"
    backgroundColor: "#FFFFFF"
    headerBackgroundColor: "#00FFFF"
    rowHoverBackgroundColor: "#FFD700"
    cellPadding: "12px"
```

# Memphis Design System

## Overview

The Memphis style emerged from the Milan-based design collective founded by Ettore Sottsass in 1981. It is a direct rejection of the "less is more" dogma of Modernism and International Style. This design system embraces chaos, irony, and pop culture. It treats UI not as a silent utility, but as a loud, declarative statement. Visual hierarchy is established through contrast and pattern rather than subtle shadows or whitespace. The goal is to create interfaces that feel playful, tactile, and deliberately unpolished.

## Colors

The palette is derived from primary colors and high-contrast neutrals. Avoid gradients. Use solid, flat fills.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Primary** | `#FF3366` | Hot Pink. Used for primary actions, highlights, and error states. |
| **Secondary** | `#00FFFF` | Cyan. Used for secondary backgrounds, info states, and decorative elements. |
| **Tertiary** | `#FFD700` | Yellow. Used for warnings, active states, and accent patterns. |
| **Neutral** | `#FFFFFF` | White. The canvas. Must be pure white to maximize contrast. |
| **Muted** | `#333333` | Charcoal Black. Used for borders, text, and hard shadows. |
| **Pattern Base** | `#F0F0F0` | Light Grey. Used for "tortoise shell" or "squiggle" background patterns. |

**Rule:** Never use purple, blue (unless cyan), or green (unless neon). Never blend colors.

## Typography

Typography is stark, geometric, and industrial. It contrasts with the playful shapes.

- **Headings:** `Futura` or `Century Gothic`. Geometric sans-serif. Bold, uppercase, tight tracking.
- **Body:** `Courier New` or `Courier`. Monospaced typewriter font. This introduces the "anti-design" human element against the geometric headings.
- **Caption/Labels:** Monospaced, all caps, bold.

**Rule:** Never use Inter, Roboto, Helvetica, or any "friendly" rounded sans-serif. Never use serif fonts like Garamond.

## Layout

- **Grid:** Rigid, but broken. Use a standard 12-column grid, but allow elements to overlap, spill out, or sit asymmetrically.
- **Alignment:** Hard left alignment for text. Elements can be rotated slightly (e.g., 2-5 degrees) to create tension.
- **Whitespace:** Sparse. Fill empty space with patterns (dots, zigzags, squiggles).

## Elevation & Depth

No blur. No soft shadows. Depth is achieved through **hard offsets**.

- **Shadow Style:** `box-shadow: 6px 6px 0px #000000;`
- **Interaction:** On hover/active, the shadow reduces to `2px 2px 0px #000000` and the element translates `4px 4px`. This simulates a physical block being pressed down.
- **Layering:** Use distinct background colors to separate layers, not transparency.

## Shapes

Geometry is the language of Memphis.

- **Borders:** Always `2px` or `3px` solid black (`#000000`).
- **Corners:** Always `0px` (sharp squares). Never rounded corners.
- **Decorative Elements:**
  - **Dots:** Solid black or colored circles.
  - **Zigzags:** SVG paths for borders or dividers.
  - **Squiggles:** Hand-drawn style curves.
  - **Triangles:** Solid colored triangles pointing in various directions.

## Components

### Button Primary
A blocky, aggressive button.
- **Style:** Solid Primary color (`#FF3366`).
- **Border:** 3px solid black.
- **Shadow:** 4px 4px 0px black.
- **Text:** White, Monospace, Bold, Uppercase.
- **Hover:** Background changes to Tertiary (`#FFD700`). Shadow shrinks.

### Card
A container that feels like a sticker or a postcard.
- **Background:** White or Cyan.
- **Border:** 2px solid black.
- **Shadow:** 6px 6px 0px black.
- **Content:** High contrast text. Include a decorative geometric shape (e.g., a black triangle) in the top-right corner.

### Table
A structured but loud data display.
- **Header:** Cyan background (`#00FFFF`), black text, bold monospace.
- **Rows:** White background.
- **Borders:** 2px solid black grid lines.
- **Hover:** Row background turns Yellow (`#FFD700`).

### Input Field
- **Style:** White background, 2px black border.
- **Focus:** Border turns Pink (`#FF3366`), box-shadow becomes `0px 0px 0px 3px #FF3366`.
- **Placeholder:** Monospace, grey, italic.

### Navigation
- **Style:** Horizontal bar, Yellow background (`#FFD700`), black text.
- **Active Item:** White background, black border, inverted colors.
- **Divider:** Vertical black line between items.

## Do's and Don'ts

### Do
- **DO** use high-contrast color combinations (Pink/Cyan, Yellow/Black).
- **DO** use geometric shapes (triangles, circles, squares) as decorative accents.
- **DO** use monospace fonts for body text to create a typewriter aesthetic.
- **DO** use hard, offset shadows to create physical depth.
- **DO** allow slight asymmetry and rotation in layout elements.

### Don't
- **DON'T** use gradients or glassmorphism.
- **DON'T** use rounded corners (`border-radius > 0`).
- **DON'T** use soft, blurred drop shadows.
- **DON'T** use "friendly" sans-serif fonts like Inter or Poppins.
- **DON'T** minimize visual noise. Embrace it.
- **DON'T** use purple or blue (except cyan) in the primary palette.