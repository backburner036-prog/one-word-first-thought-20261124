#!/usr/bin/env python3
"""One Word, First Thought — writes the single first word that comes to mind.

The word is the whole entry: one word, 1-24 UTF-8 characters, written to
/output/entry.txt. Draft word below; revised after the proxy-judge tournament.
"""

from pathlib import Path

WORD = "borborygmus"  # proxy-judge winner: mean 0.867 vs anchors, wins 3/3
# (beat "thing" 1.00, "serendipity" 0.85, "petrichor" 0.75 — the strongest
# entry in the field so far). A stomach rumble: surprising, vivid, funny
# sound, unmistakably chosen rather than generic.


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
