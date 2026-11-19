
import pandas as pd
import numpy as np


def perform_analysis(data, output_dir="output"):
    """
    Perform statistical analysis on healthcare data.

    Parameters:
        data (DataFrame): Cleaned healthcare dataset.
        output_dir (str): Directory to save analysis results.

    Returns:
        DataFrame: Statistical summary.
    """

    import os
    os.makedirs(output_dir, exist_ok=True)

    numerical_columns = [
        "Age",
        "Blood_Pressure",
        "Glucose_Level",
        "BMI",
        "Hospital_Visits"
    ]

    # Calculate statistical summary
    summary = data[numerical_columns].describe()

    # Save statistical summary
    summary.to_csv(
        os.path.join(output_dir, "statistical_summary.csv")
    )

    # Calculate frequency distributions
    for column in ["Disease", "Gender", "Recovery_Status"]:
        frequency = data[column].value_counts()

        frequency.to_csv(
            os.path.join(output_dir, f"{column.lower()}_frequency.csv")
        )

    print("Statistical analysis completed!")

    return summary
