# Grok Archive — Complete Transcripts

Source export: `d1147757-bd15-428e-a265-6f1310816d48.zip`
Source file inside: `ttl/30d/export_data/6e14f714-1808-4d85-b363-3eaf83ed51b7/prod-grok-backend.json` (43,084,997 bytes)
SHA-256 of source ZIP: a4e6a48944b186f6202036d4fcd1d27b9f37be198d58579e58fb44b185cd985e

## Verified counts (counted directly from the source JSON, 2026-11-25, corrected)

- Total conversations: 137
- Total real messages (unique message IDs): 12,448
  - human: 6,207
  - assistant (lowercase): 5,863
  - ASSISTANT (uppercase): 378
  - Total Grok replies: 6,241 (5,863 + 378)
- Transcript files: 137, one per conversation, in `transcripts/`
- No placeholders. No abbreviated transcripts. All wording is verbatim from the source export.
- Each transcript preserves: conversation ID, title, created / modified times, message ID, timestamp (UTC, ISO), speaker (Jade/human vs Grok/assistant), model where present, parent response ID, and file attachment IDs.

### Note on the two sender labels

- `assistant` (lowercase, 5,863) and `ASSISTANT` (uppercase, 378) are both Grok.
  They have the same models (grok-3, grok-4), the same thinking-trace / web-search fields,
  and they alternate with human messages in the same way. The uppercase label is used
  for all Grok replies in the earliest conversations, and for a few replies in later ones.
  It is a Grok export format difference, not a third party.
- There are also 51 nodes in the source with no sender, no message, and no message ID —
  only `{"response_id": "..."}`. Every one of those 51 resolves to a real message already
  in the same conversation. They are pointer / branch stubs in Grok's tree, not messages,
  and they are NOT counted in the 12,448 above, and NOT included as empty entries in the transcripts.
  An earlier count of 12,499 mistakenly counted those 51 stubs; that has been corrected.

## Files

- `INDEX.md` — full index, all 137 conversations
- `index.json` — machine-readable manifest with the same counts
- `transcripts/` — 137 complete transcripts
- `README.md` — this file

## Part 1–4 ZIPs — what they are

`part 1.zip`, `part2.zip`, `part3.zip`, and `part4.zip` are NOT separate conversation exports.
They are the file-attachment parts of this same Grok export:

- `part 1.zip`: 110 attachment `content` files
- `part2.zip`: 110 attachment `content` files
- `part3.zip`: 110 attachment `content` files
- `part4.zip`: 102 attachment `content` files, plus 1 profile picture (`pgkIQMUpJrLCoizR-profile-picture.webp`)
- Total attachment content files across parts 1–4: 432

Attachment IDs in the transcripts (e.g. in `file_attachments:` lines) correspond to the folder names inside those part ZIPs. The attachment files themselves are binary/media content and are not embedded in the text transcripts; they remain in the original part ZIPs at the repository root.

## Previous incomplete attempt

A 2026-11-05 attempt left only 5 transcript files in this folder, 2 of them 11-byte placeholders, with an index claiming 137 but listing only 2 rows. That incomplete set has been replaced by this complete extraction.

## Handling note

These files were extracted in a sandbox, as data only. No code from the export was executed.
