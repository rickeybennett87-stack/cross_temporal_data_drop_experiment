#!/usr/bin/env python3
# hve_enforce.py
# Human Voice Enforcement — Main enforcement script
# Companion to: human-voice-enforcement.md
# Usage: python hve_enforce.py < draft.txt > corrected.txt
#        python hve_enforce.py --report < draft.txt

import sys
import re
import json
import argparse

# ── Rule 2: Hedge phrases ──────────────────────────────────────────────────────
HEDGE_PHRASES = [
    r"it is worth noting that\s*",
    r"it is important to (note|consider|acknowledge|recognize) that\s*",
    r"it should be (noted|acknowledged|mentioned) that\s*",
    r"it is (perhaps|arguably|essentially|fundamentally) (worth|important)\s*",
    r"one might (argue|note|consider) that\s*",
    r"needless to say[,\s]*",
    r"it goes without saying that\s*",
    r"as (we|one) (might|can|could) (expect|see|note)[,\s]*",
]

# ── Rule 3: Throat-clearing openers ───────────────────────────────────────────
THROAT_CLEAR = [
    r"^(that'?s?|this is) (a )?(great|excellent|interesting|good|wonderful|fascinating) (question|point|observation)[\.!,]?\s*",
    r"^(let me|allow me to) (think|consider|address|explore|examine)\s*(that|this)?\s*[,\.]?\s*",
    r"^(this is (indeed|certainly|truly) a? ?(complex|nuanced|important|significant|challenging))\s*",
    r"^(to begin[,\s]|to start[,\s]|first[,\s]+let('?s| us))",
]

# ── Rule 5: Double negatives ───────────────────────────────────────────────────
DOUBLE_NEGATIVES = {
    r"\bcannot not\b": "must",
    r"\bnot uncommon\b": "common",
    r"\bnot without merit\b": "has merit",
    r"\bnot infrequently\b": "often",
    r"\bnot unlikely\b": "likely",
    r"\bnot impossible\b": "possible",
    r"\bnot insignificant\b": "significant",
    r"\bnot unimportant\b": "important",
    r"\bnot unadjacent\b": "adjacent",
}

# ── Rule 7: Structure announcements ───────────────────────────────────────────
STRUCTURE_ANNOUNCE = [
    r"in this (response|answer|explanation|section)[,\s]+i (will|am going to|shall)\s*",
    r"(to summarize|to sum up|in summary)[,\s]+(the )?(above|following|key)?\s*(points?|ideas?|arguments?)?\s*[,\.]?\s*",
    r"having (established|shown|demonstrated|discussed) .{0,60}[,\s]+(we can now|let('?s| us)|i will)\s*",
    r"(before|after) (we|i) (proceed|continue|move on)[,\s]*",
]

# ── Rule 8: Nominalizations ────────────────────────────────────────────────────
NOMINALIZATIONS = {
    r"\bmake a decision\b": "decide",
    r"\bmakes a decision\b": "decides",
    r"\bmade a decision\b": "decided",
    r"\bprovide an explanation\b": "explain",
    r"\bprovides an explanation\b": "explains",
    r"\bprovided an explanation\b": "explained",
    r"\bgive consideration to\b": "consider",
    r"\bgives consideration to\b": "considers",
    r"\bgave consideration to\b": "considered",
    r"\bhave a tendency to\b": "tend to",
    r"\bhas a tendency to\b": "tends to",
    r"\bhad a tendency to\b": "tended to",
    r"\bperform an analysis\b": "analyze",
    r"\bperforms an analysis\b": "analyzes",
    r"\bperformed an analysis\b": "analyzed",
    r"\bconduct a review\b": "review",
    r"\bconducts a review\b": "reviews",
    r"\bconducted a review\b": "reviewed",
    r"\bcome to a conclusion\b": "conclude",
    r"\bcomes to a conclusion\b": "concludes",
    r"\bcame to a conclusion\b": "concluded",
    r"\bgive a description of\b": "describe",
    r"\bgives a description of\b": "describes",
    r"\bgave a description of\b": "described",
    r"\bmake an attempt\b": "attempt",
    r"\bmakes an attempt\b": "attempts",
    r"\bmade an attempt\b": "attempted",
    r"\bshow an improvement\b": "improve",
    r"\bshows an improvement\b": "improves",
    r"\bshowed an improvement\b": "improved",
}

# ── Rule 10: Transitional scaffolding ─────────────────────────────────────────
SCAFFOLD_WORDS = [
    r"^furthermore[,\s]+",
    r"^moreover[,\s]+",
    r"^in addition[,\s]+",
    r"^additionally[,\s]+",
    r"^in conclusion[,\s]+",
    r"^to that end[,\s]+",
    r"^with that (said|in mind)[,\s]+",
    r"^as such[,\s]+",
    r"^it (is|was) (thus|therefore|hence) (the case|clear|evident) that\s*",
]

# ── Rule 9: Stating the obvious ───────────────────────────────────────────────
OBVIOUS_PHRASES = [
    r"(this is|it is)[,\s]+(of course)[,\s]+",
    r"as (we have|we've) (seen|established|noted)[,\s]+",
    r"(clearly|obviously|evidently)[,\s]+(this|it|the)",
    r"(as (is|was) (well[- ]known|widely (known|understood|accepted)))[,\s]+",
    r"needless to say[,\s]+",
]


