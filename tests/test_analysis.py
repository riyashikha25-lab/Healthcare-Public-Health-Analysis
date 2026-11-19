
import pandas as pd
import pytest

from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analysis import perform_analysis


def test_valid_dataset_loading():
    data = load_data("data/healthcare_data.csv")
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 251


def test_missing_values_handling():
    data = pd.DataFrame({
        "Age": [20, None, 40],
        "Glucose_Level": [90, 100, None],
        "BMI": [22, None, 28]
    })

    cleaned = clean_data(data)
    assert cleaned.isnull().sum().sum() == 0


def test_duplicate_removal():
    data = pd.DataFrame({
        "Age": [20, 20],
        "Glucose_Level": [90, 90],
        "BMI": [22, 22]
    })

    cleaned = clean_data(data)
    assert len(cleaned) == 1


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        load_data("invalid_file.csv")


def test_statistical_analysis():
    data = pd.DataFrame({
        "Age": [20, 30, 40],
        "Blood_Pressure": [100, 110, 120],
        "Glucose_Level": [90, 100, 110],
        "BMI": [20, 25, 30],
        "Hospital_Visits": [1, 2, 3],
        "Disease": ["Flu", "Diabetes", "Asthma"],
        "Gender": ["Male", "Female", "Male"],
        "Recovery_Status": [
            "Recovered",
            "Under Treatment",
            "Recovered"
        ]
    })

    summary = perform_analysis(data, "output/test_results")
    assert summary.loc["mean", "Age"] == 30
