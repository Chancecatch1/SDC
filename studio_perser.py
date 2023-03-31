import pandas as pd
import glob
import os
from bs4 import BeautifulSoup as bs

file_path = './Personal_Rent_files/*.html'
all_files = glob.glob(file_path)

cols = ['단체명', '대표자성명', '단체(개인) 소개 및 주요경력', '세부내용', '사업내용(주제)', '사용인원',
        '사용자 명단','대관 특이사항 / 반입물', '예술공간', '신청구분', '단체종류', '담당자이메일',
        '담당자연락처','사업자등록번호']

dfs = []

for file in all_files:
    with open(file, 'r', encoding='utf-8') as f:
        page = f.read()
        soup = bs(page, "html.parser")
        rows = soup.select('table.bluetop tr')
        data_dict = {}
        for row in rows:
            titles = row.find_all('th')
            values = row.find_all('td')
            for title, value in zip(titles, values):
                if title.text.strip() in cols:
                    data_dict[title.text.strip()] = value.text.strip()
        dfs.append(pd.DataFrame([data_dict]))

combined_df = pd.concat(dfs, ignore_index=True)
combined_df = combined_df.replace('\n', ' ', regex=True)
combined_df = combined_df.replace('\r\n', ' ', regex=True)
combined_df['신청구분'] = combined_df['신청구분'].str[46:]
combined_df['예술공간'] = combined_df['예술공간'].str[82:]
combined_df = combined_df[cols]

def remove_unnecessary_spaces(text):
    if pd.isna(text):
        return text
    return ' '.join(text.split())

for col in combined_df.columns:
    combined_df[col] = combined_df[col].apply(remove_unnecessary_spaces)

combined_df.to_excel('updated_combined_rent_1.xlsx', index=False)