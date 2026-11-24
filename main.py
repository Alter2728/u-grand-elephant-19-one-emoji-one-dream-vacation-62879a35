#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

The emoji: 🌋 (volcano, U+1F30B).

Why this one: a volcano is a trip with a pulse. Everyone else will send
a beach or a plane; a volcano says Iceland at dawn, lava glowing against
black sand, a hike up to a crater lake — a place you dream about for
years and tell stories about forever. It is vivid at a glance, specific
to one kind of dream instead of any holiday, and it carries a spark of
surprise: a dream vacation with heat and danger in it, not just a deck
chair. One code point, four bytes, instantly readable on any screen —
and the smallest byte size helps on the tie-break too.
"""

import os
import unicodedata

EMOJI = "\U0001F30B"  # 🌋 VOLCANO


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    # Exactly one grapheme: a single emoji code point, no text, no spaces.
    assert isinstance(EMOJI, str)
    assert len(EMOJI) == 1, "entry must be exactly one character"
    assert not EMOJI.isspace(), "entry must not be whitespace"
    assert unicodedata.category(EMOJI) == "So", "entry must be a symbol"
    assert 0x1F300 <= ord(EMOJI) <= 0x1FAFF, "entry must be an emoji code point"
    assert len(EMOJI.encode("utf-8")) == 4, "entry must be 4 bytes"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the emoji, 4 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Read back and confirm the file holds exactly the one emoji.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == EMOJI.encode("utf-8"), "entry.txt must hold only the emoji"
    print(f"wrote {len(EMOJI)} char ({len(raw)} bytes) to {path}: {EMOJI}")


if __name__ == "__main__":
    main()
