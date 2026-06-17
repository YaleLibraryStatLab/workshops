# Workshop Codebook

Two datasets are available for this workshop. Selected variables are documented below — not every column is included, only those most useful for exploratory analysis, hypothesis testing, and modeling exercises.

---

## Dataset 1: NHANES 2017–2018

**Source:** National Health and Nutrition Examination Survey, CDC  
**Files:** `data/nhanes/DEMO_J.XPT`, `data/nhanes/DIQ_J.XPT`  
**Participants:** ~9,254 (all ages)  
**Link key:** `SEQN` — merge the two files on this variable

### Linking the Files

```r
library(haven)
demo <- read_xpt("data/nhanes/DEMO_J.XPT")
diq  <- read_xpt("data/nhanes/DIQ_J.XPT")
nhanes <- dplyr::left_join(demo, diq, by = "SEQN")
```

### Special Response Codes (applies to all survey variables)

| Code | Meaning |
|------|---------|
| `7` | Refused |
| `9` | Don't know |
| `NA` | Not applicable (e.g., question not asked of this age group) |

Exclude codes 7 and 9 before analysis.

---

### Demographics (`DEMO_J.XPT`)

| Variable | Label | Type | Values / Range |
|----------|-------|------|----------------|
| `SEQN` | Respondent sequence number | Integer | Unique ID — merge key |
| `RIDAGEYR` | Age at screening (years) | Continuous | 0–80 (80+ top-coded to 80) |
| `RIAGENDR` | Sex | Categorical | 1 = Male, 2 = Female |
| `RIDRETH1` | Race / Hispanic origin | Categorical | 1 = Mexican American, 2 = Other Hispanic, 3 = Non-Hispanic White, 4 = Non-Hispanic Black, 5 = Other / Multi-racial |
| `DMDEDUC2` | Education level (adults 20+) | Ordinal | 1 = Less than 9th grade, 2 = 9–11th grade, 3 = High school diploma / GED, 4 = Some college / AA, 5 = College graduate or above; 7 = Refused, 9 = Don't know; NA if age < 20 |
| `INDFMPIR` | Family income-to-poverty ratio | Continuous | 0.00–5.00 (5.00 = at or above 500% of poverty line); NA if unknown or income not reported |

| `DMDMARTL` | Marital status (adults 20+) | Categorical | 1 = Married, 2 = Widowed, 3 = Divorced, 4 = Separated, 5 = Never married, 6 = Living with partner; 77 = Refused; NA if age < 20 |
| `RIDRETH3` | Race / Hispanic origin (6-category) | Categorical | 1 = Mexican American, 2 = Other Hispanic, 3 = Non-Hispanic White, 4 = Non-Hispanic Black, 6 = Non-Hispanic Asian, 7 = Other / Multi-racial (adds Asian and splits Other vs. Multi vs. `RIDRETH1`) |
| `DMDBORN4` | Country of birth | Categorical | 1 = Born in US, 2 = Born outside US; 77 = Refused |
| `DMDHHSIZ` | Total number of people in household | Count | 1–7 (7 = 7 or more) |
| `INDHHIN2` | Annual household income | Categorical | Ordinal ladder of dollar ranges (1–15); 77 = Refused, 99 = Don't know — use `INDFMPIR` for continuous analysis |

**Notes:**
- `RIDAGEYR` is right-censored at 80 — treat ≥80 as "80+" in descriptive tables
- `DMDEDUC2` and `DMDMARTL` have ~3,685 NAs because both are only asked of participants aged 20+
- `RIDRETH3` is a more granular alternative to `RIDRETH1` — prefer it when Asian ethnicity is analytically relevant
- `INDFMPIR` is the most continuous SES measure (~1,231 NAs); `INDHHIN2` captures the full income ladder but is categorical with many refusal/unknown codes

---

### Diabetes Questionnaire (`DIQ_J.XPT`)

| Variable | Label | Type | Values |
|----------|-------|------|--------|
| `SEQN` | Respondent sequence number | Integer | Merge key |
| `DIQ010` | Doctor told you have diabetes | Categorical | 1 = Yes, 2 = No, 3 = Borderline, 9 = Don't know |
| `DIQ160` | Doctor told you have prediabetes | Categorical | 1 = Yes, 2 = No, 9 = Don't know; NA if `DIQ010 == 1` (already diabetic) |
| `DIQ050` | Currently taking insulin | Categorical | 1 = Yes, 2 = No, 9 = Don't know |
| `DIQ070` | Currently taking oral diabetes medication | Categorical | 1 = Yes, 2 = No, 9 = Don't know; NA if not applicable |

