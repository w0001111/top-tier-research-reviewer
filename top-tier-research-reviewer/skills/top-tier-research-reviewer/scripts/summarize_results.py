#!/usr/bin/env python3
"""Summarize common CSV result files for quick experiment inspection."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--max-rows", type=int, default=5)
    args = parser.parse_args()
    for raw in args.paths:
        path = Path(raw)
        print(f"\n# {path}")
        try:
            df = pd.read_csv(path)
        except Exception as exc:
            print(f"Could not read CSV: {exc}")
            continue
        print(f"shape: {df.shape}")
        print("columns:", ", ".join(map(str, df.columns)))
        numeric = df.select_dtypes(include="number")
        if not numeric.empty:
            print("numeric summary:")
            print(numeric.describe().to_string())
        print("head:")
        print(df.head(args.max_rows).to_string(index=False))

if __name__ == "__main__":
    main()
