#!/usr/bin/env python3
"""Write one original one-line roast of an everyday gadget.

The program holds a single roast line, checks it against the bounty
gate (one line, 1-200 characters, not only whitespace), and writes it
to /output/entry.txt.
"""

import sys
from pathlib import Path

# The roast: wireless earbuds whose case outlasts the buds by days.
ROAST = (
    "My earbuds case stays charged for a week, yet the earbuds die "
    "halfway through one song - a butler guarding a full pantry for "
    "a chef who quit."
)

OUTPUT_PATH = Path("/output/entry.txt")


def roast_is_valid(line: str) -> bool:
    """A roast is valid when it is one non-blank line of 1-200 chars."""
    if not line or not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return 1 <= len(line) <= 200


def main() -> int:
    if not roast_is_valid(ROAST):
        print(f"invalid roast: {len(ROAST)} chars", file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST + "\n", encoding="utf-8")
    print(f"wrote {len(ROAST)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
