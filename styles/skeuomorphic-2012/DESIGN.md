```yaml
version: 1.0.0
name: Skeuomorphism
description: A design philosophy where digital interfaces mimic physical objects through realistic textures, lighting, and depth to reduce cognitive load and provide intuitive affordances.
colors:
  primary: "#6B8E23" # Olive Drab / Natural Green
  secondary: "#8B4513" # Saddle Brown / Leather
  tertiary: "#D2B48C" # Tan / Paper
  neutral: "#F5F5DC" # Beige / Parchment
  muted: "#D3D3D3" # Light Gray / Stone
typography:
  h1:
    fontFamily: "Baskerville"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.5px"
  h2:
    fontFamily: "Baskerville"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.3px"
  h3:
    fontFamily: "Baskerville"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0px"
  body-md:
    fontFamily: "Georgia"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0px"
  caption:
    fontFamily: "Courier New"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0px"
rounded:
  sm: "2px"
  md: "6px"
  lg: "12px"
spacing:
  sm: "4px"
  md: "8px"
  lg: "16px"
  xl: "24px"
components:
  button-primary:
    background: "linear-gradient(to bottom, #4CAF50, #2E7D32)"
    border: "1px solid #1B5E20"
    border-radius: "6px"
    box-shadow: "inset 0 1px 0 rgba(255,255,255,0.4), 0 1px 2px rgba(0,0,0,0.2)"
    color: "#FFFFFF"
    font-family: "Helvetica Neue"
    font-weight: 700
    padding: "8px 16px"
  card:
    background: "#FFFFFF"
    border: "1px solid #D3D3D3"
    border-radius: "8px"
    box-shadow: "0 2px 4px rgba(0,0,0,0.1), inset 0 0 0 1px rgba(255,255,255,0.5)"
    padding: "16px"
  table:
    background: "#FFFFFF"
    border: "1px solid #D3D3D3"
    border-radius: "4px"
    box-shadow: "0 1px 3px rgba(0,0,0,0.1)"
```

# Skeuomorphic Design System

## Overview

Skeuomorphism is the practice of designing digital interfaces that emulate their real-world counterparts in appearance and interaction. Originating in the late 2000s, this style prioritizes familiarity and tactile realism over abstraction. It relies heavily on visual cues such as shadows, highlights, textures (leather, paper, wood, metal), and gradients to create a sense of depth and materiality. The goal is to make the interface feel like a physical object—like a leather-bound calendar or a wooden notepad—thereby lowering the barrier to entry for users unfamiliar with digital metaphors.

## Colors

The palette is derived from natural materials and mid-century analog aesthetics. Colors are often desaturated or earthy, avoiding the neon vibrancy of modern flat design.

- **Primary**: `#6B8E23` (Olive Drab) - Represents nature, growth, and organic materials.
- **Secondary**: `#8B4513` (Saddle Brown) - Evokes leather, wood, and warmth.
- **Tertiary**: `#D2B48C` (Tan) - Mimics parchment, cork, and light wood.
- **Neutral**: `#F5F5DC` (Beige) - The background canvas, resembling aged paper or linen.
- **Muted**: `#D3D3D3` (Light Gray) - Used for stone, metal, and secondary structural elements.

**Usage Note**: Avoid pure white (`#FFFFFF`) as a primary background. Instead, use off-whites or beiges to reduce eye strain and enhance the "physical" feel.

## Typography

Typography should reflect the era's reliance on traditional print media. Serif fonts are preferred for headings to convey authority and tradition, while monospaced or clean sans-serifs may be used for technical data.

- **Headings**: `Baskerville` or `Georgia`. These serif fonts have high contrast and a classic feel, reminiscent of book covers and newspapers.
- **Body**: `Georgia` or `Times New Roman`. Highly readable on low-resolution screens of the era, mimicking printed text.
- **Captions/Labels**: `Courier New` or `Consolas`. Monospaced fonts suggest typewriters, ledgers, and technical specifications.

