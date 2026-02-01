# Weekly Temperature Report (Python)

This project is a simple Python script that generates a **weekly temperature report** using random values. It demonstrates the use of:

- Lists
- Loops
- `zip()` function
- ANSI color codes
- Basic statistics (average, min, max)

## Features

- Generates random daily temperatures between **1°C and 35°C**
- Displays a colorful weekly report in the terminal
- Calculates the **weekly average temperature**
- Finds and shows the **hottest and coldest days of the week**

## Example Output

- Weekly temperature list
- Average temperature
- Hottest day
- Coldest day  
(All displayed in colored terminal output)

## How It Works

1. A list of days is defined.
2. Random temperatures are generated using `random.randint()`.
3. Data is printed using formatted strings and ANSI color codes.
4. The script calculates:
   - Weekly average temperature
   - Maximum (hottest)
   - Minimum (coldest)

## Requirements

- Python 3.x

## How to Run

```bash
python weekly_temperature_report.py
