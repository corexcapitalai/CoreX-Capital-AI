#!/usr/bin/env python3
"""Lightweight public-boundary validator for this repository.

The goal is to catch common accidental disclosures before they reach the
public branch. This is defense in depth, not a replacement for secret scanning,
review, SAST, dependency analysis, or legal/licensing review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = ROOT / "site"

REQUIRED = (
    "README.md",
    "LICENSE.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "docs/PUBLIC_BOUNDARY.md",
    "docs/ARCHITECTURE.md",
    "docs/PRODUCT_OVERVIEW.md",
    "docs/SOURCES.md",
    "openapi/public-api.yaml",
    "examples/sample_signal.json",
    "site/index.html",
    "site/signal-ai.html",
    "site/brokerage-infrastructure.html",
    "site/axisoption.html",
    "site/strategy-os.html",
    "site/governance.html",
    "site/technology.html",
    "site/about.html",
    "site/404.html",
    "site/styles.css",
    "site/app.js",
    "site/assets/corex-mark.svg",
    "site/robots.txt",
    "site/sitemap.xml",
    "site/.nojekyll",
)

SKIP_PARTS = {".git", "__pycache__", ".venv", "venv", "node_modules"}
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".js",
    ".json",
    ".yaml",
    ".yml",
    ".html",
    ".css",
    ".svg",
    ".xml",
    ".toml",
}

# Deliberately conservative patterns for credential-like material. Examples in
# documentation should use obviously synthetic placeholders that do not match.
# The GitHub expression intentionally includes ghs_ installation tokens; the
# length is open-ended so both legacy and newer stateless token formats match.
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    "generic bearer token": re.compile(r"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._~+/=-]{20,}"),
}

# File types / names that should never appear in this public reference repo.
DISALLOWED_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".onnx", ".pt", ".pth", ".h5", ".joblib"}
DISALLOWED_NAMES = {".env", "secrets.json", "credentials.json", "production.env"}
ALLOWED_SITE_DOTFILES = {".nojekyll"}


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "Makefile"}:
            files.append(path)
    return files


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required public file: {relative}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name.lower() in DISALLOWED_NAMES or path.suffix.lower() in DISALLOWED_SUFFIXES:
            errors.append(f"disallowed public artifact: {path.relative_to(ROOT)}")

    # The Pages artifact intentionally includes hidden files so .nojekyll is
    # deployed. Restrict the deployable site directory to that one known dotfile.
    if SITE_ROOT.is_dir():
        for path in SITE_ROOT.rglob("*"):
            if not path.is_file():
                continue
            hidden_parts = [part for part in path.relative_to(SITE_ROOT).parts if part.startswith(".")]
            if hidden_parts and path.name not in ALLOWED_SITE_DOTFILES:
                errors.append(f"unexpected hidden deployable file: {path.relative_to(ROOT)}")

    text_files = iter_text_files()
    for path in text_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"unexpected non-UTF8 text file: {path.relative_to(ROOT)}")
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} in {path.relative_to(ROOT)}")

    if errors:
        print("Public repository validation FAILED:\n")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Public repository validation passed ({len(text_files)} text files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
