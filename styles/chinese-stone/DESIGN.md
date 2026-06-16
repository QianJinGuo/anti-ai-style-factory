# 碑帖 (Beitie) Design Specification

## 1. Overview

The **Beitie** style is not merely a visual aesthetic; it is a digital restoration of the physical act of inscription. Drawing from the tradition of Chinese stele rubbing (Beitie), this design system rejects the ephemeral, glossy nature of modern UI in favor of permanence, texture, and gravity.

It is built on three pillars:
1.  **Stone Texture (石刻质感):** Interfaces should feel carved, not drawn. Surfaces have grain, edges have weight.
2.  **Brush Stroke (笔锋):** Typography must retain the irregularity of hand-drawn strokes. Fonts are selected for their calligraphic character, not geometric neutrality.
3.  **Stele Layout (碑文布局):** Content is structured with the solemnity of ancient inscriptions, often favoring vertical rhythms and centered alignments over left-aligned web grids.

This system is intended for cultural archives, high-end editorial, literary platforms, and heritage institutions. It is **not** for SaaS dashboards, e-commerce, or fast-paced consumer apps.

## 2. Colors

The palette is derived from natural pigments used in traditional seal carving and ink painting. It is low-saturation, high-contrast, and earthy.

| Token | Name | Hex | Usage |
| :--- | :--- | :--- | :--- |
| `primary` | **Cinnabar (朱砂)** | `#B22222` | **Seals.** Used sparingly for primary actions, active states, or key data points. It represents the "stamp of authority." |
| `secondary` | **Ink Black (墨黑)** | `#1A1A1A` | **Text & Carving.** The primary color for text and borders. It should never be pure `#000000` to avoid harsh digital contrast; it must feel like dried ink. |
| `tertiary` | **Ochre (赭石)** | `#8B4513` | **Accent.** Used for secondary borders, dates, or metadata. Evokes the color of aged stone or wood blocks. |
| `neutral` | **Rice Paper (宣纸)** | `#F5F2EB` | **Canvas.** The background. Must have a slight warm tint to simulate paper texture. Avoid pure white. |
| `muted` | **Dust Grey (灰土)** | `#8C8C8C` | **Placeholder/Disabled.** Faint, like worn stone or faded ink. |

**Do Not Use:**
-   Gradients (unless simulating natural light on stone).
-   Neon colors.
-   Pure `#FFFFFF` backgrounds (causes eye strain against Rice Paper tone).

## 3. Typography

Typography is the soul of Beitie. We reject sans-serif geometric fonts (Inter, Roboto) as they feel too "manufactured." Instead, we use serif fonts with calligraphic origins.

### Font Stack