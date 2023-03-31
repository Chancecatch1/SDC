import pandas as pd

# Set the path and filename of the Excel file
excel_file = '대관신청회원_임예지_20230308.xls'

# Read the Excel file
df = pd.read_excel(excel_file)

# Set the path and filename of the CSV file
csv_file = 'example.csv'

# Write the DataFrame to a CSV file
df.to_csv(csv_file, index=False, encoding='utf-8-sig')