/*
 * Neon Coast presentation enhancement.
 * This module only changes presentation and uses original fictional names.
 * It does not copy characters, assets, dialogue, or branding from a third-party game.
 */
(function () {
  'use strict';

  var replacements = {
    'Vice City': 'Neon Coast',
    'VICE CITY': 'NEON COAST',
    'Vice Day': 'Neon Coast day',
    'Vice Local': 'Coast Local',
    'Vice Bank': 'Neon Coast Bank',
    'Vice Payphone': 'Coast Payphone',
    'GTA-6': 'Neon Coast',
    'GTA': 'Neon Coast'
  };

  function rebrandText() {
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    var node;
    while ((node = walker.nextNode())) {
      var text = node.nodeValue;
      var next = text;
      Object.keys(replacements).forEach(function (from) {
        next = next.split(from).join(replacements[from]);
      });
      if (next !== text) node.nodeValue = next;
    }
    document.title = 'Neon Coast — Open-World Sandbox';
    var description = document.querySelector('meta[name="description"]');
    if (description) {
      description.setAttribute('content', 'Neon Coast — an original neon open-world sandbox with enhanced procedural characters.');
    }
  }

  function addPresentationEnhancements() {
    var style = document.createElement('style');
    style.id = 'neon-coast-presentation';
    style.textContent = `
      html, body { -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
      canvas.main {
        filter: saturate(1.03) contrast(1.035) brightness(1.015) !important;
      }
      #neon-coast-character-note {
        position: fixed;
        right: max(12px, env(safe-area-inset-right));
        bottom: max(12px, env(safe-area-inset-bottom));
        z-index: 20;
        padding: 6px 9px;
        border: 1px solid rgba(255,255,255,.14);
        border-radius: 8px;
        background: rgba(8,10,18,.62);
        color: rgba(236,232,240,.82);
        font-size: 9px;
        letter-spacing: .09em;
        pointer-events: none;
        opacity: 0;
        transition: opacity .3s ease;
      }
      @media (max-width: 520px) { #neon-coast-character-note { display: none; } }
    `;
    document.head.appendChild(style);

    var note = document.createElement('div');
    note.id = 'neon-coast-character-note';
    note.textContent = 'ORIGINAL PROCEDURAL CHARACTER SYSTEM';
    document.body.appendChild(note);
    requestAnimationFrame(function () { note.style.opacity = '1'; });
  }

  function observeForGameUI() {
    rebrandText();
    addPresentationEnhancements();
    if ('MutationObserver' in window) {
      var observer = new MutationObserver(function () {
        rebrandText();
      });
      observer.observe(document.documentElement, { childList: true, subtree: true, characterData: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', observeForGameUI, { once: true });
  } else {
    observeForGameUI();
  }
})();
