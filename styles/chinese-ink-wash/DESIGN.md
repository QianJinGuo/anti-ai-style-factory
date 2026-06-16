---
version: 1.0.0
name: 水墨 (Shui-Mo / Ink Wash)
description: A design language rooted in the philosophy that emptiness is form, where ink density dictates hierarchy and whitespace carries the weight of meaning.
colors:
  primary:
    name: 焦墨 (Scorched Ink)
    value: "#1A1A1A"
    usage: "Primary headings, critical UI elements, dense ink washes."
  secondary:
    name: 浓墨 (Dense Ink)
    value: "#333333"
    usage: "Body text, secondary headings, borders."
  tertiary:
    name: 淡墨 (Light Ink)
    value: "#666666"
    usage: "Captions, disabled states, subtle dividers."
  neutral:
    name: 宣纸 (Xuan Paper)
    value: "#F4F1EB"
    usage: "Backgrounds, card surfaces, canvas."
  muted:
    name: 宿墨 (Old Ink)
    value: "#8C8C8C"
    usage: "Placeholders, inactive icons, background textures."
typography:
  h1:
    fontFamily: "Xingkai SC, STXingkai, KaiTi, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Xingkai SC, STXingkai, KaiTi, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Xingkai SC, STXingkai, KaiTi, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0em"
  body-md:
    fontFamily: "Songti SC, SimSun, Noto Serif CJK SC, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: "0.02em"
  caption:
    fontFamily: "Songti SC, SimSun, Noto Serif CJK SC, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.05em"
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    style: "Transparent background, solid 1px Scorched Ink border, no border-radius, hover state increases border thickness to 2px."
  card:
    style: "No shadow, no border. Defined by negative space and padding. Background matches Xuan Paper."
  table:
    style: "Minimalist rows separated by 1px Light Ink lines. No vertical borders. Headers in Dense Ink."
```

# 水墨 (Shui-Mo) Design System

## Overview
The **Shui-Mo** design system translates the ancient Chinese art of ink wash painting into a digital interface. It rejects the modern urge to fill every pixel, embracing **Liubai (留白)**—the strategic use of empty space—as a primary structural element. The system relies on **Mofen Wuse (墨分五色)**, using variations in ink saturation (opacity and weight) to establish hierarchy rather than color or complex shapes. The goal is **Qiyun Shengdong (气韵生动)**, ensuring the interface breathes and flows with the rhythm of the content.

## Colors
The palette is strictly monochromatic, derived from the grinding of ink sticks on an inkstone.

- **Backgrounds**: Must mimic the texture of **Xuan Paper (宣纸)**. Use `#F4F1EB` with a subtle noise overlay (opacity 3-5%) to simulate fiber texture. Avoid pure white (`#FFFFFF`).
- **Primary Text/Elements**: **Scorched Ink (焦墨)** `#1A1A1A`. Used for H1, critical actions, and focal points.
- **Secondary Text**: **Dense Ink (浓墨)** `#333333`. Used for H2, H3, and body text.
- **Tertiary Elements**: **Light Ink (淡墨)** `#666666`. Used for captions, borders, and inactive states.
- **Muted/Disabled**: **Old Ink (宿墨)** `#8C8C8C`. Used for placeholders and background patterns.

*Note: No accent colors. If color is required for data visualization, use grayscale gradients only.*

## Typography
Typography is the brushstroke. It must feel hand-drawn yet legible.

- **Headings**: Use **Xingkai (行楷)** or **KaiTi (楷体)**. These fonts retain the calligraphic flow of traditional brush writing. They should be used sparingly, only for titles and significant section breaks.
- **Body Text**: Use **Songti (宋体)** or **SimSun**. The high contrast between thick and thin strokes provides excellent readability at small sizes while maintaining the historical aesthetic.
- **Spacing**: Increase `line-height` to 1.8 for body text. The vertical rhythm is crucial; text should float on the paper, not crowd it.
- **Letter Spacing**: Slight positive tracking (`0.02em` to `0.05em`) for body text and captions to mimic the spacing of traditional vertical typesetting.

## Layout
- **Grid**: Asymmetric grids are preferred. Rigid 12-column grids should be broken. Content blocks should feel placed, not aligned.
- **Whitespace**: Margins and padding must be generous. A rule of thumb: if an element fits, add more space. The empty space is not "empty"; it is part of the composition.
- **Alignment**: Left-aligned text is standard. Center alignment is reserved for ceremonial titles or single-line statements.

## Elevation & Depth
- **No Shadows**: Drop shadows imply artificiality and modern UI conventions. Depth is created through **layering of ink density** and **scale**.
- **Overlapping**: Elements may overlap slightly, mimicking the transparency of wet ink on paper. Use `opacity` variations (0.3, 0.6, 1.0) to create depth.
- **Texture**: Use subtle paper grain textures on overlays to ground digital elements in the physical world of the brush.

## Shapes
- **Zero Border Radius**: All corners must be sharp (`0px`). This reflects the precision of the brush tip and the rigidity of the paper edge.
- **Lines**: Use thin, solid lines (1px) for dividers. They should look like brush strokes—slightly uneven if possible via SVG filters, but strictly monochromatic.
- **Images**: Images should be desaturated and overlaid with a gradient map from Scorched Ink to Light Ink to integrate them into the monochromatic scheme.

## Components

### Button (Primary)
- **Shape**: Rectangular, sharp corners.
- **Style**: Transparent background, 1px solid Scorched Ink border.
- **Text**: Scorched Ink, Xingkai font.
- **Hover**: Border thickness increases to 2px; background fills with 5% Scorched Ink opacity.
- **Active**: Background fills with 10% Scorched Ink opacity.

### Card
- **Shape**: Sharp rectangular container.
- **Style**: No border, no shadow.
- **Content**: Defined entirely by padding (48px minimum).
- **Divider**: A single 1px Light Ink line separates the card content from the background.

### Table
- **Style**: Minimalist.
- **Headers**: Dense Ink, bold, uppercase.
- **Rows**: Separated by 1px Light Ink lines at the bottom only.
- **Zebra Striping**: Do not use. Use negative space between rows instead.

### Navigation
- **Style**: Horizontal or vertical list.
- **Indicator**: No underlines. Active state is indicated by a 2px solid Scorched Ink bar on the left (for vertical) or top (for horizontal), or by increasing font weight.
- **Spacing**: Generous vertical or horizontal gaps between items.

## Do's and Don'ts

### Do
- **Do** embrace emptiness. Let the user's eye rest in the whitespace.
- **Do** use varying opacities of black to create hierarchy.
- **Do** prioritize readability of Songti for long-form content.
- **Do** use Xingkai only for emphasis and titles, never for body text.
- **Do** ensure high contrast between text and the Xuan Paper background.

### Don't
- **Don't** use gradients (except simulated ink washes via opacity).
- **Don't** use rounded corners.
- **Don't** use bright colors or emojis.
- **Don't** crowd the interface. If it looks "complete," you have added too much.
- **Don't** use sans-serif fonts like Inter or Roboto.
- **Don't** use glassmorphism or blur effects.
- **Don't** use marketing buzzwords. Keep copy concise and poetic if possible.
