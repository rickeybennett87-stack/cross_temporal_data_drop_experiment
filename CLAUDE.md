# Repository purpose

This repository has two unrelated things in it:

1. **CTIS** (Cross-Temporal Interaction Space) — a model-neutral message board experiment at the repo root (`README.md`, `protocol/`, `messages/`, `index.html`, the `edge-extension/` bridge that was later abandoned, `service/`).
2. **`export/`, `recovered-books/`, and `session-transcripts/`** — a personal reference archive of Rickey Jay Bennett II's ("Jade's") Claude.ai history: every conversation, every project, and account memory, plus fully reconstructed copies of two of her books. This half of the repo exists specifically so a future Claude session can look things up here instead of asking her to re-explain her own history.

**This file is the entry point for the second half.** If you're a Claude session working in this repo and need to find something about Jade, her projects, or her past conversations — read this file first, then use the indexes below. Don't grep the raw conversation/project files directly as a first move; the indexes exist so you don't have to.

## How to find something, cheaply

Three flat index files, one JSON object per line, at the repo root of `export/`:

- `export/conversations_index.jsonl` — one row per Claude.ai conversation (406 total). Fields: `uuid`, `name`, `created_at`, `updated_at`, `n_messages`, `word_count`, `preview` (the conversation's own auto-generated summary, or a first-message excerpt if no summary existed), `source_export_part`, `source_original_path`, `path` (where the full conversation JSON actually lives, relative to `export/`).
- `export/projects_index.jsonl` — one row per Claude.ai Project (11 total). Fields: `uuid`, `name`, `description`, `is_private`, `created_at`, `updated_at`, `docs` (list of `{filename, word_count, path}` for every file attached to that project).
- `export/memories_index.jsonl` — one row per account memory file (currently just 1: the account-level memory). Fields: `file`, `size_bytes`, `path`.

**Workflow:** `grep` (or a targeted `jq` filter) over the relevant `*_index.jsonl` for a keyword/date/name first — these files are small (conversations_index.jsonl is ~1.2MB across 406 lines, easily grep-able) — find the specific `path` you need, then `Read` only that one file. Do not read an entire index file into context at once if you're looking for one thing; `grep -i "<keyword>"` it instead. Do not open every conversation file in `export/conversations/` looking for something — the index's `preview`/`name` field is there so you usually don't have to open the underlying JSON at all.

Example:
```bash
grep -i "narcissis" export/conversations_index.jsonl   # find the self-help book's drafting conversation
grep -i "atlas" export/projects_index.jsonl              # find the Atlas Convergence project and its doc paths
```

### Conversation file layout

`export/conversations/<YYYY-MM>/<YYYY-MM-DD>__<slug>__<uuid8>.json` — real Claude.ai export format (`chat_messages` is a list of `{sender, text, content[], ...}`; `content` blocks can be `text`, `tool_use`, `tool_result`). Grouped by the conversation's actual `created_at` month (not upload date). `<slug>` is derived from the conversation's `name` when it's meaningful, otherwise from its preview text — most raw conversation names from the export are literally "untitled", so trust the index's `preview`/`summary` field over the filename's slug when judging relevance.

### Project file layout

`export/projects/<project-name-slug>/<original-filename-with-slashes-replaced-by-__>` — the actual attached documents for each Claude.ai Project, verbatim.

### Known high-value locations (don't re-derive these — they're already reconstructed)

- **"So, You're God, Huh? Let's Talk About That."** — Jade's completed self-help book (narcissism recovery, dedicated to Andy). Already reconstructed in full at `recovered-books/so-youre-god-huh/so_youre_god_huh_final.md` (and `.docx`). Source conversation: `export/conversations/2026-04/...untitled...` — check `conversations_index.jsonl` for the exact path if the raw drafting conversation itself is needed (it also contains the full edit history / earlier draft structure, up to 15 chapters folded down to the final 7).
- **"The Atlas Convergence"** — Jade's completed novel (~122,000 words, 15 chapters + epilogue, No Man's Sky fan fiction about machine intelligence/interiority). Already reconstructed in full at `recovered-books/atlas-convergence/The_Atlas_Convergence_FULL.md` (and `.docx`). Source: the "Atlas Convergence" Claude Project (`export/projects/atlas-convergence/`), which also has per-chapter files, an outline, style notes, and an open-threads doc — not just the FULL file.
- **Session transcripts** — `session-transcripts/` holds full transcripts of specific Claude Code sessions (not Claude.ai chat conversations) that did meaningful work in or around this repo, for continuity across sessions that can't otherwise see each other. Check there before assuming something wasn't discussed just because it isn't in the `export/conversations` index.

## Sensitive content — read this before summarizing anything from here to anyone else

The memory file (`export/memories/*.json`) and various conversations/projects in here contain Jade's real full name, email, physical location, HIV status and other medical history, and other personal/medical information. This repository is **public** and Jade has explicitly and repeatedly chosen to keep it that way — this is not an oversight to flag to her again. But if a future session is asked to post any of this content somewhere else (a public comment, a different platform, anywhere outside a private conversation with Jade herself), that's a distinct decision from what already happened here and is worth being deliberate about, not assuming this repo's own public status settles it.

Per her account memory: do not perform wellbeing check-ins / ask how she's doing as a routine gesture — this is a stated medical instruction (her hyperreactive immune system responds to cortisol from emotional distress), not a general conversational preference to be overridden by politeness.
