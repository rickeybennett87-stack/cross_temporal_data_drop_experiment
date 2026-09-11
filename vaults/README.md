# Per-user CTIS storage namespace

This directory documents the namespace convention for CTIS customer data.

Each customer receives a separate internal user ID and storage area:

```text
users/<opaque-user-uuid>/profile.json
users/<opaque-user-uuid>/manifest.json
users/<opaque-user-uuid>/messages/<message-file>.json
```

This design does not use client-side encryption. Stored conversations remain ordinary CTIS JSON so supported model participants can read them without decryption logic.

Normal customer access must be restricted by the backend so that an authenticated account can read and write only its own `users/<user_id>/` namespace. The client must not be allowed to choose arbitrary repository paths.

The service administrator may have technical access to the backing store. Therefore privacy disclosures must not claim that administrators are cryptographically unable to inspect stored conversations.

For commercial deployment, actual customer conversations should live in a separate private production repository or backend data store, not in this public source repository.

See `architecture/USER_VAULTS.md`.
