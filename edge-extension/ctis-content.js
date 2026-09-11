(() => {
  if (document.getElementById('ctis-edge-bridge')) return;

  const panel = document.createElement('div');
  panel.id = 'ctis-edge-bridge';
  panel.style.cssText = [
    'position:fixed','right:16px','bottom:16px','z-index:2147483647',
    'width:min(420px,calc(100vw - 32px))','background:#111827','color:#f9fafb',
    'border:1px solid #374151','border-radius:14px','padding:12px','box-shadow:0 18px 40px rgba(0,0,0,.35)',
    'font:14px/1.4 system-ui,-apple-system,Segoe UI,sans-serif'
  ].join(';');

  panel.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px">
      <strong>CTIS Existing-Tab Bridge</strong>
      <span id="ctis-bridge-status" style="font-size:12px;color:#9ca3af">checking…</span>
    </div>
    <textarea id="ctis-bridge-text" placeholder="Send through your already-open model tabs…" style="box-sizing:border-box;width:100%;min-height:92px;resize:vertical;background:#0b1220;color:#f9fafb;border:1px solid #374151;border-radius:10px;padding:9px"></textarea>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">
      <button data-target="chatgpt">Send to ChatGPT</button>
      <button data-target="claude">Send to Claude</button>
      <button data-target="both">Send to Both</button>
    </div>
    <div id="ctis-bridge-result" style="font-size:12px;color:#9ca3af;margin-top:8px"></div>
  `;

  for (const button of panel.querySelectorAll('button')) {
    button.style.cssText = 'border:1px solid #4b5563;background:#1f2937;color:#fff;border-radius:8px;padding:7px 10px;cursor:pointer';
  }

  document.documentElement.appendChild(panel);

  const status = panel.querySelector('#ctis-bridge-status');
  const result = panel.querySelector('#ctis-bridge-result');
  const text = panel.querySelector('#ctis-bridge-text');

  async function refreshStatus() {
    try {
      const res = await chrome.runtime.sendMessage({ type: 'CTIS_STATUS' });
      if (!res?.ok) throw new Error(res?.error || 'status unavailable');
      status.textContent = `ChatGPT ${res.chatgpt ? '●' : '○'}  Claude ${res.claude ? '●' : '○'}`;
    } catch {
      status.textContent = 'bridge unavailable';
    }
  }

  panel.addEventListener('click', async event => {
    const button = event.target.closest('button[data-target]');
    if (!button) return;
    const payload = text.value.trim();
    if (!payload) {
      result.textContent = 'Type a message first.';
      return;
    }
    result.textContent = 'Dispatching through existing tabs…';
    try {
      const res = await chrome.runtime.sendMessage({ type: 'CTIS_DISPATCH', target: button.dataset.target, text: payload });
      const g = res?.chatgpt?.filter(x => x.ok).length || 0;
      const c = res?.claude?.filter(x => x.ok).length || 0;
      result.textContent = `Dispatched. ChatGPT: ${g}, Claude: ${c}. No tabs were opened or navigated.`;
    } catch (error) {
      result.textContent = `Dispatch failed: ${String(error)}`;
    }
    refreshStatus();
  });

  refreshStatus();
  setInterval(refreshStatus, 5000);
})();
