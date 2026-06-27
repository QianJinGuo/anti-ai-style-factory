---
version: "1.0.0"
name: "Cyberpunk"
description: "A visual language reflecting the dissonance between high-tech infrastructure and societal decay, characterized by aggressive neon contrast, digital corruption, and utilitarian grit."
colors:
  primary: "#FF00FF"
  secondary: "#00FFFF"
  tertiary: "#FFFF00"
  neutral: "#1A1A1A"
  muted: "#404040"
typography:
  h1:
    fontFamily: "Share Tech Mono"
    fontSize: "3rem"
    fontWeight: "400"
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Share Tech Mono"
    fontSize: "2rem"
    fontWeight: "400"
    lineHeight: "1.2"
    letterSpacing: "0.05em"
  h3:
    fontFamily: "Share Tech Mono"
    fontSize: "1.25rem"
    fontWeight: "400"
    lineHeight: "1.4"
    letterSpacing: "0.1em"
  body-md:
    fontFamily: "Share Tech Mono"
    fontSize: "1rem"
    fontWeight: "400"
    lineHeight: "1.5"
    letterSpacing: "0"
  caption:
    fontFamily: "Share Tech Mono"
    fontSize: "0.75rem"
    fontWeight: "400"
    lineHeight: "1.2"
    letterSpacing: "0.15em"
rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
spacing:
  sm: "4px"
  md: "8px"
  lg: "16px"
  xl: "32px"
components:
  button-primary:
    background: "#000000"
    border: "1px solid #FF00FF"
    color: "#FF00FF"
    padding: "8px 16px"
    fontFamily: "Share Tech Mono"
    fontSize: "0.875rem"
    letterSpacing: "0.1em"
    textTransform: "uppercase"
    transition: "none"
    hover:
      background: "#FF00FF"
      color: "#000000"
  card:
    background: "#1A1A1A"
    border: "1px solid #404040"
    padding: "16px"
    position: "relative"
  table:
    borderCollapse: "collapse"
    width: "100%"
    fontFamily: "Share Tech Mono"
    fontSize: "0.875rem"
    color: "#E0E0E0"
  input:
    background: "#0A0A0A"
    border: "1px solid #404040"
    color: "#00FFFF"
    fontFamily: "Share Tech Mono"
    padding: "8px"
    caretColor: "#00FFFF"
    focus:
      border: "1px solid #00FFFF"
      boxShadow: "0 0 5px #00FFFF"
```

# Cyberpunk Design System

## Overview

This design system is built on the philosophy of **High Tech, Low Life**. It rejects the smooth, friendly, and accessible aesthetics of modern corporate web design in favor of raw, utilitarian, and often hostile interfaces. The visual language mimics the aesthetic of 1980s sci-fi concept art and early computer terminal displays: harsh, high-contrast, and glitch-prone. It is not designed to be "pleasant"; it is designed to be functional within a dystopian context.

## Colors

The palette is defined by extreme contrast. Backgrounds are near-black to simulate dark urban environments or unlit screens. Foregrounds are saturated neon colors that vibrate against the dark background.

### Palette
- **Primary (Neon Magenta):** `#FF00FF` - Used for primary actions, active states, and critical warnings.
- **Secondary (Neon Cyan):** `#00FFFF` - Used for secondary information, data streams, and hover states.
- **Tertiary (Acid Yellow):** `#FFFF00` - Used for alerts, error states, and highlighting corrupted data.
- **Neutral (Charcoal):** `#1A1A1A` - The primary background color. Not pure black, to reduce eye strain slightly while maintaining darkness.
- **Muted (Gunmetal):** `#404040` - Used for borders, disabled states, and secondary text.

### Usage Rules
- **No Gradients:** Gradients are forbidden. They imply smoothness and polish, which contradicts the gritty reality of the style.
- **High Contrast:** Text must always be legible against its background. Neon on black is the standard.
- **Glitch Accents:** Use `#FFFF00` sparingly to indicate system errors or data corruption.

## Typography

