---
version: 1.0.0
name: 俄国先锋派 (Russian Avant-Garde)
description: 一种基于构成主义哲学的视觉语言，强调几何刚性、集体功能性与工业美学，拒绝装饰性，主张形式追随生产。
colors:
  primary: '#D32F2F'       # Constructivist Red: 革命、能量、警告
  secondary: '#1A1A1A'     # Industrial Black: 油墨、钢铁、重量
  tertiary: '#F5F5F0'      # Unbleached Paper: 粗糙纸张、新闻载体
  neutral: '#424242'       # Slate Grey: 阴影、混凝土
  muted: '#9E9E9E'         # Faded Ink: 旧报纸、次要信息
typography:
  h1:
    fontFamily: 'Oswald, Impact, sans-serif'
    fontSize: 48px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -1px
  h2:
    fontFamily: 'Oswald, Impact, sans-serif'
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  h3:
    fontFamily: 'Oswald, Impact, sans-serif'
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0px
  body-md:
    fontFamily: 'Roboto Condensed, Arial Narrow, sans-serif'
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption:
    fontFamily: 'Roboto Condensed, Arial Narrow, sans-serif'
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
rounded:
  sm: 0px
  md: 0px
  lg: 0px
spacing:
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    style: 'solid-red-background, black-text, sharp-corners, uppercase, bold'
  card:
    style: 'border-left: 4px solid red, no-shadow, grid-aligned'
  table:
    style: 'borderless, alternating-row-grey, thick-black-header'
---

# 俄国先锋派 (Russian Avant-Garde) Design System

## Overview

本设计系统源自1910-1930年间的俄国先锋派运动，特别是构成主义（Constructivism）和至上主义（Suprematism）。它不是关于“美观”，而是关于“功能”和“传播”。视觉元素被视为工业材料，排版被视为建筑结构。设计必须服务于集体目标，清晰、直接、具有冲击力。拒绝任何无意义的装饰，所有视觉决策必须证明其存在必要性。

## Colors

色彩仅使用三种基本色调，模拟早期印刷技术和工业涂料的限制。

- **Constructivist Red (`#D32F2F`)**: 主色调。象征革命、能量和紧急性。仅用于关键行动点、标题强调和几何分割线。
- **Industrial Black (`#1A1A1A`)**: 文本和主要结构色。模拟油墨印刷效果。
- **Unbleached Paper (`#F5F5F0`)**: 背景色。模拟粗糙的新闻纸或画布，避免纯白的数字冷漠感。
- **Slate Grey (`#424242`)**: 次要文本和边框。
- **Faded Ink (`#9E9E9E`)**: 禁用状态或极度次要的信息。

## Typography

字体选择必须具有几何感、机械感和可读性。严禁使用衬线体（Serif）用于正文，严禁使用圆润字体。

- **Display (H1-H3)**: `Oswald` 或 `Impact`。
  - 特征：高对比度、压缩宽度、极粗字重。
  - 用途：仅用于标题。字号极大，行高极小（0.9-1.0），形成紧凑的块状效果。
- **Body (Body-MD)**: `Roboto Condensed` 或 `Arial Narrow`。
  - 特征：窄体、无装饰、中性。
  - 用途：正文内容。保持高可读性，模拟报纸排版。
- **Caption/UI**: `Roboto Condensed` (Bold/All-Caps)。
  - 特征：全大写、宽字间距（Letter-spacing: 1px）。
  - 用途：标签、按钮、元数据。

**关键规则**:
- 标题不使用常规对齐，可尝试左对齐或右对齐，避免居中（除非是海报式布局）。
- 字体大小对比必须极端。H1 应为 Body 的 3 倍以上。

## Layout

布局基于网格（Grid）和不对称平衡（Asymmetrical Balance）。

- **刚性网格**: 所有内容必须严格对齐到 8px 或 16px 的网格系统。
- **对角线元素**: 允许使用 45 度或 90 度的红色几何色块作为视觉引导，打破水平垂直的单调。
- **留白**: 留白不是“空”，而是“结构空间”。元素之间应有明确的间隔，而非柔和的过渡。
- **摄影蒙太奇**: 图片不应有圆角或阴影，应直接嵌入网格，边缘锐利，可与文字重叠或并置。

## Elevation & Depth

**禁止使用阴影（Drop Shadows）**。深度通过以下方式表现：

1. **图层叠放**: 元素之间通过明确的边界（边框或颜色块）区分层级。
2. **颜色对比**: 红色背景上的黑色文字，或黑色背景上的白色文字。
3. **物理边缘**: 使用 2px-4px 的实线边框，而非模糊的阴影。

## Shapes

- **Border Radius**: **全部为 0px**。所有元素必须是矩形、三角形或圆形（仅限纯几何图标，非拟物）。
- **几何图形**: 大量使用直线、直角、三角形和圆形。这些是构成主义的基本语汇。

## Components

### Button-Primary
- **外观**: 红色实心背景，黑色粗体文字，全大写。
- **样式**: `background: #D32F2F; color: #1A1A1A; border: none; padding: 12px 24px; font-family: 'Oswald'; text-transform: uppercase; letter-spacing: 1px;`
- **交互**: 悬停时无变化或仅轻微变暗，保持工业感。

### Card
- **外观**: 无边框，左侧有 4px 红色竖条作为视觉锚点。
- **结构**: 标题使用 H2，正文使用 Body-MD。图片置于顶部，无圆角。
- **背景**: 白色或浅灰色背景，与页面背景形成微弱对比。

### Table
- **外观**: 无边框表格。
- **表头**: 黑色背景，白色文字，全大写，粗体。
- **行**: 交替行使用极浅的灰色（`#F5F5F0` vs `#FFFFFF`）。
- **分隔**: 仅使用水平细线（1px `#E0E0E0`）分隔行。

### Image
- **样式**: `border-radius: 0; display: block;`
- **处理**: 可应用高对比度滤镜，模拟印刷效果。
- **叠加**: 可在图片上叠加红色几何色块或黑色半透明遮罩，以突出文字。

## Do's and Don'ts

### Do's
- **Do** 使用大胆的几何形状和强烈的色彩对比。
- **Do** 将文字视为图形元素，调整字号和字重以创造视觉节奏。
- **Do** 使用全大写和宽字间距提升可读性和正式感。
- **Do** 保持布局的不对称性和动态平衡。
- **Do** 使用真实的工业材料和纸张纹理作为背景。

### Don'ts
- **Don't** 使用圆角（Border Radius > 0）。
- **Don't** 使用柔和的阴影或渐变背景。
- **Don't** 使用优雅的衬线字体（如 Garamond, Baskerville）。
- **Don't** 使用居中对齐的正文段落（除非是诗歌或宣言）。
- **Don't** 使用过多的颜色（限制在 3-4 种以内）。
- **Don't** 使用装饰性图标（如星星、心形），仅使用几何符号（三角形、圆形、线条）。