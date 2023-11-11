import etl_code as r
# Log the initialization of the ETL process 
r.log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
r.log_progress("Extract phase Started") 
extracted_data = r.extract() 

print(extracted_data)

 
# Log the completion of the Extraction process 
r.log_progress("Extract phase Ended") 

 
# Log the beginning of the Transformation process 
r.log_progress("Transform phase Started") 
transformed_data = r.transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
r.log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
r.log_progress("Load phase Started") 
r.load_data(r.target_file,transformed_data) 
 
# Log the completion of the Loading process 
r.log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
r.log_progress("ETL Job Ended") 