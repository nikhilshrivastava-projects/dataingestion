# dataingestion
Data Ingestion from multiple sources

Steps to execute the program:
1. Run the mainscript.py and the output will contain the concatinated data from csv and json files. 

Data directory:
- This directory contains input files for csv, json and sql data

scripts directory:
- Contains following scripts:
    - data_cleaning.py - script to clean the data from the concatinated dataframe
    - dataingestion.py - contains script which reads data from csv, json and sql files
    - mainscript.py - executable script to get the output

Note: 
1. For sql data input, the development is done however the data concatination is returning None as of now and needs to invest more time to resolve it.
2. Data cleaning needs to be handled properly - need to check more on this.
3. users.db is created manually using sql_input.sql file by running below command:
    sqlite3 users.db < sql_input.sql
