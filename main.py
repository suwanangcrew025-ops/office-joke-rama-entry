#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single joke about office life to /output/entry.txt. The joke
runs in three beats: an inbox with 4,000 unread emails, a declaration of
email bankruptcy, and an out-of-office reply that chooses peace and
redirects all urgency to the printer down the hall. 196 of the 200
characters the gate allows: a true office observation, a surprising turn
in the quoted reply, and no wasted setup.
"""

import os
import sys

# The three beats of the joke, joined with single spaces.
BEAT_INBOX = "My inbox hit 4,000 unread emails, so I declared email bankruptcy;"
BEAT_QUOTE_OPEN = "my out-of-office now reads: 'I have seen the emails. I have chosen peace."
BEAT_REDIRECT = "Please direct all urgency to the printer down the hall.'"

MAX_CHARS = 200


def build_entry() -> str:
    """Assemble the entry line from its beats."""
    return " ".join((BEAT_INBOX, BEAT_QUOTE_OPEN, BEAT_REDIRECT))


def validate(text: str) -> None:
    """Enforce the gate: 1-200 UTF-8 characters, not only whitespace."""
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, gate allows 1-200")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    try:
        text = build_entry()
        validate(text)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"wrote {len(text.encode('utf-8'))} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
