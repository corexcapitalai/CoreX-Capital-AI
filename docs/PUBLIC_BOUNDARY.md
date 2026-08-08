# Public / Private Boundary

This file is the repository's primary disclosure-control policy.

## Allowed in this repository

- public product descriptions already intended for external audiences;
- high-level architecture and system-boundary diagrams;
- synthetic UI data and sample payloads;
- read-only illustrative API schemas;
- documentation, accessibility, security and contribution policies;
- mock clients and mock servers that cannot place trades or reach private services;
- public website links and public brand references.

## Explicitly excluded

The following must not be committed, copied, mirrored, generated from private code, or reconstructed here:

- proprietary signal-generation or trading algorithms;
- proprietary feature engineering, scoring formulas, model weights, prompts, thresholds, or training pipelines;
- order placement, broker routing, settlement, position management, or live execution code;
- real credentials, tokens, certificates, account identifiers, KYC/user data, private datasets, or production logs;
- internal deployment manifests, private hostnames, network topology, secrets-management configuration, or database credentials;
- source code or assets from any private CoreX repository;
- licensed third-party charting source, private charting credentials, or private integration implementation;
- confidential commercial terms, contracts, customer information, or non-public partner material.

## Review rule

When there is doubt, keep the material private. Public usefulness is not a reason to disclose implementation details that create security, intellectual-property, licensing, privacy, or contractual risk.

## Synthetic-data rule

Every example that resembles a price, confidence score, latency, win rate, risk metric, trade signal, account value, or execution result must be treated as illustrative unless an explicit source and verification method are documented.
