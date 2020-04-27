# 23. セクション構造Permalink
# 記事中に含まれるセクション名とそのレベル
# （例えば”== セクション名 ==”なら1）を表示せよ．

## 21. カテゴリ名を含む行を抽出Permalink
## 記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import gzip
import os
import re

def SpecialCharacterRemoval(words):
    return words.replace('=','').replace(' ','')


path = os.getcwd()
#path = path + '\\Python100\\chapter03'
os.chdir(path)
with gzip.open('wiki_data/jawiki-country.json.gz') as f:
    for line in f:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            # ==文化== 1
            # ===食文化=== 2
            for line_text in json_dict['text'].split('\n'):
#                print(line_text)
                if(re.match(r'\=+',line_text)):
                        print(str((line_text.count('=')-2)/2) + ' : ' + SpecialCharacterRemoval(line_text))
                        
