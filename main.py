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
    """Write the locked title to the output file with the required modes.

    Returns 0 on success, 1 on any I/O error (message on stderr).
    """
    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            f.write(TITLE)
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write entry to {output_path!r}: {exc}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
