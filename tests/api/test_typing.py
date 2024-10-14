"""Test completeness of stub with examples of re2 use."""

# pyright: reportPrivateUsage = false
from __future__ import annotations

from typing_extensions import assert_type

import re2


def test_typing_only_tests() -> None:
    _1: re2._Match[str] | None = re2.search(b"", "")
    _2: re2._Match[bytes] | None = re2.search(b"", b"")
    _3: re2._Match[bytes] | None = re2.search("", b"")
    _4: re2._Match[str] | None = re2.search("", "")

    _5: re2._Match[str] | None = re2.compile(b"").search("")
    _6: re2._Match[bytes] | None = re2.compile(b"").search(b"")
    _7: re2._Match[str] | None = re2.compile("").search("")
    _8: re2._Match[bytes] | None = re2.compile("").search(b"")

    assert assert_type(re2.sub(b"", "", ""), str) == ""
    assert assert_type(re2.sub("", b"", b""), bytes) == b""

    def repl_str(m: re2._Match[str]) -> str:
        return ""

    def repl_bytes(m: re2._Match[bytes]) -> bytes:
        return b""

    assert assert_type(re2.compile(b"").sub("", ""), str) == ""
    assert assert_type(re2.compile("").sub("", ""), str) == ""
    assert assert_type(re2.compile(b"").sub(repl_str, ""), str) == ""
    assert assert_type(re2.compile("").sub(b"", b""), bytes) == b""
    assert assert_type(re2.compile("").sub(repl_bytes, b""), bytes) == b""


def test_runtime_types() -> None:
    assert re2.sub(b"", "", "") == ""
    assert re2.sub("", b"", b"") == b""

    def repl_str(m: re2._Match[str]) -> str:
        return ""

    def repl_bytes(m: re2._Match[bytes]) -> bytes:
        return b""

    assert re2.compile(b"").sub("", "") == ""
    assert re2.compile("").sub("", "") == ""
    assert re2.compile(b"").sub(repl_str, "") == ""
    assert re2.compile("").sub(b"", b"") == b""
    assert re2.compile("").sub(repl_bytes, b"") == b""
