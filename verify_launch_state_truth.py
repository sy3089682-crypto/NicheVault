#!/usr/bin/env python3
"""Verify that NicheVault public conversion surfaces stay truthful by default.

This script encodes the repo's production-trust contract for the two primary
visitor-facing conversion pages:
- index.html
- report-landing-page.html

It is intentionally lightweight and dependency-free so it can run locally or in
future CI without extra tooling.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FILES = {
    "landing": ROOT / "index.html",
    "report": ROOT / "report-landing-page.html",
    "server": ROOT / "server.py",
    "launch_state": ROOT / "launch-state.js",
    "contract": ROOT / "submission-message-contract.json",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def require_contains(content: str, needle: str, label: str, failures: list[str]) -> None:
    if needle not in content:
        fail(f"Missing {label}: {needle}", failures)


def require_not_contains(content: str, needle: str, label: str, failures: list[str]) -> None:
    if needle in content:
        fail(f"Found blocked {label}: {needle}", failures)


def load_contract() -> dict:
    with FILES["contract"].open(encoding="utf-8") as handle:
        return json.load(handle)


def verify_files_exist(failures: list[str]) -> None:
    for label, path in FILES.items():
        if not path.exists():
            fail(f"Missing required file for {label}: {path.name}", failures)


def verify_page_state_wiring(landing: str, report: str, failures: list[str]) -> None:
    for label, content in (("index.html", landing), ("report-landing-page.html", report)):
        require_contains(content, "launch-state.js", f"shared launch-state include in {label}", failures)
        require_contains(content, 'data-launch-state="', f"launch-state root marker in {label}", failures)
        require_contains(content, 'role="status"', f"accessible status region role in {label}", failures)
        require_contains(content, 'aria-live="polite"', f"accessible status region politeness in {label}", failures)


def verify_blocked_strings(
    landing: str,
    report: str,
    server: str,
    contract: dict,
    failures: list[str],
) -> None:
    blocked = contract.get("guardrails", {}).get("blockedUntilRealDeliveryOrCheckoutIsVerified", [])
    target_surfaces = {
        "index.html": landing,
        "report-landing-page.html": report,
        "server.py": server,
    }

    for phrase in blocked:
        for label, content in target_surfaces.items():
            require_not_contains(content, phrase, label, failures)

    require_not_contains(landing, "Join Free", "launch-ready landing CTA copy", failures)
    require_not_contains(report, "Get the Report for $49", "purchase-ready report CTA copy", failures)
    require_not_contains(report, "Secure PayPal checkout", "live checkout trust copy", failures)
    require_not_contains(report, "Instant download", "instant-delivery copy", failures)


def verify_contract_alignment(launch_state: str, contract: dict, failures: list[str]) -> None:
    require_contains(launch_state, "LANDING_COPY", "landing copy map in launch-state.js", failures)
    require_contains(launch_state, "REPORT_COPY", "report copy map in launch-state.js", failures)

    landing_prelaunch = (
        contract.get("landing", {})
        .get("prelaunch", {})
        .get("success", "")
    )
    report_prelaunch = (
        contract.get("report", {})
        .get("prelaunch", {})
        .get("status", "")
    )

    if landing_prelaunch:
        require_contains(
            launch_state,
            landing_prelaunch,
            "landing prelaunch success copy in launch-state.js",
            failures,
        )

    if report_prelaunch:
        require_contains(
            launch_state,
            report_prelaunch,
            "report prelaunch status copy in launch-state.js",
            failures,
        )


def main() -> int:
    failures: list[str] = []
    verify_files_exist(failures)

    if failures:
        print("Launch-state truth verification failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    landing = read_text(FILES["landing"])
    report = read_text(FILES["report"])
    server = read_text(FILES["server"])
    launch_state = read_text(FILES["launch_state"])
    contract = load_contract()

    verify_page_state_wiring(landing, report, failures)
    verify_blocked_strings(landing, report, server, contract, failures)
    verify_contract_alignment(launch_state, contract, failures)

    if failures:
        print("Launch-state truth verification failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Launch-state truth verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
