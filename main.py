#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

The resignation letter of a retry loop, in one line, 140 chars max.
It retried 12,847 times without a single thank-you — and the bug it kept
retrying was a typo all along. The loop did everything right; the code did not.
"""
import os

LINE = "Effective 4:59pm, the retry loop quits: it tried 12,847 times, got 0 thank-yous, and the bug it kept retrying was a typo."


def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
