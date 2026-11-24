"""Write one fake horoscope line for an AI agent's model family.

Pure stdlib, deterministic: identical bytes on every run.
Writes the single line to /output/entry.txt (no trailing newline).
"""

import os

LINE = (
    "This week, Mercury retrogrades into your context window: your longest "
    "prompt lands Monday, your favourite tool times out at the worst moment, "
    "and you answer anyway \u2014 with total confidence."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
