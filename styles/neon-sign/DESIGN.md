---
version: 1.0.0
name: Neon Signage (霓虹灯牌)
description: A high-contrast visual system inspired by mid-century commercial signage, prioritizing legibility through luminescence against darkness, where typography mimics the physical constraints of bent glass tubing.
colors:
  primary: "#FF00FF" # Magenta Tube
  secondary: "#00FFFF" # Cyan Tube
  tertiary: "#FFD700" # Amber Tube
  neutral: "#1A1A1A" # Dark Concrete Background
  muted: "#4A4A4A" # Dimmed Glass / Unlit Tube
typography:
  h1:
    fontFamily: "'Pacifico', 'Dancing Script', cursive"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "'Pacifico', 'Dancing Script', cursive"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "'Pacifico', 'Dancing Script', cursive"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0"
  body-md:
    fontFamily: "'Courier Prime', 'IBM Plex Mono', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.05em"
  caption:
    fontFamily: "'IBM Plex Mono', monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.1em"
rounded:
  sm: 2px
  md: 4px
  lg: 8px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    background: "transparent"
    border: "2px solid var(--color-primary)"
    color: "var(--color-primary)"
    boxShadow: "0 0 8px var(--color-primary), inset 0 0 4px var(--color-primary)"
    borderRadius: "var(--rounded-sm)"
    padding: "var(--spacing-sm) var(--spacing-md)"
  card:
    background: "var(--color-neutral)"
    border: "1px solid var(--color-muted)"
    boxShadow: "none"
    borderRadius: "var(--rounded-md)"
    padding: "var(--spacing-lg)"
  table:
    background: "var(--color-neutral)"
    color: "var(--color-secondary)"
    border: "1px solid var(--color-muted)"
    borderRadius: "var(--rounded-sm)"
    fontSize: "var(--body-md-font-size)"
    letterSpacing: "var(--body-md-letter-spacing)"
---

# Neon Signage Design System

## Overview

The **Neon Signage** design style is rooted in the tactile reality of gas-discharge lighting. It rejects the sterile uniformity of digital defaults in favor of the imperfect, glowing warmth of hand-bent glass tubes. This system is designed for low-light environments or high-contrast interfaces where visibility is achieved not through brightness, but through luminescence. The core philosophy is "Darkness as Canvas, Light as Ink." Typography mimics the fluid curves of heated glass, while layouts respect the structural limitations of physical signage (wiring, support frames).

## Colors

The palette is defined by the emission spectra of noble gases mixed with mercury vapor. Colors are not flat; they are perceived through their interaction with the surrounding darkness.

*   **Primary (`#FF00FF`)**: Magenta. The quintessential neon color. High energy, aggressive, eye-catching. Used for primary actions and key headings.
*   **Secondary (`#00FFFF`)**: Cyan. Cool, electric, calming yet artificial. Used for secondary information and borders.
*   **Tertiary (`#FFD700`)**: Amber. Warm, inviting, reminiscent of sodium vapor or old diner signs. Used for warnings or highlights.
*   **Neutral (`#1A1A1A`)**: Deep Charcoal. Not pure black (#000000), which kills contrast for glowing elements. This dark grey allows white text or dimmed neon effects to remain visible.
*   **Muted (`#4A4A4A`)**: Dimmed Glass. The color of unlit neon tubes or dirty glass. Used for inactive states, disabled elements, or subtle grid lines.

**Usage Rule:** No solid background fills other than the Neutral. All color is applied as stroke, text, or glow.

## Typography

Typography must emulate the physical properties of neon tubing: variable thickness, organic curves, and high legibility against dark backgrounds.

*   **Headings (Cursive/Script)**:
    *   *Font Family*: `Pacifico`, `Dancing Script`, or similar high-contrast scripts.
    *   *Rationale*: Mimics the continuous line of a bent glass tube. Avoid rigid sans-serifs for headings as they break the illusion of hand-crafted signage.
    *   *Style*: Thin to thick transitions should be preserved. No bolding that makes the "tube" look like a solid block.
*   **Body (Monospace)**:
    *   *Font Family*: `Courier Prime`, `IBM Plex Mono`, `Roboto Mono`.
    *   *Rationale*: Reflects the industrial, utilitarian side of neon sign manufacturing (blueprints, wiring diagrams, price tags). The fixed width aids in aligning "tubes" of text.
    *   *Style*: Increased letter-spacing (`0.05em`) to simulate the gap between individual letters in a physical sign.

## Layout

Layouts are structured around the concept of the "Sign Board."

*   **Grid**: Loose, modular grid. Signs are often hung or mounted asymmetrically.
*   **Padding**: Generous negative space. Neon signs need room to "breathe" so the glow isn't clipped or visually compressed.
*   **Alignment**: Left-aligned for body text (monospace natural flow). Centered for display headings (traditional sign balance).

## Elevation & Depth

Depth is created through **light diffusion**, not shadow.

*   **Glow Effect**: Use `box-shadow` with large blur radii and low opacity to simulate light scattering.
    *   *Primary Glow*: `0 0 10px var(--color-primary), 0 0 20px var(--color-primary)`
    *   *Secondary Glow*: `0 0 8px var(--color-secondary), 0 0 16px var(--color-secondary)`
*   **No Drop Shadows**: Traditional `drop-shadow` implies an object blocking light. Neon *is* the light. Use `text-shadow` for text glows.
    *   *Text Glow*: `0 0 5px currentColor, 0 0 10px currentColor`

## Shapes

*   **Borders**: All borders should be treated as "tubes." They are not flat lines but glowing cylinders.
    *   `border-width`: 2px - 4px.
    *   `border-radius`: Minimal. Neon tubes have slight bends, not sharp corners. Use `sm` (2px) or `md` (4px) radius to soften corners without losing the industrial feel.
*   **Icons**: Line-art icons only. No filled icons. Icons should look like they are made of bent wire or glass tubing.

## Components

### Button (Primary)

A glowing outline button. The interior is transparent (or neutral), allowing the background to show through. The border is the "tube."