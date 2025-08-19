# Package Sorter

This project classifies packages as `STANDARD`, `SPECIAL`, or `REJECTED` based on their dimensions and mass, following specific rules.

## Files
- `sort_packages.py`: Contains the sorting logic.
- `main.py`: Interactive script to test the sort function.
- `sort_packages_tests.py`: Unit tests for the sort function.

## Requirements
- Python 3.x

No external dependencies are required.

## How to Check if Python is Installed

Before installing Python, check if it is already installed on your system:

### Windows
1. Open the Command Prompt (`cmd`).
2. Run the following command:
   ```bash
   python --version
   ```
   If Python is installed, it will display the version number.

### macOS
1. Open the Terminal.
2. Run the following command:
   ```bash
   python3 --version
   ```
   If Python is installed, it will display the version number.

## How to Install Python

If Python is not installed, follow the steps below:

### Windows
1. Visit the [official Python website](https://www.python.org/downloads/).
2. Download the latest version for Windows.
3. Run the installer and ensure the option **Add Python to PATH** is checked.
4. Follow the installation steps.

### macOS
1. Open the Terminal and install Python using Homebrew (if Homebrew is installed):
   ```bash
   brew install python
   ```
   Alternatively, visit the [official Python website](https://www.python.org/downloads/) and download the latest version for macOS.

After installation, verify Python is installed by running the version check command again.

## How to Run the Main File

To interactively classify a package, run in the terminal:

```bash
python main.py
```

You will be prompted to enter the width, height, length (in cm), and mass (in kg) of the package. The script will print the classification result.

## How to Run the Tests

To run all unit tests and verify the logic, use in the terminal:

```bash
python sort_packages_tests.py
```

This will execute all test cases and show the results in the terminal.

## Author
Esther de Mattos