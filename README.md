# CoreX Capital AI — Public Ecosystem Reference

[![CoreX Capital AI](https://img.shields.io/badge/CoreX-Capital%20AI-111827?style=flat-square)](https://corexcapitalai.com/)
[![CoreX Signal AI](https://img.shields.io/badge/Product-CoreX%20Signal%20AI-0f766e?style=flat-square)](https://corexsignalai.com/)
[![AxisOption](https://img.shields.io/badge/Ecosystem-AxisOption-1d4ed8?style=flat-square)](https://axisoption.com/)
[![Public Boundary](https://img.shields.io/badge/Scope-Public%20Reference-7c3aed?style=flat-square)](docs/PUBLIC_BOUNDARY.md)

> **Public reference edition.** This repository explains the publicly documented CoreX Capital AI ecosystem without exposing proprietary source code, production credentials, model weights, private infrastructure, internal datasets or licensed third-party source.

## What CoreX Capital AI is

CoreX Capital AI publicly positions itself as a **financial-technology infrastructure provider and AI company**. The ecosystem combines institutional-style real-time infrastructure, market intelligence, custom agentic systems, brokerage technology and independent control/governance concepts.

CoreX's white-label documentation explicitly distinguishes the parent company from a brokerage operator: CoreX builds and maintains technology infrastructure; it states that it does not hold client funds or act as the market counterparty.

## Ecosystem map

| Layer | Public product / capability | Role |
| --- | --- | --- |
| Parent infrastructure | **CoreX Capital AI** | AI, financial infrastructure, real-time systems, enterprise engineering |
| Enterprise product | **White-Label Brokerage Platform** | End-to-end brokerage infrastructure under a partner's brand |
| Intelligence product | **CoreX Signal AI** | Explainable, multi-timeframe market-intelligence and signal presentation |
| Trading product | **AxisOption** | Client-facing options platform whose site states its infrastructure is powered by CoreX Capital AI |
| Custom engineering | **Strategy OS™** | Converts manual strategies/objectives into dedicated AI and automation systems |
| Governance | **Physics Core + Autonomous Veto Protocol** | Independent control and risk-veto concepts outside probabilistic model confidence |

## Enterprise infrastructure

The public white-label product documents a complete stack rather than a front-end-only toolkit. It includes:

- web and mobile trading interfaces;
- trading, pricing and risk engines;
- administration portal and broker analytics dashboard;
- CRM and client lifecycle tooling;
- wallet and payment-provider integration;
- KYC and document-verification workflows;
- affiliate / introducing-broker management;
- configurable exposure and risk controls;
- reporting, notifications and messaging;
- multi-admin user management and RBAC;
- REST API integration surfaces;
- white-label, dedicated, managed and custom deployment models.

## Publicly documented technology

Across the CoreX Capital AI white-label material and CoreX Signal AI product site, the public stack includes concepts and technologies such as:

- WebSocket real-time delivery;
- Redis caching and pub/sub;
- asynchronous message queues;
- REST APIs;
- MongoDB and relational/ACID storage;
- PostgreSQL as listed by CoreX Signal AI;
- horizontal scaling, load balancing and container orchestration;
- auto-failover, monitoring, structured logs and alerting;
- TLS encryption, MFA, RBAC, signed/token-authenticated APIs, audit logging and DDoS/network controls;
- Python quantitative processing;
- signal-processing / ML ensemble layers;
- PWA delivery and Flask-SocketIO as documented by CoreX Signal AI;
- HMAC-SHA256 authentication and dual-pipeline/data-integrity concepts on the Signal AI architecture page.

CoreX Signal AI also publicly lists technology/data integrations including MetaTrader 5, Bloomberg, Refinitiv/LSEG, FactSet, S&P Global, ICE, TradingView, Binance, Cloudflare, PostgreSQL, Redis and MongoDB. Third-party names identify technologies/integrations listed by the product and do not imply endorsement.

## CoreX Signal AI

The public product presents an AI Command Center with explainability-oriented surfaces including cross-timeframe coherence, market-regime context, execution-optimization views, probabilistic forecasting, depth mapping, attribution/impact drivers, macro/NLP intelligence and factor analysis.

The product site explicitly labels dashboard previews and sample signal layouts as **simulated / illustrative**, not guaranteed performance.

## AxisOption

AxisOption is a separate client-facing options trading platform in the broader ecosystem. Its public materials describe:

- TradingView chart-based trading;
- one-click BUY / SELL interaction;
- forex, crypto, commodities and stocks from one terminal;
- demo and live environments;
- flexible expiry times;
- payout and expiry conditions shown before trade confirmation;
- multilingual access and 24/7 direct client support;
- CoreX Capital AI enterprise trading infrastructure as its technology foundation.

AxisOption has its own Terms of Service and Risk Disclosure. Financial markets involve risk of loss.

## Strategy OS™

Strategy OS™ is the custom-engineering path for traders, funds, asset managers, brokers and B2B platforms. The public process is described as:

1. define the strategy or objective;
2. design the custom system;
3. train the AI;
4. apply control and veto layers;
5. deliver the system and ownership model.

## Governance philosophy

A recurring public CoreX principle is that **AI confidence is not final authorization**. Probabilistic intelligence and strategy logic are presented as separate from independent control, stability and risk constraints. The Physics Core and Autonomous Veto Protocol represent this governance philosophy at a public conceptual level.

This repository does not publish the proprietary implementation, exact thresholds or internal execution logic behind those systems.

## Primary public sources

- CoreX Capital AI: https://corexcapitalai.com/
- CoreX About / Mission: https://corexcapitalai.com/about.html
- White-Label Infrastructure: https://corexcapitalai.com/white-label.html
- Strategy OS™: https://corexcapitalai.com/strategy.html
- Autonomous Veto Protocol: https://corexcapitalai.com/veto-protocol.html
- CoreX Signal AI: https://corexsignalai.com/
- AxisOption: https://axisoption.com/
- AxisOption Products: https://axisoption.com/products.html

## Repository map

| Path | Purpose |
| --- | --- |
| [`site/`](site/) | Public ecosystem homepage and technical overview |
| [`docs/`](docs/) | Product, architecture, security and disclosure documentation |
| [`openapi/`](openapi/) | Illustrative public-safe API contract for repository demonstration only |
| [`examples/`](examples/) | Synthetic local examples; not production services |
| [`scripts/`](scripts/) | Public-boundary validation |
| [`.github/`](.github/) | Repository automation and templates |

## Preview the public site

```bash
python -m http.server 8080 --directory site
```

Then open `http://localhost:8080`.

## Public/private boundary

Never place proprietary trading logic, model weights, internal thresholds, production credentials, user/account data, private datasets, broker secrets, private infrastructure details or licensed third-party source in this repository. See [`docs/PUBLIC_BOUNDARY.md`](docs/PUBLIC_BOUNDARY.md).

## Important disclosure

This repository is informational and is not a production trading system, investment advice, audited performance or a guarantee of future results. Where linked product websites display sample prices, confidence values, win-rate-style metrics or example signals, their own disclosures apply. Third-party trademarks remain the property of their respective owners.

---

Copyright © 2026 CoreX Capital AI. All rights reserved.
