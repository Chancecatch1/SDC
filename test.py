import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': ['apple', 'banana', 'cherry', None],
    'C': [10, None, 30, 40]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Drop rows where the cell value in column 'B' is empty or NaN
df = df.dropna(subset=['B'])
print("\nDataFrame after removing rows with empty cells in column 'B':")
print(df)