---
version: 1.0.0
name: Dutch Golden Age
description: A design system rooted in 17th-century Dutch realism, emphasizing chiaroscuro lighting, rich material textures, and a restrained, scholarly elegance that prioritizes substance over ornamentation.
colors:
  primary:
    name: Ochre Deep
    hex: '#8A6D3B'
    description: A deep, earthy yellow-brown inspired by aged parchment and raw ochre pigments.
  secondary:
    name: Vermeer Blue
    hex: '#2C3E50'
    description: A dark, muted ultramarine reminiscent of Delftware and heavy woolen fabrics.
  tertiary:
    name: Burnt Umber
    hex: '#5C4033'
    description: Rich, warm brown used for structural elements and deep shadows.
  neutral:
    name: Linen White
    hex: '#F4F1EA'
    description: A warm, off-white background color simulating unbleached canvas or aged paper.
  muted:
    name: Slate Shadow
    hex: '#3A3A3A'
    description: Near-black used for text and primary contrast, softer than pure black to mimic ink on paper.
typography:
  h1:
    fontFamily: 'Playfair Display'
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
  h2:
    fontFamily: 'Playfair Display'
    fontSize: 1.875rem
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  h3:
    fontFamily: 'Playfair Display'
    fontSize: 1.5rem
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: 'Lora'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: 'Lora'
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
    fontStyle: italic
rounded:
  sm: 2px
  md: 4px
  lg: 0px
spacing:
  sm: 0.5rem
  md: 1rem
  lg: 2rem
  xl: 4rem
components:
  button-primary:
    background: '#2C3E50'
    color: '#F4F1EA'
    border: 1px solid '#1A252F'
    padding: 0.75rem 1.5rem
    borderRadius: 2px
    fontFamily: 'Playfair Display'
    fontWeight: 600
    fontSize: 1rem
    letterSpacing: 0.05em
    textTransform: uppercase
    transition: background-color 0.2s ease
    hover:
      background: '#1A252F'
  card:
    background: '#FFFFFF'
    border: 1px solid '#D3CFC4'
    borderRadius: 0px
    padding: 1.5rem
    boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
    fontFamily: 'Lora'
  table:
    fontFamily: 'Lora'
    fontSize: 0.95rem
    borderColor: '#D3CFC4'
    headerBackground: '#F4F1EA'
    headerColor: '#2C3E50'
    rowStriping: true
    rowStripingColor: '#FAF8F3'