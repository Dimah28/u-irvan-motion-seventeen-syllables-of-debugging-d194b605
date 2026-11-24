"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku (three lines, 5-7-5 syllables, 17 total) about
debugging to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: stdlib only, no network, no clock, no randomness.
"""

import os

HAIKU = (
    "Breakpoint at midnight\n"
    "the stack trace dies in silence\n"
    "it was my typo\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)


if __name__ == "__main__":
    main()
