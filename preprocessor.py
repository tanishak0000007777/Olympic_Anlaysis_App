import pandas as pd

def preprocessor():
    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')

    # Strip column names to avoid hidden space issues
    df.columns = df.columns.str.strip()
    region_df.columns = region_df.columns.str.strip()

    # Filter only Summer Olympics
    df = df[df['Season'] == 'Summer']

    # Drop 'region' and 'notes' if already present in athlete_events.csv
    if 'region' in df.columns:
        df.drop(columns=['region'], inplace=True)
    if 'notes' in df.columns:
        df.drop(columns=['notes'], inplace=True)

    # Merge safely on NOC
    df = df.merge(region_df, on='NOC', how='left')

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # One-hot encoding Medal column
    df = pd.concat([df, pd.get_dummies(df['Medal']).astype(int)], axis=1)

    return df
