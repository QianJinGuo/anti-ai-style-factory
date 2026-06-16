---
version: 1.0.0
name: Mexican Muralism (Muralismo)
description: A design system rooted in social realism, utilizing earthy pigments, bold geometric forms, and narrative depth to elevate public discourse and collective identity.
colors:
  primary:
    name: "Rosa Mexicano"
    hex: "#E4007C"
    usage: "Primary actions, headlines, focal points"
  secondary:
    name: "Ochre Earth"
    hex: "#D97706"
    usage: "Secondary accents, warnings, highlights"
  tertiary:
    name: "Prussian Blue"
    hex: "#1E3A8A"
    usage: "Data visualization, structural elements, depth"
  neutral:
    name: "Stucco White"
    hex: "#F5F5F0"
    usage: "Backgrounds, card surfaces, text on dark"
  muted:
    name: "Dusty Terracotta"
    hex: "#8D5524"
    usage: "Borders, disabled states, subtle dividers"
  text:
    name: "Charcoal Black"
    hex: "#111111"
    usage: "Primary body text"
  text-muted:
    name: "Graphite Grey"
    hex: "#4B5563"
    usage: "Secondary text, captions"

typography:
  h1:
    fontFamily: "Anton, Impact, sans-serif"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
    description: "Bold, condensed, industrial. Used for main titles to command attention like a headline on a factory wall."
  h2:
    fontFamily: "Anton, Impact, sans-serif"
    fontSize: "36px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
    description: "Strong subheadings that maintain visual weight without competing with the hero."
  h3:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.05em"
    description: "Uppercase tracking for section headers, mimicking stencil typography."
  body-md:
    fontFamily: "Merriweather, 'Georgia', serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "0.01em"
    description: "High-readability serif that grounds the design in tradition and narrative seriousness."
  caption:
    fontFamily: "Oswald, 'Arial Narrow', sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.1em"
    description: "Uppercase, tracked out for metadata, dates, and tags."

rounded:
  sm: "2px"
  md: "4px"
  lg: "0px"
  description: "Radii are minimal or non-existent. We prioritize sharp, decisive geometry over softness."

spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
  xxl: "128px"
  description: "Generous whitespace is used sparingly; elements often abut or overlap to create density and urgency."

components:
  button-primary:
    background: "#E4007C"
    color: "#FFFFFF"
    border: "2px solid #111111"
    borderRadius: "0px"
    padding: "12px 24px"
    fontFamily: "Oswald, sans-serif"
    fontWeight: 700
    letterSpacing: "0.1em"
    textTransform: "uppercase"
    boxShadow: "4px 4px 0px #111111"
    hover:
      background: "#C2006A"
      transform: "translate(2px, 2px)"
      boxShadow: "2px 2px 0px #111111"
    description: "Hard-edged, high-contrast button. The offset shadow mimics the relief of fresco painting."
  card:
    background: "#FFFFFF"
    border: "2px solid #111111"
    borderRadius: "0px"
    boxShadow: "8px 8px 0px rgba(0,0,0,0.15)"
    padding: "24px"
    description: "Cards are not floating; they are anchored blocks of content with heavy borders, resembling framed murals or concrete panels."
  table:
    headerBackground: "#1E3A8A"
    headerColor: "#FFFFFF"
    rowBackground: "#F5F5F0"
    rowAltBackground: "#FFFFFF"
    borderColor: "#8D5524"
    borderWidth: "1px"
    description: "High-contrast grid. Headers are solid blocks of color. No rounded corners on cells."
  input:
    background: "#FFFFFF"
    border: "2px solid #8D5524"
    borderRadius: "0px"
    padding: "12px"
    fontFamily: "Merriweather, serif"
    focus:
      border: "2px solid #E4007C"
      boxShadow: "none"
    description: "Inputs are rectangular fields, not pills. Focus states use primary color borders without blur."

---

# Mexican Muralism Design System

## 1. Overview

This design system is inspired by the **Mexican Muralism** movement (1920–1970), led by figures such as Diego Rivera, José Clemente Orozco, and David Alfaro Siqueiros. It rejects decorative minimalism in favor of **social narrative**, **monumental scale**, and **cultural identity**.

The interface treats digital space as a public wall. Content is not merely displayed; it is **inscribed**. The aesthetic prioritizes legibility, historical weight, and emotional resonance over fleeting trends. It is anti-corporate, anti-sterile, and pro-human.

## 2. Colors

