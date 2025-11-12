# app/utils.py
import pandas as pd
import os

# -----------------------
# Load country data
# -----------------------
def load_country_data(country: str, data_dir: str, uploaded_file=None):
    """
    Load a country's CSV either from an uploaded file or from local data folder.
    
    Parameters:
    - country: Name of the country ("Benin", "Sierra Leone", "Togo")
    - data_dir: path to local data folder
    - uploaded_file: file object from Streamlit uploader (optional)
    
    Returns:
    - pandas DataFrame
    """
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    
    # fallback to local CSV
    file_map = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",
        "Togo": "togo_clean.csv"
    }
    path = os.path.join(data_dir, file_map[country])
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        return pd.DataFrame()  # empty DF if file missing

# -----------------------
# Summary statistics
# -----------------------
def summary_statistics(df: pd.DataFrame, cols=None):
    if cols is None:
        cols = ["GHI", "DNI", "DHI"]
    existing_cols = [c for c in cols if c in df.columns]
    if not existing_cols:
        return pd.DataFrame()
    summary = df[existing_cols].agg(["mean", "median", "std"]).round(2)
    return summary

# -----------------------
# Country metrics (average per country)
# -----------------------
def get_country_metrics(data_dir: str, uploaded_files=None):
    """
    Get average GHI, DNI, DHI for each country.
    
    Parameters:
    - data_dir: path to local data folder
    - uploaded_files: dict of {country_name: uploaded_file} (optional)
    
    Returns:
    - pandas DataFrame
    """
    countries = ["Benin", "Sierra Leone", "Togo"]
    results = []
    
    if uploaded_files is None:
        uploaded_files = {}

    for c in countries:
        uploaded_file = uploaded_files.get(c)
        df = load_country_data(c, data_dir, uploaded_file=uploaded_file)
        if not df.empty:
            summary = df[["GHI", "DNI", "DHI"]].mean()
            summary["country"] = c
            results.append(summary)
    
    if results:
        return pd.DataFrame(results)
    else:
        return pd.DataFrame(columns=["GHI", "DNI", "DHI", "country"])
