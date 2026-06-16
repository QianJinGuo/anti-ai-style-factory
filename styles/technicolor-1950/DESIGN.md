---
version: 1.0.0
name: Technicolor Dramatic
description: A high-contrast, saturated design system inspired by the three-strip Technicolor process, emphasizing bold primary hues, deep blacks, and serif typography for maximum visual impact.
colors:
  primary:
    name: Technicolor Red
    value: "#D91E26"
    hex: "#D91E26"
    usage: "Primary actions, headlines, critical alerts"
  secondary:
    name: Technicolor Green
    value: "#009B4D"
    hex: "#009B4D"
    usage: "Secondary actions, success states, decorative accents"
  tertiary:
    name: Technicolor Blue
    value: "#005EB8"
    hex: "#005EB1"
    usage: "Tertiary actions, links, informational elements"
  neutral:
    name: Deep Black
    value: "#0A0A0A"
    hex: "#0A0A0A"
    usage: "Text, borders, heavy structural elements"
  muted:
    name: Paper White
    value: "#F4F1EA"
    hex: "#F4F1EA"
    usage: "Backgrounds, cards, negative space"
typography:
  h1:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: 48
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02
  h2:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: 36
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01
  h3:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: 24
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Source Serif Pro, Merriweather, serif"
    fontSize: 16
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01
  caption:
    fontFamily: "IBM Plex Mono, Courier New, monospace"
    fontSize: 12
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05
rounded:
  sm: 2px
  md: 4px
  lg: 8px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    background: "#D91E26"
    color: "#F4F1EA"
    border: "2px solid #0A0A0A"
    borderRadius: "2px"
    fontWeight: 700
    textTransform: "uppercase"
    letterSpacing: 0.1
  card:
    background: "#F4F1EA"
    border: "4px solid #0A0A0A"
    boxShadow: "8px 8px 0px #0A0A0A"
    borderRadius: "4px"
  table:
    headerBg: "#0A0A0A"
    headerColor: "#F4F1EA"
    rowHover: "#E8E4DB"
    borderColor: "#0A0A0A"
    borderWidth: "2px"
---

# Technicolor Dramatic Design System

## Overview

This design language draws directly from the Golden Age of Hollywood (1935–1970), specifically the aesthetic of the three-strip Technicolor process. It rejects the softness of modern UI in favor of hard edges, intense saturation, and typographic hierarchy. The interface should feel like a printed program from a 1940s premiere: bold, theatrical, and unapologetically analog.

## Colors

The palette is built on the subtractive primary colors used in the original Technicolor printing process, contrasted against deep, void-like blacks and warm, aged paper whites.

- **Technicolor Red (#D91E26)**: The dominant accent. Used for primary interactions and key visual anchors. It must appear vibrant, not neon.
- **Technicolor Green (#009B4D)**: A deep, organic green. Used for secondary states and decorative borders.
- **Technicolor Blue (#005EB1)**: A rich, saturated blue. Used for tertiary elements and links.
- **Deep Black (#0A0A0A)**: Not pure #000000, but a rich charcoal-black used for text and hard shadows to simulate ink density.
- **Paper White (#F4F1EA)**: A warm, off-white background that simulates the texture of aged paper or film stock, reducing eye strain compared to pure white.

## Typography

Typography is the backbone of this system. Sans-serif fonts are strictly prohibited.

- **Headings**: *Playfair Display* (or Georgia). High-contrast serif fonts evoke the elegance of movie posters and mastheads. Headings should be large, bold, and tightly tracked.
- **Body**: *Source Serif Pro* (or Merriweather). A readable serif that maintains the historical context while ensuring legibility at small sizes.
- **Captions/Code**: *IBM Plex Mono* (or Courier New). Monospace fonts represent the technical aspect of film processing, metadata, or credits.

## Layout

- **Grid**: Rigid, column-based layouts reminiscent of newspaper columns or program booklets.
- **Whitespace**: Generous but structured. Use the "Paper White" background to create breathing room, but fill it with content.
- **Alignment**: Strict left alignment for body text; centered alignment for major headlines and title cards.

## Elevation & Depth

Depth is achieved through **hard shadows**, not blur. This mimics the look of cut-out paper or printed layers.

- **Shadows**: `box-shadow: 8px 8px 0px #0A0A0A;`
- **No Blur**: All shadows must be solid offsets. No `rgba` transparency or `blur` values.
- **Borders**: Thick, solid borders (2px–4px) define structure.

## Shapes

- **Borders**: Sharp or slightly rounded (2px–4px). Never fully circular.
- **Cards**: Rectangular with hard edges.
- **Buttons**: Rectangular with sharp corners or minimal rounding (2px).

## Components

### Button Primary

A bold, rectangular button with a hard black border and a solid black offset shadow.