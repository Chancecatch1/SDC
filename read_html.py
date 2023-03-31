import pandas as pd
import os

# Define path to folder with HTML files
folder_path = "./Personal_Rent_files/"

# Get list of HTML files in the folder
html_files = [file for file in os.listdir(folder_path) if file.endswith(".html")]

# Create an empty list to store dataframes
dfs = []

# Define the list of specific cell values to use as column titles
column_titles = ["예술공간", "담당자연락처", "신청구분"]  # Replace with your specific cell values

# Loop through each HTML file and append the dataframe to the list
for file in html_files:
    html = pd.read_html(os.path.join(folder_path, file))
    df = html[0]  # assuming there is only one table in each HTML file

    # Find the row index containing the desired cell values
    title_row_index = None
    for index, row in df.iterrows():
        if set(column_titles).issubset(row.values):
            title_row_index = index
            break

    if title_row_index is not None:
        # Set the desired row as the column titles
        df.columns = df.iloc[title_row_index]

        # Drop the row with the titles to avoid duplication
        df = df.drop(title_row_index)

    dfs.append(df)

# Concatenate all the dataframes in the list into a single dataframe
df_combined = pd.concat(dfs)

# Write the combined dataframe to an Excel file
df_combined.to_excel("combined_html_read.xlsx", index=False)
