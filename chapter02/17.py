## 17. １列目の文字列の異なり
## 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# python 17.py hightemp.txt

import sys

print("17. １列目の文字列の異なり")

# ファイルの読み込み
f = open(sys.argv[1], 'r').readlines()

# リストの初期化
word_list = list()

# 1列目のみをリスト化
for line in f:
    word_list.append(line.split()[0])

# 集合にする
word_list = set(word_list)

# 表示
print(word_list)

# $ cut -f 1 -d "$(printf "\t")" hightemp.txt | sort |uniq 
# 千葉県
# 埼玉県
# 大阪府
# 山形県
# 山梨県
# 岐阜県
# 愛媛県
# 愛知県
# 群馬県
# 静岡県
# 高知県
# 和歌山県