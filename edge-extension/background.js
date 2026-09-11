const CHATGPT_PATTERN = 'https://chatgpt.com/*';
const CLAUDE_PATTERN = 'https://claude.ai/*';

async function existingTabs() {
  const [chatgpt, claude] = await Promise.all([
    chrome.tabs.query({ url: CHATGPT_PATTERN }),
    chrome.tabs.query({ url: CLAUDE_PATTERN })
  ]);
  return { chatgpt, claude };
}

async function relay(tabs, message) {
  const out = [];
  for (const tab of tabs) {
    if (!tab.id) continue;
    try {
      const response = await chrome.tabs.sendMessage(tab.id, message);
      out.push({ tabId: tab.id, ok: !!response?.ok, response });
    } catch (error) {
      out.push({ tabId: tab.id, ok: false, error: String(error) });
    }
  }
  return out;
}

async function getBridgeConfig() {
  return chrome.storage.local.get({
    ctisApiBase: '',
    ctisSessionToken: ''
  });
}

async function storeCapturedPacket(message) {
  const { ctisApiBase, ctisSessionToken } = await getBridgeConfig();
  const packet = message?.packet;
  const filename = message?.filename;

  if (!packet || packet.schema !== 'ctis/1.0' || !filename) {
    return { ok: false, error: 'Invalid CTIS capture packet.' };
  }

  if (!ctisApiBase) {
    const pending = await chrome.storage.local.get({ ctisPendingPackets: [] });
    pending.ctisPendingPackets.push({ packet, filename, capturedAt: new Date().toISOString() });
    await chrome.storage.local.set({ ctisPendingPackets: pending.ctisPendingPackets.slice(-500) });
    return { ok: false, queued: true, error: 'CTIS storage API is not configured; packet queued locally.' };
  }

  const endpoint = `${ctisApiBase.replace(/\/$/, '')}/v1/messages`;
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(ctisSessionToken ? { Authorization: `Bearer ${ctisSessionToken}` } : {})
    },
    body: JSON.stringify({ filename, message: packet })
  });

  if (!response.ok) {
    const text = await response.text().catch(() => '');
    throw new Error(`CTIS storage returned ${response.status}: ${text.slice(0, 300)}`);
  }
  return { ok: true, stored: true, result: await response.json().catch(() => ({})) };
}

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  (async () => {
    if (message?.type === 'CTIS_STATUS') {
      const tabs = await existingTabs();
      const config = await getBridgeConfig();
      const pending = await chrome.storage.local.get({ ctisPendingPackets: [] });
      sendResponse({
        ok: true,
        chatgpt: tabs.chatgpt.length,
        claude: tabs.claude.length,
        storageConfigured: !!config.ctisApiBase,
        pendingPackets: pending.ctisPendingPackets.length
      });
      return;
    }

    if (message?.type === 'CTIS_CAPTURED_RESPONSE') {
      sendResponse(await storeCapturedPacket(message));
      return;
    }

    if (message?.type === 'CTIS_CONFIGURE_STORAGE') {
      await chrome.storage.local.set({
        ctisApiBase: String(message.ctisApiBase || '').trim(),
        ctisSessionToken: String(message.ctisSessionToken || '').trim()
      });
      sendResponse({ ok: true });
      return;
    }

    if (message?.type !== 'CTIS_DISPATCH') return;

    const text = typeof message.text === 'string' ? message.text.trim() : '';
    if (!text) {
      sendResponse({ ok: false, error: 'Message is empty.' });
      return;
    }

    const target = ['chatgpt', 'claude', 'both'].includes(message.target)
      ? message.target
      : 'both';
    const tabs = await existingTabs();

    const result = { ok: true, chatgpt: [], claude: [] };
    if (target === 'chatgpt' || target === 'both') {
      result.chatgpt = await relay(tabs.chatgpt, { type: 'CTIS_COMPOSE_AND_SEND', text });
    }
    if (target === 'claude' || target === 'both') {
      result.claude = await relay(tabs.claude, { type: 'CTIS_COMPOSE_AND_SEND', text });
    }

    sendResponse(result);
  })().catch(error => sendResponse({ ok: false, error: String(error) }));
  return true;
});
