from dataingestion import DataIngestion
import pandas as pd

di = DataIngestion()
di.csv_df('data/csv_input.csv')
di.json_df('data/json_input.json', records='all')
# result = di.sql_df()
result = di.df_concat()
# result = DataCleaning(result)
print(result)