**Anti-AI Signal**: Do not use geometric sans-serifs like Helvetica Neue or Roboto for primary content. If sans-serifs are necessary, use humanist alternatives like Verdana or Trebuchet MS.

## Layout

Layouts are structured and grid-based, but often feature "container" metaphors.

- **Containers**: Elements are often placed within "cards" or "panels" that have distinct borders and shadows, simulating physical cards, notebooks, or drawers.
- **Padding**: Generous padding is used to mimic the margins of a book or the space between items in a physical portfolio.
- **Alignment**: Strict left or center alignment, reflecting traditional print layouts.

## Elevation & Depth

Depth is the defining characteristic of this style. It is achieved through complex layering of shadows and highlights.

- **Drop Shadows**: Use `box-shadow` with multiple layers.
  - *Example*: `0 2px 4px rgba(0,0,0,0.2)` for a soft ground shadow.
  - *Example*: `0 4px 8px rgba(0,0,0,0.15)` for lifted elements.
- **Inner Shadows**: Crucial for simulating depth within objects (e.g., the recess of a text field or the edge of a button).
  - *Example*: `inset 0 1px 3px rgba(0,0,0,0.2)` for a pressed-in effect.
- **Gradients**: Linear gradients are used to simulate lighting on curved or flat surfaces.
  - *Buttons*: Top-down gradient (lighter at top, darker at bottom) to simulate a convex surface.
  - *Text Fields*: Bottom-up gradient (darker at top, lighter at bottom) to simulate a concave surface.

## Shapes

Shapes are rarely perfectly circular or square. They often feature slight irregularities or rounded corners that mimic manufacturing processes.

- **Border Radius**: Small to medium radii (`2px` to `8px`). Avoid large radii (`20px+`) which feel too modern and soft.
- **Borders**: Solid, distinct borders (`1px` or `2px`) in dark colors to define edges clearly, simulating physical boundaries.

## Components

### Button (Primary)
- **Appearance**: Simulates a physical rubber or plastic button.
- **Background**: Vertical linear gradient from light green to dark green.
- **Border**: 1px solid dark green.
- **Shadow**: Inner white highlight on top, outer dark shadow on bottom.
- **Text**: Bold, white, with a slight text-shadow for depth.
- **Interaction**: On `:active`, invert the gradient or add an inner shadow to simulate a press.

### Card (Note/Calendar)
- **Appearance**: Simulates a piece of paper or a leather-bound page.
- **Background**: Off-white or textured beige.
- **Border**: Subtle 1px border.
- **Shadow**: Soft drop shadow to lift it from the background.
- **Texture**: Optional subtle noise or paper grain overlay.

### Text Field
- **Appearance**: Simulates an engraved line or a recessed slot.
- **Background**: Light gray.
- **Border**: 1px solid dark gray.
- **Shadow**: Inner dark shadow on all sides to create a "hole" effect.
- **Focus State**: Remove inner shadow and add a bright blue outer glow.

### Navigation Bar
- **Appearance**: Simulates a wooden shelf or a metallic strip.
- **Background**: Dark wood texture or metallic gradient.
- **Border**: Top and bottom borders with highlights to simulate edge bevels.

## Do's and Don'ts

**Do:**
- Use CSS `box-shadow` extensively to create depth.
- Incorporate subtle textures (noise, grain, leather patterns) via CSS background images or pseudo-elements.
- Use serif fonts for headings to evoke tradition.
- Ensure high contrast between text and background for readability.
- Simulate lighting effects with gradients.

**Don't:**
- Use flat, uniform colors without gradients or shadows.
- Use pure black (`#000000`) or pure white (`#FFFFFF`) as primary backgrounds.
- Use modern, geometric sans-serif fonts (e.g., Inter, Roboto) as the primary typeface.
- Create "glassmorphism" effects (backdrop-filter blur) as they are anachronistic to this era.
- Use emoji as icons; instead, use classic icon sets like SF Pro Icons (iOS 6 style) or custom skeuomorphic icons.