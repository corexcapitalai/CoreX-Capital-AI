#!/usr/bin/env python3
"""Zero-dependency local mock API for the CoreX Capital AI public repository.

This server returns synthetic data only. It has no production credentials,
no broker connectivity, no private service access, and no execution endpoint.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

HOST = "127.0.0.1"
PORT = 8787
SAMPLE_PATH = Path(__file__).with_name("sample_signal.json")


def load_sample() -> dict[str, Any]:
    payload = json.loads(SAMPLE_PATH.read_text(encoding="utf-8"))
    payload["generated_at"] = datetime.now(UTC).isoformat().replace("+00:00", "Z")
    return payload


class Handler(BaseHTTPRequestHandler):
    server_version = "CoreXPublicMock/1.0"

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        if self.path == "/v1/health":
            self._send_json(200, {"status": "ok", "environment": "public-mock", "synthetic": True})
            return

        if self.path == "/v1/system":
            self._send_json(
                200,
                {
                    "product": "CoreX Capital AI",
                    "api_version": "1.0",
                    "environment": "public-mock",
                    "capabilities": [
                        "explainable-signal-contract",
                        "deterministic-governance-state",
                        "synthetic-demo-data",
                    ],
                    "synthetic": True,
                },
            )
            return

        if self.path == "/v1/signals/example":
            self._send_json(200, load_sample())
            return

        self._send_json(
            404,
            {
                "error": "not_found",
                "message": "This public mock exposes GET /v1/health, /v1/system and /v1/signals/example only.",
                "synthetic": True,
            },
        )

    def log_message(self, format: str, *args: object) -> None:
        print(f"[public-mock] {self.address_string()} - {format % args}")


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"CoreX public mock listening on http://{HOST}:{PORT}")
    print("Synthetic/read-only demonstration. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
