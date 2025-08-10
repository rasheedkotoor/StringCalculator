# StringCalculator

A Test-Driven Development (TDD) implementation of a String Calculator for the Incubyte assessment.
*This project is part of the Incubyte assessment and is for educational purposes.*


## Overview

The StringCalculator is a simple utility that takes a string of numbers and returns their sum. It demonstrates clean code principles and test-driven development practices.

## Features

- **Empty String Handling**: Returns 0 for empty input
- **Single Number**: Returns the number itself
- **Multiple Numbers**: Supports comma-separated numbers
- **Flexible Delimiters**: Supports both comma (`,`) and newline (`\n`) as delimiters
- **Whitespace Tolerance**: Handles numbers with surrounding spaces
- **Mixed Input**: Ignores non-numeric strings and processes only valid numbers
- **Floating Point Support**: Handles decimal numbers
- **Negative Numbers**: Supports negative number calculations

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd StringCalculator
    ```

2. Create and activate a virtual environment:
    ```bash
    # Create virtual environment
    python -m venv venv
    
    # Activate virtual environment
    # On Windows:
    venv\Scripts\activate
    
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```python
from StringCalculator.string_calculator import StringCalculator

calculator = StringCalculator()

# Basic usage
result = calculator.add("1,2,3")  # Returns: 6
result = calculator.add("1\n2,3")  # Returns: 6 (mixed delimiters)
result = calculator.add("1.5,2.5")  # Returns: 4.0 (floating point)
result = calculator.add("1,a,2,b,3")  # Returns: 6 (ignores non-numeric)
```

## Testing

Run the test suite using pytest:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_string_calculator.py

# Run specific test method
pytest tests/test_string_calculator.py::TestStringCalculator::test_empty_string_returns_zero
```

## Project Structure

```
StringCalculator/
├── __init__.py
├── .venv/
├── tests/
│   ├── __init__.py
│   └── test_string_calculator.py
├── string_calculator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Development

This project follows Test-Driven Development (TDD) principles:

1. **Red**: Write a failing test
2. **Green**: Write minimal code to make the test pass
3. **Refactor**: Improve code while keeping tests green
