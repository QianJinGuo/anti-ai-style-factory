```yaml
version: 1.0.0
name: Biomorphic
description: Organic, curvilinear design language derived from mid-century organic modernism, prioritizing natural forms and fluid geometry over industrial rigidity.
colors:
  primary:
    name: "Verdant Moss"
    hex: "#4A5D23"
    rgb: "rgb(74, 93, 35)"
  secondary:
    name: "Terracotta Clay"
    hex: "#C2654A"
    rgb: "rgb(194, 101, 74)"
  tertiary:
    name: "Sandstone"
    hex: "#E6DCC8"
    rgb: "rgb(230, 220, 200)"
  neutral:
    name: "Raw Linen"
    hex: "#F4F1EA"
    rgb: "rgb(244, 241, 234)"
  muted:
    name: "Driftwood"
    hex: "#8C7B6B"
    rgb: "rgb(140, 123, 107)"
typography:
  h1:
    fontFamily: "Caslon Antiqua, 'Georgia', serif"
    fontSize: 2.5rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "Caslon Antiqua, 'Georgia', serif"
    fontSize: 1.875rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  h3:
    fontFamily: "Caslon Antiqua, 'Georgia', serif"
    fontSize: 1.25rem
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Caslon Antiqua, 'Georgia', serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: "Caslon Antiqua, 'Georgia', serif"
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
rounded:
  sm: "4px 12px 4px 12px"
  md: "12px 24px 12px 24px"
  lg: "24px 48px 24px 48px"
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    background: "#4A5D23"
    color: "#F4F1EA"
    border: "none"
    borderRadius: "12px 24px 12px 24px"
    padding: "12px 24px"
    fontWeight: 400
    letterSpacing: 0.02em
    hoverBackground: "#3A4A1C"
  card:
    background: "#FFFFFF"
    border: "1px solid #E6DCC8"
    borderRadius: "24px 48px 24px 48px"
    padding: "24px"
    boxShadow: "none"
  table:
    headerBackground: "#E6DCC8"
    rowHoverBackground: "#F4F1EA"
    border: "1px solid #E6DCC8"
    borderRadius: "12px"
```

# Biomorphic Design Specification

## Overview

Biomorphic design is rooted in the mid-20th century reaction against the rigid rectilinearity of the International Style. It draws inspiration from nature's inherent geometry—cells, leaves, river stones, and seed pods. This style rejects the "machine for living" aesthetic in favor of a "living" interface. It is characterized by non-uniform curvature, tactile materiality, and a color palette derived from earth and foliage. The goal is to make digital interfaces feel organic, approachable, and structurally sound like a living organism rather than a constructed machine.

## Colors

The palette is strictly grounded in natural pigments. We avoid synthetic, electric, or neon hues. Colors should appear muted, as if viewed through natural light or printed on unbleached paper.

- **Verdant Moss (`#4A5D23`)**: Primary action color. Represents growth and structure. Used for primary buttons and key headings.
- **Terracotta Clay (`#C2654A`)**: Secondary accent. Represents earth and warmth. Used for warnings, secondary actions, or highlights.
- **Sandstone (`#E6DCC8`)**: Tertiary background. A warm, textured off-white used for cards or section backgrounds.
- **Raw Linen (`#F4F1EA`)**: Neutral background. The canvas. It should feel like paper or fabric, not sterile white.
- **Driftwood (`#8C7B6B`)**: Muted text. Used for captions, disabled states, and secondary information.

## Typography

We reject the geometric neutrality of sans-serif fonts like Helvetica or Inter. Instead, we use **Old Style Serifs** that possess humanist qualities, varying stroke weights, and organic serifs. The type should feel hand-carved or printed, not laser-cut.

- **Family**: `Caslon Antiqua` is the ideal reference. Fallbacks include `Georgia` or `Times New Roman`.
- **Hierarchy**: The hierarchy is established through size and weight, not through drastic font family changes.
- **Letter Spacing**: Slightly increased tracking (0.01em - 0.02em) to mimic the breathing room of traditional print typography.
- **Line Height**: Generous line height (1.6) to encourage slow, readable reading, akin to a novel.

## Layout

Layouts should avoid strict grids where possible. While alignment is necessary for readability, the visual weight should feel balanced rather than symmetrical.

- **Asymmetry**: Use asymmetrical balance to mimic natural growth patterns.
- **Flow**: Content should flow around organic shapes. Text should wrap around curved containers, not just rectangular boxes.
- **Whitespace**: Whitespace is treated as "air" or "space" in a natural environment. It is generous and uncluttered.

## Elevation & Depth

Biomorphic design rejects the shadow-heavy depth of Material Design and the blur-heavy depth of Glassmorphism. Depth is achieved through **layering of texture and opacity**, not drop shadows.

- **No Drop Shadows**: Avoid `box-shadow` with blur >= 10px.
- **Layering**: Use distinct background colors (e.g., Raw Linen vs. Sandstone) to create hierarchy.
- **Texture**: If texture is used, it should be subtle noise or paper grain, not gradients.

## Shapes

The defining characteristic of this style is **non-uniform border-radius**. We do not use uniform circles or squares.

- **Organic Curves**: Use `border-radius` with four distinct values to create "squircles," "leaf shapes," or "stone shapes."
  - Example: `border-radius: 24px 48px 24px 48px;` creates a gentle, asymmetrical curve.
- **Asymmetry**: The top-left radius might be smaller than the bottom-right, suggesting a natural irregularity.
- **Avoid**: Perfect circles (except for avatars or icons) and perfect squares.

## Components

### Buttons

Buttons should look like pressed clay or polished stones.

- **Shape**: `border-radius: 12px 24px 12px 24px;`
- **Color**: Primary background is Verdant Moss. Text is Raw Linen.
- **Interaction**: On hover, the color darkens slightly (`#3A4A1C`). No scale transform. No glow.
- **Text**: Uppercase or Title Case, with increased letter spacing.

### Cards

Cards should feel like floating leaves or pebbles.

- **Shape**: `border-radius: 24px 48px 24px 48px;`
- **Background**: White or very light Sandstone.
- **Border**: 1px solid Sandstone. No shadow.
- **Padding**: Generous internal padding to let content breathe.

### Tables

Tables should avoid the harsh grid lines of spreadsheets.

- **Header**: Background Sandstone, text Verdant Moss.
- **Rows**: Alternating row colors (Raw Linen vs. White) to aid readability without lines.
- **Borders**: Only top and bottom borders between rows, in a muted Driftwood color. No vertical lines.
- **Radius**: The entire table container has a slight organic radius (`12px`).

### Inputs

- **Shape**: `border-radius: 12px 24px 12px 24px;`
- **Border**: 1px solid Driftwood.
- **Focus**: The border color changes to Verdant Moss. No box-shadow glow.
- **Placeholder**: Driftwood color, italicized to suggest a handwritten note.

## Do's and Don'ts

### Do
- Use organic, asymmetrical border radii.
- Choose serif fonts with humanist characteristics.
- Use earthy, muted color palettes.
- Prioritize readability and slow pacing.
- Use natural textures (subtle noise, paper grain) if appropriate.

### Don't
- Use geometric sans-serifs (Inter, Roboto, Helvetica).
- Use purple/blue gradients or neon colors.
- Use glassmorphism (backdrop-filter: blur).
- Use uniform 12px or 16px border-radius everywhere.
- Use heavy drop shadows or glowing effects.
- Use marketing buzzwords ("revolutionary", "seamless").