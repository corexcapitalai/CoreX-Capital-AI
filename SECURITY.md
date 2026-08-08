# Security Policy

## Reporting a vulnerability

Please do **not** disclose security vulnerabilities in public issues, discussions, pull requests, or social media.

Use GitHub's private vulnerability reporting / Security Advisory mechanism for this repository when available. If that channel is unavailable, use the official contact route published on https://corexcapitalai.com/ and clearly mark the message as a security report.

A useful report should include:

- affected public component and version or commit;
- clear reproduction steps;
- security impact;
- proof of concept that does not access or alter third-party data;
- suggested mitigation, if known.

## Scope

This public repository contains demonstration and documentation surfaces only. Production services, private infrastructure, credentials, proprietary models, broker execution systems, internal datasets, and licensed third-party source are not in scope for testing through this repository.

Do not attempt to obtain access to systems or data that you are not explicitly authorized to test.

## Secret handling

No real secrets belong in this repository. Examples must use obviously synthetic placeholders. If a real credential is accidentally committed, treat it as compromised and rotate/revoke it immediately; deleting it from Git history alone is not sufficient.
