"""
Solar data analysis module.

This module provides a class-based approach to performing exploratory data analysis (EDA)
on solar irradiance datasets. It encapsulates repeated logic from country-specific notebooks
into reusable methods.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from math import pi
from typing import List, Optional, Dict, Any
from .plot_utils import show_and_save_plot


class SolarEDA:
    """
    A class for performing exploratory data analysis on solar irradiance data.

    This class handles data loading, cleaning, outlier detection, and various analyses
    including time series, correlations, distributions, and visualizations.

    Attributes:
        country (str): The country name (e.g., 'Benin', 'Togo').
        data_path (str): Path to the raw data CSV file.
        image_dir (str): Directory to save generated plots.
        output_clean_path (str): Path to save the cleaned data CSV.
        df (pd.DataFrame): The loaded raw data.
        df_clean (pd.DataFrame): The cleaned data after processing.
    """

    def __init__(self, country: str, data_path: str, image_dir: str, output_clean_path: str):
        """
        Initializes the SolarEDA instance.

        Parameters:
        - country (str): Country name for labeling.
        - data_path (str): Path to the input CSV file.
        - image_dir (str): Directory for saving plots.
        - output_clean_path (str): Path for saving cleaned data.
        """
        self.country = country
        self.data_path = data_path
        self.image_dir = image_dir
        self.output_clean_path = output_clean_path
        self.df = None
        self.df_clean = None

        # Ensure image directory exists
        os.makedirs(self.image_dir, exist_ok=True)

        # Set plotting styles
        plt.style.use("ggplot")
        sns.set_palette("viridis")

    def load_data(self) -> pd.DataFrame:
        """
        Loads the data from the specified path.

        Returns:
            pd.DataFrame: The loaded dataframe.
        """
        self.df = pd.read_csv(self.data_path)
        print("Data loaded successfully")
        print("Shape:", self.df.shape)
        print(self.df.head())
        return self.df

    def summary_statistics(self) -> None:
        """
        Prints summary statistics and missing values information.
        """
        print("Summary Statistics")
        print(self.df.describe())
        print("\nMissing Values")
        print(self.df.isna().sum())
        missing_cols = self.df.columns[self.df.isna().mean() > 0.05]
        print(f"\nColumns with >5% missing values: {list(missing_cols)}")

    def clean_data(self) -> pd.DataFrame:
        """
        Cleans the data: fills missing values, handles timestamps, detects and clips outliers.

        Returns:
            pd.DataFrame: The cleaned dataframe.
        """
        self.df_clean = self.df.copy()

        # Fill missing values for numeric columns
        for col in self.df_clean.select_dtypes(include=np.number).columns:
            self.df_clean[col] = self.df_clean[col].fillna(self.df_clean[col].median())

        # Handle Timestamp
        if 'Timestamp' in self.df_clean.columns:
            self.df_clean['Timestamp'] = pd.to_datetime(self.df_clean['Timestamp'], errors='coerce')
            self.df_clean.dropna(subset=['Timestamp'], inplace=True)

        # Outlier detection and clipping
        outlier_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
        for col in outlier_cols:
            if col in self.df_clean.columns:
                z = np.abs(stats.zscore(self.df_clean[col].dropna()))
                outliers = (z > 3).sum()
                print(f"{col}: {outliers} outliers detected (|Z|>3)")
                self.df_clean[col] = np.clip(self.df_clean[col], self.df_clean[col].quantile(0.01), self.df_clean[col].quantile(0.99))

        return self.df_clean

    def time_series_analysis(self) -> None:
        """
        Performs time series analysis for key columns.
        """
        if 'Timestamp' not in self.df_clean.columns:
            print("No Timestamp column for time series analysis.")
            return

        time_cols = ['GHI', 'DNI', 'DHI', 'Tamb']
        for col in time_cols:
            if col in self.df_clean.columns:
                plt.figure(figsize=(12, 4))
                plt.plot(self.df_clean['Timestamp'], self.df_clean[col], alpha=0.7)
                plt.title(f"{col} over Time")
                plt.xlabel("Timestamp")
                plt.ylabel(col)
                show_and_save_plot(f"time_series_{col}.png", self.image_dir)

    def cleaning_impact_analysis(self) -> None:
        """
        Analyzes the impact of cleaning on ModA and ModB.
        """
        if not {'Cleaning', 'ModA', 'ModB'}.issubset(self.df_clean.columns):
            print("Cleaning, ModA, or ModB columns missing for impact analysis.")
            return

        plt.figure(figsize=(8, 5))
        self.df_clean.groupby('Cleaning')[['ModA', 'ModB']].mean().plot(kind='bar', ax=plt.gca())
        plt.title("Average ModA & ModB Before/After Cleaning")
        plt.ylabel("Mean Irradiance (W/m²)")
        show_and_save_plot("cleaning_impact.png", self.image_dir)

    def correlation_analysis(self) -> None:
        """
        Generates correlation heatmap and scatter plots.
        """
        corr_cols = [c for c in ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'Tamb', 'RH', 'WS'] if c in self.df_clean.columns]
        if corr_cols:
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.df_clean[corr_cols].corr(), annot=True, cmap="viridis", fmt=".2f")
            plt.title("Correlation Heatmap")
            show_and_save_plot("correlation_heatmap.png", self.image_dir)

        # Scatter plots
        scatter_pairs = [('WS', 'GHI'), ('WSgust', 'GHI'), ('RH', 'Tamb'), ('RH', 'GHI')]
        for x, y in scatter_pairs:
            if {x, y}.issubset(self.df_clean.columns):
                sns.scatterplot(data=self.df_clean, x=x, y=y)
                plt.title(f"{x} vs {y}")
                show_and_save_plot(f"scatter_{x}_vs_{y}.png", self.image_dir)

    def distribution_analysis(self) -> None:
        """
        Generates histograms for key columns and wind rose if applicable.
        """
        for col in ['GHI', 'WS']:
            if col in self.df_clean.columns:
                plt.figure(figsize=(6, 4))
                sns.histplot(self.df_clean[col], kde=True, bins=30)
                plt.title(f"Distribution of {col}")
                show_and_save_plot(f"hist_{col}.png", self.image_dir)

        # Wind rose
        if {'WS', 'WD'}.issubset(self.df_clean.columns):
            wind = self.df_clean[['WS', 'WD']].dropna()
            bins = np.arange(0, 360, 30)
            wind['WD_bin'] = pd.cut(wind['WD'], bins=bins, include_lowest=True)
            avg_ws = wind.groupby('WD_bin')['WS'].mean()
            angles = np.linspace(0, 2 * np.pi, len(avg_ws), endpoint=False)
            values = avg_ws.values

            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.bar(angles, values, width=0.5, color='teal', alpha=0.7)
            ax.set_theta_zero_location("N")
            ax.set_theta_direction(-1)
            plt.title("Wind Rose: Avg Wind Speed by Direction")
            show_and_save_plot("wind_rose.png", self.image_dir)

    def temperature_analysis(self) -> None:
        """
        Analyzes temperature-related plots.
        """
        if {'RH', 'Tamb', 'GHI'}.issubset(self.df_clean.columns):
            plt.figure(figsize=(8, 5))
            sns.scatterplot(data=self.df_clean, x='RH', y='Tamb', hue='GHI', palette='coolwarm')
            plt.title("Effect of RH on Temperature and Solar Radiation")
            show_and_save_plot("RH_Tamb_GHI_effect.png", self.image_dir)

    def bubble_chart(self) -> None:
        """
        Generates a bubble chart for GHI, Tamb, RH, and BP.
        """
        if {'GHI', 'Tamb', 'RH', 'BP'}.issubset(self.df_clean.columns):
            plt.figure(figsize=(8, 6))
            plt.scatter(self.df_clean['GHI'], self.df_clean['Tamb'],
                        s=self.df_clean['RH'], c=self.df_clean['BP'], cmap='coolwarm', alpha=0.6)
            plt.title("Bubble Chart: GHI vs Tamb (Bubble = RH, Color = BP)")
            plt.xlabel("GHI (W/m²)")
            plt.ylabel("Tamb (°C)")
            plt.colorbar(label="Barometric Pressure (hPa)")
            show_and_save_plot("bubble_GHI_Tamb_RH_BP.png", self.image_dir)

    def monthly_hourly_analysis(self) -> None:
        """
        Performs monthly and hourly trend analyses.
        """
        if 'Timestamp' not in self.df_clean.columns:
            print("No Timestamp column for monthly/hourly analysis.")
            return

        self.df_clean['Month'] = self.df_clean['Timestamp'].dt.month_name()
        self.df_clean['Hour'] = self.df_clean['Timestamp'].dt.hour

        # Monthly
        monthly = self.df_clean.groupby('Month')[['GHI', 'DNI', 'DHI', 'Tamb']].mean().reindex(
            ['January','February','March','April','May','June','July','August','September','October','November','December']
        )
        monthly.plot(kind='bar', figsize=(12,6))
        plt.title("Average Monthly Solar & Temperature Patterns")
        plt.ylabel("Mean Values")
        show_and_save_plot("monthly_trends.png", self.image_dir)

        # Hourly
        hourly = self.df_clean.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()
        hourly.plot(figsize=(12,6))
        plt.title("Average Hourly Solar & Temperature Patterns")
        plt.xlabel("Hour of Day")
        plt.ylabel("Mean Values")
        show_and_save_plot("hourly_trends.png", self.image_dir)

    def save_cleaned_data(self) -> None:
        """
        Saves the cleaned data to the specified path.
        """
        self.df_clean.to_csv(self.output_clean_path, index=False)
        print(f"Cleaned data saved to: {self.output_clean_path}")
        print(f"All plots saved to: {self.image_dir}")

    def run_full_analysis(self) -> None:
        """
        Runs the complete EDA pipeline.
        """
        self.load_data()
        self.summary_statistics()
        self.clean_data()
        self.time_series_analysis()
        self.cleaning_impact_analysis()
        self.correlation_analysis()
        self.distribution_analysis()
        self.temperature_analysis()
        self.bubble_chart()
        self.monthly_hourly_analysis()
        self.save_cleaned_data()
