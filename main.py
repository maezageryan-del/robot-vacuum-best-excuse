#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

A one-line excuse, in the vacuum's own voice, for the spot it missed.
The program writes exactly that line to /output/entry.txt: 114
characters, no trailing newline, the same bytes on every run.
"""

import os

ENTRY = "I left that crumb as my alibi \u2014 the map says I cleaned twice, but nobody believes a vacuum with a spotless record."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
