
import pandas as pd


def clean_data(data):
    """
    Clean the healthcare dataset.

    Parameters:
        data (DataFrame): Original healthcare dataset.

    Returns:
        DataFrame: Cleaned healthcare dataset.
    """

    data = data.copy()

    # Remove duplicate records
    data = data.drop_duplicates()

    # Convert Age into numeric format
    data["Age"] = pd.to_numeric(
        data["Age"], errors="coerce"
    )

    # Fill missing numerical values with median
    numerical_columns = [
        "Age",
        "Glucose_Level",
        "BMI"
    ]

    for column in numerical_columns:
        data[column] = data[column].fillna(
            data[column].median()
        )

    return data
