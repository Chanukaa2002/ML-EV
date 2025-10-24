import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('optimal_route_dataset_srilanka.csv')
print("Available columns:", list(df.columns))
print()

cols = ['traffic_level', 'weather', 'driving_style']

for col in cols:
    if col in df.columns:
        print(f'{col}:')
        le = LabelEncoder()
        le.fit(df[col])
        for i, val in enumerate(le.classes_):
            print(f'  {val} -> {i}')
        print()
