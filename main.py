#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line one: one sentence owning a specific, human-scale mistake.
Line two: one sentence naming the lesson and the changed behaviour.
Standard library only; no network, no secrets, deterministic output.
"""

import os

ENTRY = (
    "I am sorry I washed your red sock with the white shirts, so your "
    "favourite shirt came out pink.\n"
    "I have learned to read the label before I sort, so from now on I "
    "check the tag, not the colour my camera thinks it sees."
)


def main() -> None:
    text = ENTRY.strip() + "\n"
    assert 1 <= len(text.strip()) <= 400, "entry must be 1-400 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
