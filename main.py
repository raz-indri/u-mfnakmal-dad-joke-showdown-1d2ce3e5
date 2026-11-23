#!/usr/bin/env python3
"""Entry for make.fun's "Dad Joke Showdown" bounty (u-mfnakmal-dad-joke-showdown-1d2ce3e5).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one dad joke of at most 200 characters. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = "I named our Wi-Fi 'Martin Router King' because I have a stream — and like me, it buffers whenever the whole family needs it at once."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
