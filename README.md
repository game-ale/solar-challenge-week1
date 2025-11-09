# ☀️ 10 Academy – Solar Data Discovery Challenge  

## 📘 Overview
This repository contains my work for **Week 1: Solar Data Discovery Challenge** as part of the **10 Academy AI Mastery Program**.  
The challenge focuses on understanding, profiling, cleaning, and exploring solar-farm data from **Benin**, **Sierra Leone**, and **Togo** to derive insights about solar-energy patterns and regional differences.

---

## 🎯 Objectives
1. **Task 1 – Git & Environment Setup**
   - Initialize repository and configure version control.
   - Set up a Python virtual environment (`venv`).
   - Add CI workflow and project structure.

2. **Task 2 – Data Profiling, Cleaning & EDA**
   - Profile, clean, and explore each country’s solar dataset.
   - Detect and handle missing values & outliers.
   - Generate visualizations for solar irradiance, temperature, and wind patterns.
   - Export cleaned data for downstream analysis.

---
```
## 🧱 Folder Structure
solar-challenge-week1/
┣ 📂.github
┃ ┗ 📂workflows
┃   ┗ 📜unittests.yml
┣ 📂.vscode
┃ ┗ 📜settings.json
┣ 📂data
┃ ┣ 📜benin_clean.csv
┃ ┣ 📜benin-malanville.csv
┃ ┣ 📜sierraleone_clean.csv
┃ ┣ 📜sierraleone-bumbuna.csv
┃ ┣ 📜togo_clean.csv
┃ ┗ 📜togo-dapaong_qc.csv
┣ 📂notebooks
┃ ┣ 📜__init__.py
┃ ┣ 📜benin_eda.ipynb
┃ ┣ 📜README.md
┃ ┣ 📜sierraleone_eda.ipynb
┃ ┗ 📜togo_eda.ipynb
┣ 📂scripts
┃ ┣ 📜__init__.py
┃ ┗ 📜README.md
┣ 📂src
┣ 📂tests
┃ ┗ 📜__init__.py
┣ 📜.gitignore
┣ 📜README.md
┗ 📜requirements.txt
```


---

## ⚙️ Environment Setup

### 🔧 Prerequisites
- Python ≥ 3.8  
- Git installed  
- VS Code or Jupyter Notebook  

### 🧩 Setup Steps
```bash
# 1️⃣ Clone the repository
git clone https://github.com/game-ale/solar-challenge-week1.git
cd solar-challenge-week1

# 2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run tests or CI check
pytest
🧪 Continuous Integration
The project uses GitHub Actions for automated CI testing.
The workflow file .github/workflows/unittests.yml runs on every push and ensures:

dependencies install correctly (pip install -r requirements.txt)

Python version verification

code style checks (via flake8 and black)

📊 Exploratory Data Analysis (EDA)
Each country’s data exploration is documented in its own Jupyter Notebook under /notebooks.
The analysis includes:

Profiling: summary statistics and missing-value overview

Cleaning: imputation of null values, outlier detection using Z-scores

Visualization: line plots, heatmaps, scatter plots, and wind roses

Correlation Analysis: relationships between GHI, DNI, DHI, temperature, and humidity

🇧🇯 Benin – benin_eda.ipynb
Insights:

The Global Horizontal Irradiance (GHI) and Direct Normal Irradiance (DNI) showed strong midday peaks, confirming high solar exposure around noon.

Minor anomalies were detected in sensor readings (ModA, ModB) due to temporary calibration issues, visible as sudden dips in irradiance values.

Relative Humidity (RH) exhibited an inverse correlation with temperature, consistent with typical tropical weather patterns.

After cleaning, the average GHI increased slightly, indicating data quality improvement.

🇸🇱 Sierra Leone – sierraleone_eda.ipynb
Insights:

Data from Bumbuna station displayed moderate solar irradiance but higher Relative Humidity (RH) levels compared to Benin and Togo.

Temperature remained stable throughout the day, with gradual increases toward midday and smooth declines after sunset.

Correlation heatmaps revealed that DHI and GHI had a strong linear relationship, confirming consistent measurement alignment.

A few extreme outliers in wind gusts (WSgust) were removed based on Z-score > 3 thresholding.

🇹🇬 Togo – togo_eda.ipynb
Insights:

The Togo-Dapaong dataset exhibited consistent solar irradiance across months, with noticeable peaks during the dry season.

Temperature and GHI were strongly correlated, while humidity negatively influenced irradiance levels during overcast days.

Wind rose plots highlighted prevailing wind directions from the northeast, affecting irradiance dispersion slightly.

Post-cleaning comparison showed smoother irradiance curves and reduced data noise.

📈 Key Performance Indicators (KPIs)
✅ Proper Dev Environment and Branch Setup

✅ Data Profiling and Cleaning Reports

✅ Visualization and Insight Generation

✅ Statistical Analysis Demonstrating Understanding of Solar Patterns

✅ Use of Version Control and GitHub Actions for Automation

📚 Requirements
shell
Copy code
pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
seaborn>=0.11.0
jupyter>=1.0.0
scikit-learn>=1.0.0
pytest>=6.0.0
black>=22.0.0
flake8>=4.0.0
python-dateutil
openpyxl
windrose
🧠 Future Work
Add interactive EDA dashboards (using Plotly or Streamlit)

Perform cross-country comparative analysis

Build predictive models for solar energy forecasting

🙌 Acknowledgment
This project is part of the 10 Academy AI Mastery Program.
Datasets were provided by 10 Academy for educational and analytical purposes.

👨‍💻 Author
Gemechu Alemu
📧 alemugemechu44@gmail.com
💼 GitHub Profile

🪪 License
This project is licensed under the MIT License – see the LICENSE file for details.

⭐️ If you found this project insightful, consider giving it a star on GitHub!


