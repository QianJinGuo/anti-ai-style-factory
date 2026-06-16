---
version: 1.0.0
name: Space Age
description: A design language rooted in the optimistic futurism of the Space Race, prioritizing aerodynamic curves, atomic precision, and the stark contrast of chrome against deep space.
colors:
  primary:
    name: Rocket Orange
    hex: "#FF5722"
    usage: "Call-to-actions, critical alerts, primary accents."
  secondary:
    name: Apollo Silver
    hex: "#E0E0E0"
    usage: "Secondary backgrounds, borders, disabled states."
  tertiary:
    name: Cosmic Blue
    hex: "#1A237E"
    usage: "Headings, primary text, deep contrast elements."
  neutral:
    name: Lunar White
    hex: "#F5F5F5"
    usage: "Base background, card surfaces."
  muted:
    name: Orbit Grey
    hex: "#9E9E9E"
    usage: "Placeholder text, subtle dividers, inactive icons.
typography:
  h1:
    fontFamily: "'Eurostile', 'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  h2:
    fontFamily: "'Eurostile', 'Montserrat', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  h3:
    fontFamily: "'Eurostile', 'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0px
  body-md:
    fontFamily: "'IBM Plex Mono', 'Share Tech Mono', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.5px
  caption:
    fontFamily: "'IBM Plex Mono', 'Share Tech Mono', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
rounded:
  sm: 2px
  md: 8px
  lg: 24px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    style: "Solid Rocket Orange background, sharp corners with slight rounding (4px), uppercase text, monospace font, sharp shadow offset."
  card:
    style: "Lunar White background, 1px Orbit Grey border, subtle drop shadow (0 2px 4px rgba(0,0,0,0.1)), rounded corners (8px)."
  table:
    style: "Striped rows (alternating Lunar White and Apollo Silver), monospace font for data, clear header separation with Cosmic Blue background."
---

# Space Age Design System

## Overview

The **Space Age** design style captures the technological optimism and aerodynamic aesthetics of the period between 1957 and 1972. It is characterized by the juxtaposition of industrial functionality (monospace fonts, grid layouts) with futuristic, organic curves (bullet shapes, boomerang motifs). This system avoids modern "flat" minimalism in favor of a structured, precise, and slightly retro-futuristic interface that feels engineered for exploration.

## Colors

The palette is derived from the materials of space travel: polished aluminum, high-visibility safety orange, and the deep void of space.

- **Rocket Orange (#FF5722)**: High-energy accent. Used sparingly for interactive elements to draw attention without overwhelming the user. Evokes heat shields and warning lights.
- **Apollo Silver (#E0E0E0)**: Metallic neutrality. Represents the hull of a spacecraft. Used for secondary UI elements and backgrounds to maintain a clean, industrial feel.
- **Cosmic Blue (#1A237E)**: Authority and depth. Replaces standard black for text to reduce harsh contrast while maintaining readability. Evokes the night sky and instrument panels.
- **Lunar White (#F5F5F5)**: The base canvas. Not pure white, but a slightly warm grey to mimic the brightness of the moon's surface.
- **Orbit Grey (#9E9E9E)**: Structural lines. Used for borders, dividers, and inactive states.

## Typography

Typography balances the precision of engineering with the boldness of futurism.

- **Headings (Eurostile/Montserrat)**: Wide, geometric sans-serif fonts. Eurostile is historically significant in mid-century modern design and was widely used in sci-fi posters and space mission branding. It conveys authority and modernity.
- **Body Text (IBM Plex Mono/Share Tech Mono)**: Monospace fonts reflect the typewriter-style displays of early computers and the precise, data-heavy nature of space missions. The fixed width ensures alignment and readability for technical content.
- **Caps and Tracking**: Headings often use slight letter-spacing or uppercase styling to mimic control panel labels.

## Layout

- **Grid System**: Strict 8px or 16px grid to reflect the precision of engineering schematics.
- **Asymmetry**: While structured, layouts may incorporate asymmetrical balance to evoke the dynamic motion of a rocket launch.
- **Whitespace**: Generous whitespace around key elements to emphasize isolation and focus, similar to a spacecraft in the void.

## Elevation & Depth

- **Shadows**: Hard, offset shadows (no blur) to simulate the look of cut-out paper or physical layers, reminiscent of mid-century graphic design.
- **Depth**: Limited use of gradients. Instead, depth is achieved through contrast between silver and white layers.

## Shapes

- **Boomerang & Bullet Shapes**: Buttons and cards may feature elongated corners or boomerang-like cuts to reference aerodynamic forms.
- **Rounded Corners**: Use `sm` (2px) for technical elements (inputs, small buttons) and `lg` (24px) for primary containers to soften the industrial feel.
- **Orbital Patterns**: Subtle background patterns of dots or concentric circles can be used to evoke radar screens or orbital paths.

## Components

### Button Primary
- **Appearance**: Solid Rocket Orange background.
- **Text**: Uppercase, monospace, white.
- **Shape**: Rectangular with sharp corners or slight rounding (4px).
- **Interaction**: On hover, invert colors (White background, Rocket Orange border/text).

### Card
- **Appearance**: Lunar White background with a 1px Orbit Grey border.
- **Shadow**: Hard shadow offset by 2px right and 2px down.
- **Content**: Clear hierarchy with heading in Cosmic Blue, body in Orbit Grey.

### Table
- **Header**: Cosmic Blue background, white text, uppercase.
- **Rows**: Alternating Lunar White and Apollo Silver backgrounds.
- **Data**: Monospace font for alignment and technical precision.

### Input Field
- **Border**: 1px Orbit Grey, solid.
- **Focus**: 2px Rocket Orange border, no shadow.
- **Label**: Uppercase, monospace, positioned above the input.

## Do's and Don'ts

### Do
- Use monospace fonts for data, labels, and technical details.
- Incorporate geometric shapes and straight lines.
- Use high-contrast colors (Orange vs. Blue/White).
- Emphasize precision and alignment.
- Use uppercase for labels and headers to mimic control panels.

### Don't
- Use rounded, soft, or overly playful fonts (e.g., Poppins, Quicksand).
- Apply heavy, blurred drop shadows (no glassmorphism).
- Use gradients unless they simulate metallic reflections.
- Use generic icon sets; prefer geometric or line-based icons.
- Over-decorate; keep the interface functional and uncluttered.