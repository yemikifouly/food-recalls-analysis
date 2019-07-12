import numpy as np
import pandas as pd

def get_samples_from_groups(grouped):
    randint = np.random.randint
    samples = []
    for group, items in grouped.items():
        start, end = items[0], items[-1]+1
        samples.append(randint(start, end))
    return samples

def extract_col_names_groups(df_dict):
    col_names_dict = {}
    for year, df in df_dict.items():
        columns = tuple(list(df.columns))
        if columns in col_names_dict:
            col_names_dict[columns].append(year)
        else:
            col_names_dict[columns] = [year]
    grouped_cols = {}
    for idx, (cols, years) in enumerate(col_names_dict.items()):
        grouped_cols[idx+1] = years
    grouped_cols
    return grouped_cols

def display_columns_by_df(df_dict, dtype=False):
    years = df_dict.keys()
    rows = []
    
    if dtype:      
        cols = df_dict[list(years)[0]].columns
        for year, df in df_dict.items():
            to_append = [np.dtype(df[col]).name for col in df.columns]
            rows.append(to_append)
        return pd.DataFrame(rows, index=years, columns=cols)
    
    for year, df in df_dict.items():
        rows.append(list(df.columns))
    return pd.DataFrame(rows, index=years)