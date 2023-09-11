import os 
import re
from ekonlpy import Mecab 
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np

def word_clous(path):
    file_list = os.listdir(path)  # 경로

    pos = []


    for file_name in file_list:

        with open(path + file_name, 'r', encoding='utf-8') as f:  # 경로
            content = f.read()
            
            regex = re.compile('[^ㄱ-ㅣ가-힣+]')

            result = regex.sub('', content)

            mecab = Mecab()
            pos_tag = mecab.pos(result)
            
            for p in pos_tag:
                
                if (p[1] == "NNG" or p[1] == "VA" or p[1] == "VAX" or p[1] == "MAG" or p[1] == "VV"):
                    pos.append(p[0])

    c = Counter(pos)

    wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, 
                max_font_size=250, background_color="white")
    gen = wc.generate_from_frequencies(c)
    plt.axis("off")

    plt.imshow(gen)