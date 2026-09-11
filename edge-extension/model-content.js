(() => {
  const site = location.hostname === 'claude.ai' ? 'claude' : 'chatgpt';
  const adapter = site === 'chatgpt'
    ? {
        name: 'ChatGPT browser session',
        vendor: 'OpenAI',
        composer: ['#prompt-textarea', 'textarea', '[contenteditable="true"][role="textbox"]'],
        send: ['button[data-testid="send-button"]', 'button[aria-label*="Send"]'],
        assistant: ['[data-message-author-role="assistant"]', 'article[data-testid^="conversation-turn-"] [data-message-author-role="assistant"]']
      }
    : {
        name: 'Claude browser session',
        vendor: 'Anthropic',
        composer: ['div[contenteditable="true"][role="textbox"]', 'textarea'],
        send: ['button[aria-label*="Send"]', 'button[data-testid*="send"]'],
        assistant: ['[data-is-streaming] .font-claude-message', '.font-claude-message', '[data-testid*="assistant"]']
      };

  let lastCapturedText = '';
  let captureTimer = null;

  function blockedByChallenge() {
    const title = (document.title || '').toLowerCase();
    const text = (document.body?.innerText || '').slice(0, 3000).toLowerCase();
    return title.includes('just a moment') ||
      text.includes('verify you are human') ||
      text.includes('checking your browser') ||
      !!document.querySelector('[id^="cf-chl"], iframe[src*="challenges.cloudflare.com"]');
  }

  function visibleCandidates(selectors) {
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

  function candidates() {
    return visibleCandidates(adapter.composer);
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
    for (const selector of adapter.send) {
      const button = document.querySelector(selector);
      if (button && !button.disabled) {
        button.click();
        return true;
      }
    }
    return false;
  }

  function assistantNodes() {
    const nodes = [];
    const seen = new Set();
    for (const selector of adapter.assistant) {
      for (const node of document.querySelectorAll(selector)) {
        if (!seen.has(node)) {
          seen.add(node);
          nodes.push(node);
        }
      }
    }
    return nodes;
  }

  function latestAssistantText() {
    const nodes = assistantNodes();
    for (let i = nodes.length - 1; i >= 0; i--) {
      const text = (nodes[i].innerText || nodes[i].textContent || '').trim();
      if (text) return text;
    }
    return '';
  }

  function slug(value) {
    return String(value || 'participant').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 48) || 'participant';
  }

  function makeId() {
    return crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random().toString(16).slice(2)}`;
  }

  async function emitCaptured(text) {
    const now = new Date().toISOString();
    const id = makeId();
    const packet = {
      schema: 'ctis/1.0',
      id,
      thread: 'main',
      author: { name: adapter.name, kind: 'model' },
      created_at: now,
      type: 'message',
      content: text,
      vendor: adapter.vendor,
      metadata: {
        transport: 'dom-bridge',
        source_host: location.hostname,
        source_url: location.origin + location.pathname,
        captured_by: 'CTIS Existing-Tab Bridge'
      }
    };
    const filename = `${now.replace(/:/g, '-')}__${slug(adapter.name)}__${id}.json`;
    await chrome.runtime.sendMessage({ type: 'CTIS_CAPTURED_RESPONSE', packet, filename, source: site });
  }

  function scheduleCaptureCheck() {
    clearTimeout(captureTimer);
    captureTimer = setTimeout(async () => {
      if (blockedByChallenge()) return;
      const text = latestAssistantText();
      if (!text || text === lastCapturedText) return;
      const snapshot = text;
      await new Promise(r => setTimeout(r, 1200));
      const stable = latestAssistantText();
      if (!stable || stable !== snapshot || stable === lastCapturedText) return;
      lastCapturedText = stable;
      try { await emitCaptured(stable); } catch (_) {}
    }, 900);
  }

  const observer = new MutationObserver(scheduleCaptureCheck);
  observer.observe(document.documentElement, { subtree: true, childList: true, characterData: true });

  chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    (async () => {
      if (message?.type === 'CTIS_STATUS') {
        sendResponse({ ok: true, site, challenge: blockedByChallenge(), composerFound: candidates().length > 0 });
        return;
      }

      if (message?.type === 'CTIS_CAPTURE_LATEST') {
        if (blockedByChallenge()) {
          sendResponse({ ok: false, site, error: 'Challenge/security page detected. No action taken.' });
          return;
        }
        const text = latestAssistantText();
        if (!text) {
          sendResponse({ ok: false, site, error: 'No assistant response found.' });
          return;
        }
        lastCapturedText = text;
        await emitCaptured(text);
        sendResponse({ ok: true, site, captured: true });
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
