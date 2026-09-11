(() => {
  const site = location.hostname === 'claude.ai' ? 'claude' : 'chatgpt';

  function blockedByChallenge() {
    const title = (document.title || '').toLowerCase();
    const text = (document.body?.innerText || '').slice(0, 3000).toLowerCase();
    return title.includes('just a moment') ||
      text.includes('verify you are human') ||
      text.includes('checking your browser') ||
      !!document.querySelector('[id^="cf-chl"], iframe[src*="challenges.cloudflare.com"]');
  }

  function candidates() {
    const selectors = site === 'chatgpt'
      ? ['#prompt-textarea', 'textarea', '[contenteditable="true"][role="textbox"]']
      : ['div[contenteditable="true"][role="textbox"]', 'textarea'];
    const found = [];
    const seen = new Set();
    for (const selector of selectors) {
      for (const node of document.querySelectorAll(selector)) {
        if (seen.has(node)) continue;
        const rect = node.getBoundingClientRect();
        const style = getComputedStyle(node);
        if (rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' && style.display !== 'none' && !node.disabled) {
          seen.add(node);
          found.push(node);
        }
      }
    }
    return found;
  }

  function fill(el, text) {
    el.focus();
    if (el instanceof HTMLTextAreaElement || el instanceof HTMLInputElement) {
      const proto = Object.getPrototypeOf(el);
      const desc = Object.getOwnPropertyDescriptor(proto, 'value');
      if (desc?.set) desc.set.call(el, text); else el.value = text;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
      return;
    }

    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(el);
    selection.removeAllRanges();
    selection.addRange(range);
    document.execCommand('insertText', false, text);
    el.dispatchEvent(new InputEvent('input', { bubbles: true, inputType: 'insertText', data: text }));
  }

  async function submit() {
    await new Promise(r => setTimeout(r, 120));
    const selectors = site === 'chatgpt'
      ? ['button[data-testid="send-button"]', 'button[aria-label*="Send"]']
      : ['button[aria-label*="Send"]', 'button[data-testid*="send"]'];
    for (const selector of selectors) {
      const button = document.querySelector(selector);
      if (button && !button.disabled) {
        button.click();
        return true;
      }
    }
    return false;
  }

  chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    (async () => {
      if (message?.type === 'CTIS_STATUS') {
        sendResponse({ ok: true, site, challenge: blockedByChallenge(), composerFound: candidates().length > 0 });
        return;
      }

      if (message?.type !== 'CTIS_COMPOSE_AND_SEND') return;
      if (blockedByChallenge()) {
        sendResponse({ ok: false, site, error: 'Challenge/security page detected. No action taken.' });
        return;
      }
      if (typeof message.text !== 'string' || !message.text.trim()) {
        sendResponse({ ok: false, site, error: 'No text supplied.' });
        return;
      }

      const composer = candidates()[0];
      if (!composer) {
        sendResponse({ ok: false, site, error: 'No active composer found. Open the chat yourself first.' });
        return;
      }

      fill(composer, message.text.trim());
      const sent = await submit();
      sendResponse({ ok: sent, site, filled: true, sent, error: sent ? null : 'Composer filled, but no enabled send button was found.' });
    })().catch(error => sendResponse({ ok: false, site, error: String(error) }));
    return true;
  });
})();
