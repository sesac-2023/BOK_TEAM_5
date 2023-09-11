from bs4 import BeautifulSoup
import requests
import time
import re
from requests import get
from urllib import request
from PyPDF2 import PdfReader
import os
import csv
from pykospacing import Spacing
import os.path
import shutil
from tika import parser
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

target_day = "2013-05-09"

url = f"https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate={target_day}&writeToDate={today}&x=0&y=0&page=1"
temp_url = "https://finance.naver.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
    'Referer': 'https://www.naver.com/'
    }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

last_page = soup.select_one('td.pgRR>a').attrs['href']
temp = "/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2013-05-09&writeToDate=2023-09-01&x=0&y=0&page="
pages = int(last_page.replace(temp,''))

for page in range(1,pages+1):
    page_url = f"https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate={target_day}&writeToDate={today}&x=0&y=0&page={page}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
        'Referer': 'https://www.naver.com/'
        }

    response = requests.get(page_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    stock_links = soup.select('table.type_1> tr')

    nomal_page = "https://finance.naver.com/research/"
    print(f"{page} 번 페이지 진행중입니다")
    for link in stock_links:
        taget = link.select("a")
        if taget == []:
            pass
        else:
            url_link = taget[0].attrs['href']
            crawling_link = nomal_page+url_link
            total_url = crawling_link

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 
                'Referer': 'https://www.naver.com/'
                }

            response = requests.get(total_url, headers=headers)
            print(total_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            maket = soup.select_one('p.source').text
            maket = maket.replace("\n",'')
            maket = maket.replace("\t",'')
            maket = maket.split("|")
            maket_name = maket[0]
            date = maket[1]

            stock_title = soup.select_one('th.view_sbj').text

            title = stock_title.replace("\n",'')
            title = title.replace("\t",'')
            title = title.split(maket_name)
            title = title[0]
            title = title.replace('  ','') #리서치 제목
            for idx in range(len(title)): #공백제거
                if title[idx] != ' ':
                    target_idx = idx
            title = title[:target_idx+1]
            new_title = ''
            for i in title:
                if i == "/":
                    new_title += "_"
                else:
                    new_title += i

            title = new_title
            print(f"리서치 제목 : {title}")
            info = soup.select_one("td.view_cnt").text
            info = info.replace('\n','')
            pdf = soup.select("a.con_link")[1].text
            if pdf == '':
                print("PDF 파일이 없습니다 이 경우엔 수집하지 않습니다")
                pass
            else:
                print("PDF 파일이 존재 합니다")
                info = info.split(pdf)
                info = info[0]
                pdf_link = soup.select_one("a.con_link").attrs['href'] #pdf 다운로드 링크
                pdf = soup.select("a.con_link")[1].text #pdf파일 이름
                if "/" in pdf:
                    pdf = pdf.replace('/','_')
                pdf_name = soup.select("a.con_link")[1].text[:-4]
                print(pdf)
                with open(pdf, "wb") as file:   # open in binary mode
                    response = get(pdf_link)               # get request
                    time.sleep(1)
                    file.write(response.content) 

                PDF_FILE_PATH = pdf

                # reader = PdfReader(PDF_FILE_PATH)
                # pages = reader.pages
                # text = ''
                # for page in pages:
                #     sub = page.extract_text()
                #     text += sub
                parsed = parser.from_file(PDF_FILE_PATH)
                text = parsed['content']
                if text is None:
                    print("pdf 파일을 읽을 수 없습니다")
                else:
                    str_text = text
                    new_str = re.sub("\n", "", str_text)
                    new_str = re.sub(" ", "", new_str)

                    spacing = Spacing()
                    kospacing_result = spacing(new_str) 

                    directory = f'./dataset/{date}'

                    if os.path.isdir(directory):
                        print(directory)
                        print("저장경로 있습니다")
                        time.sleep(1)
                    else:
                        print("저장경로가 없습니다")
                        current_path = os.getcwd()
                        os.mkdir(directory)
                        time.sleep(2)
                        if os.path.isdir(directory):
                            print("저장경로 생성하였습니다")
                        else:
                            print("저장경로 생성 실패하였습니다")
                    with open(f'{directory}/{title}_{maket_name}_{date}.text', 'w', encoding='utf-8') as f:
                        f.write('제목\n')
                        f.write(f'{title}\n')
                        f.write('\n')
                        f.write('요약\n')
                        f.write(f'{info}\n')
                        f.write('\n')
                        f.write('내용\n')
                        f.write(f'{kospacing_result}\n')
                    time.sleep(1)
                # 파일 삭제
                remove_file_path = PDF_FILE_PATH # 제거할 파일
                os.remove(remove_file_path)
