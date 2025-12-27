# Text Statistics Analyzer 
A simple Python project that analyzes a text file and computes basic text statistics such as word counts, common words, average word length, and execution time. This project was built incrementally to understand text processing, Python fundamentals, and basic project structure.

## Features
-   Read a `.txt` file
-   Extract words (lowercased, punctuation removed)
-   Count total and unique words
-   Find most common words
-   Compute average word length
-   Measure program execution time
-   Visualize top 10 most frequent words using a bar chart

## How It Works (High Level)

-   The program reads a text file.
-   Words are extracted using regular expressions.
-   Text statistics are computed from the extracted words.
-   Results are printed to the console.
-   A bar chart visualizes the top 10 most common words.
-   Execution time is measured.

## Requirements
-   Python 3.9+
-   mathplotlib

Install dependencies (if needed):
```
pip install mathplotlib
```

## Runnning The Project
- Place a text file named `data.txt` in the project directory.
- Run:
```
python main.py
```
The program will:

-   Print basic statistics
-   Display a bar chart
-   Show execution time

## Example Output
```
Text statistics
----------------
Total words       : 1250
Unique words      : 430
Avg word length   : 4.67

Execution time: 0.012345 seconds
```

## Testing
Basic unit tests are written using pytest.

Run tests from the project root:
```
pytest
```
## Design Notes
-   The project favors clarity over heavy optimization.
-   Logic is kept simple and readable.
-   Some parts are intentionally left with room for improvement to allow future refactoring and experimentation.

## Possible Future Improvements
-   Accept file paths as command-line arguments
-   Take variety of file types (PDFs etc.)
-   Improve tokenization (e.g., handling contractions)
-   Add sentence-level statistics
-   Export results to files
-   Package as a reusable module

## Purpose
This project was built as a learning exercise to:

-   Practice Python fundamentals
-   Understand text processing workflows
-   Learn basic testing and visualization
-   Get comfortable structuring small projects

## License
This project is for educational purposes.