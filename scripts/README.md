# Solar Insights Dashboard

A Streamlit-based web application for exploring and analyzing solar radiation datasets across Benin, Sierra Leone, and Togo. This dashboard provides interactive visualizations, comparisons, and insights into solar irradiance metrics such as GHI, DNI, and DHI.

## Features

- **Overview**: Get an introduction to the dashboard and view average solar irradiance per country.
- **Country Comparison**: Compare irradiance metrics across selected countries with boxplots and summary statistics.
- **Explore Country**: Dive into individual country data with time-series plots, summary statistics, and correlation heatmaps.
- **Analytics Lab**: Visualize relationships between metrics across all countries with scatter plots and global correlation heatmaps.
- **Interactive Downloads**: Export summary data and sample datasets as CSV files.

## Screenshots

### Overview Page

![Average Solar Irradiance per Country](dashboard_screenshots/Average-Solar-Irradiance-per-Country.png)

### Cross-Country Comparison

![Cross-Country Comparison](dashboard_screenshots/Cross-Country-Comparison.png)

### Explore Country Data

![Explore Country Data](dashboard_screenshots/Explore-Country-Data.png)

### Analytics Lab

![Dive deeper into the data — visualize relationships and compare performance.](dashboard_screenshots/Dive-deeper-into-the-data-visualize-relationships-and-compare-performance.png)

### Main Dashboard

![Solar Insights Dashboard](dashboard_screenshots/Solar-Insights-Dashboard.png)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Bekamgenene/solar-challenge-week0.git
   cd solar-challenge-week0
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Ensure data files are in the `data/` directory (e.g., `benin_clean.csv`, `sierraleone_clean.csv`, `togo_clean.csv`).

## Usage

Run the Streamlit app:

```
streamlit run app/main.py
```

Navigate through the sidebar to explore different sections of the dashboard.

## Data Sources

The app uses cleaned solar radiation datasets for Benin, Sierra Leone, and Togo. Ensure the data files are placed in the `data/` folder.

## Developed By

**Bekam Genene** for **10 Academy Solar Challenge Week 0**

🌞 _"Turning sunlight into insight!"_

🔗 [GitHub Repository](https://github.com/game-ale/solar-challenge-week1)