The palette is derived from natural pigments used in fresco and encaustic painting. Colors are matte, earthy, and intense.

- **Primary (Rosa Mexicano)**: A vibrant, aggressive pink-red. It represents energy, blood, and revolution. Use sparingly for critical actions.
- **Secondary (Ochre Earth)**: A warm, sandy yellow-brown. Represents the land, history, and sun.
- **Tertiary (Prussian Blue)**: A deep, industrial blue. Represents the sky, water, and structural depth.
- **Neutral (Stucco White)**: Not pure white (#FFF), but a warm off-white (#F5F5F0) that mimics aged plaster.
- **Muted (Dusty Terracotta)**: A brownish-orange used for borders and subtle structure.

**Rule**: Avoid gradients. Colors should be flat and solid, mimicking painted blocks.

## 3. Typography

Typography must feel carved, stamped, or stenciled.

- **Headings**: Use **Anton** or **Impact**. These are condensed, bold sans-serifs that evoke industrial signage and poster art. They are loud and unapologetic.
- **Body**: Use **Merriweather** or **Georgia**. A robust serif that grounds the text in tradition and readability. It contrasts with the industrial headings, creating a dialogue between the modern and the historical.
- **Captions/Tags**: Use **Oswald** in uppercase with wide letter-spacing. Mimics stenciled military or factory labels.

**Rule**: Never use Inter, Roboto, or Poppins. Never use thin font weights (300/400) for headings. Headings must be heavy.

## 4. Layout

Layouts are **dense** and **structured**.

- **Grid**: Use a rigid, visible grid. Lines and borders should be explicit, not hidden.
- **Whitespace**: Use generous spacing only to separate major narrative sections. Within sections, elements should feel packed and interconnected, like figures in a mural.
- **Hierarchy**: Establish hierarchy through **size** and **color**, not subtle opacity changes. The most important content should be the largest and most saturated.

## 5. Elevation & Depth

Depth is achieved through **hard shadows** and **layering**, not blur.

- **Shadows**: Use `box-shadow` with `blur: 0px` or `blur: 2px`. The shadow should be a solid block of black or dark grey, offset diagonally (e.g., `4px 4px 0px`). This mimics the physical relief of plaster layers.
- **Layering**: Elements can overlap. A card might sit on top of a colored block, with a hard shadow defining the boundary.
- **No Glassmorphism**: Never use `backdrop-filter: blur`. Transparency is not part of this aesthetic. Everything is solid and tangible.

## 6. Shapes

- **Borders**: Always 2px solid. Color is usually black or dark terracotta.
- **Radii**: `0px` is the default. `2px` or `4px` may be used for small UI controls (like checkboxes), but never for cards or buttons.
- **Icons**: Use simple, bold, geometric line icons or filled shapes. Avoid detailed illustrations. Icons should be legible at small sizes and match the weight of the typography.

## 7. Components

### Buttons
- **Shape**: Rectangle. No rounded corners.
- **Style**: Solid primary color with a 2px black border and a hard offset shadow.
- **Text**: Uppercase, bold, tracked out.
- **Interaction**: On hover, the button shifts down and right by 2px, and the shadow shrinks, creating a tactile "press" effect.

### Cards
- **Shape**: Rectangle with heavy black border.
- **Style**: White background with a hard shadow. No internal padding gradients.
- **Content**: Headings are large and bold. Images are full-width within the card, with no rounded corners.

### Tables
- **Style**: High contrast. Headers are solid Prussian Blue with white text. Rows alternate between Stucco White and a very light grey.
- **Borders**: Visible 1px borders in Dusty Terracotta.

### Forms
- **Inputs**: Rectangular fields with 2px terracotta borders. Focus state uses primary color border. No shadow on focus.

## 8. Do's and Don'ts

### Do
- **Do** use high-contrast, matte colors.
- **Do** use bold, condensed typography for headings.
- **Do** use hard, offset shadows for depth.
- **Do** treat the screen as a canvas for narrative.
- **Do** use uppercase tracking for labels and captions.

### Don't
- **Don't** use soft, blurred shadows or gradients.
- **Don't** use rounded corners on major elements (cards, buttons).
- **Don't** use thin, light fonts for headings.
- **Don't** use generic sans-serifs (Inter, Roboto, Poppins).
- **Don't** use emojis as icons. Use simple geometric symbols or text-based icons.
- **Don't** use marketing buzzwords. Use clear, direct, human language.