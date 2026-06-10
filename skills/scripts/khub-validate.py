#!/usr/bin/env python3
"""Validate KHub workflow YAML artifacts without external dependencies."""

from __future__ import annotations

import pathlib
import re
import sys
from typing import Any

import yaml


NOTE_TYPES = {"seed", "cognition", "concept", "viewpoint", "playbook", "prediction"}
WRITE_OPS = {"create", "append", "split_new_note"}
DECISION_STATES = {"skip_duplicate", "no_fit", "needs_human_decision"}
REPORT_RESULTS = {"added", "updated", "skipped", "blocked", "conflict"}


def load_yaml(path: str | None) -> dict[str, Any]:
    if path:
        text = pathlib.Path(path).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        fail("input must be a YAML object")
    return data


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def require(data: dict[str, Any], *keys: str) -> None:
    for key in keys:
        if key not in data or data[key] in (None, ""):
            fail(f"missing required key: {key}")


def expect(value: Any, key: str, typ: type) -> None:
    if not isinstance(value, typ):
        fail(f"{key} must be {typ.__name__}")


def expect_bool(data: dict[str, Any], key: str, expected: bool | None = None) -> None:
    expect(data.get(key), key, bool)
    if expected is not None and data[key] is not expected:
        fail(f"{key} must be {str(expected).lower()}")


def expect_md_path(data: dict[str, Any], key: str) -> None:
    value = data.get(key)
    expect(value, key, str)
    if not value.endswith(".md"):
        fail(f"{key} must end with .md")


def expect_confidence(data: dict[str, Any]) -> None:
    value = data.get("confidence")
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        fail("confidence must be a number")
    if not 0 <= float(value) <= 1:
        fail("confidence must be between 0 and 1")


def validate_route_plan(data: dict[str, Any]) -> str:
    require(
        data,
        "kind",
        "intake_id",
        "source",
        "source_id",
        "timestamp",
        "normalized_title",
        "final_type",
        "target_area",
        "target_bucket",
        "template_id",
        "operation",
        "target_note_title",
        "target_note_path",
        "confidence",
        "review_needed",
        "write_blocked",
    )
    if data["kind"] != "route-plan":
        fail("kind must be route-plan")
    if data["final_type"] not in NOTE_TYPES:
        fail(f"unexpected final_type: {data['final_type']}")
    if data["operation"] not in WRITE_OPS:
        fail(f"route-plan operation must be one of {sorted(WRITE_OPS)}")
    expect_md_path(data, "target_note_path")
    expect_confidence(data)
    expect_bool(data, "review_needed")
    expect_bool(data, "write_blocked", False)
    return "route-plan"


def validate_decision_report(data: dict[str, Any]) -> str:
    require(
        data,
        "kind",
        "intake_id",
        "status",
        "source",
        "source_id",
        "timestamp",
        "raw_text",
        "agent_read",
        "suggested_next_decisions",
        "write_blocked",
    )
    if data["kind"] != "decision-report":
        fail("kind must be decision-report")
    if data["status"] not in DECISION_STATES:
        fail(f"unexpected decision status: {data['status']}")
    expect(data["suggested_next_decisions"], "suggested_next_decisions", list)
    if not data["suggested_next_decisions"]:
        fail("suggested_next_decisions must not be empty")
    expect_bool(data, "write_blocked", True)
    return "decision-report"


def validate_note_payload(data: dict[str, Any]) -> str:
    require(
        data,
        "kind",
        "intake_id",
        "operation",
        "final_type",
        "template_id",
        "target_note_title",
        "target_note_path",
        "frontmatter",
        "sections",
    )
    if data["kind"] != "note-payload":
        fail("kind must be note-payload")
    if data["operation"] not in WRITE_OPS:
        fail(f"note-payload operation must be one of {sorted(WRITE_OPS)}")
    if data["final_type"] not in NOTE_TYPES:
        fail(f"unexpected final_type: {data['final_type']}")
    expect_md_path(data, "target_note_path")
    expect(data["frontmatter"], "frontmatter", dict)
    require(data["frontmatter"], "source", "source_id")
    expect(data["sections"], "sections", dict)
    if not data["sections"]:
        fail("sections must not be empty")
    return "note-payload"


def validate_execution_report(data: dict[str, Any]) -> str:
    require(
        data,
        "kind",
        "intake_id",
        "operation",
        "result",
        "target_note_path",
        "template_id",
        "source_trace",
        "write_attempted",
    )
    if data["kind"] != "execution-report":
        fail("kind must be execution-report")
    if data["operation"] not in WRITE_OPS:
        fail(f"execution operation must be one of {sorted(WRITE_OPS)}")
    if data["result"] not in REPORT_RESULTS:
        fail(f"unexpected result: {data['result']}")
    expect_md_path(data, "target_note_path")
    expect(data["source_trace"], "source_trace", dict)
    require(data["source_trace"], "source", "source_id")
    expect_bool(data, "write_attempted")
    if data["result"] in {"blocked", "skipped"} and data["write_attempted"]:
        fail(f"{data['result']} reports must not set write_attempted: true")
    return data["result"]


def validate_any(data: dict[str, Any]) -> str:
    kind = data.get("kind")
    if kind == "route-plan":
        return validate_route_plan(data)
    if kind == "decision-report":
        return validate_decision_report(data)
    if kind == "note-payload":
        return validate_note_payload(data)
    if kind == "execution-report":
        return validate_execution_report(data)
    fail(f"unexpected kind: {kind}")


def check_multiline_package(root: pathlib.Path) -> None:
    for path in root.rglob("*"):
        if path.is_dir() or path.suffix not in {".md", ".yaml", ".yml", ".sh", ".csv"}:
            continue
        text = path.read_text(encoding="utf-8")
        if "\r\n" in text:
            fail(f"CRLF line endings found: {path}")
        if len(text) > 200 and "\n" not in text.rstrip("\n"):
            fail(f"large text file appears to be one line: {path}")
        if path.suffix == ".sh" and not text.startswith("#!"):
            fail(f"shell script missing shebang: {path}")
        if path.suffix == ".sh" and not re.match(r"^#! */", text):
            fail(f"shell script has invalid shebang: {path}")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        fail("usage: khub-validate.py <route|decision|payload|report|any|line-endings> [path]")
    mode = argv[1]
    path = argv[2] if len(argv) > 2 else None
    if mode == "line-endings":
        check_multiline_package(pathlib.Path(path or "skills"))
        print("line endings ok")
        return 0
    data = load_yaml(path)
    validators = {
        "route": validate_route_plan,
        "decision": validate_decision_report,
        "payload": validate_note_payload,
        "report": validate_execution_report,
        "any": validate_any,
    }
    if mode not in validators:
        fail(f"unknown mode: {mode}")
    result = validators[mode](data)
    print(f"validation ok: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
