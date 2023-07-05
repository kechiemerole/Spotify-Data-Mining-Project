import json
import csv

# Read the JSON data from a file
with open('MyData/StreamingHistory0.json', 'r') as json_file:
    json_data = json.load(json_file)

data_list = json_data # Assuming your JSON has a 'data' key containing a list of dictionaries

# Open the CSV file in write mode
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    header = data_list[0].keys()  # Assuming all dictionaries in the list have the same keys

    # Write the header row
    writer.writerow(header)

    # Write the data rows
    for item in data_list:
        writer.writerow(item.values())

    # Close the CSV file
    csv_file.close()



