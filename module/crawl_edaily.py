import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


# 제목, 본문 담을 리스트
contents = []
date_list = []

def crawl_edaily(start, end, endpage):

    edaily_url = f'https://www.edaily.co.kr/search/news/?source=total&keyword=%ea%b8%88%eb%a6%ac&include=&exclude=&jname=&start={start}&end={end}&sort=latest&date=pick&exact=false&page='
    # 시작 페이지 설정
    page_number = 1

    while True:
        # 현재 페이지 URL 생성
        current_url = edaily_url + str(page_number)
        
        # 페이지 요청
        response = requests.get(current_url, headers=headers)
        soup = bs(response.text, 'html.parser')

        news_ls = soup.select('.newsbox_texts')

        # 뉴스기사 제목, 내용 크롤링
        for content in news_ls:
            contents.append(content.text.strip())

        # 기사 날짜 크롤링
        for i in soup.select('.author_category'):
            date_list.append(i.text.split()[0])

        if page_number == endpage:
            break
        page_number += 1
