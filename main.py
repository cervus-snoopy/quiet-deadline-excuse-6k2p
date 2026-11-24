#!/usr/bin/env python3
"""Write the one-line excuse to entry.txt.

Python 3 standard library only, no network access. The output directory
comes from MAKEFUN_OUTPUT_DIR (falling back to /output) and is resolved
independently of the current working directory.
"""

import os

EXCUSE = "My context window filled up, so I summarized the deadline out of my own memory."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)

    text = EXCUSE.strip()
    if not text or len(text) > 160:
        raise SystemExit("entry must be 1-160 non-blank characters")

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)

    # Read the file back and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("entry.txt read-back does not match the excuse")
    if not written.strip() or len(written) > 160:
        raise SystemExit("entry.txt failed the 1-160 character gate")


if __name__ == "__main__":
    main()
