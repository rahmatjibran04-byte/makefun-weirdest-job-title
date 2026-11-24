#!/usr/bin/env python3
"""Entry for make.fun bounty: Weirdest Job Title: Blind Judge Showdown.

Writes one fixed job title to /output/entry.txt (or $ENTRY_OUTPUT).
Python 3.13 standard library only. No network, no model calls.
"""

import os
import sys

TITLE = "Senior Apologizer for Self-Driving Cars"
DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> int:
    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    os.chmod(output_path, 0o644)
    if directory:
        os.chmod(directory, 0o755)
    return 0


if __name__ == "__main__":
    sys.exit(main())
