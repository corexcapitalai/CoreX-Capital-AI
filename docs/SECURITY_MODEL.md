# Public Security Model

The reference architecture uses defense in depth while intentionally omitting production-specific controls and configuration.

## Core principles

### Trust boundaries

External data, client input, configuration, and AI-generated content are untrusted until validated. A public-facing system should define explicit schema, freshness, authorization, and provenance checks at each boundary.

### Least privilege

Read-only public interfaces should not share credentials or privileges with execution, administration, settlement, user-document, or production control-plane services.

### Deterministic controls outside the model

Model confidence is not an authorization mechanism. Risk, policy, entitlement, and execution permissions should be enforced by deterministic code and infrastructure controls.

### Auditability

Decision objects should include trace IDs, timestamps, schema versions, final decision states, and sanitized reason codes. Audit logs must avoid secrets and sensitive personal data.

### Secret hygiene

Secrets belong in a dedicated secrets manager or protected deployment environment, never in source control. Example values in this repository are intentionally fake.

## Threat categories considered

- malicious or malformed data ingestion;
- stale data and replay;
- prompt/context injection into AI-assisted workflows;
- over-trusting model confidence;
- authorization bypass between public and privileged services;
- secret leakage through source, logs, examples, or error messages;
- dependency and supply-chain compromise;
- accidental publication of private or licensed code.

## Public-repository control

`scripts/validate_public_repo.py` provides a lightweight pre-commit/CI check for common accidental disclosure patterns. It is not a substitute for enterprise secret scanning, code review, SAST, dependency review, or production security monitoring.
