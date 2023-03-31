import pandas as pd

# Read Excel file
file_name = "updated_combined_rent_1.xlsx"
df = pd.read_excel(file_name, engine="openpyxl")

# Define the keyword and column to search
keyword = "수시"
column_name = "신청구분"

# Split the cell content in the specified column by the keyword
df_split = df[column_name].str.split(keyword, expand=True)

# Stack the split columns as new rows
df_split = df_split.stack().reset_index(level=1, drop=True).to_frame(column_name)

# Remove the original column from the original DataFrame
df = df.drop(column_name, axis=1)

# Merge the original DataFrame with the new rows
df = df.join(df_split).reset_index(drop=True)

source_column = "신청구분"

df["타임"] = df[source_column].str.slice(0, 24)
df[source_column] = df[source_column].str.slice(24)

# Save the modified DataFrame to the same Excel file
df.to_excel(file_name, index=False, engine="openpyxl")

df = pd.read_excel(file_name, engine="openpyxl")

source_column_2 = "신청구분"

df["금액"] = df[source_column_2].str.slice(0, 4)
df[source_column_2] = df[source_column_2].str.slice(4)

df.to_excel(file_name, index=False, engine="openpyxl")
