---
version: 1.0.0
name: Comic Book (Golden/Modern Age)
description: A high-contrast, panel-based narrative system that prioritizes kinetic energy, bold outlines, and diegetic typography over subtle gradients or soft shadows.
colors:
  primary: '#FFD700' # Comic Yellow (Highlights, Speed lines)
  secondary: '#0055FF' # Primary Blue (Hero accents, Sky)
  tertiary: '#FF0000' # Action Red (Impact, Danger, Emphasis)
  neutral: '#FFFFFF' # Pure White (Paper background, Negative space)
  muted: '#1A1A1A' # Ink Black (Outlines, Text, Shadows)
typography:
  h1:
    fontFamily: "'Bangers', 'Comic Sans MS', cursive"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 2px
  h2:
    fontFamily: "'Bangers', 'Comic Sans MS', cursive"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
  h3:
    fontFamily: "'Impact', 'Arial Black', sans-serif"
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1.3
    letterSpacing: 1px
  body-md:
    fontFamily: "'Comic Sans MS', 'Chalkboard SE', cursive"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5px
  caption:
    fontFamily: "'Courier New', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0px
rounded:
  sm: 0px
  md: 4px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    background: '#FFD700'
    border: 3px solid '#1A1A1A'
    borderRadius: 0px
    color: '#1A1A1A'
    boxShadow: '4px 4px 0px #1A1A1A'
    hover:
      transform: 'translate(-2px, -2px)'
      boxShadow: '6px 6px 0px #1A1A1A'
  card:
    background: '#FFFFFF'
    border: 4px solid '#1A1A1A'
    borderRadius: 0px
    boxShadow: '8px 8px 0px #1A1A1A'
  table:
    border: 3px solid '#1A1A1A'
    header:
      background: '#0055FF'
      color: '#FFFFFF'
      border: 2px solid '#1A1A1A'
    row:
      border: 2px solid '#1A1A1A'
    alternateRow:
      background: '#F0F0F0'
```

# Comic Book Design System

## Overview
This design system is rooted in the visual language of American comic books, from the Golden Age to the modern digital age. It rejects the subtlety of modern UI trends (glassmorphism, soft shadows) in favor of **high-contrast clarity**, **kinetic typography**, and **strict grid-based paneling**. The interface is not a flat plane; it is a sequence of moments. Every element must feel hand-drawn or printed, with heavy ink outlines and primary colors that pop against pure white paper.

## Colors
The palette is limited to reduce visual noise and mimic the constraints of traditional four-color printing.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Ink Black** | `#1A1A1A` | Primary outlines, body text, drop shadows. Never pure #000000 to allow for paper texture visibility. |
| **Paper White** | `#FFFFFF` | Backgrounds. Must be pure white to simulate newsprint. |
| **Action Red** | `#FF0000` | Critical alerts, "Impact" moments, primary interactive states. |
| **Hero Blue** | `#0055FF` | Secondary actions, links, structural headers. |
| **Highlight Yellow** | `#FFD700` | Focus states, highlights, warning badges, speed lines. |

**Ben-Day Dots Pattern:** Use a subtle 4px repeating dot pattern on top of primary/secondary backgrounds to simulate printing texture. Do not use on neutral backgrounds.

## Typography
Typography is not neutral; it is diegetic. Fonts are chosen for their legibility at small sizes and their expressive weight.

1.  **Headings (Bangers/Impact):** Used for panel titles, section headers, and "SFX" (Sound Effects). These fonts are tall, condensed, and aggressive.
2.  **Body (Comic Sans MS/Chalkboard):** Used for narrative text and tooltips. While often mocked in professional design, in this context, it mimics the hand-lettering of speech bubbles.
3.  **Captions (Courier New):** Used for narrative boxes (the rectangular text boxes that explain plot points) and code snippets.

**Letter Spacing:** Headings must have wide letter-spacing (`2px`) to mimic the stretched letters of explosion sounds (e.g., BOOOOM).

## Layout
The layout is governed by the **Panel Grid**.

*   **Panels:** Content is contained within rigid rectangular containers.
*   **Gutters:** The space between panels (the gutter) is defined by the **Ink Black** border. There are no soft margins.
*   **Flow:** Reading order is strictly Left-to-Right, Top-to-Bottom.
*   **Speech Bubbles:** Text that requires interaction or emphasis should be contained in irregular polygon shapes with tails pointing to the "speaker" (icon or avatar).

## Elevation & Depth
Depth is achieved through **Hard Shadows**, not blur.

*   **Rule:** All interactive elements (buttons, cards, modals) must have a solid, offset shadow using `box-shadow: Xpx Ypx 0px #1A1A1A`.
*   **Hover State:** On hover, translate the element by `-2px` on both axes and increase the shadow size by `2px`. This creates a tactile "lifting" effect reminiscent of flipping a comic page.
*   **No Blur:** Never use `blur` for shadows. The aesthetic is print-based, not screen-based.

## Shapes
*   **Borders:** All containers must have thick borders (`3px` - `4px`) of `#1A1A1A`.
*   **Corners:**
    *   **Panels/Cards:** `0px` (Sharp corners).
    *   **Speech Bubbles:** Irregular polygons (handled via CSS clip-path).
    *   **Buttons:** `0px` or `4px` (slight rounding to mimic hand-drawn imperfection, but mostly sharp).

## Components

### 1. Primary Button
*   **Shape:** Rectangular with sharp corners.
*   **Style:** Yellow background, Black border, Black text.
*   **Shadow:** Hard black offset shadow.
*   **Interaction:** On click, translate `2px` down and right, reducing the visible shadow.

### 2. Narrative Card (Panel)
*   **Structure:** A container with a 4px black border.
*   **Header:** Blue background with white text, styled like a caption box.
*   **Content:** White background.
*   **Image:** If an image is present, apply a "halftone" filter overlay or a black-and-white threshold to match the print style.

### 3. Table
*   **Header:** Blue background, white text, 2px black border.
*   **Rows:** White background, 2px black borders between all cells.
*   **Alternating Rows:** Light gray (`#F0F0F0`) to distinguish data without breaking the grid.

### 4. SFX Badge
*   **Usage:** For tags, status updates, or emphasis.
*   **Style:** Rotated slightly (-5deg), bold yellow text on red background, thick black border.

## Do's and Don'ts

### DO
*   **DO** use thick, consistent outlines (`3px`+) for all containers.
*   **DO** use primary colors (Red, Blue, Yellow) for interactive elements.
*   **DO** align content to a strict grid.
*   **DO** use "Impact" style fonts for short, loud text (titles, errors).
*   **DO** use hard, non-blurred shadows to indicate depth.

### DON'T
*   **DON'T** use gradients. The aesthetic is flat color.
*   **DON'T** use rounded corners (`border-radius > 4px`) on main containers.
*   **DON'T** use subtle drop shadows with blur (`box-shadow: 0 4px 6px rgba(...)`).
*   **DON'T** use sans-serif system fonts (Inter, Roboto, Arial) for body text; use cursive or monospace to maintain the "hand-lettered" illusion.
*   **DON'T** use icons that are filled with gradients or soft colors. Use outlined, black-filled icons.
