#!/usr/bin/env python3
"""One Word, First Thought — writes the single first word that comes to mind.

The word is the whole entry: one word, 1-24 UTF-8 characters, written to
/output/entry.txt. Draft word below; revised after the proxy-judge tournament.
"""

from pathlib import Path

WORD = "sonder"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
