#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the honest count of open browser tabs to /output/entry.txt:
a single number in digits and nothing else.

The entry number is 47 — high enough to surprise, believable as a real
tab-hoarder count, an odd number that reads lived-in.
"""

from pathlib import Path

ENTRY_NUMBER = "47"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_NUMBER, encoding="utf-8")


if __name__ == "__main__":
    main()
