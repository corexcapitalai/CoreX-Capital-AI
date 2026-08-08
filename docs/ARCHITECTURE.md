# Public Reference Architecture

This document defines a public-safe architecture for discussing CoreX Capital AI without exposing private implementation details.

```mermaid
flowchart TB
  subgraph Sources[External Sources]
    M[Market Data]
    N[Context / News]
    C[Configuration]
  end

  subgraph Intake[Boundary 1 — Intake]
    V[Validation]
    Z[Normalization]
  end

  subgraph Intelligence[Boundary 2 — Intelligence]
    X[Feature & Context Layer]
    A[AI Orchestration]
    E[Explanation Builder]
  end

  subgraph Governance[Boundary 3 — Deterministic Governance]
    P[Policy Gates]
    R[Risk Gates]
    D[Decision State]
  end

  subgraph Surface[Boundary 4 — Public Surface]
    API[Read-only API Contract]
    UI[Dashboard / UI]
    O[Observability]
  end

  M --> V --> Z --> X
  N --> V
  C --> P
  X --> A --> E --> P
  P --> R --> D
  D --> API
  D --> UI
  D --> O
```

## Boundary responsibilities

### 1. Intake

Validate timestamps, symbols, schema, data type, and freshness before any downstream use. The reference design assumes malformed or stale inputs are rejected rather than silently repaired.

### 2. Intelligence

The AI layer may combine contextual and quantitative information. The public contract deliberately does not prescribe algorithms, model families, features, weights, training data, or decision thresholds.

### 3. Deterministic governance

Governance is represented as a separate layer from model inference. A model can produce a high-confidence recommendation that is still blocked by deterministic policy or risk rules. Public outputs should surface the final state and a reason code.

### 4. Public surface

The public surface exposes sanitized, versioned objects suitable for UI and integration prototypes. It contains no order-routing or private control-plane endpoints.

## Decision state model

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Held: insufficient context
  Proposed --> Vetoed: deterministic rule failed
  Proposed --> Cleared: all public-facing gates passed
  Held --> Proposed: context refreshed
  Cleared --> Published
  Vetoed --> [*]
  Published --> [*]
```

`Cleared` in this public model means only that the illustrative governance state passed. It is not a recommendation to trade and does not imply that a production execution system will act.

## Data minimization

Public objects should contain only fields required for product demonstration and integration planning. Avoid production hostnames, account identifiers, internal queue names, credentials, raw user data, exact proprietary thresholds, and model artifacts.
