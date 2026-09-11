# `vaults/` is a ciphertext-only namespace

This directory documents the production storage convention for CTIS user vaults.

**Do not commit plaintext customer conversations here.**

Every customer is assigned a random opaque vault ID. The conceptual layout is:

```text
vaults/<opaque-vault-uuid>/vault.json
vaults/<opaque-vault-uuid>/index.enc.json
vaults/<opaque-vault-uuid>/messages/<random-object-uuid>.enc.json
```

The folder name must not contain a person's name, email address, billing ID, model provider, thread title, or timestamp.

All conversation content and private indices are encrypted in the user's browser before storage. Repository administrators may be able to see ciphertext and metadata, but must not possess the keys required to decrypt customer content.

For a commercial deployment, actual customer vault data should be written to a separate private production repository or purpose-built object store rather than this public source repository. See `architecture/USER_VAULTS.md`.
