import json
import gzip
import os

path = os.getcwd()
#path = path + '\\Python100\\chapter03'
os.chdir(path)
with gzip.open('wiki_data/jawiki-country.json.gz') as f:
    for line in f:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            print(json_dict)