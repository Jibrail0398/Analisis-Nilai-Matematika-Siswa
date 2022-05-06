import pandas as pd
import Data_load as dt

def clear_null():
    df = dt.df.dropna()
    return df
df = clear_null()
df['Learning Method'] = df['Teacher'].map(lambda x :'Traditional Method' if 'Wesson' in x else 'Standard Method') 

def clear_col():
    del df['wesson']
    return df

clean_data = clear_col()
