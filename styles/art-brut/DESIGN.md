---
version: 1.0.0
name: 原生艺术 (Art Brut)
description: 一种拒绝美学规范、拥抱未经训练之手之直觉与粗糙力量的视觉语言，强调材料的真实性与形式的自发性。
colors:
  primary: "#E25822" # Raw Ochre - Unrefined earth pigment
  secondary: "#2B2B2B" # Charcoal - Graphite sketching medium
  tertiary: "#D9C5A7" # Raw Umber - Dried clay tone
  neutral: "#F4F1EA" # Unbleached Linen - Canvas base
  muted: "#8C8C8C" # Dust - Accumulated wear and tear
typography:
  h1:
    fontFamily: "Special Elite, Courier Prime"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Special Elite, Courier Prime"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Special Elite, Courier Prime"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0em"
  body-md:
    fontFamily: "Special Elite, Courier Prime"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.01em"
  caption:
    fontFamily: "Special Elite, Courier Prime"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 4px
  md: 8px
  lg: 16px
  xl: 32px
components:
  button-primary:
    background: "#2B2B2B"
    color: "#F4F1EA"
    border: "2px solid #2B2B2B"
    borderRadius: 0px
    padding: "12px 24px"
    fontFamily: "Special Elite, Courier Prime"
    fontSize: 16px
    fontWeight: 400
    letterSpacing: "0.05em"
    hover:
      background: "#E25822"
      border: "2px solid #E25822"
      color: "#F4F1EA"
  card:
    background: "#F4F1EA"
    border: "1px solid #2B2B2B"
    borderRadius: 0px
    padding: 24px
    boxShadow: "none"
    shadow: "4px 4px 0px #2B2B2B"
  table:
    background: "#F4F1EA"
    border: "1px solid #2B2B2B"
    borderRadius: 0px
    header:
      background: "#2B2B2B"
      color: "#F4F1EA"
      padding: "12px 16px"
    row:
      padding: "12px 16px"
      borderBottom: "1px solid #2B2B2B"
---

# 原生艺术 (Art Brut) Design Specification

## Overview

This design system embodies the philosophy of **Art Brut** (Raw Art), a term coined by Jean Dubuffet to describe art created outside the bounds of official culture. It rejects professional polish, digital smoothness, and algorithmic perfection. Instead, it prioritizes **intuition**, **material honesty**, and **raw expression**. 

The interface feels hand-assembled, like a collage or a sketchbook page. It is not "clean"; it is "true." Visual noise is intentional. Misalignment suggests human error. Rough edges suggest physical touch. This is not a template; it is a canvas.

## Colors

The palette is derived from natural pigments, industrial waste, and aged paper. No digital neon. No gradients.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Primary** | `#E25822` | Raw Ochre. Used for primary actions, highlights, and emphasis. Evokes dried clay and rust. |
| **Secondary** | `#2B2B2B` | Charcoal. Used for text, borders, and primary UI elements. Hard, matte, and absorbing. |
| **Tertiary** | `#D9C5A7` | Raw Umber. Used for backgrounds of secondary elements, subtle dividers. |
| **Neutral** | `#F4F1EA` | Unbleached Linen. The main background. Warm, slightly textured off-white. |
| **Muted** | `#8C8C8C` | Dust. Used for disabled states, captions, and secondary text. |

**Rule:** Never use pure black (`#000000`) or pure white (`#FFFFFF`). Always introduce warmth or grime.

## Typography

We reject geometric sans-serifs (Inter, Roboto) as they represent corporate uniformity. We use **typewriter/monospaced fonts** to evoke the voice of the outsider, the institutional record, or the handwritten note.

- **Font Family:** `Special Elite` or `Courier Prime`. If unavailable, fall back to generic `monospace`.
- **Character:** Typewriter ink bleed, uneven spacing, mechanical rhythm.
- **Usage:** All text, including headings, uses the same font family. Hierarchy is established through **size** and **weight**, not font family changes.
- **Alignment:** Left-aligned only. Justification creates false order.

## Layout

- **Grid:** No rigid grid. Use a **loose, asymmetrical layout**. Elements may overlap. Margins may vary.
- **Structure:** Think "collage" or "sketchbook page." Content blocks are pinned, taped, or drawn onto the canvas.
- **Whitespace:** Intentional. Not "padding," but "margin." Let the background breathe.

## Elevation & Depth

No drop shadows with blur (`box-shadow: blur`). Shadows are **hard**, **solid**, and **offset**.

- **Shadow Style:** `4px 4px 0px #2B2B2B`
- **Meaning:** Represents a physical object placed on top of another. No mystery, no diffusion.
- **Layering:** Use overlapping elements with solid borders to indicate hierarchy.

## Shapes

- **Borders:** Always `1px` or `2px` solid. Never dashed or dotted unless simulating stitching or pencil marks.
- **Corners:** Always `0px` (square). Rounded corners imply industrial molding and digital smoothness. We want the cut edge.
- **Icons:** Use SVG paths that look **hand-drawn** or **sketchy**. No filled icons. No gradients. Lines should vary slightly in thickness if possible.

## Components

### Button (Primary)
A solid block of charcoal with ochre hover state. No rounded corners. No smooth transitions.