# Ukiyo-e Design System Specification

## Overview

The Ukiyo-e (浮世绘) design system translates the aesthetic principles of 17th–19th century Japanese woodblock prints into a modern digital interface. It rejects Western perspective and realistic shading in favor of **flat color fields**, **expressive contour lines**, and **strategic negative space** (Ma). The interface feels like a curated gallery scroll, where content is framed by borders rather than floating in voids. The visual language is grounded, historical, and textural, avoiding the sterile perfection of modern UI trends.

## Colors

The palette is derived from traditional natural pigments and early synthetic dyes available during the Edo period. Colors are solid and opaque, never translucent or gradient-based.

| Token | Hex | Name | Usage |
| :--- | :--- | :--- | :--- |
| `primary` | `#E63946` | Benibeni (Safflower) | Primary CTAs, seals, active states, critical alerts. |
| `secondary` | `#1D3557` | Ai (Indigo) | Headings, strong structural lines, footer backgrounds. |
| `tertiary` | `#F4F1DE` | Washi | Main background, card surfaces, negative space. |
| `neutral` | `#264653` | Sumi (Charcoal) | Body text, borders, outlines, icons. |
| `muted` | `#A8DADC` | Asagi | Secondary backgrounds, subtle dividers, decorative patterns. |
| `accent` | `#E9C46A` | Kinari | Highlights, subtle icons, decorative elements. |

**Color Rules:**
1.  **No Gradients:** All color application must be solid. If a transition is needed, use a hard step-change between two solid colors.
2.  **Contrast:** Text on `Washi` background must be `Sumi`. Text on `Benibeni` must be `Washi`.
3.  **Seals:** Use `Seal` red sparingly for interactive confirmation or branding marks (Hanko).

## Typography

Typography mimics the brushwork of woodblock prints. Serifs are pronounced and organic, not mechanical.

*   **Font Family:** `Shippori Mincho` (Primary), `Noto Serif JP` (Fallback).
*   **Rationale:** Shippori Mincho is a high-quality digital font that captures the elegance of Edo-period calligraphy. It avoids the geometric rigidity of sans-serifs.
*   **Line Height:** Generous (1.6–1.8) to mimic the vertical flow of traditional scrolls.
*   **Letter Spacing:** Slightly increased for captions to create breathing room.
*   **Case:** Use Title Case or Sentence case. Avoid ALL CAPS, which disrupts the organic rhythm.

## Layout

The layout is based on **Ma (間)**, the concept of negative space.

1.  **Grid:** Use a rigid, visible grid system. Borders are structural elements, not hidden dividers.
2.  **Margins:** Margins are generous. Content should never touch the edge of the viewport.
3.  **No Perspective:** All elements must be aligned orthogonally. No angled transforms or 3D rotations.
4.  **Vertical Rhythm:** Spacing between sections should follow a modular scale (e.g., multiples of 1rem or 2rem) to create a rhythmic reading experience.

## Elevation & Depth

**Flatness is mandatory.**

*   **No Shadows:** `box-shadow` is prohibited. Depth is implied through color contrast and border thickness.
*   **Borders:** Use `1px` or `2px` solid borders in `Sumi` to define boundaries. Thicker borders for primary containers, thinner for secondary elements.
*   **Layering:** If layering is necessary, use overlapping solid color blocks with distinct borders, not transparency.

## Shapes

*   **Corner Radius:** `0px` everywhere. Corners should be sharp, reflecting the cut of the woodblock.
*   **Dividers:** Horizontal rules should be solid lines, not dashed or dotted.
*   **Icons:** Minimalist line art. No filled icons. Icons should look like hand-drawn sketches within a rectangular frame.

## Components

### Button (Primary)
A solid block of color with a bold border. No hover animations (no scaling, no fading).