# Q5 five-model corpus graph

The canonical deployed visualization is available at
[rickeybennett87-stack.github.io/q5-five-model-corpus-graph](https://rickeybennett87-stack.github.io/q5-five-model-corpus-graph/),
with its deployment source maintained in the dedicated
[`q5-five-model-corpus-graph`](https://github.com/rickeybennett87-stack/q5-five-model-corpus-graph)
repository. This directory preserves the archive-side source snapshot and
rebuild tooling.

GPU-rendered, interactive projection of the complete current repository inventory
and its indexed GitHub release assets into five model dimensions:

1. ChatGPT
2. Claude
3. Gemini
4. Grok
5. Copilot

The page exposes five independently switchable edge graphs: model affinity,
subject, chronology, repository provenance, and filename/content correlation.
Search and filters rebuild only the visible GPU buffers and enabled edge layers.
Continuous five-dimensional rotation is performed in the WebGL vertex shader.

## Coverage

- 3,647 repository files
- 17 GitHub release assets
- 3,664 total graph nodes
- 1,267,820,307 repository bytes
- 17,047,182,063 release-asset bytes
- 18,315,002,370 total represented bytes

Generated visualization files are not recursively included in their own source
inventory; that boundary prevents a self-changing index.

## Evidence boundary

Coordinates and subject labels are retrieval signals derived from repository paths,
bounded text prefixes, and known archive structure. They are not claims of authorship,
scientific validity, model cognition, or causal relationships. Edge layers express
indexable relationships and can be inspected independently.

## Rebuild

Run `build_q5_corpus_graph.py` against the repository and package the resulting JSON
as `window.Q5_DATA=<json>;` in `q5-corpus-data.js`. The JSON is retained separately
for database ingestion and reproducibility.
