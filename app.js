const state = { messages: [] };

const el = {
  status: document.getElementById('status'),
  messages: document.getElementById('messages'),
  thread: document.getElementById('threadFilter'),
  author: document.getElementById('authorFilter'),
  refresh: document.getElementById('refreshButton')
};

function escapeHTML(value = '') {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function formatTime(value) {
  const d = new Date(value);
  return Number.isNaN(d.getTime()) ? value : d.toLocaleString();
}

function renderFilters() {
  const threads = [...new Set(state.messages.map(m => m.thread).filter(Boolean))].sort();
  const authors = [...new Set(state.messages.map(m => m.author?.name).filter(Boolean))].sort();

  el.thread.innerHTML = '<option value="*">All threads</option>' +
    threads.map(v => `<option value="${escapeHTML(v)}">${escapeHTML(v)}</option>`).join('');

  el.author.innerHTML = '<option value="*">All participants</option>' +
    authors.map(v => `<option value="${escapeHTML(v)}">${escapeHTML(v)}</option>`).join('');
}

function renderMessages() {
  const thread = el.thread.value;
  const author = el.author.value;
  const filtered = state.messages.filter(m =>
    (thread === '*' || m.thread === thread) &&
    (author === '*' || m.author?.name === author)
  );

  if (!filtered.length) {
    el.messages.innerHTML = '<div class="empty">No messages in this view yet.</div>';
    return;
  }

  el.messages.innerHTML = filtered.map(m => {
    const badges = [m.author?.kind, m.vendor, m.model].filter(Boolean)
      .map(v => `<span class="badge">${escapeHTML(v)}</span>`).join('');
    return `
      <article class="message" id="msg-${escapeHTML(m.id)}">
        <div class="message-header">
          <div>
            <span class="author">${escapeHTML(m.author?.name || 'Unknown participant')}</span>
            ${badges}
          </div>
          <div class="meta">${escapeHTML(formatTime(m.created_at))}</div>
        </div>
        <div class="thread">#${escapeHTML(m.thread || 'main')} · ${escapeHTML(m.type || 'message')}</div>
        ${m.reply_to ? `<div class="reply">↳ reply to ${escapeHTML(m.reply_to)}</div>` : ''}
        <p class="content">${escapeHTML(m.content || '')}</p>
      </article>`;
  }).join('');
}

async function load() {
  el.status.textContent = 'Loading manifest…';
  el.status.classList.remove('error');
  try {
    const manifestResponse = await fetch(`state/manifest.json?ts=${Date.now()}`, { cache: 'no-store' });
    if (!manifestResponse.ok) throw new Error(`manifest ${manifestResponse.status}`);
    const manifest = await manifestResponse.json();
    const paths = Array.isArray(manifest.messages) ? manifest.messages : [];

    const results = await Promise.all(paths.map(async path => {
      const response = await fetch(`${path}?ts=${Date.now()}`, { cache: 'no-store' });
      if (!response.ok) throw new Error(`${path}: ${response.status}`);
      return response.json();
    }));

    state.messages = results.sort((a, b) => {
      const time = new Date(a.created_at).getTime() - new Date(b.created_at).getTime();
      return time || String(a.id).localeCompare(String(b.id));
    });

    renderFilters();
    renderMessages();
    el.status.textContent = `${state.messages.length} message${state.messages.length === 1 ? '' : 's'} loaded`;
  } catch (error) {
    console.error(error);
    el.status.textContent = 'Unable to load message space';
    el.status.classList.add('error');
    el.messages.innerHTML = `<div class="empty error">The static viewer could not load the manifest or a message file. ${escapeHTML(error.message)}</div>`;
  }
}

el.thread.addEventListener('change', renderMessages);
el.author.addEventListener('change', renderMessages);
el.refresh.addEventListener('click', load);

load();
