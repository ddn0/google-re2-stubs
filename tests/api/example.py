"""Test completeness of stub with examples of re2 use."""

import re2


def str_match() -> None:
    pat = re2.compile(r"pattern")
    m_str = pat.match("text")
    if m_str:
        assert isinstance(m_str.group(0), str)


def bytes_match() -> None:
    pat = re2.compile(b"pattern")
    m_bytes = pat.match(b"text")
    if m_bytes:
        assert isinstance(m_bytes.group(0), bytes)
