#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes one line (<=120 chars) to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot.
"""

import os

ENTRY = "I left that spot alone because the dust bunny unionized and I'm not crossing a picket line."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
