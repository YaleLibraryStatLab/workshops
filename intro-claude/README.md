# Intro to Claude Code — StatLab @ Yale

This workshop assumes you have access to **Claude Code via Positron**. Start with the installation guide (`01 - installation-guide.pdf`) if you haven't set it up yet, then follow along with the slides (`02 - intro to claude code.pdf`).

---

## What You Need for This Workshop

Please set these up **before** the session. Full step-by-step instructions (Mac and Windows) are in the installation guide (`01 - installation-guide.pdf`).

1. **Claude Code installed** — the command-line tool, or, optionally, the Claude Code extension for Positron or VS Code.
2. **R and Python installed** — the demos use both languages.
3. **The Python packages** — `pandas` and `matplotlib` (`pip install pandas matplotlib`). The R demos use base R only, so no extra R packages are needed.

> **Please install everything ahead of time.** Claude Code *can* install these for you during the session, but doing so spends tokens/credits on setup instead of learning. Coming in ready means you get to spend the whole workshop on exploring what Claude Code can do.

Not sure something installed correctly? The installation guide ends with a checklist and a Common Issues page, and you can book pre-workshop setup help with a StatLab Consultant (see the guide's "Need Help?" page).

---

## Getting the Workshop Files

**Download as a ZIP (recommended):**

1. Go to [https://github.com/YaleLibraryStatLab/workshops](https://github.com/YaleLibraryStatLab/workshops)
2. Click the green **Code** button > **Download ZIP**
3. Unzip the file and locate the `intro-claude/` folder
4. In Positron, go to **File > Open Folder** and select `intro-claude/` (or a specific demo folder)

**Via Git (Positron):**

1. Open the Command Palette: `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type **Git: Clone** and select it
3. Paste: `https://github.com/YaleLibraryStatLab/workshops.git` and choose a local folder
4. When cloning finishes, go to **File > Open Folder** and select the `intro-claude/` subfolder

**Via Git (terminal):**

```bash
git clone https://github.com/YaleLibraryStatLab/workshops.git
cd workshops/intro-claude
```

Then open in Positron: **File > Open Folder** and select `workshops/intro-claude/`.

---

## What's in This Folder

| Item | What it is |
|------|-----------|
| [01 - installation-guide.pdf](01%20-%20installation-guide.pdf) | Step-by-step setup instructions |
| [02 - intro to claude code.pdf](02%20-%20intro%20to%20claude%20code.pdf) | Slide deck for the workshop |
| [prompts.md](prompts.md) | Copy-and-paste prompts for each demo |
| `demo/messy-project/` | Demo 1 — a messy folder to tidy up |
| `demo/data-analysis/` | Demos 2 and 3 — download, summarize, and cross-language verification |

For each demo, open the demo folder itself (**File > Open Folder**) so Claude Code starts in the right place, then work through the matching section of `prompts.md`.

The `demo/data-analysis/` folder ships with project instructions (`CLAUDE.md`), a hook that blocks direct reads of data files, and a `cross-lang-verify` skill — all of which the slides walk through.

---

## Learn More

- **Positron** — [A Quick Tour of Positron](https://posit.co/blog/a-quick-tour-of-positron)
- **Claude Code** — [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) (Anthropic's official intro course)

---

## Questions?

Reach out to the StatLab team or flag questions during the workshop session.
