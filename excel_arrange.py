import pandas as pd
import numpy as np

# Replace 'file.xlsx' with the path to your Excel file
file_path = 'updated_combined_rent_1.xlsx'

# Read the Excel file
df = pd.read_excel(file_path, engine='openpyxl')

df.insert(3, '사업(성격)', np.nan)
df.insert(12, '타임', np.nan)
df.insert(13, '금액', np.nan)
df.insert(14, 'x1', 'x')
df.insert(15, '일', np.nan)
df.insert(16, 'x2', 'x')
df.insert(17, 'VAT', 'vat')
df.insert(18, "'=", "'=")
df.insert(19, '합계', np.nan)
df.insert(20, '총계(원)', np.nan)

df.to_excel(file_path, index=False)