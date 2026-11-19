# System Architecture and Workflow

## 1. System Architecture

The Healthcare and Public Health Data Analysis application follows a modular architecture. Each Python module performs a specific task, making the application easier to understand, test and maintain.

The main modules are:

- **data_loader.py:** Loads the healthcare dataset from a CSV file.
- **preprocessing.py:** Removes duplicate records and handles missing or inconsistent values.
- **analysis.py:** Calculates descriptive statistics and frequency distributions.
- **visualization.py:** Generates charts using Matplotlib.
- **main.py:** Coordinates the complete data analysis process.

## 2. Application Workflow

The application follows these steps:

1. The user provides the healthcare dataset.
2. The data loader reads the dataset.
3. The preprocessing module cleans the data.
4. The analysis module calculates statistical summaries and frequency counts.
5. The visualization module generates charts.
6. The cleaned dataset, statistical summaries and visualizations are saved in the output folder.

## 3. Technologies Used

- Python for application development.
- Pandas and NumPy for data handling.
- Matplotlib for data visualization.
- Pytest for unit testing.
- Git and GitHub for version control and project management.

## 4. Conclusion

The modular architecture separates the major tasks of the application. This improves readability, maintainability, testing and reproducibility.