Typography is the primary vehicle for the aesthetic. We use a **Monospace** font to evoke the feeling of a terminal, a code editor, or a printed data sheet. The font choice is `Share Tech Mono`, a free, open-source font that resembles vintage computer terminals.

### Type Scale
- **Headings (H1, H2, H3):** Uppercase or Title Case, with generous letter-spacing (`0.05em` to `0.1em`) to create a sense of mechanical precision.
- **Body:** Monospace, fixed width. No fluid resizing.
- **Captions/Labels:** Small, uppercase, with high letter-spacing (`0.15em`).

### Rules
- **No Serifs:** Serifs imply tradition and humanity. We want machine-like clarity.
- **No Script/Handwritten Fonts:** These are forbidden.
- **Letter Spacing:** Use letter-spacing to control density. Dense text feels chaotic; wide spacing feels technical.

## Layout

Layouts are **grid-based** but rigid. There is no fluid flexibility. Containers are rectangular, with sharp corners.

### Grid
- Use a 12-column grid with a gutter width of `8px`.
- Align content to the grid lines. No floating elements.

### Spacing
- Spacing is uniform and binary: `4px`, `8px`, `16px`, `32px`.
- No arbitrary spacing values (e.g., `13px`).

### Borders
- All borders are `1px` solid.
- No rounded corners. `border-radius: 0` is mandatory.
- Borders can be dashed or dotted to simulate broken connections or low-fidelity signals.

## Elevation & Depth

**Flat design only.** Shadows are forbidden. Depth is conveyed through:
1. **Color:** Darker backgrounds for lower layers, brighter colors for higher layers.
2. **Borders:** Thick borders for active elements, thin borders for inactive ones.
3. **Layering:** Overlapping elements with solid backgrounds (no transparency).

### Rules
- **No Box Shadows:** Shadows imply softness. We want hard edges.
- **No Opacity Layers:** Transparency creates ambiguity. Elements should be opaque and clearly defined.

## Shapes

- **Rectangles:** All containers, buttons, and cards are rectangles.
- **Angles:** Sharp 90-degree angles. No curves.
- **Diagonals:** Diagonal lines can be used as decorative accents to suggest motion or instability, but only as thin lines (`1px`).

## Components

### Button
- **Shape:** Rectangle.
- **Border:** `1px` solid Primary color.
- **Background:** Transparent or `#000000`.
- **Text:** Uppercase, Monospace.
- **Hover:** Invert colors (Background becomes Primary, Text becomes Black). Add a `1px` secondary border.
- **Active:** Add a `box-shadow: 0 0 5px #FF00FF` (only on active state, not hover).

### Card
- **Shape:** Rectangle.
- **Background:** `#1A1A1A`.
- **Border:** `1px` solid `#404040`.
- **Header:** Bold, uppercase, with a bottom border of `1px` Primary color.
- **Content:** Monospace, left-aligned.

### Input Field
- **Shape:** Rectangle.
- **Background:** `#0A0A0A`.
- **Border:** `1px` solid `#404040`.
- **Focus:** Border becomes `#00FFFF`. Add a `box-shadow: 0 0 5px #00FFFF`.
- **Placeholder:** Color `#404040`.

### Table
- **Header:** Background `#2A2A2A`, Text `#00FFFF`, Uppercase.
- **Rows:** Alternating background colors (`#1A1A1A` and `#151515`) to aid readability.
- **Borders:** `1px` solid `#404040` between rows and columns.

## Do's and Don'ts

### Do
- **Do** use monospace fonts for all text.
- **Do** use high-contrast neon colors on dark backgrounds.
- **Do** keep shapes rectangular and sharp.
- **Do** use uppercase for headings and labels.
- **Do** use borders to define structure.
- **Do** incorporate subtle glitch effects (e.g., horizontal displacement) sparingly for interactive feedback.

### Don't
- **Don't** use rounded corners.
- **Don't** use gradients.
- **Don't** use box shadows (except for active state glow).
- **Don't** use serif or handwritten fonts.
- **Don't** use soft, pastel, or muted colors for primary actions.
- **Don't** use smooth animations. Animations should be instant or stuttery, not eased.
- **Don't** use glassmorphism or transparency.