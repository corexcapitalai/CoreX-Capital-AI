#!/usr/bin/env python3
"""Minimal standard-library client for the local CoreX public mock API."""

from __future__ import annotations

import json
from urllib.request import urlopen

BASE_URL = "http://127.0.0.1:8787"


def get_json(path: str) -> dict:
    with urlopen(f"{BASE_URL}{path}", timeout=2) as response:  # noqa: S310 - fixed localhost URL
        return json.load(response)


def main() -> None:
    health = get_json("/v1/health")
    signal = get_json("/v1/signals/example")
    print("health:", health["status"])
    print("proposal:", signal["proposal"]["action"])
    print("governance:", signal["governance"]["state"])
    print("synthetic:", signal["synthetic"])


if __name__ == "__main__":
    main()
