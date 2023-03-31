import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.sfac.or.kr/boffice/sy/coronation/RequestReg.do"

# 엑셀 파일로 저장하기
filename = "cms_studio.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["연번", "단체명"]
writer.writerow(columns_name)

# 웹 서버에 요청하기
headers = {"User-Agent": "[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36]"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text, "lxml")
contents_box = []

contents_box = soup.find("table", attrs={"class": "write"})
if contents_box is not None:
    contents_box.extend(contents_box.find_all("input", attrs={"class": "w90"}))
else:
    print("Could not find it on the page.")

i = 1

# 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
for contents in contents_box:
    value = contents.get("value") 
    print(f"{str(i)}위: {value}")
    data = [str(i), value]
    writer.writerow(data)
    i += 1

f.close()