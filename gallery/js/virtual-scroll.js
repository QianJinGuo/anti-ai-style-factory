/**
 * Anti-AI Style Factory — Virtual Scroll Engine
 * =============================================
 * Renders only visible cards to handle 15K+ items without DOM bloat.
 *
 * Layout: CSS Grid with fixed-height rows (each card ~148px including gap).
 * Uses padding spacers to simulate total height, only mounting ~30 cards
 * in the viewport at any time.
 */

const VirtualScroll = (() => {
  const ITEM_HEIGHT = 164; // card height (132px) + gap (16px) + card border (2px) ≈ 148, use 164 for safety
  const BUFFER = 5;          // extra rows above/below viewport

  let _items = [];
  let _container, _content, _spacerTop, _spacerBottom;
  let _rafId = null;

  function init() {
    _container = document.getElementById('vscroll-container');
    _content = document.getElementById('vscroll-content');
    _spacerTop = document.getElementById('vscroll-spacer-top');
    _spacerBottom = document.getElementById('vscroll-spacer-bottom');

    // Use passive scroll listener for performance
    _container.addEventListener('scroll', onScroll, { passive: true });
  }

  function setItems(items) {
    _items = items;
    const totalHeight = items.length * ITEM_HEIGHT;

    _spacerTop.style.height = '0px';
    _spacerBottom.style.height = totalHeight + 'px';
    _content.style.transform = 'translateY(0px)';

    if (items.length === 0) {
      _content.innerHTML = '';
      // Show/hide empty state
      const empty = document.getElementById('gallery-empty');
      if (empty) empty.style.display = 'block';
    } else {
      const empty = document.getElementById('gallery-empty');
      if (empty) empty.style.display = 'none';
    }

    render();
  }

  function onScroll() {
    if (_rafId) return;
    _rafId = requestAnimationFrame(() => {
      _rafId = null;
      render();
    });
  }

  function render() {
    if (_items.length === 0) return;

    const scrollTop = _container.scrollTop;
    const viewportHeight = _container.clientHeight;

    const startIdx = Math.max(0, Math.floor(scrollTop / ITEM_HEIGHT) - BUFFER);
    const endIdx = Math.min(_items.length,
      Math.ceil((scrollTop + viewportHeight) / ITEM_HEIGHT) + BUFFER);

    // Position content
    const offsetY = startIdx * ITEM_HEIGHT;
    _spacerTop.style.height = offsetY + 'px';
    _spacerBottom.style.height = ((_items.length - endIdx) * ITEM_HEIGHT) + 'px';
    _content.style.transform = `translateY(${offsetY}px)`;

    // Render cards
    const fragment = document.createDocumentFragment();
    for (let i = startIdx; i < endIdx; i++) {
      fragment.appendChild(createCard(_items[i]));
    }

    // Batch DOM update
    _content.innerHTML = '';
    _content.appendChild(fragment);
  }

  function createCard(item) {
    const card = document.createElement('div');
    card.className = 'style-card';
    card.dataset.id = item.id;
    card.onclick = () => App.openModal(item);

    // Color strip
    const colors = item.colors || {};
    const colorKeys = ['primary', 'secondary', 'tertiary', 'neutral', 'background'];
    const validColors = colorKeys.filter(k => colors[k]).map(k => colors[k]);

    let colorStripHtml = '';
    if (validColors.length > 0) {
      colorStripHtml = '<div class="color-strip">' +
        validColors.map(c => `<div style="background:${c}"></div>`).join('') +
        '</div>';
    }

    // Score badge class
    const score = item.total;
    let scoreClass = 's0';
    if (score >= 5) scoreClass = 's5p';
    else if (score >= 3) scoreClass = 's34';
    else if (score >= 2) scoreClass = 's2';
    else if (score >= 1) scoreClass = 's1';

    // Tags
    const tags = [];
    if (item.movement) tags.push(item.movement);
    if (item.medium) tags.push(item.medium);
    if (item.palette) tags.push(item.palette);

    card.innerHTML = `
      ${colorStripHtml}
      <div class="card-body">
        <div class="card-name" title="${escapeAttr(item.name)}">${escapeHtml(item.name)}</div>
        <div class="card-id" title="${escapeAttr(item.id)}">${escapeHtml(item.id)}</div>
        <div class="card-tags">
          ${tags.map(t => `<span class="card-tag">${escapeHtml(t)}</span>`).join('')}
        </div>
        <span class="card-score ${scoreClass}">${score}</span>
      </div>
    `;

    return card;
  }

  function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function escapeAttr(s) {
    return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
  }

  return { init, setItems };
})();
