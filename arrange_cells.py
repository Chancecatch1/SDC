import pandas as pd

# Read the Excel file
input_file = 'updated_combined_rent_1.xlsx'
output_file = 'updated_combined_rent_2.xlsx'

df = pd.read_excel(input_file)

# Update the "일자" column based on the length of the "신청구분" column
for index, row in df.iterrows():
    if len(row["신청구분"]) == 1:
        df.at[index, "일자"] = row["일자"][:10]

# Iterate through the rows
rows_to_remove = set()
for index, row in df.iterrows():
    # Initialize merged indices list
    merged_indices = [index]
    
    # Iterate through the following rows
    for index2, row2 in df.loc[index + 1:].iterrows():
        # Check if the "타임" and "단체명" values are the same
        if row['타임'] == row2['타임'] and row['단체명'] == row2['단체명'] and row['예술공간'] == row2['예술공간']:
            # Add the index of the row to be merged
            merged_indices.append(index2)
    
    # Merge the "일자" and "신청구분" values and update the current row
    if len(merged_indices) > 1:
        for index_to_merge in merged_indices[1:]:
            df.at[merged_indices[0], '일자'] = f"{df.at[merged_indices[0], '일자']}, {df.at[index_to_merge, '일자']}"
            df.at[merged_indices[0], '신청구분'] = f"{df.at[merged_indices[0], '신청구분']}, {df.at[index_to_merge, '신청구분']}"
            # Add the index of the row to be removed
            rows_to_remove.add(index_to_merge)

# Drop the rows from the DataFrame
df = df.drop(list(rows_to_remove)).reset_index(drop=True)

# Replace NaN values with a default value (e.g., 0) in the '일' column
df['일'] = df['일'].fillna(0)

# Convert the '일' column to integer data type
df['일'] = df['일'].astype(int)

# Update the '일' column by adding the length of the '신청구분' column
for index, row in df.iterrows():
    cleaned_신청구분 = row['신청구분'].replace(',', '').replace(' ', '')
    df.at[index, '일'] = len(cleaned_신청구분) + row['일']

column1 = '담당자성명'  # Replace with the first column you want to combine
column2 = '담당자연락처'  # Replace with the second column you want to combine
column3 = '담당자이메일'  # Replace with the second column you want to combine
combined_column_name = '담당자연락처1'  # Replace with the name you want for the combined column

insert_index = df.columns.get_loc(column2)

df[combined_column_name] = df[column1].astype(str) + '\n' + df[column2].astype(str) + '\n' + df[column3].astype(str)

# Delete the original columns
df.drop(columns=[column1, column2, column3], inplace=True)
df.insert(insert_index, combined_column_name, df.pop(combined_column_name))

# Save the modified DataFrame to a new Excel file
df.to_excel(output_file, index=False)
