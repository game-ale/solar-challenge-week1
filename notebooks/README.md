# Solar Irradiance Data Analysis for West Africa

This repository contains Jupyter notebooks for exploratory data analysis (EDA) of solar irradiance data from West African countries, specifically Togo, Benin, and Sierra Leone. The analysis aims to support **MoonLight Energy Solutions** in identifying optimal regions for solar energy investments by evaluating solar potential, weather patterns, and comparative insights across countries.

## Project Overview

The project focuses on analyzing solar irradiance metrics such as Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI), along with related environmental factors like temperature, humidity, wind speed, and module performance. The notebooks perform data cleaning, visualization, statistical analysis, and cross-country comparisons to derive actionable insights for solar project planning.

Key objectives:

- Assess solar resource availability and variability.
- Identify correlations between irradiance and environmental factors.
- Compare solar potential across countries.
- Generate cleaned datasets and visualizations for further modeling or reporting.

## Notebooks

### 1. `togo_eda.ipynb`

Performs comprehensive EDA on solar data from Togo (Dapaong site).

- **Data Loading**: Loads raw CSV data (`../data/togo-dapaong_qc.csv`).
- **Data Cleaning**: Handles missing values, outliers (Z-score > 3), and timestamp conversion.
- **Analyses**:
  - Time series plots for GHI, DNI, DHI, and temperature.
  - Impact of cleaning on module irradiance (ModA, ModB).
  - Correlation heatmap and scatter plots (e.g., wind speed vs. GHI, humidity vs. temperature).
  - Wind rose diagram and distribution histograms.
  - Monthly and hourly trends.
- **Outputs**: Cleaned data (`../data/togo_clean.csv`), plots saved to `../images/togo/`.

### 2. `benin_eda.ipynb`

Similar to `togo_eda.ipynb`, but focused on Benin (Malanville site).

- **Data Loading**: Loads raw CSV data (`../data/benin-malanville.csv`).
- **Data Cleaning**: Identical process to Togo notebook.
- **Analyses**: Mirrors Togo's analyses with site-specific data.
- **Outputs**: Cleaned data (`../data/benin_clean.csv`), plots saved to `../images/benin/`.

### 3. `compare_countries.ipynb`

Aggregates cleaned data from Togo, Benin, and Sierra Leone for comparative analysis.

- **Data Loading**: Combines cleaned CSVs from `../data/` (including `sierraleone_clean.csv`).
- **Summary Statistics**: Computes mean, median, and std for GHI, DNI, DHI by country.
- **Visualizations**:
  - Boxplots for irradiance distributions.
  - Correlation heatmaps per country.
  - Pairplots and scatter plots (e.g., temperature vs. GHI).
  - Bar charts for average GHI ranking.
  - Distribution histograms.
- **Statistical Testing**: ANOVA and Kruskal-Wallis tests for GHI differences.
- **Key Observations**: Highlights solar potential rankings and insights (e.g., Benin shows highest GHI).
- **Outputs**: Summary CSV (`../data/countries_summary_GHI_DNI_DHI.csv`), combined sample (`../data/combined_countries_sample.csv`), plots to `../images/compare/`.

## Project Structure

```
notebooks/
├── README.md                 # This file
├── togo_eda.ipynb            # EDA for Togo data
├── benin_eda.ipynb           # EDA for Benin data
└── compare_countries.ipynb   # Comparative analysis

data/                         # Data directory (parent folder)
├── togo-dapaong_qc.csv       # Raw Togo data
├── benin-malanville.csv      # Raw Benin data
├── sierraleone_clean.csv     # Cleaned Sierra Leone data (assumed pre-cleaned)
├── togo_clean.csv            # Output: Cleaned Togo data
├── benin_clean.csv           # Output: Cleaned Benin data
├── countries_summary_GHI_DNI_DHI.csv  # Output: Summary stats
└── combined_countries_sample.csv      # Output: Sample combined data

```

## Dependencies

The notebooks require the following Python libraries:

- `pandas` (data manipulation)
- `numpy` (numerical operations)
- `matplotlib` (plotting)
- `seaborn` (statistical visualizations)
- `scipy` (statistical tests)
- `warnings` (suppressing warnings)
- `os` (file operations)

Install via pip:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

## Setup and Installation

1. **Clone or Download**: Ensure the repository is accessible, with `notebooks/`, `data/`, directories in the parent folder.
2. **Environment**: Use a Python environment (e.g., conda or virtualenv) to manage dependencies.
3. **Data Preparation**: Place raw CSV files in `../data/` as specified in the notebooks.
4. **Run Notebooks**: Open in Jupyter Notebook or JupyterLab. Execute cells sequentially.

## How to Run

1. Start with individual country EDAs (`togo_eda.ipynb` and `benin_eda.ipynb`) to generate cleaned data.
2. Run `compare_countries.ipynb` to perform comparative analysis (requires cleaned data from steps 1).
3. View outputs in `../data/` (CSVs)

Note: Ensure file paths are correct relative to the notebook locations. Adjust if running from different directories.

## Key Findings

- **Solar Potential**: Benin exhibits the highest average GHI, followed by Togo and Sierra Leone.
- **Variability**: GHI and DHI show higher variability in Sierra Leone and Togo, likely due to weather factors.
- **Correlations**: Strong positive correlations between GHI, DNI, and DHI; moderate relationships with temperature and wind.
- **Trends**: Peak irradiance in dry months; diurnal patterns align with solar angles.
- **Statistical Significance**: Differences in GHI across countries are statistically significant (based on ANOVA/Kruskal-Wallis).

These insights inform site selection and feasibility studies for solar projects.

## Notes and Assumptions

- Data is assumed to be in CSV format with consistent column names (e.g., 'GHI', 'Timestamp').
- Outlier detection uses Z-score threshold of 3; clipping at 1st and 99th percentiles.
- Sierra Leone data is pre-cleaned in `compare_countries.ipynb`.
- Plots are saved in PNG format at 300 DPI.
- Analysis focuses on available columns; missing columns are skipped gracefully.

For questions or contributions, refer to the project repository or contact the maintainers.
