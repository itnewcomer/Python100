## 16. ファイルをN分割する
## 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys

print("16. ファイルをN分割する")

import sys
# ファイルの読み込み
f = open(sys.argv[1], 'r').readlines()
#　ファイルの行数の確認
text_linesize = len(f)

# 何行ずつに区切るのか引数の格納
line_num = 0
line_num = int(sys.argv[2])
file_num = 1
# 末尾N行出力
for i in range(0,len(f),line_num):
    file_name = 'chap_2_16_python_'+str(file_num)
    fnew = open (file_name, 'w')
    for x in f[i:i+line_num]:
        fnew.write(str(x))
    fnew.close()
    file_num += 1

## $ split -l 7 hightemp.txt chap_2_16_linux_
## $ ls -l chap_2_16_linux_a*
## -rw-r--r--  1 itnewcomer  staff  244  6 27 23:20 chap_2_16_linux_aa
## -rw-r--r--  1 itnewcomer  staff  237  6 27 23:20 chap_2_16_linux_ab
## -rw-r--r--  1 itnewcomer  staff  230  6 27 23:20 chap_2_16_linux_ac
## -rw-r--r--  1 itnewcomer  staff  102  6 27 23:20 chap_2_16_linux_ad

## $ cat chap_2_16_linux_aa 
## 高知県  江川崎  41      2013-08-12
## 埼玉県  熊谷    40.9    2007-08-16
## 岐阜県  多治見  40.9    2007-08-16
## 山形県  山形    40.8    1933-07-25
## 山梨県  甲府    40.7    2013-08-10
## 和歌山県        かつらぎ        40.6    1994-08-08
## 静岡県  天竜    40.6    1994-08-04

## $ cat chap_2_16_linux_ad
## 山梨県  大月    39.9    1990-07-19
## 山形県  鶴岡    39.9    1978-08-03
## 愛知県  名古屋  39.9    1942-08-02