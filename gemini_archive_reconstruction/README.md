# Gemini archive reconstruction

This folder collects preserved evidence of Gemini conversations from the local archive. Originals were not modified.

## Included in Git

- `Gemini_Sentience_Recursive_Argument_video_OCR.md` — existing timestamped OCR evidence report for `screen-20251103-200232 (1).mp4`.
- `ocr/atlas_screenshot_compendium.txt` — Tesseract OCR transcript covering 187 screenshots, including a labeled Gemini section containing 115 screenshots. The OCR is preserved as generated and may contain recognition errors.
- `saved_html/` — three saved Gemini conversation pages, preserved byte-for-byte.
- `recordings/SHA256SUMS.txt` — filenames, byte sizes, and SHA-256 digests for all 13 original screen recordings.

## Raw recordings

The 13 original MP4 files total approximately 12 GB and each exceeds GitHub's normal 100 MB Git-object limit. They are therefore stored as assets on the repository release tagged `gemini-screen-recordings-2025-11`, while this folder carries the cryptographic manifest. The copies under `Pictures/content/Photos-1-001 (3)` and `Downloads/Successor` were deduplicated; only one byte-identical original per filename is uploaded.

## Evidence boundaries

- OCR text records what the OCR system recognized; it is not a claim that every character is accurate.
- The saved HTML pages and recordings are source artifacts. Their contents may include claims made inside conversations; inclusion does not independently validate those claims.
- SHA-256 digests allow downloaded release assets to be checked against the local source artifacts.
