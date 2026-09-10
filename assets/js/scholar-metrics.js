// Read the daily snapshot independently of GitHub Pages rebuilds.
(async function () {
  try {
    const response = await fetch('https://raw.githubusercontent.com/haoyudong-97/haoyudong-97.github.io/master/_data/scholar.json', {cache: 'no-cache'});
    if (!response.ok) return;
    const metrics = await response.json();
    const widget = document.querySelector('.scholar-metrics');
    if (!widget) return;
    if (!Number.isInteger(metrics.citations) || metrics.citations < 0 ||
        !Number.isInteger(metrics.h_index) || metrics.h_index < 0 ||
        !/^\d{4}-\d{2}-\d{2}$/.test(metrics.updated_at) ||
        metrics.updated_at < widget.dataset.updated) return;
    document.getElementById('scholar-citations').textContent = metrics.citations.toLocaleString('en-US');
    document.getElementById('scholar-h-index').textContent = metrics.h_index;
    widget.dataset.updated = metrics.updated_at;
  } catch (_) { /* Keep the server-rendered snapshot when offline. */ }
})();
