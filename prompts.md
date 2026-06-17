## 

Attached are some sample prompts to follow when working through our vignettes. 

## Plan Merger

Make a plan to review the data under the data/nhanes folder, inspect the data, identify common variables and keys to merge the data and save the results to a new dataframe. You may read the data to identify a common key.

## Collect Summary Statistics

Write an R script "02-data-discovery.R" begin by importing the merged dataset. For the following demographic variables — RIDAGEYR (age), RIAGENDR (sex), RIDRETH1 (race/Hispanic origin), DMDEDUC2 (education level, adults 20+), and INDFMPIR (income-to-poverty ratio) — identify the R object type of each variable, and then plot the histogram for each distribution as well as its five-figure summary. Save the outputs to presentation/images (create these folders if they do not already exist.) Each figure should include the script prefix (02), the name of the demographic variable, be grey scaled, and saved as a png.


## Explore Demographic Data

Use commments to block off a new section in 02-data-discovery.R, please create some cross-tabs to show the relationships between income (INDFMPIR) and gender (RIAGENDR) on diabetes diagnosis (DIQ010 == 1, excluding refused/don't know responses). Compile these results into a single tidy table with one row per demographic category (e.g. "Male", "Female", "Income: <1x poverty") and columns for the source variable, the category label, the sample size, the probability of a diabetes diagnosis, and the difference in that probability relative to a reference category for each variable (e.g. Male as the reference for gender, the lowest income bracket as the reference for income). Save this table to presentation/tables (create this folder if it does not already exist) and quickly summarize the output.

## Run a Survival Analysis

Write an R script "03-survival-analysis.R" that imports data/tcga/brca_rotterdam_survival.csv. Fit a Kaplan-Meier survival curve for overall survival (dtime/death) stratified by ER status (er_status), and a Cox proportional hazards model for overall survival using age, tumor grade, number of positive nodes, hormonal therapy (hormon), and chemotherapy (chemo) as covariates, stratified by er_status. Save the Kaplan-Meier curve (greyscaled, with the script prefix in the filename) to presentation/images, and save a tidy table of the Cox model coefficients (including hazard ratios and confidence intervals, via broom::tidy()) to presentation/tables.

## Interpret the Results

Using the Kaplan-Meier plot and Cox model table produced by 03-survival-analysis.R, summarize the findings in plain language: how does ER status relate to overall survival, which covariates are significantly associated with the hazard of death, and what do the hazard ratios mean in practical terms? Note any results that warrant a closer look, such as violations of the proportional hazards assumption.

## Cross-Validate the Results

Invoke the /cross-lang-verify skill on 03-survival-analysis.R to replicate the Kaplan-Meier and Cox model results in Python (using lifelines), and confirm that the log-rank statistic, Cox coefficients/hazard ratios, and median survival times agree to 4 decimal places. Report any mismatches and their likely cause.