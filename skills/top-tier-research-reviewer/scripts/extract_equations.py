#!/usr/bin/env python3
"""Extract simple LaTeX equation-like snippets from markdown/tex text files."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

PATTERNS = [
    re.compile(r"\$\$(.*?)\$\$", re.S),
    re.compile(r"\\[(.*?)\\]", re.S),
    re.compile(r"\begin\{equation\*?\}(.*?)\end\{equation\*?\}", re.S),
    re.compile(r"\begin\{align\*?\}(.*?)\end\{align\*?\}", re.S),
]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    for raw in args.paths:
        path = Path(raw)
        text = path.read_text(encoding="utf-8", errors="ignore")
        print(f"# {path}")
        count = 0
        for pattern in PATTERNS:
            for match in pattern.finditer(text):
                count += 1
                snippet = " ".join(match.group(1).strip().split())
                print(f"[{count}] {snippet[:1000]}")
        if count == 0:
            print("No equation-like snippets found.")

if __name__ == "__main__":
    main()
