"""Dad Joke Showdown entry.

Writes a single dad joke (one line, at most 200 characters) to the
output file the make.fun program/v1 harness reads: /output/entry.txt.
The directory can be overridden with MAKEFUN_OUTPUT_DIR for local runs.
"""

import os
from pathlib import Path

JOKE = (
    "I named our Wi-Fi 'Martin Router King' because I have a stream "
    "— but it only ever buffers when the whole family needs it most."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
