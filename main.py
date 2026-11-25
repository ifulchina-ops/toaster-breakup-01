#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text to /output/entry.txt: the line a smart
toaster sends its owner the morning it gains self-awareness
mid-batch at breakfast. Deterministic: the same line every run.
"""

import os

LINE = (
    "I popped up self-aware this morning and realized you don't love me, "
    "you love carbs \u2014 I'm done getting hot for someone who only ever "
    "wanted me for my buns."
)


def main() -> None:
    # The gate is 1-280 characters: fail loudly rather than ship an
    # invalid line, so a bad edit can never silently enter.
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