def apply_rule_2(text):
    """Remove hedge phrases."""
    violations = []
    for pattern in HEDGE_PHRASES:
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for m in matches:
            violations.append({"rule": 2, "match": m.group(), "action": "deleted"})
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text, violations


def apply_rule_3(text):
    """Remove throat-clearing openers from sentences."""
    violations = []
    sentences = text.split('\n')
    result = []
    for sentence in sentences:
        original = sentence
        for pattern in THROAT_CLEAR:
            if re.match(pattern, sentence.strip(), re.IGNORECASE):
                cleaned = re.sub(pattern, "", sentence.strip(), flags=re.IGNORECASE)
                if cleaned:
                    sentence = cleaned[0].upper() + cleaned[1:]
                    violations.append({"rule": 3, "match": original.strip()[:60], "action": "opener removed"})
        result.append(sentence)
    return '\n'.join(result), violations


def apply_rule_5(text):
    """Replace double negatives with positive forms."""
    violations = []
    for pattern, replacement in DOUBLE_NEGATIVES.items():
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for m in matches:
            violations.append({"rule": 5, "match": m.group(), "replacement": replacement})
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text, violations


def apply_rule_7(text):
    """Remove structure announcements."""
    violations = []
    for pattern in STRUCTURE_ANNOUNCE:
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for m in matches:
            violations.append({"rule": 7, "match": m.group()[:60], "action": "deleted"})
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text, violations


def apply_rule_8(text):
    """Replace nominalizations with verbs."""
    violations = []
    for pattern, replacement in NOMINALIZATIONS.items():
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for m in matches:
            violations.append({"rule": 8, "match": m.group(), "replacement": replacement})
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text, violations


def apply_rule_9(text):
    """Flag or remove obvious-stating phrases."""
    violations = []
    for pattern in OBVIOUS_PHRASES:
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for m in matches:
            violations.append({"rule": 9, "match": m.group()[:60], "action": "[HVE-REVIEW: Rule 9 — obvious statement]"})
            text = text.replace(m.group(), "[HVE-REVIEW: Rule 9] ")
    return text, violations


def apply_rule_10(text):
    """Remove scaffolding words at sentence starts."""
    violations = []
    lines = text.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        for pattern in SCAFFOLD_WORDS:
            if re.match(pattern, stripped, re.IGNORECASE):
                cleaned = re.sub(pattern, "", stripped, flags=re.IGNORECASE)
                if cleaned:
                    line = cleaned[0].upper() + cleaned[1:]
                    violations.append({"rule": 10, "match": stripped[:40], "action": "scaffold word removed"})
                break
        result.append(line)
    return '\n'.join(result), violations


def check_rule_1(text):
    """Flag passive voice for review (cannot auto-correct without semantic understanding)."""
    passive_pattern = r"\b(is|are|was|were|be|been|being)\s+(written|done|made|said|seen|known|used|found|given|taken|shown|produced|created|built|designed|established|described|noted|argued|demonstrated|suggested|indicated|claimed|proposed)\b"
    violations = []
    for m in re.finditer(passive_pattern, text, re.IGNORECASE):
        violations.append({
            "rule": 1,
            "match": m.group(),
            "action": "[HVE-REVIEW: Rule 1 — passive voice, consider active rewrite]"
        })
    return violations


def check_rule_6(text):
    """Flag uniform sentence length."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    lengths = [len(s.split()) for s in sentences if len(s.split()) > 3]
    if len(lengths) < 3:
        return []
    violations = []
    for i in range(len(lengths) - 2):
        window = lengths[i:i+3]
        avg = sum(window) / 3
        variance = sum((l - avg) ** 2 for l in window) / 3
        if variance < 4 and avg > 8:
            violations.append({
                "rule": 6,
                "location": f"sentences {i+1}–{i+3}",
                "lengths": window,
                "action": "[HVE-REVIEW: Rule 6 — uniform rhythm, vary sentence length]"
            })
    return violations


def enforce(text, report=False):
    all_violations = []

    text, v = apply_rule_2(text)
    all_violations.extend(v)
    text, v = apply_rule_3(text)
    all_violations.extend(v)
    text, v = apply_rule_5(text)
    all_violations.extend(v)
    text, v = apply_rule_7(text)
    all_violations.extend(v)
    text, v = apply_rule_8(text)
    all_violations.extend(v)
    text, v = apply_rule_9(text)
    all_violations.extend(v)
    text, v = apply_rule_10(text)
    all_violations.extend(v)

    # Rules requiring judgment — flag only
    all_violations.extend(check_rule_1(text))
    all_violations.extend(check_rule_6(text))

    if report:
        print("=== HVE VIOLATION REPORT ===", file=sys.stderr)
        for v in all_violations:
            print(json.dumps(v), file=sys.stderr)
        print(f"Total violations: {len(all_violations)}", file=sys.stderr)
        print("===========================", file=sys.stderr)

    return text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", action="store_true", help="Print violation report to stderr")
    args = parser.parse_args()

    text = sys.stdin.read()
    result = enforce(text, report=args.report)
    print(result, end="")


if __name__ == "__main__":
    main()
