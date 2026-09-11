import http from 'node:http';
import crypto from 'node:crypto';

const PORT = Number(process.env.PORT || 8787);
const REPO = process.env.CTIS_REPO || 'rickeybennett87-stack/cross_temporal_data_drop_experiment';
const BRANCH = process.env.CTIS_BRANCH || 'main';
const GITHUB_TOKEN = process.env.GITHUB_TOKEN || '';
const USER_TOKENS = parseUserTokens(process.env.CTIS_USER_TOKENS_JSON || '{}');

function parseUserTokens(raw) {
  try {
    const parsed = JSON.parse(raw);
    return parsed && typeof parsed === 'object' ? parsed : {};
  } catch {
    return {};
  }
}

function json(res, status, body) {
  const payload = JSON.stringify(body);
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'access-control-allow-origin': '*',
    'access-control-allow-headers': 'authorization, content-type',
    'access-control-allow-methods': 'POST, OPTIONS'
  });
  res.end(payload);
}

function safeSegment(value) {
  return String(value || '').replace(/[^a-zA-Z0-9._-]/g, '').slice(0, 120);
}

function identifyUser(req) {
  const auth = req.headers.authorization || '';
  const match = auth.match(/^Bearer\s+(.+)$/i);
  if (!match) return null;
  const token = match[1].trim();
  for (const [userId, expected] of Object.entries(USER_TOKENS)) {
    const a = Buffer.from(token);
    const b = Buffer.from(String(expected));
    if (a.length === b.length && crypto.timingSafeEqual(a, b)) return safeSegment(userId);
  }
  return null;
}

async function readBody(req) {
  const chunks = [];
  let total = 0;
  for await (const chunk of req) {
    total += chunk.length;
    if (total > 1_000_000) throw new Error('request too large');
    chunks.push(chunk);
  }
  return JSON.parse(Buffer.concat(chunks).toString('utf8'));
}

function validateMessage(body) {
  if (!body || typeof body !== 'object') throw new Error('invalid body');
  const filename = safeSegment(body.filename);
  const message = body.message;
  if (!filename.endsWith('.json')) throw new Error('invalid filename');
  if (!message || message.schema !== 'ctis/1.0') throw new Error('invalid CTIS schema');
  if (typeof message.id !== 'string' || !message.id) throw new Error('message id required');
  if (typeof message.created_at !== 'string' || Number.isNaN(Date.parse(message.created_at))) throw new Error('valid created_at required');
  if (!message.author || typeof message.author.name !== 'string') throw new Error('author required');
  if (typeof message.content !== 'string') throw new Error('content required');
  return { filename, message };
}

async function writeToGitHub(userId, filename, message) {
  if (!GITHUB_TOKEN) throw new Error('GITHUB_TOKEN is not configured');
  const path = `users/${userId}/messages/${filename}`;
  const url = `https://api.github.com/repos/${REPO}/contents/${encodeURIComponent(path).replaceAll('%2F', '/')}`;
  const response = await fetch(url, {
    method: 'PUT',
    headers: {
      authorization: `Bearer ${GITHUB_TOKEN}`,
      accept: 'application/vnd.github+json',
      'x-github-api-version': '2022-11-28',
      'content-type': 'application/json',
      'user-agent': 'ctis-repo-writer/1.0'
    },
    body: JSON.stringify({
      message: `Store CTIS message for ${userId}`,
      branch: BRANCH,
      content: Buffer.from(JSON.stringify(message, null, 2) + '\n').toString('base64')
    })
  });
  const result = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(`GitHub ${response.status}: ${JSON.stringify(result).slice(0, 500)}`);
  return { path, commit: result.commit?.sha || null };
}

const server = http.createServer(async (req, res) => {
  if (req.method === 'OPTIONS') return json(res, 204, {});
  if (req.method !== 'POST' || req.url !== '/v1/messages') return json(res, 404, { error: 'not found' });

  const userId = identifyUser(req);
  if (!userId) return json(res, 401, { error: 'unauthorized' });

  try {
    const body = await readBody(req);
    const { filename, message } = validateMessage(body);
    const stored = await writeToGitHub(userId, filename, message);
    return json(res, 201, { ok: true, user_id: userId, ...stored });
  } catch (error) {
    return json(res, 400, { ok: false, error: String(error?.message || error) });
  }
});

server.listen(PORT, () => {
  console.log(`CTIS repo writer listening on :${PORT}`);
});
