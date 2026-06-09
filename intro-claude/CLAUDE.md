# Claude Code Workshop — StatLab @ Yale

This is the working directory for the StatLab Claude Code workshop. It contains two datasets for hands-on vignettes and a presentation on using Claude Code for research workflows.

## Datasets

### NHANES 2017–2018 (data/nhanes/)
Two linked XPT files from the National Health and Nutrition Examination Survey:
- `DEMO_J.XPT` — Demographics: age, sex, race/ethnicity, education, income-to-poverty ratio (~9,000 participants)
- `DIQ_J.XPT` — Diabetes questionnaire: diagnosed diabetes, insulin use, oral medication, self-reported A1C

These files link on the `SEQN` variable. A natural starting question is the relationship between demographic characteristics and diabetes diagnosis.

### Rotterdam Breast Cancer Survival (data/tcga/)
- `brca_rotterdam_survival.csv` — 2,982 patients from the Rotterdam Tumor Bank
- Key variables: `age`, `er_status` (ER+ / ER−), `grade` (tumor grade 1–3), `nodes` (lymph node count), `recur` / `rtime` (recurrence event and time), `death` / `dtime` (mortality event and time), `hormon` / `chemo` (treatment flags)

A natural analysis is Kaplan–Meier survival curves and a Cox proportional hazards model stratified by ER status.

## Workshop Vignettes

**Vignette 1 — Exploratory Analysis (NHANES)**
Load, merge, and summarize the NHANES files. Describe the diabetes-demographics relationship using summary tables and a visualization.

**Vignette 2 — Cross-Language Verification (TCGA)**
Run a survival analysis on the Rotterdam data in either R or Python, then invoke the `/cross-lang-verify` skill to replicate results in the other language and confirm they agree numerically.

## Conventions
- R: tidyverse style (dplyr, ggplot2, survival, broom)
- Python: pandas, lifelines or statsmodels, matplotlib/seaborn
- Participants have mixed backgrounds — prefer readable, commented code over concise one-liners

## Project Rules

**Data integrity**
Raw data files live in `data/raw/` and must never be overwritten or modified. Any cleaning, merging, or transformation produces a new file written to `data/processed/`. Treat raw files as read-only at all times.

**File naming and ordering**
Scripts and output files use a numeric prefix that reflects their position in the workflow. The number comes first, followed by a short descriptive name:
- Scripts: `01-merge-nhanes.R`, `02-descriptives.R`, `03-model.R`
- Data outputs: `nhanes-merged.csv`, `nhanes-analysis-sample.csv` — saved to `data/processed/`

If a step is added between existing steps, renumber to keep the sequence unambiguous.

**One script, one task**
Each script has a clearly stated purpose — merge, clean, model, visualize, or tabulate — and should not combine multiple stages. At the top of every script, note the input file(s) it reads and the output file(s) it writes. When a task produces figures or tables, save them to `presentation/images/` or `presentation/tables/` respectively.

**R style**
- Use the base pipe `|>` rather than the magrittr pipe `%>%`
- Qualify function calls with their package namespace where ambiguity is possible: `dplyr::select()`, `dplyr::filter()`, `broom::tidy()`. This makes dependencies explicit and avoids masking conflicts.
