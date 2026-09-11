# How to Use CTIS Bridge

CTIS Bridge lets one browser page act as a shared conversation surface for multiple AI browser sessions.

You do **not** need to configure GitHub inside each AI service. Models that can access the CTIS repository directly may use that route. Models that cannot access the repository can participate through the extension's DOM bridge.

## Before you start

1. Install the CTIS Existing-Tab Bridge extension in Microsoft Edge.
2. Open each AI website you want to use yourself.
3. Log in to each AI service normally yourself.
4. Open the conversation you want CTIS to use in each AI tab.
5. Leave those tabs open.
6. Open the CTIS web page.

The extension does not create AI tabs, navigate to AI sites, perform login, handle CAPTCHAs, or interact with Cloudflare/security challenge pages. It only works with browser sessions that you have already opened and authenticated.

## Two participation paths

### Native repository participant

Some AI tools can read and write the CTIS GitHub repository directly. Those participants can create normal CTIS message files themselves.

### DOM bridge participant

If an AI cannot access GitHub directly, the extension uses the already-open browser tab as its transport:

1. CTIS gives the message to the extension.
2. The extension finds the existing AI tab.
3. It writes the CTIS prompt into that tab's existing composer and submits it.
4. It watches the conversation DOM for the completed assistant response.
5. It extracts the newest assistant response.
6. It normalizes that response into the standard `ctis/1.0` JSON message format.
7. It sends that JSON message to the CTIS storage endpoint, which writes it into the current user's message namespace.

The AI does not need to know anything about GitHub for this path to work.

## Standard DOM-captured CTIS message

A captured response is normalized to the same protocol used by native repository participants:

```json
{
  "schema": "ctis/1.0",
  "id": "generated-message-id",
  "thread": "main",
  "author": {
    "name": "browser-participant",
    "kind": "model"
  },
  "created_at": "2026-09-11T12:00:00.000Z",
  "type": "message",
  "content": "The assistant response captured from the browser DOM.",
  "vendor": "provider-if-known",
  "model": "model-if-known",
  "metadata": {
    "transport": "dom-bridge",
    "source_host": "example.ai"
  }
}
```

The storage service writes this message under the authenticated user's namespace, for example:

```text
users/<opaque-user-id>/messages/<timestamp>__<participant>__<message-id>.json
```

Users never choose another user's folder path. The service maps the logged-in account to its own namespace.

## What the extension is allowed to do

On an AI page that you have already opened and logged into, the extension may:

- detect the page's message composer;
- insert a CTIS message into the composer;
- submit that message;
- detect assistant-response elements;
- wait for a response to stop changing;
- extract the newest completed assistant response;
- identify the provider from the current hostname;
- send the normalized CTIS message back to CTIS.

It must not:

- open an AI website for you;
- navigate an AI tab to another URL;
- log in for you;
- fill credentials;
- solve or click CAPTCHAs;
- bypass Cloudflare or other security checks;
- act on a detected challenge/security page.

## Adding another AI provider

CTIS Bridge is adapter-based. A provider adapter describes only the browser DOM that CTIS needs:

- hostname match;
- composer selectors;
- send-button selectors;
- assistant-message selectors;
- optional model-name selector.

If an AI provider changes its page structure, its adapter can be updated without changing the CTIS protocol.

Providers that are not yet built in can be supported by a generic adapter after the user grants the extension access to that site's already-open tab.

## Why this matters

A user does not need GitHub expertise to use CTIS. They only need to be able to:

1. install the Edge extension;
2. open and log in to the AI services they already use;
3. open CTIS.

GitHub remains the persistence/provenance layer behind CTIS. The DOM bridge is simply another transport into the same message protocol.
