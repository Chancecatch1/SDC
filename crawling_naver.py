# import requests 
# from bs4 import BeautifulSoup 

# url = "https://www.snugarchive.com" 
# res = requests.get(url) 
# res.raise_for_status() # 정상 200
# soup = BeautifulSoup(res.text, "lxml")

# # print(type(soup)) # BeautifulSoup 객체의 자료형 출력
# # print(soup.head) # HTML 문서의 'head' 태그에 해당하는 내용 출력
# # print(soup.body)  # HTML 문서의 'body' 태그에 해당하는 내용 출력
# # print(soup.title) # HTML 문서의 'title' 태그 내용 출력
# # print(soup.title.name) # HTML 문서의 'title' 태그명 출력 
# # print(soup.title.string) # HTML 문서의 'title' 태그를 제외하고 태그 안에 표시되는 텍스트만 출력

import csv
import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=228"

# 엑셀 파일로 저장하기
filename = "언론사별 많이 본 뉴스.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["순위", "뉴스 제목"]
writer.writerow(columns_name)

# 웹 서버에 요청하기
headers = {"User-Agent": "[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36]"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# soup 객체 만들기
soup = BeautifulSoup(res.text, "lxml")
# news_box = soup.find("ol", attrs={"class": "rankingnews_list"}) # '언론사별 많이 보는 뉴스' 영역으로 범위 제한
# News = news_box.find_all("a", attrs={"class": "list_title nclicks('RBP.rnknws')"}) # 위 영역에서 'a'태그 모두 찾아 변수 News에 할당

news_box = soup.find("ul", attrs={"class": "section_list_ranking_press _rankingList"})
if news_box is not None:
    News = news_box.find_all("a", attrs={"class": "list_tit nclicks('rig.renws2')"})
else:
    print("Could not find news_box on the page.")


i = 1

# 반복문으로 제목 가져오기(터미널 창 출력 및 엑셀 저장)
for news in News:
    title = news.text.strip()
    print(f"{str(i)}위: {title}")
    data = [str(i), title]
    writer.writerow(data)
    i += 1

f.close()