# Product & Ecosystem Overview

This document summarizes the CoreX Capital AI ecosystem using only information published on the official public websites. It does **not** derive from private repositories, production configuration, internal models or licensed third-party source.

## 1. CoreX Capital AI — parent infrastructure layer

CoreX Capital AI publicly presents itself as a financial-technology infrastructure provider and AI company. Its product family connects real-time financial infrastructure, agentic AI, market intelligence, custom system development and deterministic governance concepts.

The enterprise white-label material explicitly states that CoreX is an infrastructure provider rather than a brokerage operator: CoreX builds and maintains technology and does not itself hold client funds or act as market counterparty.

Official source: https://corexcapitalai.com/

## 2. White-Label Brokerage Platform — enterprise B2B product

The white-label offering is described as an end-to-end brokerage infrastructure stack delivered under a partner's own brand.

Publicly documented modules include:

- web trading platform;
- mobile platform;
- trading engine;
- AI decision / analysis layer;
- administration portal;
- broker operational dashboard;
- CRM;
- multi-currency wallet and payment integration;
- KYC and verification workflows;
- affiliate / introducing-broker system;
- configurable risk controls;
- reporting and analytics;
- notification / messaging infrastructure;
- user management and RBAC.

The platform architecture publicly references API Gateway, WebSocket, load balancing, trading and risk engines, pricing/liquidity control, databases, cache/queue layers, reporting, AI/analysis/monitoring/automation and operator systems.

Technology descriptions include Redis, asynchronous message queues, MongoDB, relational ACID storage, multi-region backup, horizontal scaling, container orchestration, auto-failover, monitoring/logging/alerting and REST APIs.

Deployment models include white-label, dedicated deployment, managed infrastructure and custom development.

Official source: https://corexcapitalai.com/white-label.html

## 3. CoreX Signal AI — intelligence product

CoreX Signal AI is the ecosystem's market-intelligence and signal-presentation product.

Its public product page documents an institutional-style AI Command Center with surfaces for:

- multi-timeframe / cross-timeframe coherence;
- directional bias, confidence, regime and risk context;
- execution-optimization views;
- probabilistic / Monte Carlo forecasting;
- institutional depth mapping;
- attribution and impact drivers;
- market-regime pulse;
- macro / NLP intelligence;
- factor-cluster analysis;
- explainable AI;
- sample signal layouts;
- chart and signal presentation.

The public architecture describes an MT5 market-data source, Python quant engine, signal processing, ML ensemble and risk engine, Flask-SocketIO relay, WebSocket delivery and a PWA client dashboard. It also lists HMAC-SHA256 authentication, dual-pipeline delivery, atomic data-integrity concepts and global CDN delivery.

The product publicly lists integrations/technologies including MetaTrader 5, Bloomberg, Refinitiv/LSEG, FactSet, S&P Global, ICE, Cloudflare, TradingView, Binance, PostgreSQL, Redis and MongoDB. Third-party names do not imply endorsement.

The product page explicitly labels dashboard previews and sample layouts as simulated/illustrative; displayed metrics are not guarantees of future results.

Official source: https://corexsignalai.com/

## 4. AxisOption — client-facing trading product

AxisOption is a professional options trading platform whose public website states that its trading infrastructure is powered by CoreX Capital AI.

Publicly described capabilities include:

- chart-based trading through TradingView;
- one-click BUY / SELL interaction;
- forex, crypto, commodities and stocks;
- demo and live platform modes;
- virtual demo balance;
- multiple expiry durations;
- payout and expiry rules shown before trade confirmation;
- direct client support via live chat and email;
- multilingual platform access.

AxisOption is a separate client-facing product with its own terms, risk disclosure and jurisdictional availability. Financial markets involve substantial risk of loss.

Official sources:

- https://axisoption.com/
- https://axisoption.com/products.html
- https://axisoption.com/about.html

## 5. Strategy OS™ — custom AI & automation engineering

Strategy OS™ is CoreX's custom engineering service for individual traders, funds/asset managers, brokers and B2B platforms.

The public offering includes manual-strategy automation, intelligent assistants, custom AI-driven signal systems, custom asset-management platforms, market simulation/backtesting, algorithmic-execution architecture, pricing engines, market simulation, B-Book infrastructure, multilingual analytics and stress/scalability simulation.

The documented process is:

1. define strategy or objective;
2. design custom system;
3. train the AI;
4. apply control and veto layers;
5. delivery and ownership.

Official source: https://corexcapitalai.com/strategy.html

## 6. Physics Core — control-theory infrastructure concept

The CoreX homepage describes the Physics Core as a proprietary matching-engine / infrastructure concept based on industrial control theory (PID). The public About material further frames CoreX's philosophy around independent physical/control constraints above probabilistic AI decisions.

This repository documents only that public role. The proprietary implementation is not included.

Official sources:

- https://corexcapitalai.com/
- https://corexcapitalai.com/about.html

## 7. Autonomous Veto Protocol — governance concept

CoreX publicly describes the Autonomous Veto Protocol as an independent supervisory/control layer intended to block operations when defined safety, stability or risk conditions are breached. A central public principle is that an AI decision can be rejected independently of model confidence.

Some marketing language on the dedicated public page uses strong or absolute descriptions. This repository does not reinterpret those statements as guarantees of financial performance or risk elimination; it records the architectural concept only.

Official source: https://corexcapitalai.com/veto-protocol.html

## 8. Shared technology themes

Across the public product family, the recurring technical themes are:

- real-time market-data processing;
- WebSocket-based delivery;
- Python quantitative / AI processing;
- model ensembles and explainability;
- deterministic risk/control separation;
- modular service architecture;
- API-driven integration;
- Redis and queue-based real-time systems;
- document and relational data stores;
- horizontal scalability and failover;
- observability, logs and alerts;
- encryption, RBAC/MFA and auditability;
- multilingual client and intelligence surfaces.

## 9. Intended audiences

### Individual / professional traders

Market intelligence, trading interfaces and custom strategy automation.

### Funds & asset managers

Custom AI platforms, market simulation/backtesting and risk-aware automation.

### Brokers

White-label infrastructure, pricing/risk controls, CRM/KYC, payment systems, back office and operational analytics.

### B2B / financial-technology partners

Dedicated infrastructure, APIs, managed deployment, multi-brand configurations and custom modules.

## 10. Public/private boundary

This public overview intentionally does not include:

- production source code;
- private repositories;
- exact proprietary algorithms or thresholds;
- model weights or internal training data;
- credentials or production configuration;
- internal broker/execution secrets;
- licensed TradingView or other third-party source code.

For disclosure rules, see [`PUBLIC_BOUNDARY.md`](PUBLIC_BOUNDARY.md).
