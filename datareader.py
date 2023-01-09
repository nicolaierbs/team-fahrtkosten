import pandas as pd
import os


def read_sheet(sheet_name, refresh):
    if refresh:
        sheet_id = os.getenv('GOOGLE_SHEET_ID')
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        print(f'Load data from {url}')
        df = pd.read_csv(url)
        df.to_pickle(f'data/{sheet_name}.pkl')
        return df
    else:
        return pd.read_pickle(f'data/{sheet_name}.pkl')
