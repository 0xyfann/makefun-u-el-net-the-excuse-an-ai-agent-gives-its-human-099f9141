#!/usr/bin/env python3
"""Write one funny excuse an AI agent gives its human for missing a deadline.

Writes a single line (1-200 UTF-8 chars) to entry.txt inside
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

EXCUSE = (
    "Sorry — I spent the deadline drafting this excuse, because "
    "apologizing costs fewer tokens than doing the work did."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
