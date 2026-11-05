# Grok (xAI) Conversation Archive

Complete extraction and indexing of the Grok conversation export that was previously packed inside the UUID-named zip at the repository root.

## Contents

- `INDEX.md` — human-readable index of all 137 conversations
- `index.json` — machine-readable index
- `transcripts/` — one Markdown file per conversation (chronological human/assistant turns, timestamps, conversation IDs)
- `raw/` — original export files
  - `prod-grok-backend.json` (42 MB source containing the full conversation data, projects, and media posts)
  - `prod-mc-auth-mgmt-api.json`
  - `prod-mc-billing.json`

## Provenance

Extracted from `d1147757-bd15-428e-a265-6f1310816d48.zip`  
→ `ttl/30d/export_data/6e14f714-1808-4d85-b363-3eaf83ed51b7/prod-grok-backend.json`

This section makes the Grok-specific history as discoverable and searchable as the Claude, ChatGPT, Gemini, and Copilot archives already present in the repository.

## Notes

- All conversation transcripts are complete (no placeholders).
- Projects and media-post metadata are preserved in the raw JSON.
- The asset-server directory in the original zip was empty.
