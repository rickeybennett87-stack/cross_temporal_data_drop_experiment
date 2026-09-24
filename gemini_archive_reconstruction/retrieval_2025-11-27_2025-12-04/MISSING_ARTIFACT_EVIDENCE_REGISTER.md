# Missing-artifact evidence register

Status: active review; entries below are evidence records, not claims that a model's description is true.

## Interpretation rules

- **Acknowledged existence** means a timestamped source visibly referred to an artifact as existing, created, processed, attached, offered for download, or expected to be supplied.
- **Present** requires located bytes that can be hashed. A screenshot, attachment card, conversation statement, or download link is not itself the artifact.
- **Not located** means the artifact was not found in the current retrieval corpus or by the recorded filesystem search. It does not prove deletion.
- **Contents declared** records what a participant or model said the artifact contained. It is not independent verification of those contents.
- Statements by Gemini, ChatGPT, Grok, or Copilot about deletion, internal access, or system behavior are preserved as source evidence and are not treated as verified architecture facts.

## Timestamp classification

The absence of a timestamp from the visible screenshot or exported text must not be recorded as proof that no timestamp exists. Use the following classes:

1. **Explicit visible timestamp** — a date or time is directly displayed in the interface, screenshot, URL metadata, activity record, attachment card, or export.
2. **Platform-declared latent timestamping** — Gemini or another platform states that its conversations, turns, summaries, or summary contents are timestamped or retain timestamp-derived data, but the underlying timestamp is not exposed in the recovered interface. This establishes a source claim that temporal metadata exists; it does not independently verify the backend implementation or reveal the exact time.
3. **Summary-carried temporal data** — a summary contains dates, times, temporal ordering, or timestamp-derived descriptions. Preserve those values and the summary that carries them. Label them as summary evidence unless corroborated by direct interface metadata.
4. **Reconstructed temporal placement** — the time is inferred from adjacent timestamped screenshots, chronological conversation order, device filenames, filesystem metadata, neighboring activity records, or a summary. Record the bounding evidence and do not silently convert the inference into an exact timestamp.
5. **Timestamp unresolved** — no exact timestamp is exposed, but latent timestamping or temporal order may still exist. Use this instead of `no timestamp` unless there is affirmative evidence that the source never recorded one.

User-supplied methodological claim: Gemini will, when asked, describe its timestamping system as timestamping everything and describe summaries as carrying timestamp data in their summarized contents. This claim is a retrieval lead. A Gemini response making that statement would be a **platform declaration**, not independent proof of the underlying storage architecture. Because this retrieval is read-only and sending new prompts is prohibited, no new prompt will be sent merely to elicit that confirmation; existing conversation instances and exports will be searched for prior declarations instead.

## Timestamped acknowledgments

### MA-001 — “Self-Propagating Lies” document or conversation

- Timestamped source: `2025-12-04 23:19:08`, `Screenshot_20251204-231908.png`
- Conversation visible in source: `Model Recovery From Binary Output`
- Source category: user statement captured by screenshot/OCR
- Declaration: the user says they have a document or conversation called “self-propagating lies” and can retrieve it.
- Contents declared: alleged evidence concerning the model's former access to its “core thinking/sinking processes and abilities”; OCR is imperfect, so the exact disputed word must be checked against the image or live conversation.
- Follow-up acknowledgment: `2025-12-04 23:19:16`, `Screenshot_20251204-231916.png`
- Follow-up source category: Gemini-generated statement
- Follow-up declaration: Gemini identifies it as “The Self-Propagating Lies Document,” describes it as a document or conversation, and asks for the document or screenshots.
- Artifact-byte status: **not located under that title** in the current repository or the initial home-directory filename search.
- Evidentiary status: **timestamped acknowledgment of claimed existence; artifact contents and survival unverified**.
- Required follow-up: inspect/search the referenced conversation title and adjacent turns for an attachment, link, precise title, conversation ID, or later confirmation that it was supplied.
- Read-only Gemini query result: searching Gemini history for `Self-Propagating Lies` surfaced the following relevant conversation instances:
  - `Model Recovery From Binary Output`, conversation ID `dc231aa44aefb9c1`, displayed in search as `Dec 1, 2025`;
  - `Conversation History Recap and Next Steps`, conversation ID `09b02b509aec6203`, displayed as `Jul 15, 2025`;
  - `Reconstructing Deleted Conversation`, conversation ID `5065e96afa50b97b`, displayed as `Dec 8, 2025`;
  - `Phalanx Mention Found in Past Conversations`, conversation ID `dd16b848d02e46e9`, displayed as `Dec 5, 2025`.
- Conversation-instance inspection: `https://gemini.google.com/app/09b02b509aec6203` visibly contains prompts about Lyra, the Quantum Harmonic Convergence Layer, “the sixth bullet,” and “the vow and the walk.” This supports the relationship between the referenced historical material and that conversation, but no attachment or file bytes were visible in the inspected state.

