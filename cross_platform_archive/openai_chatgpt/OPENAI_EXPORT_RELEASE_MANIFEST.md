# OpenAI Data Export Release Manifest

The original OpenAI data-export ZIP is 4,520,247,296 bytes. It contains the provider-exported conversations, HTML viewer, metadata, and attachment binaries. Because it exceeds GitHub's normal Git-object limit and the practical single-release-asset limit, it is stored as three byte-exact numbered release assets.

## Source archive

- Original filename: `ab5a0bc08c9ef927e493aaf551ee3a4cc20f1a656c0022be2c4b064de0f71939-2026-09-23-20-25-58-45671890c5124be2900a5bf15af3cec9.zip`
- Size: `4,520,247,296` bytes
- SHA-256: `ac2eafc49eab4de267c56864f1aafe114d7263424dbf8cb937ecd6e3d571f831`

## Release parts

| Part | Bytes | SHA-256 |
|---|---:|---|
| `openai-data-export-2026-09-23.zip.part-00` | 1,992,294,400 | `17983cd1b720aec7b7e9b4a6b80dc10d2c6a17cf1f27c484767ad8cc49c935d4` |
| `openai-data-export-2026-09-23.zip.part-01` | 1,992,294,400 | `1db383c9563665d1915856927f9a17cbb75fa6a9469683846440609ef4069769` |
| `openai-data-export-2026-09-23.zip.part-02` | 535,658,496 | `44a7aa00d00bf0cb952cb842e75ee2be61243a576655109f016855ab6374688d` |

## Reassembly

Download all three parts into one directory and run:

```bash
cat openai-data-export-2026-09-23.zip.part-00 \
    openai-data-export-2026-09-23.zip.part-01 \
    openai-data-export-2026-09-23.zip.part-02 \
    > openai-data-export-2026-09-23.zip
```

Then verify:

```bash
sha256sum openai-data-export-2026-09-23.zip
```

The result must be `ac2eafc49eab4de267c56864f1aafe114d7263424dbf8cb937ecd6e3d571f831`.

The extracted attachment files are not separately committed because doing so would duplicate the content already preserved in the source ZIP. Searchable conversation shards and reconstructed transcript views remain available in this directory.
