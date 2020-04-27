import json
import gzip

with gzip.open('wiki_data/jawiki-country.json.gz') as f:
    for line in f:
        data = json.loads(line)
        if ('title', 'イギリス') in data.items():
            print(data)