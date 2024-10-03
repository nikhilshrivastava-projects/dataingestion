import pandas as pd
def DataCleaning(df):
    df=df.fillna(df.mean(), inplace=True)
    # df=df.drop_duplicates(inplace=True)
    # df = df.rename(columns=lambda x: x.strip())
    print('printing df: ', df)
    df['date'] = pd.to_datetime(df['date'])
    return df