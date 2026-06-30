#!/usr/bin/env python3
"""Lightweight Python project inspector for research-code audits."""
from __future__ import annotations

import argparse
from pathlib import Path

KEYWORDS = {
    "data": ["data", "dataset", "loader", "preprocess", "split"],
    "model": ["model", "network", "module", "forward", "layer"],
    "train": ["train", "fit", "optimizer", "loss"],
    "eval": ["eval", "test", "metric", "predict"],
    "result": ["result", "summary", "table", "figure", "plot"],
    "config": ["config", "args", "yaml", "json"],
}

def classify(path: Path) -> list[str]:
    text = str(path).lower()
    tags = []
    for tag, words in KEYWORDS.items():
        if any(w in text for w in words):
            tags.append(tag)
    return tags or ["other"]

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--max-files", type=int, default=300)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    files = []
    for pattern in ("*.py", "*.ipynb", "*.yaml", "*.yml", "*.json", "*.csv", "*.md"):
        files.extend(root.rglob(pattern))
    files = [p for p in files if ".git" not in p.parts and "__pycache__" not in p.parts]
    files = sorted(files)[: args.max_files]
    grouped: dict[str, list[Path]] = {k: [] for k in list(KEYWORDS) + ["other"]}
    for path in files:
        for tag in classify(path.relative_to(root)):
            grouped[tag].append(path)
    print(f"Project: {root}")
    print(f"Files scanned: {len(files)}")
    for tag, paths in grouped.items():
        if not paths:
            continue
        print(f"\n[{tag}]")
        for p in paths[:50]:
            print(p.relative_to(root))

if __name__ == "__main__":
    main()
