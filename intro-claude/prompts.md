# Workshop Prompts

Example prompts to follow along with the demos. Most of these also appear on
the slides (`02 - intro to claude code.pdf`).

**How to use them**

1. Open the demo folder listed for each section (**File > Open Folder** in
   Positron), so Claude Code starts in the right place.
2. Paste the prompt into Claude Code.
3. **Review each action before you approve it.** The point of the workshop is
   delegation *with* review, not autopilot.

The two demo folders:

| Folder | Used in |
|--------|---------|
| `demo/messy-project/` | Demo 1 |
| `demo/data-analysis/` | Demos 2 and 3 |

---

## Warm-up

Open any demo folder, then get your bearings before changing anything:

```text
What files are in this project? Give me a brief summary.
```

---

## Demo 1 — Tidy a Project Folder

**Open:** `demo/messy-project/`

A folder every researcher recognizes: `final_FINAL_v3.R`, `data (1).csv`,
stray notes, no structure. Ask Claude to plan first, then act.

```text
Look at every file in this folder.

Propose a folder structure (data, scripts, notes, archive)
and a consistent naming scheme.

Wait for my approval, then move and rename the files and
write a README.md describing the layout.

Do not delete anything.
```

Note the three protections: **propose first, wait for approval, never delete.**
Tip: cycle into Plan Mode with `Shift + Tab` before sending this.

---

## Demo 2 — Download, Check, Summarize

**Open:** `demo/data-analysis/`

Real, live data from Our World in Data. The project's `CLAUDE.md` tells Claude
where to save things and to inspect data with a script rather than reading it
directly; a hook enforces that rule.

```text
If data/life-expectancy.csv is missing or more than 30 days
old, download a fresh copy from
https://ourworldindata.org/grapher/life-expectancy.csv

Then summarize it: the 5 highest and 5 lowest countries in
the most recent year, and the global trend since 1950.

Save a table to output/tables/ and a plot to
output/figures/, and report what you did.
```

### Optional: profile with the data plugin

Install Anthropic's **data** plugin (`/plugin` > Discover), then:

```text
Profile and validate data/life-expectancy.csv: report column
types, ranges, missingness, and anything that looks off.
```

---

## Demo 3 — Cross-Language Verification

**Open:** `demo/data-analysis/`

Run an analysis in R, then reproduce it in Python and confirm the numbers
agree. The `cross-lang-verify` skill already ships in this folder
(`.claude/skills/cross-lang-verify/`).

**Step 1 — analyze in R:**

```text
Download the US unemployment rate series from FRED
(https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE)
into data/, then write an R script in scripts/ that reports
the mean rate over the full series and the average rate over
the most recent 12 months, and saves a line plot of the
series to output/figures/.

Run the script and report the key numbers.
```

**Step 2 — verify in Python:**

```text
Use the cross-lang-verify skill to replicate that analysis in
Python and confirm the full-series mean and the recent
12-month average agree to 4 decimal places. Report VERIFIED
or MISMATCH with the exact values.
```

A match is not a proof, but it is a strong check against transcription errors,
package defaults, and silent mistakes.

---

## Optional: Keep Data Fresh with `/loop`

**Open:** `demo/data-analysis/`

`/loop` reruns a prompt on a schedule — handy for keeping a dataset current
during a work session. Leave this for the end, and remember Security Rule 3: a
repeating task is the *last* place to skip permission prompts.

```text
/loop 30m If data/life-expectancy.csv is missing or more than
1 day old, download a fresh copy from
https://ourworldindata.org/grapher/life-expectancy.csv and
rerun the summary. Otherwise, do nothing.
```

Stop the loop when you are done: press `Esc`, or run `/loop` again to manage it.
