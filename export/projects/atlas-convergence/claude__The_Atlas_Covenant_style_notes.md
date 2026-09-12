# The Atlas Covenant — Style Notes (no-ai-tells findings, ongoing)

Living record of prose patterns caught during drafting that need active suppression in every future chapter. Check against this list during generation, not just at cleanup.

## Banned constructions

**"the specific [abstract noun] of [someone] who [explanatory clause]"** — e.g. "the specific brisk economy of someone who measured a conversation's worth by what it had actually accomplished." Caught in chapter 5 at 36 occurrences across ~8,000 words. This is the narrator stopping to hand the reader a labeled category for a behavior instead of showing the behavior and trusting it to land — analysis wearing the costume of feeling. Flagged directly by the author as an AI tell that stands out heavily.

Fix pattern: cut "the specific" entirely in most cases; where a categorical label is still wanted, drop the "of someone who" scaffolding and either (a) show the action/dialogue with no label at all, or (b) attach the explanation as a separate short sentence rather than a trailing dependent clause.

## Standing no-ai-tells rules (carried from earlier chapters)

- Zero em dashes, ever.
- Forbidden vocabulary: delve, tapestry, pivotal, underscore, crucial, intricate, landscape-as-metaphor, foster, testament, enhance, boasts, bolstered, garner, meticulous, vibrant, showcasing, highlighting, emphasizing, interplay, enduring, "align with", camaraderie, vague "key".
- No chapter numbers or book/volume labels anywhere in prose. Caught twice in chapter 5 drafts ("chapter four's pattern," "four chapters of this project's life") — both replaced with time-based phrasing.
- Bare roman numerals only for in-chapter scene breaks, no titles attached.
- Avoid negative parallelism ("not just X but Y") unless load-bearing, rule-of-three padding, tailing participial clauses, compulsive summarizing.
- Name-generation constraints checked per new name (see outline/prior chapter notes for the full table): no open-a-terminal first names, no three-syllable liquid-stressed names, no Greek roots, no monosyllabic hard-consonant/silent-e surnames, no "-ael" male endings, and avoid the documented forbidden-name cluster.

## Verification method (per chapter, before delivery)

Exact word count via direct Python count (excluding title line and bare roman-numeral heading lines), cross-checked with an independent shell method (`tail -n +2 file | grep -vE "^(I|II|...)$" | wc -w`). Both must agree before quoting a count to the author. Per-chapter floor: 8,000 words; target 9,000+.
