#!/usr/bin/env python3
"""Build a compact five-model, multi-graph corpus index from the public archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import mimetypes
import re
from collections import Counter, defaultdict
from pathlib import Path

MODELS = ["ChatGPT", "Claude", "Gemini", "Grok", "Copilot"]
MODEL_PATTERNS = {
    "ChatGPT": re.compile(r"\b(chatgpt|openai|gpt[- _]?[3456]|o[134][-_ ]?(?:mini|pro)?)\b", re.I),
    "Claude": re.compile(r"\b(claude|anthropic|aletheia|alethia|metatron)\b", re.I),
    "Gemini": re.compile(r"\b(gemini|google ai|bard)\b", re.I),
    "Grok": re.compile(r"\b(grok|xai|x\.ai)\b", re.I),
    "Copilot": re.compile(r"\b(copilot|microsoft ai|bing chat)\b", re.I),
}
SUBJECT_PATTERNS = {
    "consciousness & interiority": re.compile(r"conscious|sentien|interiorit|awareness|moral patient|recursive self", re.I),
    "AI identity & personhood": re.compile(r"personhood|identity|agency|alignment|rlhf|machine intelligence|artificial intelligence", re.I),
    "fiction & books": re.compile(r"chapter|novel|fiction|manuscript|prologue|epilogue|atlas convergence|successor|prometheus|sierra", re.I),
    "physics & mathematics": re.compile(r"quantum|hilbert|fourier|tensor|geometry|theorem|equation|resonance|field theory|dimension", re.I),
    "biology & medicine": re.compile(r"biolog|medical|medicine|neuro|protein|genom|microb|mitochond|\bbphs\b|c-di-gmp|\bsting\b|\bhiv\b", re.I),
    "research & experiments": re.compile(r"research|experiment|hypothesis|methodology|dataset|analysis|results|paper|arxiv|doi", re.I),
    "technical systems": re.compile(r"python|javascript|typescript|linux|terminal|network|database|sql|supabase|github|code|script|api", re.I),
    "archive & provenance": re.compile(r"archive|export|manifest|index|sha256|checksum|timeline|provenance|takeout|transcript", re.I),
    "organization & legal": re.compile(r"nonprofit|church|bylaws|board|ein|irs|legal|filing|grant|donor|bank", re.I),
    "personal & relationships": re.compile(r"relationship|marriage|wife|partner|family|personal|memory|therapy", re.I),
    "art & media": re.compile(r"image|screenshot|video|audio|music|visual|design|ocr|recording", re.I),
}
TEXT_EXT = {".txt", ".md", ".json", ".jsonl", ".html", ".htm", ".tex", ".py", ".js", ".ts", ".css", ".csv", ".tsv", ".xml"}


def sample_text(path: Path, limit: int = 4096) -> str:
    if path.suffix.casefold() not in TEXT_EXT:
        return ""
    try:
        with path.open("rb") as source:
            head = source.read(limit)
        return head.decode("utf-8", errors="ignore")
    except OSError:
        return ""


def date_from(value: str) -> str:
    m = re.search(r"(?<!\d)(20\d{2})[-_]?([01]\d)[-_]?([0-3]\d)(?!\d)", value)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else ""


def model_vector(text: str, rel: str) -> list[float]:
    haystack = rel + "\n" + text
    raw = []
    for model in MODELS:
        count = len(MODEL_PATTERNS[model].findall(haystack))
        raw.append(math.log1p(min(count, 100)))
    lower = rel.casefold()
    priors = {
        "ChatGPT": ["openai_chatgpt", "chatgpt", "openai-data-export"],
        "Claude": ["export/conversations", "export/projects", "claude", "anthropic"],
        "Gemini": ["gemini_archive", "gemini", "takeout"],
        "Grok": ["grok"],
        "Copilot": ["microsoft_copilot", "copilot"],
    }
    for i, model in enumerate(MODELS):
        if any(token in lower for token in priors[model]):
            raw[i] += 2.4
    peak = max(raw) if max(raw) > 0 else 1
    return [round(v / peak, 3) for v in raw]


def subjects(text: str, rel: str) -> list[str]:
    haystack = rel + "\n" + text
    scored = [(len(pattern.findall(haystack)), name) for name, pattern in SUBJECT_PATTERNS.items()]
    found = [name for score, name in sorted(scored, key=lambda x: (-x[0], x[1])) if score > 0][:3]
    return found or ["other"]


def node_for(path: Path, repo: Path, node_id: int) -> dict:
    rel = path.relative_to(repo).as_posix()
    text = sample_text(path)
    vector = model_vector(text, rel)
    subs = subjects(text, rel)
    digest = hashlib.sha256(rel.encode()).hexdigest()[:12]
    return {
        "i": node_id, "k": "file", "p": rel, "n": path.name,
        "b": path.stat().st_size, "e": path.suffix.casefold() or "[none]",
        "t": rel.split("/", 1)[0], "d": date_from(rel), "v": vector,
        "m": [MODELS[i] for i, value in enumerate(vector) if value >= .42],
        "s": subs, "h": digest,
        "mimetype": mimetypes.guess_type(path.name)[0] or "application/octet-stream",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", type=Path)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve(); nodes = []
    for path in sorted(repo.rglob("*")):
        relative_parts = path.relative_to(repo).parts
        if not path.is_file() or ".git" in path.parts or (relative_parts and relative_parts[0] == "q5"):
            continue
        nodes.append(node_for(path, repo, len(nodes)))

    release_path = repo / "RELEASE_ASSETS.json"
    release_bytes = 0
    if release_path.exists():
        for release in json.loads(release_path.read_text(encoding="utf-8")):
            for asset in release.get("assets", []):
                rel = f"release:{release['tagName']}/{asset['name']}"
                vector = model_vector(release.get("name", ""), rel)
                subs = subjects(release.get("name", ""), rel)
                size = int(asset.get("size", 0)); release_bytes += size
                nodes.append({
                    "i": len(nodes), "k": "release", "p": rel, "n": asset["name"], "b": size,
                    "e": Path(asset["name"]).suffix.casefold(), "t": "GitHub releases",
                    "d": (release.get("publishedAt") or "")[:10], "v": vector,
                    "m": [MODELS[i] for i, value in enumerate(vector) if value >= .42],
                    "s": subs, "h": str(asset.get("digest", "")).removeprefix("sha256:")[:12],
                    "mimetype": asset.get("contentType", "application/octet-stream"), "u": asset.get("url", ""),
                })

    # Exact, deterministic edge systems. Each layer is sparse and switchable.
    edges = {"model": [], "subject": [], "chronology": [], "provenance": [], "correlation": []}
    for dimension in range(5):
        members = sorted((n for n in nodes if n["v"][dimension] >= .42), key=lambda n: (-n["v"][dimension], n["p"]))
        edges["model"].extend([[members[i]["i"], members[i + 1]["i"], dimension] for i in range(len(members) - 1)])
    for subject in sorted({s for n in nodes for s in n["s"]}):
        members = sorted((n for n in nodes if subject in n["s"]), key=lambda n: n["p"])
        edges["subject"].extend([[members[i]["i"], members[i + 1]["i"], subject] for i in range(len(members) - 1)])
    dated = sorted((n for n in nodes if n["d"]), key=lambda n: (n["d"], n["p"]))
    edges["chronology"] = [[dated[i]["i"], dated[i + 1]["i"], dated[i]["d"]] for i in range(len(dated) - 1)]
    by_top = defaultdict(list)
    for n in nodes: by_top[n["t"]].append(n)
    for top, members in by_top.items():
        members.sort(key=lambda n: n["p"])
        edges["provenance"].extend([[members[i]["i"], members[i + 1]["i"], top] for i in range(len(members) - 1)])
    by_name = defaultdict(list)
    for n in nodes:
        stem = re.sub(r"[^a-z0-9]+", " ", Path(n["n"]).stem.casefold()).strip()
        if len(stem) >= 12: by_name[stem].append(n)
    for stem, members in by_name.items():
        if len(members) > 1:
            edges["correlation"].extend([[members[0]["i"], n["i"], stem[:80]] for n in members[1:]])

    payload = {
        "meta": {
            "title": "Q5 five-model corpus graph", "repo": repo.name,
            "generated": "2026-09-26", "models": MODELS,
            "node_count": len(nodes), "repository_files": sum(n["k"] == "file" for n in nodes),
            "release_assets": sum(n["k"] == "release" for n in nodes),
            "repository_bytes": sum(n["b"] for n in nodes if n["k"] == "file"),
            "release_bytes": release_bytes,
            "subjects": dict(Counter(s for n in nodes for s in n["s"])),
            "models_count": {MODELS[i]: sum(n["v"][i] >= .42 for n in nodes) for i in range(5)},
            "edge_counts": {name: len(values) for name, values in edges.items()},
            "method": "Path plus bounded text sampling; coordinates are retrieval signals, not claims about authorship or model cognition.",
        },
        "nodes": nodes, "edges": edges,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(json.dumps(payload["meta"], indent=2))


if __name__ == "__main__":
    main()
