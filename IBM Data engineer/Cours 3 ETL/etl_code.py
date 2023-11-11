import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 


log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

# A function for the csv file.
def extract_from_csv(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe

# A function for the json file.
def extract_from_json(file_path):
    dataframe = pd.read_json(file_path, line=True)
    return dataframe

# A function for the json file.

def extract_from_xml(file_path):
    dataframe = pd.DataFrame(columns=["name","height","weight"])
    tree = ET.parse(file_path) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        # if he find the 3 variables (name, height and weight he return the datafram)
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe


# A function how englobe all the files (CSV, JSON and XML)

def extract():
    