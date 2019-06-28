## 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
## 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

# python 19.py hightemp.txt 

import collections
import sys

print("19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる")

# ファイルの読み込み
f = open(sys.argv[1], 'r').readlines()

# リストの初期化
word_list = list()

# 1列目のみをリスト化
for line in f:
    word_list.append(line.split()[0])

# Python標準ライブラリcollectionsにCounterクラスを利用
c = collections.Counter(word_list)
print(c)

# Counter({'埼玉県': 3, '山形県': 3, '山梨県': 3, '群馬県': 3, '岐阜県': 2, '静岡県': 2, '愛知県': 2, '千葉県': 2, '高知県': 1, '和歌山県': 1, '愛媛県': 1, '大阪府': 1})


# $ cut -f 1 -d "$(printf "\t")" hightemp.txt | sort |uniq -c |sort -nr
#   3 群馬県
#   3 山梨県
#   3 山形県
#   3 埼玉県
#   2 静岡県
#   2 愛知県
#   2 岐阜県
#   2 千葉県
#   1 和歌山県
#   1 高知県
#   1 愛媛県
#   1 大阪府