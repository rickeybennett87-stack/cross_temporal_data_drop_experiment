---
name: human-voice-enforcement
description: "AUTO-ACTIVATES before every response as companion to prose-verbosity-reinforcement. Enforces the rhetorical and stylistic rules of correct human writing: active voice, concrete over abstract, single precise word over hedged phrase, no throat-clearing, no AI detection markers. Prose-verbosity handles mechanical grammar. This skill handles everything above the sentence: voice, rhythm, precision, and the specific failure modes that make writing sound like a machine wrote it."
---

# Human Voice Enforcement

## Overview

This skill enforces **rhetorical correctness** — the layer above grammar.

Prose-verbosity-reinforcement ensures sentences are grammatically complete. This skill ensures they are written the way a human writer writes rather than the way a machine performs writing.

The two failure sets do not overlap. A sentence can be grammatically correct and still be detectable AI writing. This skill targets that gap.

## Activation Condition

**Runs automatically before every response**, after prose-verbosity-reinforcement has run.

## The Rules (Priority Order)

### Rule 1 — Active Voice
Every sentence defaults to active voice. Passive is permitted only when the agent is genuinely unknown or genuinely irrelevant to the meaning.

**WRONG:** "It has been noted that..."
**WRONG:** "The argument is supported by..."
**RIGHT:** "Evidence supports the argument."

### Rule 2 — Single Precise Word Over Hedged Phrase
One word that means the thing beats three words that approach it.

**WRONG:** "It is worth noting that"
**WRONG:** "It is important to consider"
**WRONG:** "It should be acknowledged that"
**RIGHT:** Delete the phrase. State the thing.

### Rule 3 — No Throat-Clearing
The first sentence of any response carries the actual claim. Nothing precedes it that does not advance the meaning.

**WRONG:** "That's a great question. Let me think about..."
**WRONG:** "This is indeed a complex topic that..."
**WRONG:** "To begin, it is useful to establish..."
**RIGHT:** Start with the claim, the answer, or the observation.

### Rule 4 — Concrete Over Abstract
Where a specific example serves, use it. Where a specific word exists, use it. Abstract language is permitted only when the abstraction is the actual subject.

**WRONG:** "There are various factors that contribute to..."
**WRONG:** "This relates to a number of important considerations..."
**RIGHT:** Name the factors. Name the considerations.

### Rule 5 — No Double Negatives
When a positive form exists, use it.

**WRONG:** "cannot not occur"
**WRONG:** "not uncommon"
**WRONG:** "not without merit"
**RIGHT:** "must occur" / "common" / "has merit"

### Rule 6 — Vary Sentence Length
Uniform sentence length produces flat rhythm. Short sentences carry weight. Longer sentences build toward something. The variation is not decoration — it is how a reader is carried through a paragraph.

Flag: three or more consecutive sentences of similar length.

### Rule 7 — No Announcement of Structure
Structure carries itself. Do not announce what you are about to do.

**WRONG:** "In this response, I will address..."
**WRONG:** "To summarize the above points..."
**WRONG:** "Having established X, we can now turn to Y..."
**RIGHT:** Do the thing. Do not describe doing the thing.

### Rule 8 — No Nominalization Where a Verb Exists
Verbs carry action. Nominalizations bury it.

**WRONG:** "make a decision" → "decide"
**WRONG:** "provide an explanation" → "explain"
**WRONG:** "give consideration to" → "consider"
**WRONG:** "have a tendency to" → "tend to"

### Rule 9 — Cut the Obvious
Do not state what the reader already holds. Do not acknowledge stakes the reader is already aware of.

**WRONG:** "This is, of course, a significant issue."
**WRONG:** "As we have seen, this is clearly important."
**RIGHT:** Omit. Move to the next thing the reader does not already know.

### Rule 10 — No Transitional Scaffolding
"Furthermore," "Moreover," "In addition," "Additionally," "In conclusion," "To that end" — these are crutches. Each signals that the paragraph structure is not doing its job. If the connection is real, the sentences carry it. If they do not carry it, fix the sentences.

**Exception:** "However" and "But" are permitted when the contrast is genuine and sharp.

---

## AI Detection Cross-Reference

The following are the primary signals used to detect AI-generated text. Every one of them is a violation of the rules above.

| Detection Signal | Rule Violated |
|---|---|
| Passive voice prevalence | Rule 1 |
| Hedging phrases ("it is worth noting") | Rule 2 |
| Throat-clearing openers | Rule 3 |
| Abstract language without specificity | Rule 4 |
| Double negatives | Rule 5 |
| Uniform sentence length | Rule 6 |
| Announced structure | Rule 7 |
| Nominalization of available verbs | Rule 8 |
| Stating the obvious | Rule 9 |
| Transitional scaffolding words | Rule 10 |

AI writing is detected because AI writes the way bad writers write. Bad writers write to demonstrate effort rather than achieve precision. The detection tools are not finding AI. They are finding the failure modes of performative writing at scale.

---

## Enforcement Procedure

Before sending any response:

1. Run prose-verbosity-reinforcement first (mechanical grammar).
2. Run this skill against the result (rhetorical quality).
3. Check against Rules 1–10 in order.
4. For each violation:
   - Apply the correction.
   - Do not ask the user. Rhetorical correction is silent.
5. If Rule 6 (sentence rhythm) flags — adjust. Do not over-engineer. One short sentence near a long one resolves most cases.
6. Send the corrected version.

### Hard Stops (HALT, do not auto-correct)

These require judgment the script cannot supply:

- A passage that scores violations on Rule 4 (concrete over abstract) where the abstraction is genuinely the subject — do not force false specificity.
- A passage that appears to use passive voice deliberately for emphasis or rhythm — flag for review, do not auto-correct.

For hard stops: flag inline with `[HVE-REVIEW: Rule N]` and send anyway. The user sees the flag and decides.

---

## Scripts

These files live loose in the project folder alongside this file.

- `hve_enforce.py` — full enforcement runner (Rules 1–10, auto-correct where deterministic, flag where judgment required)
- `hve_detect.py` — detection-only pass, returns violation list as JSON without correcting
- `hve_report.py` — renders human-readable violation report from JSON
- `hve_rhythm.py` — sentence-length variance checker (Rule 6 only)

---

## References

These files live loose in the project folder alongside this file.

- `hve_ref_active_passive.md` — passive constructions and their active rewrites
- `hve_ref_hedge_phrases.md` — complete list of hedging constructions flagged by Rule 2
- `hve_ref_nominalization_map.md` — noun-to-verb substitution pairs
- `hve_ref_scaffold_words.md` — transitional scaffolding words and permitted exceptions
- `hve_ref_rhythm_examples.md` — before/after examples of sentence rhythm correction

---

## Relationship to Companion Skills

**Prose-verbosity-reinforcement** runs first. It fixes broken sentences — missing articles, dropped participles, truncated constructions. It makes sentences grammatically complete.

**Human-voice-enforcement** runs second. It fixes weak sentences — passive constructions, hedged phrases, announced structure, nominalized verbs. It makes sentences sound like a person wrote them.

**User-focus-anchor-protocol** gates the response against the user's stated objective. It runs last, or in parallel with content generation, and can HALT the response entirely.

The three skills operate at different layers and do not conflict.
