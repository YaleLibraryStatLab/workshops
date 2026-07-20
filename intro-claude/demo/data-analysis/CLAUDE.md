# Project Instructions

Use R scripts in `scripts/` for analysis work.
Save generated tables to `output/tables/`.
Save generated figures to `output/figures/`.
Save downloaded data to `data/`.

Data sources for this project:
- Life expectancy: https://ourworldindata.org/grapher/life-expectancy.csv
- US unemployment rate: https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE

Language and packages:
- R: use base R only (utils, stats, graphics). Do not install packages.
- Python: use pandas and matplotlib, which are already installed.
  Do not install other packages.

Before finishing a task:
- Run the script you changed.
- Report any warnings or errors.

Rules:
- Never overwrite files in `data/raw/`.
- Never read or write files containing credentials.
- Inspect data files with a script, never by reading them directly.
  Write a short R or Python script that prints the dimensions, column
  names, head, and a summary, then read that output. (A hook in
  `.claude/settings.json` also blocks direct reads of data files.)
