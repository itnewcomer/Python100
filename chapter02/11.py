## 11. タブをスペースに置換
## タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

#  python 11.py hightemp.txt 

import sys

print("11. タブをスペースに置換")

fp = open(sys.argv[1], 'r')
for line in fp.readlines():
    print(line.expandtabs(1) ,end = '')
fp.close()

# https://rcmdnk.com/blog/2016/09/13/computer-gnu-bsd-linux-mac/

# sed
# sed "s/$(printf "\t")/ /g" hightemp.txt 

# tr
# cat hightemp.txt | tr '$(printf "\t")' ' '

# expand
# expand -t 1 hightemp.txt