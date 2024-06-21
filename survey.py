import json
import pandas as pd
import re
import argparse

def preprocess_json_string(json_str):
    # Replace single quotes with double quotes
    json_str = re.sub(r"'", r'"', json_str)
    # Add double quotes around keys if missing
    json_str = re.sub(r'(?<!")(\b\w+\b)(?=\s*:)', r'"\1"', json_str)
    # Fix for numbers and boolean values not needing quotes
    json_str = re.sub(r'"\b(\d+(\.\d+)?|true|false|null)\b"', r'\1', json_str)
    # Remove trailing commas
    json_str = re.sub(r",\s*([}\]])", r'\1', json_str)
    return json_str

def main(json_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        raw_data = file.read()

    # Parse the main JSON data
    data = json.loads(raw_data)

    # Correct the format of the results field
    results_str = preprocess_json_string(data['results'])

    # Parse the results field as JSON
    results = json.loads(results_str)

    # Convert the results to a pandas DataFrame
    df = pd.DataFrame(results)

    # Display the DataFrame
    print(df)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process a JSON file and convert results to a pandas DataFrame.")
    parser.add_argument("json_file", help="Path to the JSON file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the main function
    main(args.json_file)
