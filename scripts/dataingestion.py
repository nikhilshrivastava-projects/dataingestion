import pandas as pd
import sqlite3
import json

class DataIngestion:
    def __init__(self):
        self.df = []

    def csv_df(self, file):
        csvdf = pd.read_csv(file)
        self.df.append(csvdf)

    def json_df(self, file, records):
        data = pd.read_json(file)
        # data = json.loads(file)
        if records == 'single':
            for record in data:
                self.df.append(record)
        else:
            with open(file) as f:
                # data = [json.loads(line) for line in f]
                data = pd.read_json(file)
            json_df = pd.DataFrame(data)
        self.df.append(json_df)

    def sql_df(self):
        conn = sqlite3.connect('file:///Users/nikhil/Documents/git_repository/dataingestion/dataingestion/data/users.db', uri=True)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        sql_df = pd.DataFrame(cursor.fetchall(), columns=[column[0] for column in cursor.description])
        self.df = self.df.append(sql_df)
        conn.close()
        return self.df

    def df_concat(self):
        final_df = pd.concat(self.df, ignore_index=True)
        return final_df