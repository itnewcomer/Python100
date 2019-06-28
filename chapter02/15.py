## 15. 末尾のN行を出力
## 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

# python 15.py hightemp.txt 3

print("15. 末尾のN行を出力")

import sys
# ファイルの読み込み
f = open(sys.argv[1], 'r').readlines()

# 末尾何行を出力するのかの引数格納
line_num = 0
line_num = int(sys.argv[2])

# 末尾N行出力
for line in (f[len(f) - line_num:len(f)]):
    print(line,end="")

# $ tail -n 3 hightemp.txt 
# 山梨県  大月    39.9    1990-07-19
# 山形県  鶴岡    39.9    1978-08-03
# 愛知県  名古屋  39.9    1942-08-02

# http://kesin.hatenablog.com/entry/2013/05/12/004541
# colors = ['red', 'green', 'blue', 'yellow']
# for i, color in enumerate(colors):
#     print i, '-->', color

