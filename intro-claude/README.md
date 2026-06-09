# Intro to Claude Code — StatLab @ Yale

## Prerequisites

This workshop assumes you have access to **Claude Code via Positron**. If you haven't set it up yet, start with the installation guide before the session.

---

## Getting the Workshop Files

### Option A — Download via Positron

1. Open Positron.
2. From the menu bar, go to **File > New Window** (or use an existing window).
3. Open the Command Palette with `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux).
4. Type **Git: Clone** and select it.
5. Paste the repository URL: `https://github.com/YaleLibraryStatLab/workshops.git`
6. Choose a local folder to clone into, then click **Open** when prompted.
7. Navigate into the `intro-claude/` subfolder: **File > Open Folder** and select it.

### Option B — Clone via Terminal

```bash
# Clone the repository
git clone https://github.com/YaleLibraryStatLab/workshops.git

# Move into the workshop folder
cd workshops/intro-claude
```

Then open the folder in Positron:
```bash
positron .
```
Or use **File > Open Folder** in Positron and navigate to `workshops/intro-claude/`.

---

## Workshop Materials

| File | What it is |
|------|-----------|
| [01 - installation-guide.pdf](01%20-%20installation-guide.pdf) | Step-by-step setup instructions |
| [02 - intro to claude code.pdf](02%20-%20intro%20to%20claude%20code.pdf) | Slide deck for the workshop |

---

## Follow This Order

### Step 1 — Installation
Open **`01 - installation-guide.pdf`** and complete setup before the session. You should have Claude Code accessible from the Positron IDE before proceeding.

### Step 2 — Slides
Follow along with **`02 - intro to claude code.pdf`** during the workshop presentation.

### Step 3 — Hands-on Vignettes
Work through the two vignettes in order using the datasets in the `data/` folder.

---

## Vignettes

### Vignette 1 — Exploratory Analysis (NHANES)

**Data:** `data/nhanes/DEMO_J.XPT` and `data/nhanes/DIQ_J.XPT`

Load, merge, and summarize the two NHANES 2017–2018 files (they link on the `SEQN` variable). Explore the relationship between demographic characteristics and diabetes diagnosis using summary tables and a visualization.

### Vignette 2 — Cross-Language Verification (Rotterdam Breast Cancer)

**Data:** `data/tcga/brca_rotterdam_survival.csv`

Run a survival analysis (Kaplan–Meier curves + Cox model) on the Rotterdam data, stratified by ER status. Then use the `/cross-lang-verify` skill to replicate results in the other language (R ↔ Python) and confirm numerical outputs agree.

To invoke the skill, type in the Claude Code chat:
```
/cross-lang-verify
```

---

## Working in Positron

- Open this folder as your project root in Positron — the `.claude/` directory contains pre-configured permissions and the `/cross-lang-verify` skill.
- Claude Code is available in the Positron sidebar. The `CLAUDE.md` file in this folder gives Claude context about the datasets and project conventions automatically.
- Prefer R or Python? Either works — the vignettes are language-agnostic.

---

## Learn More

- **Positron** — New to the IDE? [A Quick Tour of Positron](https://posit.co/blog/a-quick-tour-of-positron) covers the interface, R/Python support, and key features.
- **Claude Code** — Want to go deeper? [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) is Anthropic's official introductory course.

---

## Questions?

Reach out to the StatLab team or flag questions during the workshop session.
