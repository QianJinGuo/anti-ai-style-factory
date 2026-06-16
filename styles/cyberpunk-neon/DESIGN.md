---
version: 1.0.0
name: 赛博朋克 (Cyberpunk)
description: A visual language of high-tech decay and digital resistance, where neon light pierces the smog of a stratified, dystopian reality.
colors:
  primary: "#FF00FF" # Neon Magenta / Hot Pink
  secondary: "#00FFFF" # Cyan / Electric Blue
  tertiary: "#FFFF00" # Acid Yellow / Warning
  neutral: "#121212" # Deep Charcoal / Smog
  muted: "#2A2A2A" # Concrete Grey
  accent: "#FF3333" # Alert Red
  success: "#39FF14" # Toxic Green
  background: "#050505" # Void Black
  surface: "#1A1A1A" # Dark Panel
typography:
  h1:
    fontFamily: '"Share Tech Mono", "Courier New", monospace'
    fontSize: "3.5rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: '"Share Tech Mono", "Courier New", monospace'
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: '"Share Tech Mono", "Courier New", monospace'
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.05em"
  body-md:
    fontFamily: '"Share Tech Mono", "Courier New", monospace'
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.02em"
  caption:
    fontFamily: '"Share Tech Mono", "Courier New", monospace'
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.1em"
    textTransform: "uppercase"
  code:
    fontFamily: '"Fira Code", "Consolas", monospace'
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
  pill: "0px"
spacing:
  sm: "4px"
  md: "8px"
  lg: "16px"
  xl: "32px"
  xxl: "64px"
components:
  button-primary:
    background: "transparent"
    border: "2px solid #FF00FF"
    color: "#FF00FF"
    padding: "12px 24px"
    fontFamily: '"Share Tech Mono", monospace'
    fontSize: "1rem"
    letterSpacing: "0.1em"
    textTransform: "uppercase"
    boxShadow: "0 0 5px #FF00FF, inset 0 0 5px #FF00FF"
    transition: "all 0.1s ease"
    hover:
      background: "#FF00FF"
      color: "#000000"
      boxShadow: "0 0 15px #FF00FF, 0 0 30px #FF00FF"
  card:
    background: "#1A1A1A"
    border: "1px solid #333333"
    borderRadius: "0px"
    padding: "24px"
    position: "relative"
    overflow: "hidden"
    boxShadow: "none"
    before:
      content: "''"
      position: "absolute"
      top: "0"
      left: "0"
      width: "4px"
      height: "100%"
      background: "#00FFFF"
  table:
    width: "100%"
    borderCollapse: "collapse"
    fontFamily: '"Share Tech Mono", monospace'
    fontSize: "0.875rem"
    color: "#CCCCCC"
    border: "1px solid #333333"
    th:
      background: "#2A2A2A"
      color: "#00FFFF"
      textTransform: "uppercase"
      letterSpacing: "0.05em"
      padding: "12px"
      borderBottom: "2px solid #00FFFF"
    td:
      padding: "12px"
      borderBottom: "1px solid #333333"
      borderLeft: "1px solid #333333"
    tr:
      hover:
        background: "#222222"
        color: "#FFFFFF"
---

# 赛博朋克 (Cyberpunk) Design System

## Overview

Cyberpunk is not a style; it is a warning. It is the aesthetic of the "high tech, low life" paradox. In this design system, we reject the clean, sterile optimism of modern corporate design. Instead, we embrace the grit, noise, and fragmentation of a world dominated by corporations and degraded by technology.

This system is built for interfaces that feel lived-in, hacked, or observed. It prioritizes information density and urgency over comfort. The visual language is characterized by harsh contrasts, monospaced typography reminiscent of terminal outputs, and a palette derived from neon signs reflected in wet asphalt.

## Colors

The color palette is derived from the contrast between the artificial glow of neon and the oppressive darkness of the urban night.

### Primary: Neon Magenta (#FF00FF)
Used for primary actions and critical alerts. It represents the artificial, the synthetic, and the seductive danger of technology. It is aggressive and impossible to ignore.

### Secondary: Cyan (#00FFFF)
Used for secondary information, data visualization, and structural borders. It evokes the cold, clinical feel of holographic displays and laser light. It cuts through the darkness with precision.

### Tertiary: Acid Yellow (#FFFF00)
Used sparingly for warnings, errors, or "glitch" effects. It mimics the caution tape and hazard signs found in industrial decay.

### Neutral: Deep Charcoal (#121212)
The base background color. It is not pure black, allowing for subtle layering and reducing eye strain in low-light environments, mimicking the smog-filled sky.

