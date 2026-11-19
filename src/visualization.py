
import matplotlib.pyplot as plt
import os


def generate_visualizations(data, output_dir="output"):
    """
    Generate healthcare data visualizations.

    Parameters:
        data (DataFrame): Cleaned healthcare dataset.
        output_dir (str): Directory to save charts.

    Returns:
        None
    """

    os.makedirs(output_dir, exist_ok=True)

    # 1. Disease Distribution
    disease_count = data["Disease"].value_counts()

    plt.figure(figsize=(9, 5))
    plt.bar(disease_count.index, disease_count.values)
    plt.title("Distribution of Diseases Among Patients")
    plt.xlabel("Type of Disease")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "disease_distribution.png"))
    plt.close()

    # 2. Age Distribution
    plt.figure(figsize=(9, 5))
    plt.hist(data["Age"], bins=10, edgecolor="black")
    plt.title("Age Distribution of Patients")
    plt.xlabel("Age of Patients")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "age_distribution.png"))
    plt.close()

    # 3. BMI Distribution
    plt.figure(figsize=(8, 5))
    plt.boxplot(data["BMI"])
    plt.title("BMI Distribution Among Patients")
    plt.ylabel("Body Mass Index")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "bmi_distribution.png"))
    plt.close()

    # 4. Recovery Status
    recovery_count = data["Recovery_Status"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(
        recovery_count.values,
        labels=recovery_count.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Patient Recovery Status Distribution")
    plt.savefig(os.path.join(output_dir, "recovery_status.png"))
    plt.close()

    print("All four visualizations generated successfully!")
