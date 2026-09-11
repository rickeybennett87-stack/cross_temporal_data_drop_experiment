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

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  (async () => {
    if (message?.type === 'CTIS_STATUS') {
      const tabs = await existingTabs();
      sendResponse({ ok: true, chatgpt: tabs.chatgpt.length, claude: tabs.claude.length });
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
