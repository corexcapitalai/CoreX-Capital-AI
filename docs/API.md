# Public API Reference

The public API in this repository is an **illustrative, read-only contract**. It does not connect to production and cannot place orders.

The canonical schema is [`../openapi/public-api.yaml`](../openapi/public-api.yaml).

## Endpoints

### `GET /v1/health`

Returns a minimal service-health object for integration testing.

### `GET /v1/system`

Returns public-safe capability metadata: product name, API version, environment label, and supported public concepts.

### `GET /v1/signals/example`

Returns one synthetic signal/explainability object. Values are deliberately illustrative.

## Decision object philosophy

A signal object separates:

- `proposal` — the AI-facing suggestion;
- `governance` — deterministic state and reason codes;
- `explanation` — user-facing context;
- `disclaimer` — explicit statement that the payload is illustrative.

The public contract does not expose proprietary features, model internals, trading thresholds, account state, execution endpoints, or broker credentials.

## Versioning

Public examples use semantic API version labels. Breaking schema changes should increment the major version. Additive fields may be introduced in a backward-compatible minor release.
