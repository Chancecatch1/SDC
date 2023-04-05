import os
import glob
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs


def process_html_files():
    file_path = './Personal_Rent_files/*.html'
    all_files = glob.glob(file_path)

    cols = ['단체명', '대표자성명', '단체(개인) 소개 및 주요경력', '사업내용(주제)', '사용인원',
            '사용자 명단','대관 특이사항 / 반입물', '예술공간', '담당자이메일', '담당자연락처','담당자성명',
            '사업자등록번호', '세부내용', '단체종류', '신청구분']  # Same columns as in the original code

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
            # Same content as in the original loop

    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df = combined_df.replace('\n', ' ', regex=True)
    combined_df = combined_df.replace('\r\n', ' ', regex=True)
    combined_df['신청구분'] = combined_df['신청구분'].str[46:]
    combined_df['예술공간'] = combined_df['예술공간'].str[82:]
    combined_df = combined_df[cols]
    # Same processing as in the original code

    combined_df.to_excel('updated_combined_rent_1.xlsx', index=False)


def modify_excel_file():
    file_path = 'updated_combined_rent_1.xlsx'

    df = pd.read_excel(file_path, engine='openpyxl')

    df.insert(3, '사업(성격)', np.nan)
    df.insert(9, '일자', np.nan)
    df.insert(10, '타임', np.nan)
    df.insert(11, '금액', np.nan)
    df.insert(12, 'x1', 'x')
    df.insert(13, '일', np.nan)
    df.insert(14, 'x2', 'x')
    df.insert(15, 'VAT', '10%')
    df.insert(16, "'=", "'=")
    df.insert(17, '합계', np.nan)
    df.insert(18, '총계(원)', np.nan)
    # Same insertions as in the original code

    df.to_excel(file_path, index=False)

def remove_unnecessary_spaces(text):
    if pd.isna(text):
        return text
    return ' '.join(text.split())

def set_amount(value):
    if value == '오전':
        return 15000
    else:
        return 20000

def split_and_save_dataframe():
    file_name = "updated_combined_rent_1.xlsx"
    df = pd.read_excel(file_name, engine="openpyxl")

    # Define the keyword and column to search
    keyword = "수시"
    column_name = "신청구분"

    # Same content as in the original split and save function
    
    df_split = df[column_name].str.split(keyword, expand=True)
    df_split = df_split.stack().reset_index(level=1, drop=True).to_frame(column_name)
    df = df.drop(column_name, axis=1)
    df = df.join(df_split).reset_index(drop=True)

    source_column = "신청구분"

    df["일자"] = df[source_column].str.slice(0, 50)
    df[source_column] = df[source_column].str.slice(50)

    df.to_excel(file_name, index=False, engine="openpyxl")

    df = pd.read_excel(file_name, engine="openpyxl")

    source_column_2 = "신청구분"

    df["타임"] = df[source_column_2].str.slice(0, 50)
    df["금액"] = df[source_column_2].str.slice(0, 50)
    df[source_column_2] = df[source_column_2].str.slice(50)

    # Apply remove_unnecessary_spaces to each column before saving
    for col in df.columns:
        df[col] = df[col].apply(remove_unnecessary_spaces)

    df = df.dropna(subset=['일자'])
    df = df[df['일자'].str.strip() != '']

    df['금액'] = df['금액'].apply(set_amount)
    df.to_excel(file_name, index=False, engine="openpyxl")

if __name__ == "__main__":
    process_html_files()
    modify_excel_file()
    split_and_save_dataframe()
