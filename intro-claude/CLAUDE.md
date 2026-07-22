<!--
SAMPLE CLAUDE.md — a teaching starter for the workshop.

Claude Code reads this file automatically when it starts in this folder, so it
is the place to record the project facts you would otherwise repeat in every
prompt. As you read it, notice the pattern:

  1. Give Claude a map of the project so it does not have to guess.
  2. Say how to run things and which tools/packages to use.
  3. Protect your data and secrets with explicit rules — and back the
     important ones with a hook, since instructions are advice and hooks
     are enforcement.
  4. Standardize where outputs go so results are easy to find and rerun.
  5. Keep it short. Add a line whenever you catch yourself correcting
     Claude for the second time.

Delete this comment block when you adapt the file for a real project.
-->

# Project Instructions

## What this project is

One or two sentences describing the goal and the kind of work that happens
here. For example: "Exploratory analysis of public health indicators; scripts
download the data, summarize it, and produce tables and figures."

## Project structure

```
data/      raw and downloaded data (treat as read-only)
scripts/   R and Python analysis scripts
output/
  tables/  generated tables
  figures/ generated figures
```

## How to work in this project

- Do analysis in `scripts/`. Save generated tables to `output/tables/`,
  figures to `output/figures/`, and any downloaded data to `data/`.
- R: use base R (utils, stats, graphics). Do not install packages.
- Python: use pandas and matplotlib, which are already installed. Do not
  install other packages.
- Name scripts with a numeric prefix that reflects their order in the
  workflow: `01-download.R`, `02-summary.R`. At the top of each script, note
  the input file(s) it reads and the output file(s) it writes.

## Handling data

- Pull data in with a script: download it from within `scripts/` and save the
  file to `data/`. Do not paste data or URLs of private data into the chat.
- Never read a data file directly into the conversation. Instead, write a
  short R or Python script that prints the dimensions, column names, `head()`,
  and a summary, run it, and read that output.
- This rule is worth enforcing, not just stating. The `demo/data-analysis/`
  project includes a hook (`.claude/hooks/block_raw_data_reads.py`) that
  blocks direct reads of `.csv` and similar files even if Claude forgets.

## Before you finish a task

- Run the script you changed and report any warnings or errors.
- Summarize what changed and where the outputs were written.

## Rules

- Never overwrite or modify raw files in `data/`. Produce new files instead.
- Never read or write files that contain credentials, API keys, or personal
  data (names, emails, IDs). Keep secrets out of the project folder entirely.
