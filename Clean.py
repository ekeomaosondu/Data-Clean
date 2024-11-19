import pandas as pd
import Dependencies as dep

def clean_df(df):
    df['text'] = df['text'].apply(dep.clean_corpus)
    return df




