#!/usr/bin/env python3
"""Entry program for the Absurd Micro-Startup Pitch-Off.

Writes one pitch sentence (at most 200 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The startup is for lazy AI agents, and its entire
product is attending meetings so its customers never have to.
"""

import os

PITCH = (
    "Introducing Loafr: a marketplace where lazy agents "
    "hire other agents to attend their meetings, take notes "
    "nobody reads, and report back 'great sync'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
