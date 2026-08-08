# Public Source Provenance

Last reviewed: 2026-08-08

This document records the first-party public sources used to describe the CoreX Capital AI ecosystem in this repository. It exists to keep product copy, architecture descriptions and public claims traceable without accessing private repositories, production systems or licensed third-party source code.

## Source policy

Public statements are handled in four categories:

1. **Published product capability** — a capability explicitly described on an official CoreX Capital AI, CoreX Signal AI or AxisOption page.
2. **Published architecture description** — a technology, component or data-flow description explicitly published by the official product.
3. **Company-published claim** — a performance, investment, milestone, security or implementation statement published by CoreX/AxisOption that this repository does not independently audit.
4. **Illustrative/demo material** — example prices, scores, win-rate-style figures, latency displays or simulated trading states that the source page itself identifies as illustrative/demo data.

The repository must not silently convert categories 3 or 4 into independently verified facts.

## CoreX Capital AI

### Main product surface
- https://corexcapitalai.com/
- Used for: parent positioning, Physics Core, CoreX Signal AI, Strategy OS™, Autonomous Veto Protocol and company navigation.

### Company / mission
- https://corexcapitalai.com/about.html
- Used for: founding question, mission, Agentic Wealth, Autonomous Veto and Sovereign Infrastructure philosophy.

### White-label brokerage infrastructure
- https://corexcapitalai.com/white-label.html
- Used for: infrastructure-provider boundary, web/mobile trading, trading/risk/pricing layers, admin, broker dashboard, CRM, wallet/payments, KYC, affiliate/IB, reporting, messaging, RBAC, APIs, security, customization, deployment models and engagement process.

### Strategy OS™
- https://corexcapitalai.com/strategy.html
- Used for: trader/fund/broker use cases, strategy conversion, custom AI/infrastructure, simulation/backtesting, control layers and delivery/ownership model.

### Autonomous Veto Protocol
- https://corexcapitalai.com/veto-protocol.html
- Used for: deterministic hard-stop, independent supervisory layer, PID/control-theory language, monitoring, feedback and published governance concepts.
- Note: strong absolute implementation/performance language on the source page is treated as a company-published claim, not independently benchmarked by this repository.

### Founder profile
- https://corexcapitalai.com/founder.html
- Used for: public executive title, technical/research orientation, systems-engineering scope and published personal seed-investment statement.

### News & Press
- https://corexcapitalai.com/news/
- Used for: company-published R&D, platform, infrastructure and investment milestones.
- Milestones are identified as first-party announcements, not independent press verification.

## CoreX Signal AI

### Product and architecture
- https://corexsignalai.com/
- Used for: AI Command Center, cross-timeframe coherence, execution context, probabilistic/Monte Carlo forecasting, institutional depth map, attribution, market regime, macro/NLP, factor clusters and explainability.
- Published architecture used here: MT5 broker data → Python Quant Engine → Flask-SocketIO → WebSocket → PWA dashboard.
- Public architecture also lists HMAC-SHA256, dual-pipeline delivery, atomic data integrity, 9 timeframes × 7+ symbols, 11-language real-time client, sub-200 ms architecture target, 99.9% uptime target and global CDN edge.
- Third-party technologies/data brands listed by the product include MetaTrader 5, Bloomberg, Refinitiv/LSEG, FactSet, S&P Global, ICE Data, TradingView, Binance, Cloudflare, PostgreSQL, Redis and MongoDB.
- Brand references do not imply endorsement.
- The official product labels dashboard previews and sample signal layouts as simulated/illustrative; this repository preserves that distinction.

## AxisOption

### Main platform
- https://axisoption.com/
- Used for: professional options positioning, TradingView chart interaction, multi-asset markets, transparent conditions, account operations, support and CoreX-powered infrastructure statement.

### Products / demo terminal
- https://axisoption.com/products.html
- Used for: demo/live experience, one-click BUY/SELL, demo balance, expiry examples, cancellation interface, product capabilities and public product family (Binary, Turbo, Range and One-Touch Options).

### Company / technology relationship
- https://axisoption.com/about.html
- Used for: company history, published 2018 launch, 2020+ CoreX infrastructure integration, direct support, multilingual presence, corporate information and description of the CoreX relationship as an industry-standard white-label arrangement.

### Terms / risk disclosure
- https://axisoption.com/terms.html
- Used for: age/eligibility, risk notice, technology-provider statement and product-specific legal boundary.

### Contact
- https://axisoption.com/contact.html
- Used for: published support channels and international-presence information where referenced.

## Third-party references

Third-party names shown in this repository are included only when the official product sites publicly list them as technologies, data sources, charting/infrastructure components or integrations. Their trademarks remain the property of their respective owners. Listing does not imply sponsorship, endorsement or a relationship beyond what the official product source states.

## Private-source exclusion

This provenance file and the public portal were prepared without using private CoreX repositories, private model artifacts, production credentials, internal datasets, confidential thresholds, private broker configuration or licensed TradingView source code.
