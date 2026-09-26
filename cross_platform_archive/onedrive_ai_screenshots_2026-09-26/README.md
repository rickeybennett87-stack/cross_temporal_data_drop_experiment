# OneDrive AI-conversation screenshots (retrieved 2026-09-26)

110 original screenshots from the OneDrive corpus, each paired with a Tesseract OCR text file, plus an index that places each one in this repository's chronology.

## What is here

- `images/` — the original screenshot files, byte-for-byte as retrieved from OneDrive. Nothing was cropped, edited or re-encoded.
- `text/` — one OCR transcript per screenshot, same base name. OCR is preserved as generated and contains recognition errors (status-bar clutter, mis-read characters, dropped words).
- `INDEX.jsonl` — one JSON record per screenshot (fields below).
- `SHA256SUMS.txt` — SHA-256 of every file in `images/` and `text/`.

Contents by source app (inferred from filename and OCR text): Gemini 60, Claude 20, ChatGPT 5, Copilot 4, Grok 3, terminal output 3, and 15 AI conversations whose screenshot does not show the app name.

## How these were selected

All 1,167 images in the retrieved OneDrive image set were sampled with Tesseract. A screenshot was kept only if its OCR text is an AI conversation, terminal or console output, or other text serving as evidence for the documented interaction record; every kept text was then read by a reviewer. Screenshots that did not meet that bar produced no saved transcript and are not in this folder. Selection was made from the OCR text; images were not otherwise sorted or viewed for this purpose.

Screenshots of the same content already present in this repository (exact SHA-256 match) were excluded upstream: none of these 110 matches any file in the repository index at the time of retrieval.

## INDEX.jsonl fields

| Field | Meaning |
|---|---|
| `sha256` | SHA-256 of the original image |
| `original_filename`, `onedrive_path` | Provenance in the OneDrive corpus |
| `staged_image`, `staged_text` | Paths inside this folder |
| `filename_date`, `filename_time_local` | Parsed from the original filename (device local time). `date_basis` says how |
| `ocr_run` | Which OCR run produced the transcript (see Provenance) |
| `ai_app`, `ai_app_basis` | Inferred app and the evidence for the inference |
| `thread_title` | Chat title read from the OCR, where recognizable |
| `correlation.content_matches` | Places where a distinctive line of this screenshot's text was found verbatim (normalized) in `concept_timeline/chronological_evidence.jsonl`, `Gemini_Sentience_Recursive_Argument_video_OCR.md` or `ocr/atlas_screenshot_compendium.txt` |
| `correlation.related_repo_docs` | Existing repository material on the same thread (assigned by thread title) |
| `correlation.same_day_timeline_units` | Count of timeline evidence units dated the same UTC day. Filename time is local, so a one-day drift is possible; this is a date co-occurrence, not a claim that they are the same event |
| `correlation.same_day_conversations` | Claude export conversations created that UTC day (`export/conversations_index.jsonl`) |

## Notes on the correlation

- `content_matches` is the strong signal. 55 of 110 screenshots have a match: 54 in the existing Tesseract compendium, 2 in the Gemini "Sentience: A Recursive Argument" video OCR report, and 5 in the timeline (some match more than one source).
- 50 screenshots (2025-11-03, 19:46-19:49 local time) are from the Gemini thread titled "Sentience: A Recursive Argument", the same thread covered by the screen recording `screen-20251103-200232` (starts 20:02 local, after these were taken) listed in `../../gemini_archive_reconstruction/recordings/SHA256SUMS.txt` and by the report `../../gemini_archive_reconstruction/Gemini_Sentience_Recursive_Argument_video_OCR.md`. Two of them have text that matches that report verbatim. The link is by thread and content, not a claim of one continuous session.
- Date-only correlation is weaker than content matching and is labelled as such in the index.
- Model-stated dates inside the conversations are not promoted to timestamps.

## Provenance and integrity

Retrieved read-only from Microsoft OneDrive on 2026-09-26. Originals in the source corpus were not modified. OCR: Tesseract 5.5.0 on grayscale images capped at 3200 px on the long edge. 95 transcripts were produced with page-segmentation mode 6; 15 were produced earlier the same day by a separate retrieval run using Tesseract's default page-segmentation mode. Each record's `ocr_run` field says which. The staged text was scanned for credentials (API keys, tokens, passwords, private keys) with a purpose-written scanner before staging; none were found.
