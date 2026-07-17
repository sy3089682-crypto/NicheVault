/**
 * NicheVault Lightweight Analytics
 * Privacy-friendly, cookie-free, localStorage-based event tracking.
 * Swap for Plausible/Cloudflare/GA4 when ready.
 */
(function() {
  'use strict';

  const STORAGE_KEY = 'nv_analytics_events';
  const MAX_EVENTS = 2000;

  function now() { return new Date().toISOString(); }

  function getEvents() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); }
    catch (e) { return []; }
  }

  function saveEvent(event) {
    const events = getEvents();
    events.push(Object.assign({ t: now(), url: location.href, ref: document.referrer || '' }, event));
    if (events.length > MAX_EVENTS) events.splice(0, events.length - MAX_EVENTS);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(events));
  }

  // Auto-track page view
  saveEvent({ type: 'pageview', page: location.pathname });

  // Track CTA clicks
  document.addEventListener('click', function(e) {
    const el = e.target.closest('a, button');
    if (!el) return;
    const text = (el.textContent || el.value || '').trim().slice(0, 50);
    const href = el.getAttribute('href') || '';
    if (text || href) {
      saveEvent({ type: 'click', text, href, tag: el.tagName.toLowerCase() });
    }
  });

  // Track form submissions
  document.addEventListener('submit', function(e) {
    const form = e.target;
    const id = form.id || form.action || '';
    saveEvent({ type: 'form_submit', form_id: id });
  });

  // Expose API
  window.NicheVaultAnalytics = {
    track: function(name, props) { saveEvent(Object.assign({ type: 'custom', name }, props)); },
    getEvents: getEvents,
    getSummary: function() {
      const ev = getEvents();
      const views = ev.filter(e => e.type === 'pageview');
      const clicks = ev.filter(e => e.type === 'click');
      const forms = ev.filter(e => e.type === 'form_submit');
      const pageCounts = {};
      views.forEach(v => { pageCounts[v.page] = (pageCounts[v.page] || 0) + 1; });
      return { total: ev.length, views: views.length, clicks: clicks.length, forms: forms.length, pages: pageCounts };
    },
    exportCSV: function() {
      const ev = getEvents();
      const rows = ev.map(e => JSON.stringify(e));
      const blob = new Blob([rows.join('\n')], { type: 'text/csv' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'nichevault-analytics-' + new Date().toISOString().slice(0,10) + '.jsonl';
      a.click();
    },
    clear: function() { localStorage.removeItem(STORAGE_KEY); }
  };
})();
