## 21. カテゴリ名を含む行を抽出Permalink
## 記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import gzip
import os
import re

path = os.getcwd()
#path = path + '\\Python100\\chapter03'
os.chdir(path)
with gzip.open('wiki_data/jawiki-country.json.gz') as f:
    for line in f:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            ## [[Category:
            for line_text in json_dict['text'].split():
#                print(line_text)
                if(re.match(r'\[\[Category\:',line_text)):
                        print(line_text)

