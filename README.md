
# Automated Analysis Project

## Overview

This project aims to automate the process of analyzing datasets, visualizing the results, and narrating a story from the data using an AI-powered script. The core of the project is a Python script, `autolysis.py`, which leverages an LLM (GPT-4o-Mini) to analyze, visualize, and summarize the dataset in a human-readable story format.

This README will guide you through setting up and running the script on your local machine to perform automated analysis on datasets, visualize the results, and generate a narrative of insights.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
3. [Running the Script](#running-the-script)
4. [Understanding the Output](#understanding-the-output)
5. [Project Structure](#project-structure)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)

---

## Requirements

Before running the script, make sure your system meets the following requirements:

1. **Python 3.7 or higher** - The script is written in Python, and you'll need Python installed on your machine.
2. **Python Libraries** - The script requires some external libraries. The easiest way to install them is by using `pip`.
   
   Here's a list of dependencies:
   - `pandas`: for handling and analyzing CSV data.
   - `matplotlib`: for creating data visualizations.
   - `seaborn`: for better visualization with more advanced plotting features.
   - `requests`: for making HTTP requests to the AI Proxy API.
   - `python-dotenv`: for loading environment variables from a `.env` file.

3. **AIPROXY_TOKEN** - You need an API token to access the AI Proxy, which you can get from the TDS team.

---

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the repository

If you haven't already, clone the repository containing the script.

```bash
git clone https://github.com/your-username/automated-analysis.git
cd automated-analysis
```

### 2. Install Python and Dependencies

If you don't have Python 3.7+ installed, you can download it from [python.org](https://www.python.org/downloads/).

After installing Python, use `pip` to install the required libraries. It's a good practice to use a virtual environment for Python projects.

#### a. Create a Virtual Environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

#### b. Install the dependencies

Make sure you have the required libraries installed:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install the required libraries individually:

```bash
pip install pandas matplotlib seaborn requests python-dotenv
```

### 3. Set up the AI Proxy Token

To communicate with the AI Proxy, you'll need to set the `AIPROXY_TOKEN` environment variable. This token will be provided by your course instructors or TDS team.

Create a `.env` file in the root directory of the project and add the token like so:

```ini
AIPROXY_TOKEN=your-token-here
```

Make sure **not** to commit this `.env` file to the repository to protect your token.

### 4. Verify the Environment

Before running the script, verify that everything is set up correctly by checking if the required libraries and the environment variable are in place.

Run the following command to ensure the environment is ready:

```bash
python -c "import requests; import pandas as pd; print('Libraries are installed correctly')"
```

---

## Running the Script

Now that everything is set up, you can run the `autolysis.py` script on any CSV dataset. This script analyzes the dataset, generates visualizations, and uses an AI model to narrate a story based on the analysis.

### 1. Prepare the Dataset

The script is designed to work with any valid CSV file. You can use datasets like `goodreads.csv`, `happiness.csv`, or `media.csv` provided for the project or use your own dataset.

### 2. Run the Script

Use the `uvicorn` tool to run the Python script with the dataset of your choice. Replace `dataset.csv` with the actual CSV file path.

```bash
uv run autolysis.py dataset.csv
```

The script will perform the following tasks:
- Load and analyze the dataset.
- Generate summary statistics, handle missing values, and perform correlation analysis.
- Create visualizations like correlation heatmaps and missing values charts.
- Send relevant insights to the AI Proxy for narration.
- Generate a `README.md` file with the analysis results and visualizations.
- Save the visualizations as PNG images.

### 3. Output Files

After running the script, you should see the following files in the current directory:

- `README.md` - A markdown file with the analysis results written as a story.
- `*.png` files - Visualizations like correlation heatmaps and missing value bar charts (names will vary based on the dataset).

---

## Understanding the Output

After running the script, the output will be organized in the following way:

1. **README.md**
   - This file contains the narrative of the analysis, including:
     - Summary of the dataset.
     - Insights from the data analysis.
     - Implications of the findings.
     - Visualizations that support the analysis.
   
2. **Charts (PNG files)**
   - Charts like the **Correlation Heatmap** and **Missing Values Bar Chart** are saved as `.png` files and included in the `README.md`.
   - The visualizations provide supporting evidence for the story generated by the LLM.

---

## Project Structure

Here's a breakdown of the project's structure:

```
automated-analysis/
├── autolysis.py          # The main Python script that performs analysis and generates the story
├── .env                  # Contains the AI Proxy token (not committed to the repo)
├── requirements.txt      # List of required Python libraries
├── goodreads.csv         # Example dataset (optional)
├── happiness.csv         # Example dataset (optional)
├── media.csv             # Example dataset (optional)
└── README.md             # The generated markdown file with the analysis story
```

---

## Troubleshooting

Here are some common issues and solutions:

### 1. **Error: Missing dependencies**

Ensure that all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

### 2. **Error: Missing AIPROXY_TOKEN**

If the token is not set, make sure you've added it to the `.env` file in the correct format:

```ini
AIPROXY_TOKEN=your-token-here
```

Then reload the environment variables using:

```bash
source .env  # On Windows, use `set` to load variables
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By following these instructions, you should be able to successfully run the automated analysis script and generate insights from any dataset you choose.
