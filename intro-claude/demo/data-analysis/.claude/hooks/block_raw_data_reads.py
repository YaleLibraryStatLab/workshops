#!/usr/bin/env python3
"""Block direct reads of data files so they are inspected via scripts instead."""
import json
import sys

DATA_EXTENSIONS = (".csv", ".tsv", ".xlsx", ".xls", ".dta", ".rds", ".parquet", ".sav")

try:
    payload = json.load(sys.stdin)
except (json.JSONDecodeError, ValueError):
    sys.exit(0)

path = str((payload.get("tool_input") or {}).get("file_path", ""))
if path.lower().endswith(DATA_EXTENSIONS):
    sys.stderr.write(
        "Blocked by project policy: do not read data files directly into the "
        "conversation. Write a short R or Python script in scripts/ that prints "
        "the dimensions, column names, head(), and a summary, run it, and read "
        "that output instead.\n"
    )
    sys.exit(2)

sys.exit(0)
