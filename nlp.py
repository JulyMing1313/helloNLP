# -*- encoding: utf-8 -*-

import os, os.path
from bosonnlp import BosonNLP
import requests
import json
import re
from bs4 import BeautifulSoup

# 情感分析
nlp = BosonNLP('uHKVapyC.24007.8mn_T4Zs1Tlm')

# 网易云音乐歌词id
id = 191232
url='http://music.163.com/api/song/lyric?' + 'id=' + str(id) + '&lv=1&kv=1&tv=-1'
lyric = requests.get(url)
json_obj = lyric.text
j = json.loads(json_obj)
lrc = j['lrc']['lyric']
pat = re.compile(r'\[.*\]')
lrc = re.sub(pat, "", lrc)
print(lrc)
lrc = lrc.strip()
lrc = lrc.split()
# 除去歌词开头的作者
lrc = lrc[6:len(lrc)]

def main():
        print('loading ...歌曲id:' + str(id))
        lrc1 = [line for line in lrc if line]
        print(lrc1[1])
        all_proba = nlp.sentiment(lrc1[1])
        text_with_proba = zip(lrc1, all_proba)
        sort_text = sorted(text_with_proba, key=lambda x : x[1][1], reverse=False)
        # output
        for text, sentiment in sort_text:
            print(sentiment, text)
        
if __name__ == '__main__':
    main()