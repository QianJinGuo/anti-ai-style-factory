---
version: 1.0.0
name: Nordic Modern
description: A design system rooted in democratic design principles, prioritizing natural materials, functional clarity, and understated elegance through restrained palettes and organic geometry.
colors:
  primary:
    name: "Nordic Pine"
    value: "#4A5D46"
    usage: "Primary actions, brand accents, deep foliage references"
  secondary:
    name: "Fjord Mist"
    value: "#7A8B8C"
    usage: "Secondary information, disabled states, subtle borders"
  tertiary:
    name: "Clay Tile"
    value: "#C4A484"
    usage: "Warm accents, hover states, decorative elements"
  neutral:
    name: "Raw Linen"
    value: "#F5F5F0"
    usage: "Page backgrounds, card surfaces, light mode base"
  muted:
    name: "Charcoal Ash"
    value: "#333333"
    usage: "Primary text, high-contrast labels"
  error:
    name: "Dried Berry"
    value: "#8B3A3A"
    usage: "Error states, destructive actions"
  warning:
    name: "Mustard Ochre"
    value: "#D4A017"
    usage: "Warning states, attention-grabbing non-critical alerts"

typography:
  h1:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.02em"
    usage: "Page titles, hero sections. Clean, authoritative, unadorned."
  h2:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "-0.01em"
    usage: "Section headers. Clear hierarchy without visual shouting."
  h3:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0em"
    usage: "Subsection headers, card titles. Slight weight increase for structure."
  body-md:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0em"
    usage: "Primary reading text. High legibility, generous spacing."
  caption:
    fontFamily: "'Helvetica Neue', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0.01em"
    usage: "Footnotes, metadata, secondary labels. Small but readable."

rounded:
  sm: "2px"
  md: "4px"
  lg: "8px"
  usage: "Subtle rounding only. Avoids plastic feel; maintains material honesty."

spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  usage: "Consistent rhythm based on 8px grid. Breathing room is a feature, not a bug."

components:
  button-primary:
    backgroundColor: "#4A5D46"
    color: "#F5F5F0"
    border: "none"
    borderRadius: "4px"
    padding: "10px 20px"
    fontSize: "16px"
    fontWeight: "400"
    letterSpacing: "0.02em"
    hover:
      backgroundColor: "#3A4A36"
    usage: "Main CTAs. Solid, grounded, no shadows."
  button-secondary:
    backgroundColor: "transparent"
    color: "#4A5D46"
    border: "1px solid #7A8B8C"
    borderRadius: "4px"
    padding: "9px 19px"
    fontSize: "16px"
    fontWeight: "400"
    usage: "Secondary actions. Outlined, low visual weight."
  card:
    backgroundColor: "#FFFFFF"
    border: "1px solid #E8E8E3"
    borderRadius: "4px"
    padding: "24px"
    boxShadow: "none"
    usage: "Content containers. Flat, clean edges, no elevation tricks."
  table:
    headerBackgroundColor: "#F5F5F0"
    headerColor: "#333333"
    rowBackgroundColor: "#FFFFFF"
    rowHoverBackgroundColor: "#FAFAF7"
    borderColor: "#E8E8E3"
    borderStyle: "solid"
    borderWidth: "1px"
    usage: "Data display. Clear grid lines, no heavy headers."
---

# Nordic Modern Design System

## Overview

Nordic Modern is a design philosophy born from the mid-20th century Scandinavian ethos: **democratic, functional, and humane**. It rejects ornamentation for its own sake, favoring clarity, natural textures, and a restrained color palette. This system is not about "looking cool"; it is about respecting the user’s time and eyes. Every element serves a purpose. Every space is intentional. The result is calm, legible, and enduring.

## Colors

Our palette is derived from the natural environment of Scandinavia: deep pine forests, grey fjords, warm clay, and raw linen.

