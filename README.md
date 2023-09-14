# 텍스트 마이닝을 활용한 금융통화위원회 의사록 분석

## 📢 프로젝트 개요
 Deciphering Monetary Policy Board Minutes with
Text Mining: The Case of South Korea 논문 구현 프로젝트로 뉴스기사, 채권분석리포트를 크롤링해 텍스트 데이터를 얻고 데이터를 자연어 처리, 토픽 모델링 과정을 거쳐 감정 분석을 진행합니다. 이를 통해 머신 러닝 모델에 학습시켜 다음 금리의 방향성을 예측합니다.

<img src="https://github.com/sesac-2023/BOK_TEAM_5/assets/138412359/1712fcd3-7b2a-4447-ae08-d521b7a2b4b2" width="800" height="300"/>
<img src="https://github.com/sesac-2023/BOK_TEAM_5/assets/138412359/3b761292-73e5-492e-8d58-b95f506bc56f" width="800" height="300"/>

## 🗓️ 프로젝트 기간 
2023년 08월 30일(수) ~ 2023년 09월 08일(금)

## 📝 프로젝트 진행 과정

<img src="https://github.com/sesac-finance/NEWS_TEAM_3/assets/138412359/a40eda8a-db82-4953-8f0d-4ab7f60a46c9" width="800" height="300"/>


## module 설명
- BOK_Naive Bayes Classifier.ipynb : NBC 모델을 이용하여 감정분석하는 모듈
- BOK_ngram2vec.ipynb : Ngram2vec 모델을 이용하여 감정분석하는 모듈
- MPB_crawling.py : 금융통화위원회 의사록을 크롤링하는 모듈
- call_rate_crawler.py : 콜금리 월단위로 크롤링하는 모듈
- crawl_edaily.py : 이데일리에서 '금리'로 검색했을 때, 나오는 뉴스 크롤링하는 모듈
- infomax_crawler.py : 연합인포맥스에서 '금리'로 검색했을 때, 나오는 뉴스 크롤링하는 모듈
- naver_stock.py : 네이버 채권분석 리포트 크롤링하는 모듈
- word_cloud.py : 워드 클라우드로 시각화하는 모듈



## <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> 팀주소
- https://www.notion.so/b8a76cca45c847e3a0e80acc198e2c83


## 🤼‍♂️ 팀명 : BOK_TEAM_5
- 김세영 : ssss6820@naver.com
- 정준화 : behappy_jh@naver.com
- 이성현 : lsh3215013@naver.com
- 박상민 : psm6320@naver.com


## 참고자료
- 논문 : Ngram2vec: Learning Improved Word Representations from Ngram Co-occurrence Statistics
- 금융통화위원회 의사록 : https://www.bok.or.kr/portal/bbs/B0000245/list.do?menuNo=200761
- 채권분석 리포트 : https://finance.naver.com/research/debenture_list.naver
- 뉴스기사('금리'로 검색)
    - 이데일리 : https://www.edaily.co.kr/
    - 인포맥스 : https://news.einfomax.co.kr/
- 콜 금리(대한상공회의소) : https://www.korcham.net/nCham/Service/EconBrief/appl/ProspectBoardList.asp

## 🛠️ Stacks

- **Environment**
    - <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"/>
    - <img src="https://img.shields.io/badge/google drive-4285F4?style=for-the-badge&logo=google drive&logoColor=white">
    - <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&loge=Jupyter&logoColor=white">
    - <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">
    - <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"/>
    - <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
    
   

- **Development**
    - <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
    - <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>
    - <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
    