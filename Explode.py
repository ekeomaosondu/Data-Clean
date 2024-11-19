import pandas as pd
import Dependencies as dep

def explode_df(df):
    exploded_rows = []
    
    cleaned = dep.clean_df(df)
    
    for i in range(len(cleaned)):
        row = cleaned.iloc[i]
        sentences = row['text'].split('. ')

        for sent in sentences:
            new_row = row.copy()
            new_row['text'] = sent.strip()
            exploded_rows.append(new_row)

    exploded_df = pd.DataFrame(exploded_rows, columns=df.columns)
    return exploded_df

