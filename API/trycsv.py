# import json
# import csv

# # Load the JSON data from the file
# with open('response.json', 'r', encoding='utf-8') as jsonfile:
#     items = json.load(jsonfile)
  

# # Define the CSV file name
# filename = 'response.csv'

# # Open the CSV file for writing
# with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#     # Define the fieldnames (column headers) including nested 'owner' fields
#     fieldnames = ['account_id', 'reputation', 'user_id', 'user_type',
#                   'profile_image', 'display_name', 'link']
    
#     # Create a writer object specifying the fieldnames
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     # Write the header row
#     writer.writeheader()
    
#     # Process each item and write it to the CSV
#     for item in items:
#         # Flatten the 'owner' nested object
#         owner = item.pop('owner')
#         item['account_id'] = owner['account_id']
#         item['reputation'] = owner['reputation']
#         item['user_id'] = owner['user_id']
#         item['user_type'] = owner['user_type']
#         item['profile_image'] = owner['profile_image']
#         item['display_name'] = owner['display_name']
#         item['owner_link'] = owner['link']
        
#         # Convert 'tags' list to a string
#         item['tags'] = ', '.join(item['tags'])
        
#         # Write the item to the CSV
#         writer.writerow(item)
        
# print(f"Data saved to {filename}")



import json
import csv

# Load the JSON data from the file
with open('data.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# The list of items is under the 'items' key
items = data['items']

# Define the CSV file name
filename = 'owner_data.csv'

# Open the CSV file for writing
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Define the fieldnames (column headers) based on your requirements
    fieldnames = ['account_id', 'reputation', 'user_id', 'user_type',
                  'profile_image', 'display_name', 'link']
    
    # Create a writer object specifying the fieldnames
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Process each item to extract and write the 'owner' information
    for item in items:
        # Extract the 'owner' object from the current item
        owner = item['owner']
        
        # Create a new dictionary only with the specified keys
        owner_info = {key: owner[key] for key in fieldnames if key in owner}
        
        # Write the 'owner' info to the CSV
        writer.writerow(owner_info)
        
print(f"Data saved to {filename}")
