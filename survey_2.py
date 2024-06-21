import json
import re
import pandas as pd

def file_to_string(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def preprocess_json_string(json_str):
    # Replace single quotes with double quotes
    json_str = re.sub(r"'fileId': '", r'"fileId": "', json_str)
    json_str = re.sub(r"', 'task': 'platon', 'task_version': '1.6', 'stdlib_version': 'v0.0.13', 'results'", r'", "task": "platon", "task_version": "1.6", "stdlib_version": "v0.0.13", "results"', json_str)
    return json_str

json_string = preprocess_json_string(file_to_string('DRR022997.json'))

# Parse the results field as JSON
results = json.loads(json_string)

# Convert the results to a pandas DataFrame
df = pd.DataFrame(results)

# Display the DataFrame
print(df)