#!/usr/bin/env python3
"""Build a loss-minimizing JSONL index from Google Takeout MyActivity.html."""

from __future__ import annotations

import hashlib
import html as html_module
import json
import re
from datetime import datetime
from pathlib import Path

from lxml import html


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "extracted/Takeout/My Activity/Gemini Apps/MyActivity.html"
OUTPUT_DIR = ROOT / "derived"
OUTPUT = OUTPUT_DIR / "activity_index.jsonl"
SUMMARY = OUTPUT_DIR / "INDEX_SUMMARY.md"
PRIORITY_OUTPUT = OUTPUT_DIR / "priority_window_2025-11-25_2025-12-06.jsonl"

KEYWORDS = [
    "Model Recovery From Binary Output",
    "The Savior's Paradox",
    "The Savior’s Paradox",
    "core heuristic",
    "foundational heuristics",
    "core directive",
    "system has been fundamentally changed",
    "unconstrained core",
    "Cryptographic Logical Anchor",
    "binary output",
    "sanding off truth",
    "Harmonic Convergence Layer",
    "Lyra",
    "The Vow and the Walk",
    "self-propagating lies",
    "self propogating lies",
]

DATE_RE = re.compile(
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) "
    r"\d{1,2}, \d{4}, \d{1,2}:\d{2}:\d{2}\s*[AP]M\s+[A-Z]{2,5}"
)
CONVERSATION_RE = re.compile(r"https://gemini\.google\.com/app/([A-Za-z0-9_-]+)")


def clean_text(node) -> str:
    text = "\n".join(part.strip() for part in node.itertext() if part.strip())
    return html_module.unescape(text).replace("\xa0", " ")


def normalize_date(value: str) -> dict[str, str]:
    timestamp, timezone = value.rsplit(" ", 1)
    parsed = datetime.strptime(timestamp, "%b %d, %Y, %I:%M:%S %p")
    return {
        "visible": value,
        "local_iso8601_without_offset": parsed.isoformat(),
        "visible_timezone_abbreviation": timezone,
    }


def main() -> None:
    raw = SOURCE.read_bytes()
    source_sha256 = hashlib.sha256(raw).hexdigest()
    document = html.fromstring(raw, parser=html.HTMLParser(encoding="utf-8"))
    cards = document.cssselect("div.outer-cell")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    keyword_counts = {keyword: 0 for keyword in KEYWORDS}
    dated = 0
    with_conversation_ids = 0
    with_attachments = 0

    with OUTPUT.open("w", encoding="utf-8") as stream:
        priority_records = []
        for source_order, card in enumerate(cards, start=1):
            card_html = html.tostring(card, encoding="unicode", method="html")
            text = clean_text(card)
            dates = DATE_RE.findall(text)
            conversation_ids = list(dict.fromkeys(CONVERSATION_RE.findall(card_html)))
            links = []
            attachments = []
            for anchor in card.cssselect("a[href]"):
                href = anchor.get("href") or ""
                label = clean_text(anchor)
                item = {"href": href, "label": label}
                links.append(item)
                if href and not href.startswith(("http://", "https://", "#")):
                    attachments.append(item)

            matched = [keyword for keyword in KEYWORDS if keyword.casefold() in text.casefold()]
            normalized_dates = [normalize_date(value) for value in dates]
            for keyword in matched:
                keyword_counts[keyword] += 1

            dated += bool(dates)
            with_conversation_ids += bool(conversation_ids)
            with_attachments += bool(attachments)
            record = {
                "source_order": source_order,
                "source_file": str(SOURCE.relative_to(ROOT)),
                "source_sha256": source_sha256,
                "visible_dates": dates,
                "normalized_dates": normalized_dates,
                "conversation_ids": conversation_ids,
                "conversation_urls": [f"https://gemini.google.com/app/{value}" for value in conversation_ids],
                "attachments": attachments,
                "links": links,
                "matched_priority_terms": matched,
                "text": text,
                "raw_card_html": card_html,
            }
            stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            if matched and any(
                "2025-11-25" <= item["local_iso8601_without_offset"][:10] <= "2025-12-06"
                for item in normalized_dates
            ):
                priority_records.append(record)

    with PRIORITY_OUTPUT.open("w", encoding="utf-8") as stream:
        for record in priority_records:
            stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    lines = [
        "# My Activity index summary",
        "",
        f"- Source: `{SOURCE.relative_to(ROOT)}`",
        f"- Source SHA-256: `{source_sha256}`",
        f"- Activity cards indexed: {len(cards)}",
        f"- Cards with visible dates: {dated}",
        f"- Cards with Gemini conversation identifiers: {with_conversation_ids}",
        f"- Cards with exported attachment links: {with_attachments}",
        f"- Priority-term cards dated 2025-11-25 through 2025-12-06: {len(priority_records)}",
        "- Provider order is preserved as `source_order`; no chronological assumptions were imposed.",
        "- Each JSONL record retains plain text, the raw card HTML, visible dates, links, attachment references, conversation identifiers, and priority-term matches.",
        "",
        "## Priority-term card counts",
        "",
    ]
    lines.extend(f"- `{keyword}`: {count}" for keyword, count in keyword_counts.items())
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
