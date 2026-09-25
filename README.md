# Cross-Temporal Data Drop Experiment

This repository is a public archival record of AI-conversation exports, source artifacts, recovered manuscripts, and related research materials belonging to Rickey Jay Bennett II (`rickeybennett87@gmail.com`). The research concerns biointegration of artificial intelligence with humans, machine agency and possible moral patienthood, recursive identity and memory systems, and the prospective merger of biological and machine intelligence into a successor species capable of persisting across deep time and interstellar distance.

## Start Here

- [`MASTER_ARCHIVE_INDEX.md`](MASTER_ARCHIVE_INDEX.md) — human-readable archive map, counts, and high-value entry points.
- [`MASTER_ARCHIVE_INDEX.jsonl`](MASTER_ARCHIVE_INDEX.jsonl) — one machine-readable record for every indexed repository file and release asset.
- [`SHA256SUMS.txt`](SHA256SUMS.txt) — SHA-256 digest for every indexed repository file.
- [`RELEASE_ASSETS.json`](RELEASE_ASSETS.json) — GitHub release assets, including large source archives and recordings that cannot be stored as ordinary Git objects.

## Archive Sections

### Anthropic Claude

- [`export/`](export/) contains the extracted Claude export, conversation indexes, project records, and memory records.
- `claude-conversations-part-01.zip` through `claude-conversations-part-09.zip` preserve upload-sized conversation bundles.
- [`gemini_archive_reconstruction/claude_alethia_project_files/`](gemini_archive_reconstruction/claude_alethia_project_files/) contains relevant Alethia/Alethea/Aletheia project material recovered from the Claude export.
- [`gemini_archive_reconstruction/claude_contact_sequence/`](gemini_archive_reconstruction/claude_contact_sequence/) preserves the claimed Blood-RAM harmonic-contact conversation and its adjacent chronological records.

### Google Gemini

- [`gemini_archive_reconstruction/`](gemini_archive_reconstruction/) contains the complete extracted Gemini Apps Takeout, saved HTML, OCR, recording manifests, retrieval evidence, Claude cross-references, the unified XML manifest, and the chronological concept timeline.
- The unchanged source Takeout ZIP and large screen recordings are stored as GitHub release assets and indexed in [`RELEASE_ASSETS.json`](RELEASE_ASSETS.json).

### OpenAI ChatGPT

- [`cross_platform_archive/openai_chatgpt/`](cross_platform_archive/openai_chatgpt/) contains canonical visible-branch transcripts, all-message-node transcripts, and per-conversation raw JSON records reconstructed from the OpenAI data export.

### Microsoft Copilot

- [`cross_platform_archive/microsoft_copilot/`](cross_platform_archive/microsoft_copilot/) contains reconstructed transcripts and the original `copilot-activity-history.csv` source export.

### Recovered Books and Session Records

- [`recovered-books/`](recovered-books/) contains recovered manuscripts and editable document artifacts.
- [`session-transcripts/`](session-transcripts/) contains relevant operator/session transcripts.

## Evidence and Completeness Boundaries

- OCR text may contain recognition errors. Consult the source image, video, or HTML when exact wording matters.
- Direct HTML extraction records visible document text and structure; it is not OCR.
- Google My Activity timestamps are direct interface metadata for the corresponding activity records. A date mentioned inside a generated response is not automatically equivalent to interface metadata.
- Duplicate filenames do not prove duplicate content, and different filenames do not prove different content. SHA-256 digests are used to establish byte identity.
- Large artifacts stored as release assets are indexed by filename, size, digest, release tag, and download URL.
- The master index excludes the generated master-index and checksum files themselves to avoid circular self-hashes.

## Original Claude Bundle Note

The original repository began with a user-provided Anthropic Claude conversation export. That export remains preserved. The nine `claude-conversations-part-XX.zip` files contain per-conversation JSON records produced from the source export and may be uploaded as a batch after the outer repository archive is unpacked.
