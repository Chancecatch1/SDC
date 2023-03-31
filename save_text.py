from bs4 import BeautifulSoup
import pandas as pd
import glob

# Create an empty DataFrame to store the data
data = pd.DataFrame(columns=["담당자성명"])

# Loop over each HTML file in the specified directory
for file_path in glob.glob('./Personal_Rent_files/*.html'):

    # Open the HTML file and create a Beautiful Soup object
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the table element in the HTML and extract its contents
    table = soup.find('tr')
    for row in table.find_all('th'):
        if row.th and "단체명" in row.th.text:
            data.loc[row.td.text.strip(), "단체명"] = row.find_all('td')[1].text.strip()

# Write the data to a new Excel file
data.to_excel('data_studio_rent.xlsx')