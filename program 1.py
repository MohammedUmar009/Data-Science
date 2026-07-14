import pandas as pd

df = pd.read_csv("CSV file.csv")

print("First 10 Rows:")
print(df.head(10))

rows, cols = df.shape
print("\nNumber of Rows:", rows)
print("Number of Columns:", cols)

print("\nSummary Statistics:")
print(df.describe())