### Muted: Concrete Grey (#2A2A2A)
Used for surfaces, cards, and inactive elements. It represents the brutalist architecture and concrete infrastructure of the dystopian city.

### Accent: Alert Red (#FF3333)
Used exclusively for critical system failures, danger, or "corrupted" data states.

## Typography

Typography is the backbone of the Cyberpunk aesthetic. We strictly avoid humanist sans-serifs (like Inter or Roboto) as they feel too "organic" and "friendly."

### Font Family: Share Tech Mono / Courier New
We use monospaced fonts to simulate terminal interfaces, code editors, and raw data streams. The lack of proportional spacing creates a rhythmic, mechanical feel.

*   **H1/H2:** Large, bold, and slightly tracked out to mimic header banners on industrial signage.
*   **Body:** Small to medium size, high readability but with a rigid structure.
*   **Caption:** Uppercase, heavily tracked out, used for metadata, timestamps, and system logs.

### Glitch Effect
Text should occasionally exhibit a "glitch" effect: slight horizontal displacement, color channel splitting (RGB shift), or pixelation. This reinforces the theme of digital instability and surveillance.

## Layout

### Grid & Structure
The layout is based on a rigid, modular grid, reflecting the structured chaos of the city. However, elements can "break out" of this grid through overlapping, clipping, or z-index manipulation.

### Asymmetry
Perfect symmetry is avoided. Asymmetrical layouts create tension and visual interest, mimicking the unplanned, organic growth of slums amidst planned corporate towers.

### Information Density
High information density is preferred. White space is considered "wasted bandwidth." Interfaces should feel packed with data, reflecting the overwhelming nature of the digital age.

## Elevation & Depth

Elevation is not achieved through soft shadows (which feel too modern and clean). Instead, depth is created through:

1.  **Layering:** Overlapping elements with distinct borders.
2.  **Opacity:** Semi-transparent backgrounds to show underlying data.
3.  **Glow:** Hard, distinct glows around neon elements (`box-shadow` with low blur).
4.  **Scanlines:** A subtle horizontal line pattern overlay to simulate CRT monitors.

## Shapes

### Zero Border Radius
All elements are strictly rectangular. No rounded corners. This reinforces the industrial, utilitarian, and harsh nature of the aesthetic.

### Diagonal Cuts
Accents may include diagonal cuts or clipped corners to suggest military or tactical gear.

## Components

### Button-Primary
*   **Style:** Transparent background, 2px solid Neon Magenta border.
*   **Hover:** Background fills with Magenta, text turns Black, glow intensifies.
*   **Text:** Uppercase, monospaced, wide letter-spacing.
*   **Interaction:** Instant feedback, no smooth transitions.

### Card
*   **Style:** Dark grey background, 1px solid border.
*   **Accent:** A 4px vertical line on the left edge in Cyan.
*   **Content:** Dense, with clear hierarchy.
*   **Overlay:** Optional scanline pattern overlay.

### Table
*   **Style:** Minimal borders, only horizontal lines between rows and vertical lines between columns.
*   **Header:** Cyan text, uppercase, bold.
*   **Rows:** Subtle background change on hover.
*   **Data:** Monospaced, right-aligned for numbers, left-aligned for text.

### Alert/Notification
*   **Style:** Full-width banner, Acid Yellow background, Black text.
*   **Icon:** Text-based symbol (e.g., `[!]`).
*   **Animation:** Flashing border or text glitch effect.

## Do's and Don'ts

### Do's
*   **Use Monospaced Fonts:** Maintain the terminal aesthetic.
*   **Embrace Darkness:** Use dark backgrounds to make neon pop.
*   **Add Noise:** Incorporate subtle grain, scanlines, or glitch effects.
*   **Be Honest:** Show system status, errors, and raw data.
*   **Use Borders:** Define structure with hard lines, not shadows.

### Don'ts
*   **No Rounded Corners:** Keep everything sharp and angular.
*   **No Soft Shadows:** Avoid `box-shadow` with high blur values.
*   **No Humanist Sans-Serifs:** Do not use Inter, Roboto, Poppins, or Helvetica.
*   **No Warm Gradients:** Avoid cozy, inviting gradients. Stick to cold, artificial neon.
*   **No Fluffy Icons:** Use geometric, pixelated, or text-based icons.
*   **No Marketing Speak:** Use technical, clinical, or dystopian language.

## Philosophy

> "The street finds its own uses for things."

This design system is not about beauty; it is about function in a hostile environment. It is the interface of the hacker, the corporate spy, and the street samurai. It is ugly, yes, but it is honest. It reflects the world it inhabits: broken, bright, and dangerous.