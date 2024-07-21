import pandas as pd
import json


# Read the CSV file
csv_file_path = 'data.csv'
data_frame = pd.read_csv(csv_file_path)

# Convert the DataFrame to a dictionary
data_dict = data_frame.to_dict(orient='records')

# Write the dictionary to a JSON file
json_file_path = 'data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(f"Converted {csv_file_path} to {json_file_path}")
