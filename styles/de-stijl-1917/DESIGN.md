---
version: 1.0.0
name: De Stijl (Neoplasticism)
description: A radical reduction of form to vertical/horizontal lines and primary colors (red, yellow, blue) plus black/white/gray, emphasizing non-symmetrical balance and universal harmony.
colors:
  primary: "#E3000F" # Pure Red
  secondary: "#0055A4" # Pure Blue
  tertiary: "#FFD500" # Pure Yellow
  neutral: "#FFFFFF" # White
  muted: "#000000" # Black
  background: "#F5F5F5" # Off-white (paper-like)
  surface: "#FFFFFF"
typography:
  h1:
    fontFamily: "'Futura', 'Century Gothic', 'Avant Garde', sans-serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "'Futura', 'Century Gothic', 'Avant Garde', sans-serif"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "'Futura', 'Century Gothic', 'Avant Garde', sans-serif"
    fontSize: 24
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', 'Arial', 'Lato', sans-serif"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', 'Arial', 'Lato', sans-serif"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    backgroundColor: "#000000"
    color: "#FFFFFF"
    borderRadius: 0px
    padding: "12px 24px"
    fontWeight: 700
    textTransform: uppercase
    letterSpacing: 0.1em
    border: 2px solid #000000
    hover:
      backgroundColor: "#E3000F"
      borderColor: "#E3000F"
  card:
    backgroundColor: "#FFFFFF"
    border: 1px solid #000000
    borderRadius: 0px
    boxShadow: none
    padding: 0
  table:
    borderCollapse: collapse
    borderColor: "#000000"
    borderWidth: 1px
    header:
      backgroundColor: "#E3000F"
      color: "#FFFFFF"
      fontWeight: 700
    row:
      border: 1px solid #E5E5E5
      hover:
        backgroundColor: "#F9F9F9"
---

# De Stijl Design System

## Overview

De Stijl (The Style), also known as Neoplasticism, is a design philosophy founded in the Netherlands in 1917. It seeks to express a new utopian ideal of spiritual harmony and order. By reducing visual language to its absolute essentials—vertical and horizontal lines, rectangular forms, and primary colors plus black and white—De Stijl rejects naturalism and ornamentation in favor of pure abstraction and universal truth. This design system applies these principles to digital interfaces, creating a grid-based, asymmetrical, and highly structured aesthetic that prioritizes clarity and structural integrity over decoration.

## Colors

The palette is strictly limited to the three primary colors and the three neutral tones (black, white, gray). No gradients, no opacity layers, no secondary hues.

*   **Red (`#E3000F`)**: Used for primary actions, critical alerts, and dominant visual anchors.
*   **Blue (`#0055A4`)**: Used for secondary information links and structural accents.
*   **Yellow (`#FFD500`)**: Used for highlights, warnings, or tertiary emphasis.
*   **Black (`#000000`)**: The primary color for lines, text, and borders. It defines structure.
*   **White (`#FFFFFF`)**: The canvas. Pure background space.
*   **Off-White (`#F5F5F5`)**: Used for subtle background differentiation without breaking the monochrome neutrality.

**Usage Rule:** Colors must be solid. No transparency. No mixing. A component should never contain more than one color from the primary/secondary/tertiary set at a time, except in combination with black/white/gray.

## Typography

Typography is geometric, modernist, and utilitarian. We avoid serif fonts entirely. The goal is legibility and structural alignment with the grid.

*   **Headings:** `Futura`, `Century Gothic`, or `Avant Garde`. These fonts reflect the geometric purity of the movement. They are bold, clean, and lack unnecessary flourishes.
*   **Body Text:** `Helvetica Neue`, `Arial`, or `Lato`. Neutral, highly readable sans-serif fonts that recede into the background, allowing the structure to speak.
*   **Caps:** All captions and small labels should be uppercase with increased letter-spacing to emphasize the horizontal/vertical grid alignment.

**Usage Rule:** Never italicize. Never use decorative fonts. Align text strictly to the grid.

## Layout

The layout is governed by the grid. Everything is aligned to vertical and horizontal axes. Diagonal lines are prohibited.

*   **Grid System:** A strict 12-column or 24-column grid with fixed gutters.
*   **Asymmetry:** Balance is achieved through asymmetrical composition, not symmetry. A large red block on the left might be balanced by a small blue square on the right.
*   **Whitespace:** Whitespace is active, not passive. It defines the space between elements just as strongly as the elements themselves.
*   **Lines:** Black lines (1px or 2px) are used to separate content areas, mimicking the structural lines in Mondrian's paintings.

## Elevation & Depth

Depth is not achieved through shadows or blurs. Depth is achieved through **color blocking** and **overlapping**.

*   **No Shadows:** `box-shadow` is strictly forbidden.
*   **No Blur:** `backdrop-filter` is forbidden.
*   **Layering:** Elements sit on top of each other. A white card might overlap a yellow background block. The boundary is defined by a hard black line, not a soft shadow.
*   **Z-Index:** Use high z-index values for overlays, but ensure they are bordered in black to maintain the aesthetic.

## Shapes

*   **Rectangles Only:** All containers, buttons, images, and cards must be perfect rectangles.
*   **No Curves:** `border-radius` is always `0px`. Circles, rounded corners, and arcs are forbidden.
*   **Lines:** Vertical and horizontal lines are the primary decorative element. They can be thick (structural) or thin (content separation).

## Components

### Button (Primary)
A solid black rectangle with white uppercase text. On hover, it inverts to red with white text. No rounded corners. No shadows.