- **Primary (Nordic Pine #4A5D46)**: Used for primary actions and key brand elements. It is grounded and organic, not electric.
- **Secondary (Fjord Mist #7A8B8C)**: A cool, neutral grey for borders, icons, and secondary text. It recedes, allowing content to lead.
- **Tertiary (Clay Tile #C4A484)**: A warm earth tone used sparingly for accents, hover states, or decorative dividers. It adds humanity without shouting.
- **Neutral (Raw Linen #F5F5F0)**: The background color. Not pure white, which is harsh, but a soft, warm off-white that reduces eye strain.
- **Muted (Charcoal Ash #333333)**: For primary text. Dark grey is more readable and less fatiguing than pure black.
- **Error (Dried Berry #8B3A3A)**: A muted red for errors. Avoids the alarmist nature of bright red.
- **Warning (Mustard Ochre #D4A017)**: A historical pigment used for warnings. Distinct but not aggressive.

**Rule**: Never use pure black (#000000) or pure white (#FFFFFF) for large surfaces or text. Always use the defined neutrals.

## Typography

We use **Helvetica Neue** (or Arial as fallback) because it is the quintessential Swiss/Nordic sans-serif: neutral, legible, and timeless. It does not have personality; it lets the content have personality.

- **Headings**: Light weight (400), tight letter-spacing for a clean, modern look. No bolding unless necessary for hierarchy.
- **Body**: Regular weight, generous line-height (1.6). Readability is paramount.
- **Captions**: Small but legible, with slight letter-spacing for clarity.

**Rule**: Do not use decorative fonts. Do not use bold headings for visual impact alone. Use size and spacing to create hierarchy.

## Layout

- **Grid**: 8px baseline grid. All spacing, margins, and padding are multiples of 8.
- **Whitespace**: Generous. Whitespace is not empty; it is active. It gives content room to breathe.
- **Alignment**: Left-aligned text for readability. Centered alignment only for short, impactful statements (e.g., hero titles).
- **Container**: Max-width 1200px, centered. Content should not stretch to the edges of wide screens.

## Elevation & Depth

**Nordic Modern does not use shadows.** Depth is created through:

1. **Color**: Slightly lighter backgrounds for elevated surfaces.
2. **Borders**: Thin, light borders to define edges.
3. **Spacing**: More whitespace around important elements.

**Rule**: Never use `box-shadow` with blur. If you need to indicate hierarchy, use size, color, or position.

## Shapes

- **Borders**: Subtle rounding. `sm: 2px`, `md: 4px`, `lg: 8px`.
- **Avoid**: Perfect circles (except for avatars), heavy rounded corners (`>12px`), or sharp 90-degree angles without any rounding.
- **Justification**: Rounded corners should feel natural, like a stone, not plastic.

## Components

### Buttons

- **Primary**: Solid background (Nordic Pine), white text. No border. `4px` border-radius.
- **Secondary**: Transparent background, solid border (Fjord Mist), primary text color. `4px` border-radius.
- **Text**: No background, no border, primary text color. Underlined on hover.

### Cards

- **Background**: White (`#FFFFFF`).
- **Border**: `1px solid #E8E8E3`.
- **Shadow**: None.
- **Padding**: `24px`.
- **Border-Radius**: `4px`.
- **Usage**: For grouping related content. Not for decorative purposes.

### Tables

- **Headers**: Background `#F5F5F0`, text `#333333`.
- **Rows**: Background `#FFFFFF`, hover `#FAFAF7`.
- **Borders**: `1px solid #E8E8E3` between rows and columns.
- **Usage**: For data. Clean, grid-like, no heavy headers.

## Do's and Don'ts

### Do:
- Use natural, muted colors.
- Prioritize readability and clarity.
- Use generous whitespace.
- Keep interfaces simple and uncluttered.
- Use Helvetica Neue for its neutrality.

### Don't:
- Use bright, saturated colors (except for the defined error/warning states).
- Use gradients.
- Use drop shadows or glassmorphism.
- Use decorative fonts.
- Use emojis as icons.
- Use marketing language ("revolutionary", "seamless").
- Make elements look "clickable" through shadows; make them look clickable through clear affordances (buttons, links).