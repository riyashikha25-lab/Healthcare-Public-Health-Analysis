
import pandas as pd


def load_data(file_path):
    """
    Load healthcare data from a CSV file.

    Parameters:
        file_path (str): Location of the CSV file.

    Returns:
        DataFrame: Loaded healthcare dataset.
    """
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return data

    except FileNotFoundError:
        raise FileNotFoundError("Dataset file not found.")

    except Exception as error:
        raise ValueError(f"Error loading dataset: {error}")
