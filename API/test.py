# import requests
# import json

# # API URL
# url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'

# # Make the GET request
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse JSON response
#     data = response.json()
    
#     # Define the filename
#     filename = 'response.json'
    
#     # Write the data to a file
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)
        
#     print(f"Data saved to {filename}")
# else:
#     print(f"Failed to fetch data: {response.status_code}")


import requests
import csv

# API URL
url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract the items (assuming 'items' contains the data we want)
    items = data.get('items', [])
    
    # Define the CSV file name
    filename = 'response.csv'
    
    # Open the CSV file for writing
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Determine the fieldnames from the first item keys (column headers)
        fieldnames = items[0].keys() if items else []
        
        # Create a writer object specifying the fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Write the rest of the rows
        for item in items:
            writer.writerow(item)
            
    print(f"Data saved to {filename}")
else:
    print(f"Failed to fetch data: {response.status_code}")
