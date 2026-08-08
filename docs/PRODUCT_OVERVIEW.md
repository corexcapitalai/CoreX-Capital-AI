# Product Overview

CoreX Capital AI presents a layered approach to AI-assisted financial infrastructure: probabilistic intelligence can propose or explain an action, while deterministic controls can enforce policy and risk boundaries before that action reaches a user or downstream system.

## Public product pillars

### Physics Core

A public-facing name for the deterministic control layer. The public repository describes its role—not its proprietary implementation. Its job in the reference architecture is to turn policy and system constraints into explicit allow, hold, or veto outcomes.

### CoreX Signal AI

The signal and intelligence experience focuses on presenting market context together with confidence, reason codes, time horizon, and risk context. Public examples are synthetic and demonstrate interface structure only.

### Strategy OS™

A conceptual orchestration layer for converting a strategy's intent into structured inputs, rules, model calls, checks, and observable outputs. Proprietary strategy conversion and execution logic is excluded.

### Autonomous Veto Protocol

A deterministic guardrail pattern: an AI recommendation is never assumed to be executable merely because a model produced it. Policy and risk checks can veto or hold the action and return a reason.

## Design principles

1. **Explainability before action** — outputs should carry human-readable reason codes and context.
2. **Deterministic guardrails** — policy and risk constraints sit outside probabilistic model confidence.
3. **Auditability** — public contracts model trace identifiers, timestamps, schema versions, and decision states.
4. **Separation of concerns** — data ingestion, intelligence, governance, presentation, and execution are distinct boundaries.
5. **Public/private separation** — public documentation must remain useful without exposing proprietary implementation details.

## What this repository is not

It is not the production engine, a trading bot, a broker integration package, a model distribution channel, or a source for real-time financial advice.
