# Testing and Validation

## 1. Introduction
Testing was performed to verify the reliability and correctness
of the Healthcare and Public Health Data Analysis application.

The Pytest framework was used to execute automated unit tests.

## 2. Testing Framework
Pytest was selected because it provides a simple way to
write and execute Python unit tests.

## 3. Unit Tests Performed

1. Valid Dataset Loading: Checks whether the CSV dataset loads successfully.
2. Missing Values Handling: Checks whether missing values are handled.
3. Duplicate Removal: Verifies that duplicate records are removed.
4. Invalid File Handling: Checks whether the application handles a missing file.
5. Statistical Analysis: Verifies that statistical analysis produces the expected mean.

## 4. Test Results

| Test Case | Result |
|---|---|
| Dataset Loading | PASSED |
| Missing Values Handling | PASSED |
| Duplicate Removal | PASSED |
| Invalid File Handling | PASSED |
| Statistical Analysis | PASSED |

Total Tests: 5  
Passed: 5  
Failed: 0

## 5. Reliability
Unit testing helps identify errors in individual modules.
Successful execution of all five tests indicates that
the tested functions behave as expected for the test cases.

## 6. Conclusion
The application successfully passed all five unit tests.
Testing improves confidence in the application's data
loading, preprocessing and analysis functions.
