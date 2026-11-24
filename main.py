#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: a roast of lawmakers
who would regulate AI, crypto or the internet but cannot convert a file
to PDF. One sentence, 180 characters, well under the 320-character limit.
No real person is named; the joke is about the situation.
"""

import os

ENTRY = (
    "The senator who wants to license every AI model in America still "
    "emails his staff a photo of his screen because he cannot find the "
    "button that turns a document into a PDF."
)


def main() -> None:
    # Self-check against the scorer's gate: UTF-8 text, 1-320 chars,
    # not only whitespace, one sentence on one line.
    assert 1 <= len(ENTRY) <= 320, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