**Notes:**
- For a clean "diagnosed diabetes" outcome, keep `DIQ010 == 1` and exclude values 3, 7, 9
- `DIQ160` (prediabetes) is not asked of those who already have diabetes (`DIQ010 == 1`), so NAs are expected
- `DIQ070` has ~7,223 NAs because oral medication questions are only asked of those with a diabetes diagnosis

---

### Suggested Analyses (NHANES)

- **Descriptive:** Distribution of age, sex, race, education, and income in the full sample
- **Cross-tabulation:** Diabetes prevalence (`DIQ010 == 1`) by sex and race/ethnicity
- **Continuous predictor:** Logistic regression of diabetes on income-to-poverty ratio, adjusted for age and sex
- **Dose-response:** Does diabetes prevalence vary monotonically across education levels?
- **Subgroup:** Restrict to adults 20+ (complete education data) and compare insulin vs. oral medication use

---

## Dataset 2: Rotterdam Breast Cancer Survival

**Source:** Rotterdam Tumor Bank (Foekens et al., 2000)  
**File:** `data/tcga/brca_rotterdam_survival.csv`  
**Patients:** 2,982 primary breast cancer cases  
**Period:** 1978–1993

```r
brca <- read.csv("data/tcga/brca_rotterdam_survival.csv")
```

---

### Variable Reference

| Variable | Label | Type | Values / Range |
|----------|-------|------|----------------|
| `pid` | Patient ID | Integer | Unique identifier |
| `age` | Age at surgery (years) | Continuous | 24–90 |
| `year` | Year of surgery | Integer | 1978–1993 |
| `meno` | Menopausal status at surgery | Binary | 0 = Premenopausal, 1 = Postmenopausal |
| `size` | Tumor size | Categorical | `"<=20"`, `"20-50"`, `">50"` (mm) |
| `grade` | Tumor grade | Ordinal | 2 = Moderately differentiated, 3 = Poorly differentiated |
| `nodes` | Number of positive lymph nodes | Count | 0–34 |
| `er` | Estrogen receptor level | Continuous | 0–3,275 fmol/mg protein |
| `pgr` | Progesterone receptor level | Continuous | 0–5,004 fmol/mg protein |
| `hormon` | Hormonal therapy received | Binary | 0 = No, 1 = Yes |
| `chemo` | Chemotherapy received | Binary | 0 = No, 1 = Yes |
| `rtime` | Follow-up time to recurrence (days) | Continuous | 36–7,043 |
| `recur` | Recurrence event | Binary | 0 = Censored, 1 = Recurrence observed |
| `dtime` | Follow-up time to death (days) | Continuous | 36–7,043 |
| `death` | Death event | Binary | 0 = Censored / alive, 1 = Died |

---

### ER Status — Data Quality Note

The dataset includes an `er_status` character column (`"Positive"` / `"Negative"`), but it is **incorrectly coded**: only 27 patients are labeled `"Positive"`, all of whom have `er == 1` (an implausibly small subset). This column should not be used as-is.

**Recommended approach:** Derive ER status from the continuous `er` variable using the standard clinical threshold of ≥ 10 fmol/mg protein:

```r
brca <- brca |>
  dplyr::mutate(er_pos = dplyr::if_else(er >= 10, "ER+", "ER-"))
```

Under this definition, ~76% of patients are ER+ (n ≈ 2,278), consistent with published literature on this cohort.

---

### Outcome Definitions

| Analysis | Time variable | Event variable |
|----------|--------------|----------------|
| Overall survival | `dtime` | `death` (1 = died) |
| Recurrence-free survival | `rtime` | `recur` (1 = recurred) |

Both outcomes use standard right-censored survival notation. Patients who did not experience the event by the end of follow-up are censored (event = 0).

---

### Suggested Analyses (Rotterdam)

- **Kaplan-Meier:** Overall survival stratified by `er_pos`; log-rank test for group difference
- **Cox model:** Overall survival ~ `age + grade + nodes + hormon + chemo`, stratified by `er_pos`
- **Prognostic factors:** Compare unadjusted hazard ratios for `nodes`, `grade`, and `size`
- **Treatment effect:** Does `hormon` or `chemo` modify survival within ER+ vs. ER− subgroups?
- **Continuous predictor:** Model lymph node count (`nodes`) as a continuous or spline term — is the relationship linear?
- **Recurrence vs. mortality:** Fit parallel models for `recur`/`rtime` and `death`/`dtime` — do the same predictors matter for both endpoints?
