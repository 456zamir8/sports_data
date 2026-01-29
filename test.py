import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('t20.csv')

df.drop(columns=["Unnamed: 0", "Unnamed: 15"], inplace=True)

df['Not_Out_HS'] = df['HS'].astype(str).str.contains(r'\*')
df['HS'] = (
    df['HS']
    .astype(str)
    .replace('-', pd.NA)
    .str.replace('*', '', regex=False)
    .astype('Int64')
)

numeric_cols = ['Mat', 'Inns', 'NO', 'Runs', 'Ave', 'BF', 'SR', '100', '50', '0', '4s', '6s']

df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df["Name"] = df["Player"].str.extract(r'^(.*?)\s*\(')
df["Country"] = df["Player"].str.extract(r'\((.*?)\)')

np.random.seed(42)
df['Age'] = np.random.randint(18, 40, size=len(df))

df.drop(columns=['Player'], inplace=True)

df = df.dropna()