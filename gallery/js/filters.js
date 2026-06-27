/**
 * Anti-AI Style Factory — Filter & Search Module
 * ===============================================
 * Multi-dimensional filtering, fuzzy search, URL hash routing.
 */

const Filters = (() => {
  const PALETTE_LABELS = {
    warm:       '暖调',
    cool:       '冷调',
    earth:      '大地',
    neon:       '霓虹',
    monochrome: '单色',
    pastel:     '柔和',
    jewel:      '宝石',
    muted:      '浊色'
  };

  const MEDIUM_LABELS = {
    poster:              '海报',
    'book-cover':        '书籍封面',
    dashboard:           '仪表盘',
    landing:             '着陆页',
    'editorial-spread':  '杂志跨页',
    packaging:           '包装',
    signage:             '导视',
    exhibition:          '展览',
    infographic:         '信息图',
    'card-ui':           '卡片界面',
    'typography-specimen': '字体样张',
    wayfinding:          '寻路',
    'album-art':         '唱片封面',
    stamp:               '邮票',
    banknote:            '纸币',
    map:                 '地图',
    recipe:              '食谱',
    ticket:              '票券',
    catalog:             '目录',
    'annual-report':     '年报'
  };

  let _styles = [];
  let _filtered = [];
  let _options = {};

  // Filter state
  const state = {
    movement: '',
    medium: '',
    palette: '',
    maxScore: 16,
    query: ''
  };

  /** Initialize with data and bind DOM elements */
  function init(styles, filterOptions) {
    _styles = styles;
    _options = filterOptions;

    populateSelect('filter-movement', filterOptions.movements, '全部运动');
    populateSelect('filter-medium', filterOptions.mediums, '全部媒介');
    renderPaletteChips();

    // Bind events
    document.getElementById('filter-movement').addEventListener('change', e => {
      state.movement = e.target.value;
      apply();
    });
    document.getElementById('filter-medium').addEventListener('change', e => {
      state.medium = e.target.value;
      apply();
    });
    document.getElementById('filter-score').addEventListener('input', e => {
      state.maxScore = parseInt(e.target.value);
      document.getElementById('score-range-label').textContent = state.maxScore;
      apply();
    });

    // Search with debounce
    let searchTimer;
    document.getElementById('search-input').addEventListener('input', e => {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        state.query = e.target.value.trim().toLowerCase();
        apply();
      }, 300);
    });

    // Restore from hash
    restoreFromHash();

    // Listen for hash changes
    window.addEventListener('hashchange', restoreFromHash);

    // Initial filter
    apply();
  }

  function populateSelect(id, items, placeholder) {
    const sel = document.getElementById(id);
    sel.innerHTML = `<option value="">${placeholder}</option>` +
      items.map(v => `<option value="${v}">${v}</option>`).join('');
  }

  function renderPaletteChips() {
    const container = document.getElementById('palette-chips');
    const palettes = _options.palettes || [];
    container.innerHTML = palettes.map(p =>
      `<button class="chip${state.palette === p ? ' active' : ''}" data-palette="${p}">${p}</button>`
    ).join('');

    container.addEventListener('click', e => {
      const chip = e.target.closest('.chip');
      if (!chip) return;
      const val = chip.dataset.palette;
      state.palette = state.palette === val ? '' : val;
      // Toggle active
      container.querySelectorAll('.chip').forEach(c =>
        c.classList.toggle('active', c.dataset.palette === state.palette));
      apply();
    });
  }

  function apply() {
    const q = state.query;

    _filtered = _styles.filter(s => {
      if (state.movement && s.movement !== state.movement) return false;
      if (state.medium && s.medium !== state.medium) return false;
      if (state.palette && s.palette !== state.palette) return false;
      if (s.total > state.maxScore) return false;
      if (q) {
        if (!s.name.toLowerCase().includes(q) && !s.id.toLowerCase().includes(q)) return false;
      }
      return true;
    });

    updateHash();
    updateCounts();

    // Trigger virtual scroll re-render
    if (typeof VirtualScroll !== 'undefined') {
      VirtualScroll.setItems(_filtered);
    }
  }

  function updateHash() {
    const params = new URLSearchParams();
    if (state.movement) params.set('movement', state.movement);
    if (state.medium) params.set('medium', state.medium);
    if (state.palette) params.set('palette', state.palette);
    if (state.maxScore < 16) params.set('maxScore', state.maxScore);
    if (state.query) params.set('q', state.query);

    const hash = 'gallery' + (params.toString() ? '?' + params.toString() : '');
    if (window.location.hash !== '#' + hash) {
      window.history.replaceState(null, '', '#' + hash);
    }
  }

  function restoreFromHash() {
    const hash = window.location.hash.slice(1); // remove #
    if (!hash.startsWith('gallery')) return;

    const queryIdx = hash.indexOf('?');
    const params = queryIdx >= 0 ? new URLSearchParams(hash.slice(queryIdx + 1)) : new URLSearchParams();

    state.movement = params.get('movement') || '';
    state.medium   = params.get('medium') || '';
    state.palette  = params.get('palette') || '';
    state.maxScore = parseInt(params.get('maxScore')) || 16;
    state.query    = params.get('q') || '';

    // Sync DOM
    document.getElementById('filter-movement').value = state.movement;
    document.getElementById('filter-medium').value = state.medium;
    document.getElementById('filter-score').value = state.maxScore;
    document.getElementById('score-range-label').textContent = state.maxScore;
    document.getElementById('search-input').value = state.query;

    document.querySelectorAll('#palette-chips .chip').forEach(c =>
      c.classList.toggle('active', c.dataset.palette === state.palette));
  }

  function updateCounts() {
    document.getElementById('filtered-count').textContent = _filtered.length;
    document.getElementById('total-count').textContent = _styles.length;
  }

  function getFiltered() { return _filtered; }

  function getLabel(type, value) {
    if (type === 'palette') return PALETTE_LABELS[value] || value;
    if (type === 'medium') return MEDIUM_LABELS[value] || value;
    return value;
  }

  return { init, getFiltered, getLabel, PALETTE_LABELS, MEDIUM_LABELS };
})();
