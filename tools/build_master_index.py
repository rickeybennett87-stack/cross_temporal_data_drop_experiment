#!/usr/bin/env python3
import hashlib
import json
import mimetypes
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {
    'MASTER_ARCHIVE_INDEX.jsonl',
    'MASTER_ARCHIVE_INDEX.md',
    'SHA256SUMS.txt',
}

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def section(path):
    first = path.parts[0] if path.parts else 'root'
    if first == 'cross_platform_archive' and len(path.parts) > 1:
        return '/'.join(path.parts[:2])
    if first == 'gemini_archive_reconstruction' and len(path.parts) > 1:
        return '/'.join(path.parts[:2])
    return first

def main():
    records = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or '.git' in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if rel.as_posix() in EXCLUDED:
            continue
        stat = path.stat()
        records.append({
            'record_type': 'repository_file',
            'path': rel.as_posix(),
            'section': section(rel),
            'bytes': stat.st_size,
            'sha256': digest(path),
            'extension': path.suffix.lower(),
            'mime_type': mimetypes.guess_type(path.name)[0] or 'application/octet-stream',
        })

    releases_path = ROOT / 'RELEASE_ASSETS.json'
    if releases_path.exists():
        releases = json.loads(releases_path.read_text(encoding='utf-8'))
        for release in releases:
            for asset in release.get('assets', []):
                records.append({
                    'record_type': 'github_release_asset',
                    'path': f"release://{release['tagName']}/{asset['name']}",
                    'section': 'github_releases',
                    'bytes': asset.get('size'),
                    'sha256': (asset.get('digest') or '').removeprefix('sha256:'),
                    'mime_type': asset.get('contentType') or 'application/octet-stream',
                    'release_tag': release['tagName'],
                    'release_name': release.get('name'),
                    'url': asset.get('url'),
                })

    jsonl = ROOT / 'MASTER_ARCHIVE_INDEX.jsonl'
    with jsonl.open('w', encoding='utf-8') as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')

    file_records = [r for r in records if r['record_type'] == 'repository_file']
    with (ROOT / 'SHA256SUMS.txt').open('w', encoding='utf-8') as stream:
        for record in file_records:
            stream.write(f"{record['sha256']}  {record['path']}\n")

    counts = Counter(r['section'] for r in records)
    total_bytes = sum((r.get('bytes') or 0) for r in records)
    md = ROOT / 'MASTER_ARCHIVE_INDEX.md'
    with md.open('w', encoding='utf-8') as stream:
        stream.write('# Master Archive Index\n\n')
        stream.write('This index covers every repository file except the three generated master-index/checksum files, which are excluded to prevent circular self-hashes. GitHub release assets are indexed separately in the same JSONL catalog.\n\n')
        stream.write(f'- Indexed records: **{len(records):,}**\n')
        stream.write(f'- Repository files: **{len(file_records):,}**\n')
        stream.write(f'- GitHub release assets: **{len(records) - len(file_records):,}**\n')
        stream.write(f'- Indexed bytes: **{total_bytes:,}**\n\n')
        stream.write('## Sections\n\n| Section | Records |\n|---|---:|\n')
        for name, count in sorted(counts.items()):
            stream.write(f'| `{name}` | {count:,} |\n')
        stream.write('\n## High-Value Entry Points\n\n')
        stream.write('- [`README.md`](README.md) — archive purpose, provenance rules, and navigation.\n')
        stream.write('- [`gemini_archive_reconstruction/README.md`](gemini_archive_reconstruction/README.md) — Gemini reconstruction map.\n')
        stream.write('- [`gemini_archive_reconstruction/manifests/manifest.xml`](gemini_archive_reconstruction/manifests/manifest.xml) — OCR and direct-HTML evidence manifest.\n')
        stream.write('- [`gemini_archive_reconstruction/concept_timeline/TIMELINE.md`](gemini_archive_reconstruction/concept_timeline/TIMELINE.md) — chronological Lyra, sixth-bullet, HCL, TMS, and MRS evidence.\n')
        stream.write('- [`gemini_archive_reconstruction/concept_timeline/chronological_evidence.jsonl`](gemini_archive_reconstruction/concept_timeline/chronological_evidence.jsonl) — machine-readable concept evidence.\n')
        stream.write('- [`cross_platform_archive/README.md`](cross_platform_archive/README.md) — ChatGPT and Copilot archive guide.\n')
        stream.write('- [`RELEASE_ASSETS.json`](RELEASE_ASSETS.json) — large artifacts stored outside normal Git objects.\n')
        stream.write('\n## Machine Retrieval\n\nUse `MASTER_ARCHIVE_INDEX.jsonl` to filter by `section`, `path`, `extension`, `mime_type`, `bytes`, or `sha256`. A `release://` path identifies a GitHub release asset and includes its direct download URL.\n')

if __name__ == '__main__':
    main()
