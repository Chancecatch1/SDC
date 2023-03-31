import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('cocatenated_dance_studio.xlsx')
df.to_csv('cocatenated_dance_studio.csv', index=False)

df_csv = pd.read_csv('cocatenated_dance_studio.csv')
# print(df_csv.head())
df.info()
print(df.columns)
print(df['대관명'])

value_counts = df['대관명'].value_counts(dropna=False)
percentages = value_counts / len(df) * 100

percentages.plot(kind='bar')
plt.title('Percentage of Studio')
plt.xlabel('Value')
plt.ylabel('Percentage')
plt.show()