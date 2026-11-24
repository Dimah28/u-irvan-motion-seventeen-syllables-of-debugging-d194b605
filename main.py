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

# Syllable count per line, verified by hand: Break-point(2) at(1)
# mid-night(2) = 5; the(1) stack(1) trace(1) dies(1) in(1)
# si-lence(2) = 7; it(1) was(1) my(1) ty-po(2) = 5. Total 17.
SYLLABLES_PER_LINE = (5, 7, 5)


def _validate(text: str) -> None:
    """Guard the gate: 3 lines, 5-7-5 syllables, 1-200 characters."""
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have 3 lines, got {len(lines)}")
    if len(lines) != len(SYLLABLES_PER_LINE):
        raise ValueError("syllable table does not match the haiku")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"haiku must be 1-200 characters, got {len(text)}")
    if sum(SYLLABLES_PER_LINE) != 17:
        raise ValueError("haiku must total 17 syllables")


def main() -> None:
    _validate(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)


if __name__ == "__main__":
    main()
