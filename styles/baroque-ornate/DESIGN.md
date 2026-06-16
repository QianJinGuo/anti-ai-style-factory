# Baroque Design System

## Overview

The Baroque design system is an architectural approach to digital interfaces that rejects neutrality in favor of emotional resonance. Inspired by the artistic movement of the 17th and 18th centuries, this system emphasizes **drama**, **movement**, and **ornamentation**. It is not designed for speed or efficiency alone, but for presence and authority. Every element is weighted, every border is intentional, and every interaction feels substantial. This is UI for institutions, heritage brands, and high-stakes narratives where gravity matters.

## Colors

The palette is derived from the pigments of the Old Masters and the materials of royal courts: deep crimsons, oxidized greens, and heavy gold leaf.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| **Primary** | `#8B0000` | Deep Crimson. Used for primary actions, headers, and critical alerts. Represents power and passion. |
| **Secondary** | `#D4AF37` | Metallic Gold. Used for borders, icons, and accents. Provides the "glint" of luxury. |
| **Tertiary** | `#2F4F4F` | Dark Slate Green. Used for backgrounds of secondary sections or footer areas. Grounds the design. |
| **Neutral** | `#F5F5DC` | Beige/Parchment. The primary background color. Avoids sterile white for a warmer, aged paper feel. |
| **Muted** | `#4A4A4A` | Charcoal. For body text. Softer than black, ensuring readability against parchment. |

## Typography

Typography is the voice of the system. We reject geometric sans-serifs in favor of high-contrast didone typefaces that evoke the engraved title pages of antiquarian books.

*   **Headings (`Bodoni Moda`)**: High contrast between thick and thin strokes. Sharp, elegant, and authoritative. Used for all display text.
*   **Body (`EB Garamond`)**: A transitional serif with excellent legibility. It provides a humanist counterpoint to the sharpness of the headings, ensuring long-form reading comfort.
*   **Captions/UI**: Small caps or tracked-out Garamond for labels, creating a sense of formal precision.

## Layout

Layouts are structured but not rigid. While we maintain a grid for alignment, the visual weight is distributed asymmetrically to create tension.

*   **Asymmetry**: Avoid centering everything. Use offset columns and varying whitespace to guide the eye in a dynamic path.
*   **Framing**: Content is rarely "floating." It is almost always framed by borders, columns, or distinct background zones.
*   **Hierarchy**: Size and contrast are the primary tools for hierarchy. There is no ambiguity; the most important element is always the largest and darkest.

## Elevation & Depth

Baroque design does not use soft, diffuse shadows (neumorphism or material elevation). Depth is achieved through **layering** and **contrast**.

*   **Hard Shadows**: Use sharp, dark shadows (`box-shadow: 4px 4px 0px rgba(0,0,0,0.2)`) to create a physical sense of cards or panels resting on the parchment.
*   **Borders**: Borders are structural. They define space more than shadows do.
*   **Layering**: Overlapping elements should have clear z-indexing, with gold borders acting as the visual separator between layers.

## Shapes

*   **Rectilinear Base**: The fundamental shape is the rectangle.
*   **Ornamental Corners**: While `rounded` tokens exist for compatibility, the aesthetic preference is sharp corners (`sm: 2px`).
*   **Frames**: Use double borders (one solid gold, one thin black) to mimic picture frames around images or key content blocks.

## Components

### Button Primary
A substantial, rectangular button with a gold border and crimson fill. The text is gold. On hover, the background deepens, and the border becomes a pale gold.