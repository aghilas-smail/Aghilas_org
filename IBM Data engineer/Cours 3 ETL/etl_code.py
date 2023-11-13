import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"

# Function to extract data from CSV files
def extract_from_csv(file_path):
    try:
        dataframe = pd.read_csv(file_path)
        if not dataframe.empty:
            return dataframe
        else:
            print(f"Empty CSV file: {file_path}")
            return None
    except pd.errors.EmptyDataError:
        print(f"Empty CSV file: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {file_path}, Error: {str(e)}")
        return None

# Function to extract data from JSON files
def extract_from_json(file_path):
    try:
        dataframe = pd.read_json(file_path, lines=True)  # Use lines=True for JSON lines format
        if not dataframe.empty:
            return dataframe
        else:
            print(f"Empty JSON file: {file_path}")
            return None
    except Exception as e:
        print(f"Error reading JSON file: {file_path}, Error: {str(e)}")
        return None

# Function to extract data from XML files
def extract_from_xml(file_path):
    try:
        dataframe = pd.DataFrame(columns=["name", "height", "weight"])
        tree = ET.parse(file_path)
        root = tree.getroot()
        for person in root:
            name = person.find("name").text
            height = float(person.find("height").text)
            weight = float(person.find("weight").text)
            dataframe = pd.concat([dataframe, pd.DataFrame([{"name": name, "height": height, "weight": weight}])], ignore_index=True)
        return dataframe
    except Exception as e:
        print(f"Error reading XML file: {file_path}, Error: {str(e)}")
        return None

# Function to extract data from all supported file types
def extract():
    extracted_data = []  # Use a list for more efficient concatenation

    # Process all CSV files
    for csvfile in glob.glob("*.csv"):
        data = extract_from_csv(csvfile)
        if data is not None:
            extracted_data.append(data)

    # Process all JSON files
    for jsonfile in glob.glob("*.json"):
        data = extract_from_json(jsonfile)
        if data is not None:
            extracted_data.append(data)

    # Process all XML files
    for xmlfile in glob.glob("*.xml"):
        data = extract_from_xml(xmlfile)
        if data is not None:
            extracted_data.append(data)

    if extracted_data:
        return pd.concat(extracted_data, ignore_index=True)  # Concatenate the list of dataframes
    else:
        return pd.DataFrame(columns=["name", "height", "weight"])  # Return an empty DataFrame if no data


def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data 

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 
    
    
def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 
        
# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 