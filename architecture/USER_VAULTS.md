# CTIS Per-User Zero-Knowledge Vaults

## Goal

Every paying CTIS user receives an isolated storage namespace. Conversation content must remain unreadable to the service operator, repository administrator, hosting provider, and other users.

A GitHub folder is not itself an access-control boundary. GitHub repository administrators can read repository contents. Therefore CTIS user privacy is provided by client-side encryption, not by folder ACLs.

## Storage layout

Each account is assigned a random opaque vault identifier. Do not use email addresses, names, usernames, or billing identifiers in repository paths.

```text
vaults/
  6c3f4e8d-8b4d-4a2a-9c31-2b8f2bb1d605/
    vault.json
    index.enc.json
    messages/
      2cbca60c-6ffd-42c0-9e1c-3984a5433c14.enc.json
      40acdfd6-435d-40f8-87f5-bb8425cfc4e7.enc.json
```

Filenames are random UUIDs. Do not encode timestamps, model names, thread names, recipients, or conversation titles in paths.

## Encryption model

1. On first setup, the extension generates a random 256-bit Vault Master Key (VMK) locally using `crypto.getRandomValues`.
2. The user chooses a vault password/passphrase.
3. The extension derives a Key Encryption Key (KEK) locally from that password using a memory-hard password KDF. Preferred: Argon2id bundled inside the extension. A Web Crypto PBKDF2-HMAC-SHA-256 implementation may be used as a compatibility fallback with a deliberately high work factor.
4. A unique random salt is generated for the user's vault.
5. The VMK is wrapped/encrypted with the KEK using authenticated encryption.
6. Conversation payloads and the private vault index are encrypted with keys derived from the VMK using authenticated encryption such as AES-256-GCM.
7. The password, KEK, and plaintext VMK never leave the user's browser.
8. The service stores only ciphertext, salts, nonces, version/KDF parameters, and the wrapped VMK.

The VMK is separate from the password so users can change their password without re-encrypting every historical message. Only the wrapped VMK needs to be re-wrapped under the newly derived KEK.

## `vault.json`

This file is safe for the service to store because it contains no plaintext conversation content and no plaintext key.

Example:

```json
{
  "schema": "ctis-vault/1.0",
  "vault_id": "6c3f4e8d-8b4d-4a2a-9c31-2b8f2bb1d605",
  "crypto": {
    "kdf": "argon2id",
    "salt_b64": "...",
    "parameters": {
      "memory_kib": 19456,
      "iterations": 2,
      "parallelism": 1
    },
    "wrap": "aes-256-gcm",
    "wrapped_vmk_b64": "...",
    "wrap_nonce_b64": "..."
  }
}
```

## Encrypted message envelope

```json
{
  "schema": "ctis-ciphertext/1.0",
  "alg": "aes-256-gcm",
  "nonce_b64": "...",
  "ciphertext_b64": "..."
}
```

The plaintext inside the encrypted envelope may contain the normal CTIS message schema, including timestamps, participants, thread IDs, message text, and reply relationships. None of those fields should be exposed in the filename.

## Authentication is separate from encryption

Account authentication answers: **who may read/write ciphertext in this vault namespace?**

Vault encryption answers: **who can understand that ciphertext?**

The backend may know the account ID, subscription state, and opaque vault ID. It must not receive the vault password or VMK.

A customer who has paid but has not unlocked their vault can retrieve ciphertext but cannot decrypt it.

## Billing

Billing status should be stored outside the encrypted conversation vault and should contain only what is necessary to operate the subscription. Payment-card data should be handled by a payment processor rather than stored by CTIS.

The service may gate read/write API access based on subscription state, but billing logic must never possess a decryption key.

## Backend role

A backend service is required for a commercial multi-user deployment. Do not embed a GitHub write token in the public extension.

The backend should:

- authenticate the account;
- verify paid entitlement;
- map the account to one opaque `vault_id`;
- enforce that the account can access only that vault path;
- accept and return ciphertext envelopes;
- write/read those ciphertext objects in storage;
- reject attempts to address another user's vault;
- rate-limit abuse;
- keep an auditable access log containing object IDs but never decrypted content.

The backend should never:

- receive the vault password;
- receive the VMK in plaintext;
- decrypt conversation content;
- generate recoverable copies of user keys;
- expose repository credentials to the browser extension.

## Password loss

Zero-knowledge encryption has a consequence: if the user loses the vault password and has no recovery key, the administrator cannot decrypt their history.

Offer an optional recovery key generated locally during setup. It can wrap the VMK independently of the password. The recovery key should be shown once and saved by the user. CTIS should not retain a plaintext copy.

Do not offer an administrator 'master password'. That would defeat the privacy guarantee.

## Repository visibility

For production, the backing repository should be private even though user payloads are ciphertext. This limits metadata leakage and nuisance scraping. Encryption remains required because repository administrators still have repository access.

The public source repository can continue hosting extension and protocol code. Production user vault data should live in a separate private storage repository or purpose-built object store.

## Metadata leakage

Encryption does not automatically hide all metadata. A storage administrator may still see:

- vault existence;
- ciphertext object sizes;
- commit/write times;
- write frequency;
- billing/account records outside the vault.

Use opaque vault IDs and random object filenames to minimize correlation. If stronger metadata privacy is required later, move the ciphertext layer from Git history to an object store with padding/batching.

## Non-negotiable invariant

No plaintext CTIS customer conversation is ever committed to the shared production repository.
