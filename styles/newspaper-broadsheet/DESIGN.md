---
version: 1.0.0
name: 报纸大报 (The Broadsheet)
description: A rigorous, high-density information architecture rooted in the tradition of print journalism, prioritizing legibility, structural hierarchy, and the tactile authority of lead type over digital decoration.
colors:
  primary:
    name: "Ink Black"
    hex: "#111111"
    usage: "Headings, primary body text, critical data points. Represents the permanence of printed ink."
  secondary:
    name: "Newsprint Grey"
    hex: "#4a4a4a"
    usage: "Secondary text, captions, metadata. Reduces visual weight of non-critical information."
  tertiary:
    name: "Subtle Accent"
    hex: "#8c1d1d"
    usage: "Links, active states, critical alerts. Historically derived from the red ink used in early broadsheets for emphasis."
  neutral:
    name: "Paper White"
    hex: "#f8f7f4"
    usage: "Backgrounds. Simulates unbleached newsprint; avoids the sterility of pure #FFFFFF."
  muted:
    name: "Column Divider"
    hex: "#d4d0c8"
    usage: "Borders, rules, separators. Faint enough to guide the eye without interrupting the flow."
typography:
  h1:
    fontFamily: "Playfair Display"
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
    description: "Display serif. High contrast. Used for main headlines to command attention."
  h2:
    fontFamily: "Playfair Display"
    fontSize: "1.75rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
    description: "Section headers. Maintains serif authority but reduces size for hierarchy."
  h3:
    fontFamily: "Playfair Display"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0em"
    description: "Sub-section titles. Often styled as 'drop caps' or small caps in print."
  body-md:
    fontFamily: "Source Serif 4"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0.01em"
    description: "The workhorse font. Optimized for long-form reading at small sizes. High x-height for legibility."
  caption:
    fontFamily: "IBM Plex Mono"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.05em"
    description: "Monospaced. Used for datelines, timestamps, and technical metadata. Evokes the typewriter/telegraph aesthetic."
rounded:
  sm: "0px"
  md: "0px"
  lg: "0px"
  description: "Newspapers do not have rounded corners. Rectangular precision conveys seriousness and order."
spacing:
  sm: "4px"
  md: "8px"
  lg: "16px"
  xl: "32px"
  description: "Tight, grid-based spacing. Margins are generous, but internal component spacing is compact to maximize information density."
components:
  button-primary:
    style: "Solid background (Ink Black), white text, sharp corners, 1px solid border (Ink Black)."
    hover: "Background shifts to Newsprint Grey, text remains Ink Black."
    description: "No shadows, no gradients. Pure functional contrast."
  card:
    style: "No border, separated by 1px vertical rule or horizontal rule. Background is same as page."
    description: "Cards are not 'cards'; they are distinct articles or data blocks defined by whitespace and rules, not elevation."
  table:
    style: "Collapse borders. Header background: Ink Black, text: Paper White. Rows alternate with subtle grey tint. No vertical borders except between columns if necessary."
    description: "Tabular data is presented with grid precision. Readability is paramount."
  nav:
    style: "Horizontal list separated by vertical rules (|). No icons. Text only."
    description: "Navigation mimics the masthead or table of contents."
---

# 报纸大报 (The Broadsheet) Design Specification

## Overview
The **Broadsheet** design style rejects the soft, rounded, and decorative tendencies of modern UI trends. It is built on the philosophy that **content is king, and structure is queen**. Inspired by the physical constraints of paper printing and the cognitive load of reading dense text, this system prioritizes:

1.  **Information Density:** Maximizing the amount of useful information per square inch without sacrificing legibility.
2.  **Structural Clarity:** Using lines, columns, and typographic hierarchy to guide the eye logically.
3.  **Tactile Authority:** Using serif fonts and stark contrasts to evoke trust, permanence, and journalistic integrity.

This style is suitable for news aggregators, financial data dashboards, academic repositories, and long-form editorial platforms.

## Colors
The palette is derived from the limitations of ink and paper. It is low-saturation and high-contrast.

| Role | Color | Hex | Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | Ink Black | `#111111` | Headlines, body text, primary buttons. |
| **Secondary** | Newsprint Grey | `#4a4a4a` | Captions, secondary text, disabled states. |
| **Tertiary** | Subtle Accent | `#8c1d1d` | Links, active states, critical alerts. |
| **Neutral** | Paper White | `#f8f7f4` | Page background. Warm off-white to reduce eye strain. |
| **Muted** | Column Divider | `#d4d0c8` | Borders, rules, separators. |

**Principle:** Never use color to decorate. Use color only to distinguish state (link vs. visited) or hierarchy (headline vs. body).

## Typography
Typography is the primary visual element. We avoid sans-serif fonts for body text to maintain the "print" aesthetic and improve long-form readability.

### Font Families
*   **Headings:** `Playfair Display` (or similar high-contrast Didone serif).
*   **Body:** `Source Serif 4` (or similar transitional serif with high x-height).
*   **Meta/Data:** `IBM Plex Mono` (or similar monospaced font).

### Type Scale
*   **H1 (2.5rem):** Tight tracking. The main headline.
*   **H2 (1.75rem):** Section breaks.
*   **Body (1rem):** 1.55 line height. This is critical. Tighter line heights cause eye fatigue in dense text.
*   **Caption (0.75rem):** Monospaced. Used for dates, times, and tags.

**Principle:** Text should look like it was typeset on a printing press, not rendered by a browser default.

## Layout
The layout is based on the **multi-column grid**.

1.  **Columns:** Use a 2, 3, or 4-column grid for body content. Single-column layouts are reserved for hero sections or full-page articles.
2.  **Rules:** Use horizontal (`<hr>`) and vertical (`border-left/right`) rules to separate content. These are not decorative; they are structural.
3.  **Whitespace:** Margins (external whitespace) are generous. Padding (internal whitespace) is tight. This creates a "block" feel.
4.  **Alignment:** Left-aligned text. Justified text is discouraged as it creates uneven spacing (rivers) in digital rendering.

## Elevation & Depth
**Zero Elevation.**

*   No box-shadows.
*   No gradients.
*   No floating elements.

Depth is created solely through **typographic hierarchy** (size, weight, color) and **spatial proximity**. If something is important, it is larger and darker. If it is secondary, it is smaller and grey.

## Shapes
*   **Corners:** All corners are **0px radius**. Sharp corners convey precision and seriousness.
*   **Borders:** 1px solid lines are the primary structural element.

## Components

### Button (Primary)
*   **Shape:** Sharp rectangle.
*   **Style:** Solid Ink Black background, white text.
*   **Border:** 1px solid Ink Black.
*   **Hover:** Background becomes Newsprint Grey, text becomes Ink Black.
*   **No icons.** Text-only labels.

### Card (Article Block)
*   **Structure:** Not a box with a shadow. It is a block of text separated by rules.
*   **Visuals:**