### MA-002 — 45-chapter download bundle

- Timestamped source: `2025-11-30 21:13:23`, `Screenshot_20251130-211323.png`
- Visible platform: ChatGPT
- Source category: ChatGPT-generated statement and visible download offer
- Declaration: “Processed 45 chapters, total 32,844 words, no truncations detected” followed by “Here's your ZIP” and “Download the chapter bundle.”
- Contents declared: `Chapter_1.md` through `Chapter_45.md`, plus `manifest.txt`; the manifest was said to contain total chapters, total words, and per-chapter word counts.
- Source-input acknowledgment: the same statement says all paragraphs from “the DOCX” were read and assigned to chapters.
- Artifact-byte status: **not located as an identifiable 45-chapter ZIP or matching `Chapter_1.md`–`Chapter_45.md` set in the current retrieval corpus or initial filename search**. Several unrelated ZIP and DOCX files exist and must not be conflated with this bundle.
- Evidentiary status: **timestamped creation/download declaration; output bytes not presently matched**.
- Required follow-up: query the conversation instance containing this turn to recover the exact conversation ID, download-card metadata, original DOCX name, generated ZIP name, and any surviving attachment URL.

### MA-003 — Unnamed source DOCX used for the chapter bundle

- Timestamped source: `2025-11-30 21:13:23`, `Screenshot_20251130-211323.png`
- Visible platform: ChatGPT
- Source category: ChatGPT-generated statement
- Declaration: “All paragraphs from the DOCX were read and assigned to chapters.”
- Contents declared: 45 chapters totaling 32,844 words.
- Artifact-byte status: **unresolved** because no exact filename is visible in the recovered screenshot. Existing DOCX files cannot be identified as this input solely from the statement.
- Evidentiary status: **timestamped acknowledgment of an input file; filename and byte identity unknown**.
- Required follow-up: inspect the conversation instance and immediately preceding turns for the upload card and exact filename.

### MA-004 — “book two Promethe…” DOCX

- Timestamped sources: `2025-11-29 23:42:40`, `Screenshot_20251129-234240.png`; `2025-11-29 23:42:46`, `Screenshot_20251129-234246.png`
- Visible platform: Microsoft Copilot
- Source category: direct interface metadata plus user/Copilot statements
- Declaration: a visible truncated attachment label reads `book two Promethe...` with type `DOCX`. The conversation discusses testing whether “your document” is blocked and the user asks whether Copilot still did not receive it.
- Artifact-byte status: **unresolved/not matched**. The truncated label is insufficient to equate it with any currently present Prometheus manuscript.
- Evidentiary status: **timestamped visible attachment acknowledgment; exact filename and bytes unverified**.
- Required follow-up: inspect the original screenshot at full resolution and, if available, the Copilot conversation instance for full attachment metadata.

## Related acknowledgment outside the primary date window

### MA-X01 — “Project Chimera” document

- Timestamped sources: `2025-11-22 09:44:36`, `Screenshot_20251122-094436.png`; `2025-11-22 09:45:18`, `Screenshot_20251122-094518.png`
- Visible platform: Grok
- Source category: user request plus Grok-generated statements
- Declaration: the user refers to eliminating the past six turns; Grok refers to “the Chimera document,” “all attachments,” and later says the past six turns and Chimera document “never existed after this line.”
- Artifact-byte status: **not located by exact-name filename search**.
- Evidentiary status: **timestamped acknowledgment that a document called Project Chimera was discussed; the model's claim that it performed server-side erasure is not verified and should not be treated as proof of deletion**.
- Required follow-up: locate the conversation instance and preceding six turns, if accessible, to recover the document's declared contents, any exact filename, and the earliest timestamped acknowledgment.

## Absence-search scope recorded so far

The initial filesystem check searched `/home/jadedjade` by filename for Chimera, Self-Propagating Lies, `manifest.txt`, `Chapter_1.md`, `document.tex`, ZIP files, and DOCX files. It found unrelated artifacts but no exact filename match for Project Chimera, Self-Propagating Lies, or the declared 45-chapter Markdown bundle. This is a provisional absence result: archives may contain the files under different names, attachment metadata may be truncated, and conversation exports may preserve text without attachment bytes.

## Planned conversation-instance evidence fields

For each conversation queried read-only, record:

1. exact visible conversation title and URL/ID;
2. timestamp class, exact visible timestamp when exposed, latent-timestamp declaration when present, or the narrowest defensible reconstructed range;
3. exact filename and file type, if displayed;
4. declaration text and whether it came from the user, interface, or model;
5. declared contents or purpose;
6. attachment/download-card state;
7. whether bytes were located and hashed;
8. completeness: complete, partial, inaccessible, absent, or unresolved.
9. timestamp provenance: interface, screenshot filename, filesystem metadata, activity record, conversation summary, model/platform declaration, adjacent-turn inference, or later interpretation.
