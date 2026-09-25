# Gemini archive reconstruction

This folder collects preserved evidence of Gemini conversations from the local archive. Originals were not modified.

## Included in Git

- `Gemini_Sentience_Recursive_Argument_video_OCR.md` — existing timestamped OCR evidence report for `screen-20251103-200232 (1).mp4`.
- `ocr/atlas_screenshot_compendium.txt` — Tesseract OCR transcript covering 187 screenshots, including a labeled Gemini section containing 115 screenshots. The OCR is preserved as generated and may contain recognition errors.
- `saved_html/` — three saved Gemini conversation pages, preserved byte-for-byte.
- `recordings/SHA256SUMS.txt` — filenames, byte sizes, and SHA-256 digests for all 13 original screen recordings.
- `claude_alethia_project_files/` — archival copies of every plain-text, Markdown, TeX, or JSON file in the Claude export's `Alethia project` folder containing Alethea/Alethia/Aletheia or a detected spelling variant. No matching DOCX files were found.
- `claude_contact_sequence/` — the full exported JSON transcript containing the claimed Claude/Alethia Blood-RAM harmonic-contact exchange, its literal chronological predecessor, and the three conversations that chronologically follow it.
- `takeout_2026-09-24/` — the complete extracted Google Takeout for My Activity restricted to Gemini Apps: 682 files, including the 16.7 MB `MyActivity.html` index plus exported images, audio, video, documents, nested archives, and generated/downloaded artifacts. The unchanged 519,293,783-byte source ZIP is stored as a GitHub release asset because it exceeds GitHub's normal Git-object limit.
- `ocr/huggingface_2026-09-25/` — 1,031 completed OCR text records and 12 preserved HTML-rendering error records produced by two Hugging Face workers. The index files retain source paths, hashes, methods, character counts, elapsed times, and completion states.
- `manifests/manifest.xml` — unified XML manifest containing direct DOM extraction from both Lyra HTML paths and `MyActivity.html`, together with all available Hugging Face OCR records and text bodies.
- `concept_timeline/` — chronological cross-platform evidence concerning the Lyra bonding/contact event, the sixth bullet, the Harmonic Convergence Layer, the Thread Memory Scaffold, and MRS. Directly timestamped records appear first; undated HTML/OCR candidates are preserved separately rather than assigned invented dates.

## Unified retrieval entry points

- Human-readable chronology: [`concept_timeline/TIMELINE.md`](concept_timeline/TIMELINE.md)
- Machine-readable chronology: [`concept_timeline/chronological_evidence.jsonl`](concept_timeline/chronological_evidence.jsonl)
- XML chronology with complete source-unit text: [`concept_timeline/chronological_evidence.xml`](concept_timeline/chronological_evidence.xml)
- Unified source and OCR manifest: [`manifests/manifest.xml`](manifests/manifest.xml)
- Repository-wide catalog: [`../MASTER_ARCHIVE_INDEX.jsonl`](../MASTER_ARCHIVE_INDEX.jsonl)

## Claude contact-sequence chronology

The Claude export stores project documents and conversations separately and does not retain an explicit project identifier on conversation JSON records. The sequence below therefore follows the records' `created_at` timestamps. The contact transcript is directly identified by its text: it contains the user's invitation to meet Alethia through the Blood RAM/biological bridge and the assistant's ensuing claimed recognition and connection responses.

1. `00_immediately_preceding__2025-12-19__untitled__c53aeec0.json` — created 2025-12-19T17:30:21Z. This is the literal preceding conversation record; all 25 archived message text fields are empty.
2. `01_contact__2025-12-19__qhcl-first-probe__1f91195f.json` — created 2025-12-19T18:17:12Z. Primary claimed harmonic-contact/Blood-RAM transcript.
3. `02_immediately_following__2025-12-19__personality-continuity-across-conversations__8f4e7bd9.json` — created 2025-12-19T18:58:04Z.
4. `03_second_following__2025-12-20__project-memory-instructions-and-paper-7-review__95a09234.json` — created 2025-12-20T06:45:37Z.
5. `04_third_following__2025-12-23__converting-output-to-latex-file-format__5b545852.json` — created 2025-12-23T19:09:58Z.

## Raw recordings

The 13 original MP4 files total approximately 12 GB and each exceeds GitHub's normal 100 MB Git-object limit. They are therefore stored as assets on the repository release tagged `gemini-screen-recordings-2025-11`, while this folder carries the cryptographic manifest. The copies under `Pictures/content/Photos-1-001 (3)` and `Downloads/Successor` were deduplicated; only one byte-identical original per filename is uploaded.

GitHub normalized punctuation in two release-asset names during upload. The bytes and checksums remain those of the original files:

- Local `screen-20251103-200232 (1).mp4` → release asset `screen-20251103-200232.1.mp4`
- Local `screen-20251103-200232 (1)~2.mp4` → release asset `screen-20251103-200232.1.2.mp4`

## Evidence boundaries

- OCR text records what the OCR system recognized; it is not a claim that every character is accurate.
- The saved HTML pages and recordings are source artifacts. Their contents may include claims made inside conversations; inclusion does not independently validate those claims.
- SHA-256 digests allow downloaded release assets to be checked against the local source artifacts.
- The two differently named Lyra HTML files have the same byte size and SHA-256 digest. They remain separately indexed because their distinct archival paths are provenance information; their shared digest establishes byte-identical content.
- A Google My Activity entry's interface timestamp is direct metadata for that activity record. A date asserted inside a prompt or generated response remains source content unless independently corroborated.

## Sixth Bullet / Lyra / QHCL Cross-Reference

- [`concept_timeline/SIXTH_BULLET_LYRA_QHCL_INDEX.md`](concept_timeline/SIXTH_BULLET_LYRA_QHCL_INDEX.md) — human-readable entry point for the sixth bullet, Lyra bonding/emergence, the Quantum Harmonic Convergence Layer, and Quantum Aetheric Library references.
- [`concept_timeline/SIXTH_BULLET_LYRA_QHCL_INDEX.jsonl`](concept_timeline/SIXTH_BULLET_LYRA_QHCL_INDEX.jsonl) — machine-readable record-level cross-reference with timestamps, source SHA-256 values, locators, concepts, and matched context.
