/**
 * Anti-AI Style Factory — 8-Dimension Scorer (Browser Edition)
 * =============================================================
 * Direct port of src/scorer/eight_dim.py.
 * Scores HTML against the 8-dim AI-taste rubric.
 * Total score 0-16. Target: ≤4 for anti-AI-taste output.
 *
 * This is the "尺子" (ruler) — usable standalone in any browser,
 * no Python, no dependencies.
 */

const CLICHE_FONTS = new Set([
  'Inter', 'Roboto', 'Lato', 'Open Sans', 'Helvetica Neue', 'Poppins'
]);

const PURPLE_GRAD_COLORS = [
  /#667eea/i, /#764ba2/i, /#8b5cf6/i, /#a78bfa/i,
  /rgba?\(\s*102\s*,\s*126\s*,\s*234/i,
  /rgba?\(\s*118\s*,\s*75\s*,\s*162/i
];

const EMOJI_RE = new RegExp(
  '[' +
  '\\uD83C\\uDF00-\\uD83C\\uDFFF' +   // U+1F300-1F9FF
  '\\uD83D\\uDE00-\\uD83D\\uDE4F' +   // U+1F600-1F64F
  '\\uD83D\\uDE80-\\uD83D\\uDEFF' +   // U+1F680-1F6FF
  '\\uD83C\\uE000-\\uD83C\\uE0FF' +   // U+1FA00-1FAFF (approximation)
  '\\u2600-\\u27BF' +                   // U+2600-27BF
  '\\uD83C\\uDC00-\\uD83C\\uDFFF' +   // U+1F300-1F5FF (emoji presentation)
  '\\u2700-\\u27BF' +                   // dingbats
  ']'
);

const MARKETING_STEMS = [
  'futur', 'next-gen', 'next generation', 'empower', 'seamless',
  'cutting-edge', 'revolutionar', 'innovati'
];

/** Dimension metadata for display */
const DIMENSIONS = {
  font_cliche:      { label: 'Font Cliché',     desc: 'Uses AI-default fonts as PRIMARY font (Inter, Roboto, Lato, Open Sans, Helvetica Neue, Poppins)' },
  purple_gradient:   { label: 'Purple Gradient',  desc: 'Contains AI-signature purple-blue gradient colors (#667eea, #764ba2, #8b5cf6, #a78bfa)' },
  glassmorphism:     { label: 'Glassmorphism',    desc: 'Uses backdrop-filter: blur + rgba white background' },
  uniform_radius:    { label: 'Uniform Radius',   desc: 'All elements have the same border-radius (especially 12px or 16px)' },
  emoji_icons:       { label: 'Emoji Icons',      desc: 'Contains emoji characters used as icons' },
  placeholder_copy:  { label: 'Placeholder Copy',  desc: 'Contains marketing language (future, next-gen, empower, seamless, revolutionary, innovative)' },
  heavy_shadow:      { label: 'Heavy Shadow',     desc: 'Uses fluffy colored box-shadows with blur >= 20px AND rgba color' },
  element_density:   { label: 'Element Density',  desc: 'Extremely widget-heavy page (>= 40 HTML tags in one page)' }
};

/**
 * Score an HTML string against the 8-dimension anti-AI rubric.
 * Returns { dim1: 0-2, dim2: 0-2, ..., total: 0-16, pass: bool }
 * @param {string} html - Raw HTML source
 * @param {number} [threshold=4] - Pass threshold for total score
 * @returns {object} Scores object
 */
function scoreHtml(html, threshold = 4) {
  const h = html.toLowerCase();

  // 1. font_cliche — only flag if AI font is the PRIMARY (first) declared font
  const fontMatch = html.match(/font-family\s*[:=]\s*['"]?([^;"'>]+)/i);
  let declared = [];
  if (fontMatch) {
    declared = fontMatch[1].split(',').map(s => s.trim().split(/\s+/)[0].replace(/['"]/g, ''));
  }
  const primaryFont = declared[0] || '';
  const fontClicheScore = CLICHE_FONTS.has(primaryFont) ? 2 : 0;

  // 2. purple_gradient
  const hasPurple = PURPLE_GRAD_COLORS.some(re => re.test(h));
  const purpleGradScore = hasPurple ? 2 : 0;

  // 3. glassmorphism — needs BOTH blur AND rgba white overlay
  const hasBlur = /(?:filter|backdrop-filter)\s*:\s*blur\s*\(\s*([5-9]|[1-9][0-9])/i.test(h);
  const hNoSpace = h.replace(/\s/g, '');
  const hasRgba = ['rgba(255,255,255,0.1', 'rgba(255,255,255,0.2', 'rgba(255,255,255,0.3'].some(s => hNoSpace.includes(s));
  const glassScore = (hasBlur && hasRgba) ? 2 : 0;

  // 4. uniform_radius — flag only when ALL radii identical AND it's AI-typical 12/16px
  const radiiMatches = h.matchAll(/border-radius\s*:\s*(\d+)px/g);
  const radii = [...radiiMatches].map(m => parseInt(m[1])).filter(r => r > 0);
  let radiusScore = 0;
  if (radii.length > 0) {
    const unique = new Set(radii);
    if (unique.size === 1) {
      const val = [...unique][0];
      if (val === 12 || val === 16) radiusScore = 2;
    }
  }

  // 5. emoji_icons
  const emojiCount = (html.match(EMOJI_RE) || []).length;
  const emojiScore = emojiCount >= 5 ? 2 : (emojiCount >= 1 ? 1 : 0);

  // 6. placeholder_copy — check only in visible text, strip style/script
  const visible = html.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
                      .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
  const visibleLower = visible.toLowerCase();
  const copyHits = MARKETING_STEMS.filter(stem => visibleLower.includes(stem)).length;
  const copyScore = copyHits >= 3 ? 2 : (copyHits >= 1 ? 1 : 0);

  // 7. heavy_shadow — fluffy shadows (blur >= 20 AND rgba color)
  const shadowMatches = [...h.matchAll(/box-shadow\s*:\s*([^;}{]+)/g)].map(m => m[1]);
  let fluffyCount = 0;
  for (const sv of shadowMatches) {
    const hasBigBlur = /\b([2-9][0-9]|1[0-9]{2,})px\b/.test(sv);
    const hasRgbaColor = sv.includes('rgba(');
    if (hasBigBlur && hasRgbaColor) fluffyCount++;
  }
  const shadowScore = fluffyCount >= 3 ? 2 : (fluffyCount >= 1 ? 1 : 0);

  // 8. element_density — extremely widget-heavy pages
  const elemCount = (h.match(/<[a-z]+/g) || []).length;
  const densityScore = elemCount >= 40 ? 2 : 0;

  const scores = {
    font_cliche:     fontClicheScore,
    purple_gradient: purpleGradScore,
    glassmorphism:   glassScore,
    uniform_radius:  radiusScore,
    emoji_icons:     emojiScore,
    placeholder_copy: copyScore,
    heavy_shadow:    shadowScore,
    element_density: densityScore
  };
  scores.total = Object.values(scores).reduce((a, b) => a + b, 0);
  scores.pass = scores.total <= threshold;
  return scores;
}

// Export for use as module or global
if (typeof window !== 'undefined') {
  window.AntiAIScorer = { scoreHtml, DIMENSIONS, CLICHE_FONTS, MARKETING_STEMS };
}
if (typeof module !== 'undefined') {
  module.exports = { scoreHtml, DIMENSIONS, CLICHE_FONTS, MARKETING_STEMS };
}
