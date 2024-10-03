from dataingestion import DataIngestion
import pandas as pd
from db_script import Database
# from data_cleaning import DataCleaning


def DataCleaning(df):
    df=df.fillna(df.mean(), inplace=True)
    # df=df.drop_duplicates(inplace=True)
    # df = df.rename(columns=lambda x: x.strip())
    print('printing df: ', df)
    df['date'] = pd.to_datetime(df['date'])
    return df

di = DataIngestion()
di.csv_df('data/csv_input.csv')
di.json_df('data/json_input.json', records='all')
# result = di.sql_df()
result = di.df_concat()
# result = DataCleaning(result)
print(result)