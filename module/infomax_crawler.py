import requests
from bs4 import BeautifulSoup
import os

# 크롤링할 페이지의 수를 추출
url = f"https://news.einfomax.co.kr/news/articleList.html?page=1&total=6417&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=2019-01-01&sc_edate=2019-12-31&sc_serial_number=&sc_word=%EA%B8%88%EB%A6%AC&box_idxno=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_user_name=&sc_order_by=E&view_type=sm"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://www.naver.com/'
    }
base = 'https://news.einfomax.co.kr'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
total = soup.select_one('#sections > section > header > h3 > small').text
total_num = ''
for i in total:
    if i.isdigit():
        total_num += i
total_num = int(total_num)
page_num_0 = total_num / 20
page_num_1 = total_num // 20
if page_num_0 != page_num_1:
    pages = page_num_1 + 1
else:
    pages = page_num_1
pages #1~페이지부터 pages 까지 크롤링
for page in range(1,pages+1):
    url = f"https://news.einfomax.co.kr/news/articleList.html?page={page}&total=6417&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=2019-01-01&sc_edate=2019-12-31&sc_serial_number=&sc_word=%EA%B8%88%EB%A6%AC&box_idxno=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_user_name=&sc_order_by=E&view_type=sm"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Referer': 'https://www.naver.com/'
        }
    base = 'https://news.einfomax.co.kr'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    li_tg = soup.select('ul.type2>li>h4.titles>a') #해당 페이지에 있는 뉴스기사 링크 리스트
    for i in li_tg:
        target = i.attrs['href']
        crawling_url = base + target
        response = requests.get(crawling_url, headers=headers)
        crawling_soup = BeautifulSoup(response.text, 'html.parser') # 해당 뉴스기사 링크의 html 정보 추출
        title = crawling_soup.select_one('h3.heading').text
        new_title = '' #타이틀 전처리 결과
        for i in title:
            if i == "/":
                new_title += "_"
            else:
                new_title += i
        date_li = crawling_soup.select('ul.infomation>li')[1].text
        date_li = date_li.split("입력")
        date = date_li[-1]
        date = date.replace('.','_')
        date = date.replace(':','_')
        
        date #날짜
        info = crawling_soup.select_one('#article-view-content-div').text
        info = info.replace('\n','')
        info = info.replace('\r','')
        info = info.replace('\t','')
        info #내용
        
        #파일 작성
        print(f'./news/2019{date}_연합인포맥스.text')
        with open(f'./news/2019/{date}_연합인포맥스.text', 'w', encoding='utf-8') as f:
            f.write('제목\n')
            f.write(f'{new_title}\n')
            f.write('\n')
            f.write('내용\n')
            f.write(f'{info}\n')