## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
## 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

# python 12.py hightemp.txt

import sys

print("12. 1列目をcol1.txtに，2列目をcol2.txtに保存")

fp = open(sys.argv[1], 'r')
fnew1 = open ('output/col1.txt', 'w')
fnew2 = open ('output/col2.txt', 'w')
for line in fp.readlines():
    my_list = list()
    my_list = line.split()
    fnew1.write(my_list[0]+'\n')
    fnew2.write(my_list[1]+'\n')
fp.close()
fnew1.close()
fnew2.close()

# cut -f 1 -d "$(printf "\t")" hightemp.txt > col1_linux.txt 
# cut -f 2 -d "$(printf "\t")" hightemp.txt > col2_linux.txt 
# diff col1.txt col1_linux.txt 
# diff col2.txt col2_linux.txt 