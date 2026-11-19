
import os

from data_loader import load_data
from preprocessing import clean_data
from analysis import perform_analysis
from visualization import generate_visualizations


def main():
    """
    Execute the complete healthcare data analysis application.
    """

    input_file = "data/healthcare_data.csv"
    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    # Load dataset
    data = load_data(input_file)

    # Clean dataset
    cleaned_data = clean_data(data)

    # Save cleaned dataset
    cleaned_data.to_csv(
        os.path.join(output_dir, "cleaned_healthcare_data.csv"),
        index=False
    )

    # Perform statistical analysis
    perform_analysis(cleaned_data, output_dir)

    # Generate visualizations
    generate_visualizations(cleaned_data, output_dir)

    print("\nHealthcare Data Analysis Completed!")
    print("Cleaned records:", len(cleaned_data))
    print("Output directory:", output_dir)


if __name__ == "__main__":
    main()
