# app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from utils import load_country_data, summary_statistics, get_country_metrics

# -----------------------
# Page & style settings
# -----------------------
st.set_page_config(
    page_title="Solar Insights Dashboard 🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)
sns.set_style("whitegrid")

DATA_DIR = os.path.join(os.getcwd(), "data")

# -----------------------
# Sidebar navigation
# -----------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:", ["Overview", "Country Comparison", "Explore Country", "Analytics Lab"]
)

# -----------------------
# Helper function
# -----------------------
def get_country_df(country, key_prefix=""):
    """Load from local data folder or uploaded CSV"""
    uploaded_file = st.file_uploader(f"Upload {country} CSV", type="csv", key=f"{key_prefix}_{country}")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.info(f"{country} CSV loaded from upload ✅")
        return df
    else:
        file_path = os.path.join(DATA_DIR, f"{country.lower().replace(' ','')}_clean.csv")
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            return df
        else:
            return pd.DataFrame()  # empty dataframe

# -----------------------
# Overview Page
# -----------------------
if page == "Overview":
    st.title("☀️ Solar Insights Dashboard")
    st.markdown("""
    Welcome to the **Solar Data Discovery Dashboard** developed for **10 Academy Week 0**.
    
    This app enables dynamic exploration of solar radiation datasets across **Benin**, **Sierra Leone**, and **Togo**.

    ---    
    **Features:**
    - Compare GHI, DNI, and DHI across countries
    - Explore trends within each dataset
    - Generate correlation heatmaps and statistical summaries
    - Download results interactively
    """)

    # Upload CSVs for each country
    df_benin = get_country_df("Benin", key_prefix="overview")
    df_sierra = get_country_df("Sierra Leone", key_prefix="overview")
    df_togo = get_country_df("Togo", key_prefix="overview")

    dfs = [df for df in [df_benin, df_sierra, df_togo] if not df.empty]

    if dfs:
        # Calculate summary from uploaded data or local CSVs
        df_summary = pd.DataFrame()
        for df, country in zip(dfs, ["Benin","Sierra Leone","Togo"]):
            if not df.empty:
                avg = df[["GHI","DNI","DHI"]].mean()
                avg["country"] = country
                df_summary = pd.concat([df_summary, pd.DataFrame([avg])], ignore_index=True)

        st.subheader("Average Solar Irradiance per Country")
        st.dataframe(df_summary.set_index("country"))

        fig, ax = plt.subplots(figsize=(7,5))
        sns.barplot(data=df_summary, x="country", y="GHI", palette="viridis")
        ax.set_title("Average GHI by Country", fontsize=13)
        st.pyplot(fig)
    else:
        st.info("No data available. Please upload CSVs above.")

# -----------------------
# Country Comparison Page
# -----------------------
elif page == "Country Comparison":
    st.title("🌍 Cross-Country Comparison")
    st.markdown("Compare irradiance metrics across selected countries.")

    countries = st.multiselect(
        "Select countries to compare:",
        ["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )
    metric = st.selectbox("Select metric:", ["GHI", "DNI", "DHI"])

    dfs = []
    for c in countries:
        df = get_country_df(c, key_prefix="comparison")
        if not df.empty:
            df["country"] = c
            dfs.append(df)

    if len(dfs) == 0:
        st.warning("No data available. Upload CSVs above.")
        st.stop()

    df_all = pd.concat(dfs, ignore_index=True)

    fig, ax = plt.subplots(figsize=(10,6))
    sns.boxplot(data=df_all, x="country", y=metric, palette="viridis")
    ax.set_title(f"{metric} Distribution by Country")
    st.pyplot(fig)

    st.subheader("📊 Summary Table")
    summary = df_all.groupby("country")[metric].agg(["mean", "median", "std"]).round(2)
    st.dataframe(summary)

    csv = summary.to_csv().encode("utf-8")
    st.download_button("⬇️ Download Summary CSV", csv, file_name="comparison_summary.csv", mime="text/csv")

# -----------------------
# Explore Country Page
# -----------------------
elif page == "Explore Country":
    st.title("📈 Explore Country Data")
    country = st.selectbox("Choose a country:", ["Benin", "Sierra Leone", "Togo"])
    df = get_country_df(country, key_prefix="explore")

    if df.empty:
        st.stop()

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    metric = st.selectbox("Select Metric to visualize:", ["GHI", "DNI", "DHI", "Tamb", "RH"])

    if "Timestamp" in df.columns:
        min_date, max_date = df["Timestamp"].min(), df["Timestamp"].max()
        date_range = st.slider(
            "Select date range:",
            min_value=min_date.to_pydatetime(),
            max_value=max_date.to_pydatetime(),
            value=(min_date.to_pydatetime(), max_date.to_pydatetime())
        )
        df = df[(df["Timestamp"] >= date_range[0]) & (df["Timestamp"] <= date_range[1])]

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(df["Timestamp"], df[metric], color="darkorange", alpha=0.8)
    ax.set_title(f"{metric} over Time - {country}")
    ax.set_xlabel("Time")
    ax.set_ylabel(metric)
    st.pyplot(fig)

    st.subheader("Summary Statistics")
    st.dataframe(summary_statistics(df))

    st.subheader("Correlation Heatmap")
    corr_cols = [c for c in ["GHI","DNI","DHI","Tamb","RH","WS"] if c in df.columns]
    fig, ax = plt.subplots(figsize=(7,5))
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    ax.set_title(f"Correlation Matrix - {country}")
    st.pyplot(fig)

# -----------------------
# Analytics Lab Page
# -----------------------
elif page == "Analytics Lab":
    st.title("🧠 Analytics Lab")
    st.markdown("Dive deeper into the data — visualize relationships and compare performance.")

    countries = ["Benin", "Sierra Leone", "Togo"]
    metric_x = st.selectbox("Select X-axis Metric:", ["GHI", "DNI", "DHI", "Tamb"])
    metric_y = st.selectbox("Select Y-axis Metric:", ["Tamb", "RH", "WS", "DHI"])

    dfs = []
    for c in countries:
        df = get_country_df(c, key_prefix="analytics")
        if not df.empty:
            df["country"] = c
            dfs.append(df)

    if len(dfs) == 0:
        st.warning("No data available. Upload CSVs above.")
        st.stop()

    df_all = pd.concat(dfs, ignore_index=True)

    fig, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(data=df_all, x=metric_x, y=metric_y, hue="country", alpha=0.7)
    ax.set_title(f"{metric_x} vs {metric_y} by Country")
    st.pyplot(fig)

    st.subheader("Global Correlation Heatmap (All Countries Combined)")
    corr_cols = [c for c in ["GHI","DNI","DHI","Tamb","RH","WS","BP"] if c in df_all.columns]
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(df_all[corr_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig)

    csv_data = df_all.sample(min(1000, len(df_all)), random_state=42).to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Sample Combined Data", csv_data, file_name="combined_sample.csv")

# -----------------------
# Footer
# -----------------------
st.markdown("""
---
Developed by **Bekam Genene** for **10 Academy Solar Challenge Week 0**  
🌞 *"Turning sunlight into insight!"*  
🔗 [GitHub Repository](https://github.com/Bekamgenene/solar-challenge-week0)
""")
