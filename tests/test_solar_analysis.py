"""
Unit tests for src/solar_analysis.py
"""

import pytest
import pandas as pd
import numpy as np
import os
import tempfile
from src.solar_analysis import SolarEDA


@pytest.fixture
def sample_data():
    """Creates a sample dataframe for testing."""
    np.random.seed(42)
    dates = pd.date_range('2020-01-01', periods=100, freq='H')
    data = {
        'Timestamp': dates,
        'GHI': np.random.normal(200, 50, 100),
        'DNI': np.random.normal(150, 30, 100),
        'DHI': np.random.normal(50, 20, 100),
        'Tamb': np.random.normal(25, 5, 100),
        'RH': np.random.normal(60, 10, 100),
        'WS': np.random.normal(3, 1, 100),
        'WD': np.random.uniform(0, 360, 100),
        'BP': np.random.normal(1013, 10, 100),
        'Cleaning': np.random.choice([0, 1], 100),
        'ModA': np.random.normal(180, 40, 100),
        'ModB': np.random.normal(170, 35, 100),
        'WSgust': np.random.normal(4, 1.5, 100)
    }
    return pd.DataFrame(data)


@pytest.fixture
def temp_dirs():
    """Creates temporary directories for data and images."""
    with tempfile.TemporaryDirectory() as temp_dir:
        data_dir = os.path.join(temp_dir, 'data')
        image_dir = os.path.join(temp_dir, 'images')
        os.makedirs(data_dir)
        os.makedirs(image_dir)
        yield temp_dir, data_dir, image_dir


def test_solar_eda_init(sample_data, temp_dirs):
    """Test initialization of SolarEDA."""
    temp_dir, data_dir, image_dir = temp_dirs
    data_path = os.path.join(data_dir, 'test.csv')
    sample_data.to_csv(data_path, index=False)
    output_path = os.path.join(data_dir, 'clean.csv')

    eda = SolarEDA('Test', data_path, image_dir, output_path)
    assert eda.country == 'Test'
    assert eda.data_path == data_path
    assert eda.image_dir == image_dir
    assert eda.output_clean_path == output_path


def test_load_data(sample_data, temp_dirs):
    """Test data loading."""
    temp_dir, data_dir, image_dir = temp_dirs
    data_path = os.path.join(data_dir, 'test.csv')
    sample_data.to_csv(data_path, index=False)
    output_path = os.path.join(data_dir, 'clean.csv')

    eda = SolarEDA('Test', data_path, image_dir, output_path)
    df = eda.load_data()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert 'GHI' in df.columns


def test_clean_data(sample_data, temp_dirs):
    """Test data cleaning."""
    temp_dir, data_dir, image_dir = temp_dirs
    data_path = os.path.join(data_dir, 'test.csv')
    sample_data.to_csv(data_path, index=False)
    output_path = os.path.join(data_dir, 'clean.csv')

    eda = SolarEDA('Test', data_path, image_dir, output_path)
    eda.load_data()
    df_clean = eda.clean_data()
    assert isinstance(df_clean, pd.DataFrame)
    assert 'Timestamp' in df_clean.columns
    assert pd.api.types.is_datetime64_any_dtype(df_clean['Timestamp'])


def test_summary_statistics(sample_data, temp_dirs, capsys):
    """Test summary statistics printing."""
    temp_dir, data_dir, image_dir = temp_dirs
    data_path = os.path.join(data_dir, 'test.csv')
    sample_data.to_csv(data_path, index=False)
    output_path = os.path.join(data_dir, 'clean.csv')

    eda = SolarEDA('Test', data_path, image_dir, output_path)
    eda.load_data()
    eda.summary_statistics()
    captured = capsys.readouterr()
    assert "Summary Statistics" in captured.out
    assert "Missing Values" in captured.out


def test_save_cleaned_data(sample_data, temp_dirs):
    """Test saving cleaned data."""
    temp_dir, data_dir, image_dir = temp_dirs
    data_path = os.path.join(data_dir, 'test.csv')
    sample_data.to_csv(data_path, index=False)
    output_path = os.path.join(data_dir, 'clean.csv')

    eda = SolarEDA('Test', data_path, image_dir, output_path)
    eda.load_data()
    eda.clean_data()
    eda.save_cleaned_data()
    assert os.path.exists(output_path)


# Note: Plotting tests are omitted as they require matplotlib backend setup in CI.
# In a real scenario, use pytest-mpl or mock plt.show.
