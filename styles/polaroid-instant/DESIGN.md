---
version: 1.0.0
name: Polaroid
description: A design language rooted in the tactile immediacy of analog instant photography, prioritizing human imperfection, warm nostalgia, and the raw honesty of unedited moments.
colors:
  primary:
    name: "Polaroid White"
    hex: "#F4F4F0"
    usage: "Backgrounds, card surfaces, negative space. Represents the physical paper border."
  secondary:
    name: "Lead Grey"
    hex: "#2C2C2C"
    usage: "Primary text, borders, camera body accents. Represents the ink and metal."
  tertiary:
    name: "Sepia Wash"
    hex: "#D4C5B0"
    usage: "Secondary text, subtle dividers, aged paper tones. Represents chemical fading."
  neutral:
    name: "Film Grain"
    hex: "#E8E6E1"
    usage: "Input fields, disabled states, subtle backgrounds."
  muted:
    name: "Chemical Stain"
    hex: "#B8A99A"
    usage: "Hovers, focus states, subtle shadows. Represents the uneven chemical development."
typography:
  h1:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 32
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5
  h2:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 24
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3
  h3:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 18
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.2
  caption:
    fontFamily: "'Comic Sans MS', 'Chalkboard SE', 'Marker Felt', sans-serif"
    fontSize: 14
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.5
rounded:
  sm: 2px
  md: 4px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    style: "Solid Lead Grey background, Polaroid White text, no border radius, sharp corners, slight texture."
  card:
    style: "Polaroid White background, 1px Lead Grey border, padding 24px, no shadow (flat), slight paper texture overlay."
  table:
    style: "Thin Lead Grey borders, Courier New font, alternating subtle Sepia Wash rows, no rounded corners."
  input:
    style: "Lead Grey border, 1px solid, Courier New font, focus state is Chemical Stain border, no rounded corners."
---

# Polaroid Design System

## Overview

The Polaroid design system rejects the sterile perfection of digital minimalism. It embraces the **tactile reality** of instant photography: the wait for development, the uneven chemical spread, the handwritten notes on the white border, and the inherent grain of analog film. 

This system is built for interfaces that value **authenticity over polish**. It is not "clean"; it is "real." It acknowledges that human moments are imperfect, warm, and slightly faded. The design avoids smooth gradients and soft shadows in favor of hard edges, monospaced typewriter fonts, and textures that mimic physical paper and chemical stains.

## Colors

The palette is derived from the physical materials of the Polaroid camera and the aging process of the photograph.

