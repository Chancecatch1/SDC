import pandas as pd

# Read the Excel file
input_file = 'updated_combined_rent_1.xlsx'
output_file = 'updated_combined_rent_2.xlsx'

df = pd.read_excel(input_file)

# Update the "일자" column based on the length of the "신청구분" column
for index, row in df.iterrows():
    if len(row["신청구분"]) == 1:
        df.at[index, "일자"] = row["일자"][:10]

# Save the modified DataFrame to a new Excel file
df.to_excel(output_file, index=False)

# Read the Excel file
input_file = 'updated_combined_rent_2.xlsx'
output_file = 'updated_combined_rent_3.xlsx'

df = pd.read_excel(input_file)

# Store the indices of the rows to be removed
rows_to_remove = []

# Iterate through the rows
for index, row in df.iterrows():
    # Iterate through the following rows
    for index2, row2 in df.loc[index + 1:].iterrows():
        # Check if the "타임" and "단체명" values are the same
        if row['타임'] == row2['타임'] and row['단체명'] == row2['단체명'] and row['예술공간'] == row2['예술공간']:
            # Combine the "일자" values and update the current row
            df.at[index, '일자'] = f"{row['일자']}, {row2['일자']}"
            df.at[index, '신청구분'] = f"{row['신청구분']}, {row2['신청구분']}"
            # Add the index of the row to be removed
            rows_to_remove.append(index2)

# Drop the rows from the DataFrame
df = df.drop(rows_to_remove).reset_index(drop=True)

# Save the modified DataFrame to a new Excel file
df.to_excel(output_file, index=False)