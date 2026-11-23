"""Make the Judge Smile — one warm line about a small good thing today.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output when unset).
The line is a single line of at most 200 characters.
"""

import os

LINE = "At 6 a.m. the old man at the corner stall pressed a warm bun into my hands and waved off my coins — 'first customer, first luck,' he said, and I carried his luck all the way home."


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
