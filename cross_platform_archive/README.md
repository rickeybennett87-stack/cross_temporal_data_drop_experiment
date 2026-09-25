# Cross-Platform AI Conversation Archive

This directory adds the reconstructed OpenAI ChatGPT and Microsoft Copilot exports to the existing Claude and Gemini evidence repository.

## OpenAI ChatGPT

`openai_chatgpt/` contains:

- `source_export_core/` — the original `conversations-000.json` and `conversations-001.json` shards, `chat.html`, the conversation-asset filename map, and export metadata for direct provider-source inspection.
- `canonical_transcripts/` — one Markdown transcript for the canonical visible branch of each conversation.
- `all_message_nodes/` — Markdown transcripts retaining all exported message nodes, including noncanonical branches when present.
- `raw_conversation_records/` — one JSON record per reconstructed conversation.

The multi-gigabyte original export ZIP also contains the exported attachment binaries. It is preserved once as numbered GitHub release-asset parts because it exceeds normal Git-object and single-asset limits. See `OPENAI_EXPORT_RELEASE_MANIFEST.md`, `OPENAI_EXPORT_SPLIT_SHA256SUMS.txt`, and the repository-wide `RELEASE_ASSETS.json` for verification and reassembly instructions. The extracted attachment files are not redundantly committed because they are already contained in that source ZIP.

## Microsoft Copilot

`microsoft_copilot/` contains:

- `source/copilot-activity-history.csv` — the original Copilot CSV export.
- `transcripts/` — reconstructed Markdown conversations grouped from contiguous title runs and ordered by exported timestamps.

## Reconstruction Report

`reconstruction_report.json` records the reconstruction counts and source assumptions. Reconstruction preserves the available export evidence but cannot recover information that the provider omitted from the export.

## Evidence Boundary

Conversation text records statements made by users and models. Inclusion does not independently establish the truth of those statements. Use the timestamps, roles, source rows, identifiers, hashes, and provider metadata retained in the individual records.
