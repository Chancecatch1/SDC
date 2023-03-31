import pandas as pd

file1 = pd.read_excel("C:/Users/User/Desktop/Test/black.xlsx", engine='openpyxl')
file2 = pd.read_excel("C:/Users/User/Desktop/Test/white.xlsx", engine='openpyxl')
file3 = pd.read_excel("C:/Users/User/Desktop/Test/11111.xlsx", engine='openpyxl')
file4 = pd.read_excel("C:/Users/User/Desktop/Test/22222.xlsx", engine='openpyxl')
file5 = pd.read_excel("C:/Users/User/Desktop/Test/33333.xlsx", engine='openpyxl')

concatenated = pd.concat([file1, file2, file3, file4, file5], axis=0)

concatenated.to_excel("cocatenated_dance_studio.xlsx", index=False)