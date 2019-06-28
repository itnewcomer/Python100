## 14. 先頭からN行を出力
## 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

# python 14.py hightemp.txt 3

print("14. 先頭からN行を出力")

import sys
line_num = 0
line_num = int(sys.argv[2])
i = 0
fp = open(sys.argv[1], 'r')
for line in fp.readlines():
    if i < line_num:
        print(line,end="")
        i += 1
    else:
        break

# head -n 3 hightemp.txt