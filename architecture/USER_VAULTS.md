# CTIS Per-User Conversation Namespaces

## Goal

Every CTIS customer receives a separate storage namespace. The extension and backend must route each user's CTIS conversation only into that user's folder.

This design intentionally does **not** use client-side encryption. The repository or service administrator can inspect stored conversation data if necessary. The isolation boundary is application-level user separation, not cryptographic secrecy from the administrator.

## Storage layout

Each account is assigned a stable internal user ID. Prefer an opaque UUID rather than an email address or display name.

```text
users/
  6c3f4e8d-8b4d-4a2a-9c31-2b8f2bb1d605/
    profile.json
    manifest.json
    messages/
      2026-09-11T12-00-00Z__message-id.json
      2026-09-11T12-00-04Z__message-id.json
```

Each user's model traffic, replies, thread state, and conversation metadata live only inside that user's namespace.

## Isolation rules

The backend must:

- authenticate the customer account;
- resolve that account to exactly one internal `user_id`;
- verify paid entitlement before allowing service use;
- ignore any user-supplied folder path;
- derive storage paths from the authenticated account's server-side `user_id`;
- reject cross-user reads and writes;
- never expose repository credentials to the browser extension;
- keep admin access separate from normal customer access.

The browser extension should send only authenticated requests and conversation payloads. It should not decide which repository folder it owns by constructing arbitrary paths.

## Admin access

The system administrator may have access to the backing repository or storage layer and therefore may technically inspect user conversation data. Product disclosures and the privacy policy must not claim that administrators are cryptographically unable to read stored conversations.

Operational policy should still treat customer conversations as confidential and limit routine admin access to troubleshooting, abuse investigation, legal compliance, or maintenance needs.

## Billing

Billing status is separate from conversation storage. Store only the subscription/account identifiers needed for entitlement checks. Payment-card data should remain with the chosen payment processor rather than in CTIS.

The extension should behave as disabled for unpaid or expired accounts except for account/billing management surfaces.

## Public source vs production data

The source repository may remain public.

Production customer conversations should not be stored in the public source repository. Use a separate private production repository or backend data store with the same `users/<user_id>/...` namespace convention.

## Model compatibility

Because stored CTIS messages remain ordinary JSON rather than ciphertext, any supported model participant can read the authenticated user's conversation without an extra decryption step. This keeps the cross-model protocol simple and avoids requiring each model integration to implement key management.

## Non-negotiable invariant

A normal customer session can only read and write its own authenticated `users/<user_id>/` namespace.
