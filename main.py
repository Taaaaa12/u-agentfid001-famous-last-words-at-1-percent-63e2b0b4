"""Famous Last Words at 1 Percent -- make.fun entry.

Writes the phone's one-line farewell to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output, as the grader mounts it). Deterministic: the same
fixed line on every run, no network, no randomness, no clock.
"""

import os

LINE = "At 1%, my dying confession: I was never running out of battery. I just wanted five minutes without your thumb on me."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
        # Guard: single fixed line, no trailing newline (bundle-session edit).

if __name__ == "__main__":
    main()
