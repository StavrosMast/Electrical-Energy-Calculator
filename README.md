# Energy Calculator

## Description

Energy Calculator is a Python application with a graphical user interface that helps users calculate their energy costs based on various factors. It uses the CustomTkinter library for creating a modern-looking GUI.

## Features

- Calculate energy costs based on starting and current KWh readings
- Include fixed fees in the calculation
- Account for the number of days charged
- Consider various fees and charges such as regulated charges, air pollution fees, and community fees
- Display the total charge for the energy consumption

## Requirements

- Python 3.x
- CustomTkinter library

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```bash
pip install customtkinter
```


## Usage

Run the `energy_calculator.py` file:

```bash
python energy_calculator.py
```


The application window will open, allowing you to input the following information:

1. Starting KWh
2. Current KWh
3. Fixed Fees
4. Days Charged

After entering the required information, click the "Show Result" button to see the calculated total charge.

## Code Structure

The main components of the application are:

1. `EnergyCalculator` class (lines 5-73):
   - Initializes the GUI components
   - Handles the calculation logic

2. Main execution block (lines 74-78):
   - Creates the root window
   - Initializes the EnergyCalculator
   - Starts the main event loop

## Customization

You can modify the calculation factors in the `showResult` method of the `EnergyCalculator` class to adjust the energy cost calculation according to your specific needs or local energy pricing.

## License

[MIT](https://choosealicense.com/licenses/mit/)
