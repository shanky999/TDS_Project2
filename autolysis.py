import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests  # To make requests to the API proxy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the AI Proxy Token from the environment
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")  # Token starting with 'ey-'

# Check if the token is set
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN environment variable not set. Please ensure it's in the .env file.")

# Set up the proxy API endpoint (replace with actual proxy URL)
PROXY_API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions" 

# Function to analyze the dataset
def analyze_dataset(filename):
    try:
        # Load the CSV file
        #data = pd.read_csv(filename)
        data = pd.read_csv(filename, encoding='latin1')
        
        # Generate summary statistics
        summary = data.describe(include='all').transpose()
        missing_values = data.isnull().sum()
        
        # Generate correlation matrix if data is numerical
        correlation = data.corr(numeric_only=True)
        
        # Return analysis results
        return {
            "summary": summary,
            "missing_values": missing_values,
            "correlation": correlation,
            "columns": data.columns,
            "data_head": data.head(),
            "data": data  # Return the dataset for visualizations
        }

    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

# Function to create visualizations
def create_visualizations(data, correlation, filename):
    """
    Generate visualizations such as correlation heatmap and missing values bar chart.
    Args:
        data (pd.DataFrame): The input dataset.
        correlation (pd.DataFrame): The correlation matrix.
    Returns:
        List[str]: List of file paths for the saved visualizations.
    """
    visualizations = []

    # Correlation heatmap
    if correlation is not None and not correlation.empty and correlation.shape[0] > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm")
        base_name = os.path.splitext(os.path.basename(filename))[0]
        heatmap_file = f"{base_name}_correlation_heatmap.png"
        plt.title("Correlation Heatmap")
        plt.savefig(heatmap_file)
        plt.close()
        visualizations.append(heatmap_file)

    # Missing values bar chart
    missing_values = data.isnull().sum()
    if missing_values.sum() > 0:
        plt.figure(figsize=(8, 6))
        missing_values[missing_values > 0].plot(kind="bar")
        plt.title("Missing Values per Column")
        plt.ylabel("Count")
        missing_file = f"{base_name}_missing_values.png"
        plt.savefig(missing_file)
        plt.close()
        visualizations.append(missing_file)

    return visualizations

# Function to generate a story using the AI Proxy
def narrate_story(data_info, visualizations, filename):
    try:
        # Prepare the content for the prompt
        user_content = f"""
        You are a data analyst. Summarize the following dataset analysis as a story.

        Dataset Summary:
        {data_info['summary']}

        Missing Values:
        {data_info['missing_values']}

        Correlation Matrix:
        {data_info['correlation']}

        Columns:
        {list(data_info['columns'])}

        Example Data Rows:
        {data_info['data_head']}

        Visualizations:
        {visualizations}

        Write a story about the insights from the analysis.
        """

        # Prepare the headers
        headers = {
            "Authorization": f"Bearer {AIPROXY_TOKEN}",
            "Content-Type": "application/json"
        }

        # Prepare the payload
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a data analyst."},
                {"role": "user", "content": user_content}
            ],
            "max_tokens": 500
        }

        # Make the POST request to the proxy
        response = requests.post(PROXY_API_URL, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the story from the response
            story = response.json()["choices"][0]["message"]["content"].strip()
            base_name = os.path.splitext(os.path.basename(filename))[0]
            readme_file = f"README_{base_name}.md"

            # Save the story to README.md
            with open(readme_file, "w") as f:
                f.write(story)

            print("Story generated and saved in README.md")

        else:
            print(f"Error: {response.status_code} - {response.text}")
            sys.exit(1)

    except Exception as e:
        print(f"Error generating story: {e}")
        sys.exit(1)


# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    filename = sys.argv[1]

    # Analyze the dataset
    data_info = analyze_dataset(filename)

    # Create visualizations
    visualizations = create_visualizations(data_info["data"], data_info["correlation"], filename)

    # Narrate the story using the AI Proxy
    narrate_story(data_info, visualizations, filename)

    print("Analysis complete. Results saved in README.md and visualizations as PNG files.")

if __name__ == "__main__":
    main()


