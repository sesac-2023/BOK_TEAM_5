from bs4 import BeautifulSoup as bs 
from pykospacing import Spacing
from datetime import datetime
from tika import  parser
import requests
import time
import os
import re

def MPB_crawling(start_date, end_date):

    page = 1
    
    st_date = datetime.strptime(start_date,'%Y-%m-%d')
    en_date = datetime.strptime(end_date,'%Y-%m-%d')

    while page:
        url = f"https://www.bok.or.kr/portal/bbs/B0000245/list.do?menuNo=200761&pageIndex={page}"
        response = requests.get(url)
        soup = bs(response.text, 'html5lib')

        sel = 'div.bdLine.type2 ul li div span a span span'

        target_str = soup.select(sel)

        num = 0

        for target in target_str:
            
            d = target.text.split('(', 2)[2].split(')')[0]
            target_date = d.replace('.', '-')

            if target_date[-1] == '-':
                target_date = target_date[:-1]
            else:
                pass

            tar_date = datetime.strptime(target_date,'%Y-%m-%d')
            
            if st_date <= tar_date <= en_date:
                
                sel = "#content > div.bdLine.type2 > ul > li > div > span > a"
                title = soup.select(sel)[num]

                num += 1

                
                sub_url = "https://www.bok.or.kr/" + title['href'][1:]
                response = requests.get(sub_url)
                sp = bs(response.text, 'html5lib')


                sel_1 = "#board > div > dl > dd > div > ul > li:nth-child(2) > a:nth-child(1)"
                sel_2 = "#board > div > dl > dd > div > ul > li:nth-child(1) > a:nth-child(1)"

                sel_1_file = sp.select_one(sel_1)
                file_name = sel_1_file.text.strip()[-3:]  

                if file_name == "pdf":
                    
                    file_url = "https://www.bok.or.kr" + sel_1_file['href']
                    response = requests.get(file_url)

                    with open("../MPB_dataset/{}.pdf".format(title.text.strip()), "wb") as f:  # 파일경로 수정
                        f.write(response.content)

                else:
                    sel_2_file = sp.select_one(sel_2)
                    file_url = "https://www.bok.or.kr" + sel_2_file['href']
                    
                    response = requests.get(file_url)

                    with open("../MPB_dataset/{}.pdf".format(title.text.strip()), "wb") as f:  # 파일경로 수정
                        f.write(response.content)
                        
                time.sleep(1)

                pdf_title = title.text.strip() 
            
                target = '../MPB_dataset/' + pdf_title + ".pdf"  # 파일경로 수정

                parsed = parser.from_file(target)

                str_target = parsed['content']
                
                new_str = re.sub("\n", "", str_target)
                str_ = re.sub(" ", "", new_str)

                spacing = Spacing()
                kospacing_result = spacing(str_)

                target_x = "위원 토의 내용"
                for idx in range(len(kospacing_result)-len(target_x)):
                    target_word = kospacing_result[idx:idx+len(target_x)]
                    if target_word == target_x:
                        idx_x = idx+len(target_x)
                        break        

                text = kospacing_result[idx_x:]

                target_y = "심의 결과"
                for idx in range(len(text)-len(target_y)):
                    target_word = text[idx:idx+len(target_y)]
                    if target_word == target_y:
                        idx_y = idx
                        break

                context = text[:idx_y]
                    
                MPB_date = str(tar_date)[:10]

                print(MPB_date)

                with open(f'../MPB_dataset/{MPB_date}.txt', 'w', encoding='utf-8') as f:  # 파일경로 수정
                    f.write(context[:-4])
                
                time.sleep(1)

                os.remove(target)    


        print(page) # 페이지 출력
        page += 1

        if (st_date > tar_date) or (en_date < tar_date):

            break
        