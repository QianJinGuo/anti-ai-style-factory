/**
 * Anti-AI Style Factory — Main Application
 * =========================================
 * Orchestrates scorer, filters, virtual scroll, and modal.
 * Entry point: loaded last in index.html.
 */

const App = (() => {
  let _galleryData = null;
  let _currentTab = 'scorer';

  // ── Init ──
  function init() {
    setupFileUpload();
    loadGalleryData();
  }

  // ── Tab switching ──
  function switchTab(tab) {
    _currentTab = tab;

    // Update nav tabs
    document.querySelectorAll('.nav-tab').forEach(t =>
      t.classList.toggle('active', t.dataset.tab === tab));

    // Show/hide panels
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.getElementById(`panel-${tab}`).classList.add('active');

    // Update hash for scorer
    if (tab === 'scorer') {
      window.location.hash = 'scorer';
    }

    // Lazy-init virtual scroll on first gallery visit
    if (tab === 'gallery' && _galleryData && !VirtualScroll._initialized) {
      VirtualScroll.init();
      VirtualScroll._initialized = true;
      Filters.init(_galleryData.styles, _galleryData.filterOptions);
    }
  }

  // ── Scorer ──
  function scoreInput() {
    const html = document.getElementById('html-input').value;
    if (!html.trim()) return;

    const scores = AntiAIScorer.scoreHtml(html);
    renderScoreResult(scores);
  }

  function renderScoreResult(scores) {
    document.getElementById('scorer-empty').style.display = 'none';
    const result = document.getElementById('score-result');
    result.classList.add('visible');

    // Total
    const total = document.getElementById('score-total');
    total.className = 'score-total ' + (scores.pass ? 'pass' : 'fail');
    document.getElementById('score-number').textContent = scores.total;

    const verdict = scores.pass ? '✅ 通过 — 反 AI 味合格' : '❌ 不通过 — AI 味过重';
    document.getElementById('score-verdict').textContent =
      `${verdict} (阈值: ≤ 4)`;

    // Dimension bars
    const barsEl = document.getElementById('dim-bars');
    barsEl.innerHTML = '';

    const dimKeys = ['font_cliche', 'purple_gradient', 'glassmorphism',
                     'uniform_radius', 'emoji_icons', 'placeholder_copy',
                     'heavy_shadow', 'element_density'];

    dimKeys.forEach(key => {
      const val = scores[key];
      const dim = AntiAIScorer.DIMENSIONS[key];
      const row = document.createElement('div');
      row.className = 'dim-row' + (val > 0 ? ' flagged' : '');
      row.title = dim.desc;

      row.innerHTML = `
        <div class="dim-label">${dim.label}</div>
        <div class="dim-bar">
          <div class="dim-bar-fill s${val}"></div>
        </div>
        <div class="dim-value">${val}/2</div>
      `;
      barsEl.appendChild(row);
    });
  }

  // ── File upload ──
  function setupFileUpload() {
    const zone = document.getElementById('upload-zone');
    const input = document.getElementById('file-input');

    zone.addEventListener('click', () => input.click());

    input.addEventListener('change', e => {
      const file = e.target.files[0];
      if (file) readFile(file);
    });

    zone.addEventListener('dragover', e => {
      e.preventDefault();
      zone.classList.add('drag-over');
    });

    zone.addEventListener('dragleave', () => {
      zone.classList.remove('drag-over');
    });

    zone.addEventListener('drop', e => {
      e.preventDefault();
      zone.classList.remove('drag-over');
      const file = e.dataTransfer.files[0];
      if (file) readFile(file);
    });
  }

  function readFile(file) {
    if (!file.name.match(/\.html?$/i)) return;
    const reader = new FileReader();
    reader.onload = e => {
      document.getElementById('html-input').value = e.target.result;
    };
    reader.readAsText(file);
  }

  // ── Gallery data loading ──
  function loadGalleryData() {
    const loading = document.getElementById('gallery-loading');
    fetch('data/styles.json')
      .then(r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(data => {
        _galleryData = data;
        loading.style.display = 'none';

        // Update nav stats
        const stats = data.stats;
        document.getElementById('nav-stats').textContent =
          `${stats.total.toLocaleString()} styles · ${stats.movements} movements`;

        // Check if gallery tab is active via hash
        if (window.location.hash.startsWith('#gallery')) {
          switchTab('gallery');
        }
      })
      .catch(err => {
        loading.textContent = 'Failed to load gallery data. Run: python scripts/build_gallery.py';
        loading.style.color = '#dc2626';
        console.error('Gallery load error:', err);
      });
  }

  // ── Modal ──
  function openModal(item) {
    const overlay = document.getElementById('modal-overlay');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';

    // Title + metadata
    document.getElementById('modal-title').textContent = item.name;
    document.getElementById('modal-id').textContent = item.id;
    document.getElementById('modal-movement').textContent =
      item.movement || '—';
    document.getElementById('modal-medium').textContent =
      item.medium ? Filters.getLabel('medium', item.medium) : '—';
    document.getElementById('modal-palette').textContent =
      item.palette ? Filters.getLabel('palette', item.palette) : '—';
    document.getElementById('modal-status').textContent =
      item.status === 'validated' ? '✅ 已验证' : item.status;

    // Scores in sidebar
    renderModalScores(item.scores);

    // Download links
    document.getElementById('btn-download-html').href =
      `../styles/${item.id}/reference.html`;
    document.getElementById('btn-download-design').href =
      `../styles/${item.id}/DESIGN.md`;

    // Load iframe
    const iframe = document.getElementById('modal-iframe');
    iframe.src = `../styles/${item.id}/reference.html`;
  }

  function closeModal(e) {
    if (e && e.target !== document.getElementById('modal-overlay')) return;

    const overlay = document.getElementById('modal-overlay');
    overlay.classList.remove('open');
    document.body.style.overflow = '';

    // Unload iframe to free resources
    document.getElementById('modal-iframe').src = 'about:blank';
  }

  function renderModalScores(scores) {
    const container = document.getElementById('modal-dim-bars');
    container.innerHTML = '';

    const dimKeys = ['font_cliche', 'purple_gradient', 'glassmorphism',
                     'uniform_radius', 'emoji_icons', 'placeholder_copy',
                     'heavy_shadow', 'element_density'];

    dimKeys.forEach(key => {
      const val = scores ? (scores[key] || 0) : 0;
      const dim = AntiAIScorer.DIMENSIONS[key];
      const row = document.createElement('div');
      row.className = 'dim-row' + (val > 0 ? ' flagged' : '');
      row.title = dim.desc;

      row.innerHTML = `
        <div class="dim-label">${dim.label}</div>
        <div class="dim-bar">
          <div class="dim-bar-fill s${val}"></div>
        </div>
        <div class="dim-value">${val}/2</div>
      `;
      container.appendChild(row);
    });
  }

  // Keyboard: Escape to close modal
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeModal();
  });

  // ── Boot ──
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  return { switchTab, scoreInput, openModal, closeModal };
})();