- **Polaroid White (#F4F4F0)**: Not pure white, but a warm, slightly off-white paper tone. It serves as the canvas.
- **Lead Grey (#2C2C2C)**: The color of the camera body and the ink used for captions. High contrast, heavy, and grounded.
- **Sepia Wash (#D4C5B0)**: The tone of aged photographs. Used for secondary information, dates, and subtle dividers.
- **Chemical Stain (#B8A99A)**: The unpredictable brownish-grey hue that appears where chemicals pool unevenly. Used for hover states and accents to introduce organic variation.

**Rule:** Never use pure black (#000000) or pure white (#FFFFFF). Always introduce warmth and age.

## Typography

Typography is the voice of the system. It rejects modern sans-serifs in favor of fonts that mimic **mechanical reproduction** and **human handwriting**.

- **Primary Font: Courier New (or similar monospace)**
  - Used for all headings, body text, and data.
  - Justification: Mimics the typewriter used to write captions on Polaroid photos. It is rigid, mechanical, and legible.
  - Letter-spacing: Slightly increased for body text to mimic the spacing of typewriter keys.

- **Secondary Font: Comic Sans MS (or similar casual script)**
  - Used *only* for captions, dates, and handwritten notes.
  - Justification: Represents the personal, human element added after the photo is taken. It is intentionally informal and imperfect.

**Rule:** Do not use system sans-serifs (Helvetica, Inter, Roboto). The monospace font is non-negotiable for the "instant" aesthetic.

## Layout

The layout is **modular and frame-based**.

- **The White Border:** Every piece of content (image, card, post) should be framed by a generous amount of Polaroid White space, mimicking the physical border of a Polaroid print.
- **Asymmetry:** Avoid perfect symmetry. Allow elements to be slightly offset, mimicking the haphazard placement of photos on a wall or fridge.
- **Grid:** Use a loose, irregular grid. Content should feel placed, not calculated.

**Rule:** Content should never touch the edge of the screen. Always maintain a "border" margin, reinforcing the idea of a physical object.

## Elevation & Depth

Depth is achieved through **contrast and texture**, not shadow.

- **No Drop Shadows:** Polaroid photos do not cast soft, blurred shadows on digital interfaces. They cast hard, distinct shadows or sit flat.
- **Hard Edges:** All borders are 1px solid Lead Grey. No rounded corners on images or cards (lg: 0px).
- **Texture Over Shadow:** Use subtle noise or grain overlays to create depth. A "Chemical Stain" border can indicate elevation instead of a shadow.

**Rule:** If it looks like glass or plastic, it is wrong. It should look like paper, metal, and ink.

## Shapes

- **Rectangles Only:** All major elements are rectangles with sharp corners (0px border-radius).
- **Irregularities:** Introduce slight rotations (±1-2 degrees) to cards or images to mimic the casual placement of physical photos.
- **Handwritten Accents:** Use SVG paths that mimic handwriting for dividers or decorative elements.

**Rule:** No circles, no pills, no rounded buttons. The aesthetic is industrial and analog.

## Components

### Button (Primary)
- **Shape:** Sharp rectangle (0px border-radius).
- **Color:** Lead Grey background, Polaroid White text.
- **Text:** Monospace, uppercase, slightly tracked out.
- **Hover:** Background shifts to Chemical Stain.
- **Focus:** 1px solid Chemical Stain border.
- **Text:** "CAPTURE" or "SAVE" – verbs that imply action and permanence.

### Card (Photo/Post)
- **Structure:** 
  - Outer container: Polaroid White, padding 24px (the white border).
  - Inner content: Image with sharp corners, no border.
  - Caption area: Below the image, using Comic Sans MS for date/name, Courier New for description.
- **Texture:** Subtle paper grain overlay on the white area.
- **Shadow:** None. Use a 1px solid Lead Grey border around the entire card.

### Table
- **Structure:** 
  - Headers: Lead Grey text, bold, monospace.
  - Rows: Alternating Sepia Wash and Polaroid White backgrounds.
  - Borders: 1px solid Lead Grey.
- **Imperfection:** Allow some cells to have handwritten-style annotations (using the secondary font) to indicate notes or corrections.

### Input Field
- **Style:** 
  - Border: 1px solid Lead Grey.
  - Background: Polaroid White.
  - Font: Courier New.
- **Focus:** Border becomes Chemical Stain.
- **Placeholder:** Sepia Wash, italicized, mimicking a faded note.

## Do's and Don'ts

### Do:
- **Embrace Imperfection:** Allow for slight misalignments, grain, and uneven coloring.
- **Use Monospace Fonts:** Courier New is the backbone of this system.
- **Frame Content:** Always use white space as a border around images and cards.
- **Add Handwritten Notes:** Use the secondary font for dates, names, or personal touches.
- **Keep it Warm:** Use warm greys and beiges, never cool blues or purples.

### Don't:
- **Use Rounded Corners:** Sharp edges only.
- **Add Soft Shadows:** Depth comes from contrast and texture, not blur.
- **Use Sans-Serif Fonts:** Inter, Roboto, and Helvetica are forbidden.
- **Make it Too Clean:** If it looks too polished, add noise or a slight rotation.
- **Use Purple/Blue Gradients:** The palette is strictly analog and earthy.
- **Ignore the "Wait":** Design for moments of anticipation, not instant gratification.

---
*This design system is a tribute to the analog era. It is not about efficiency; it is about presence.*