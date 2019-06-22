## hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
## 以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
## さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

## 10. 行数のカウント
## 行数をカウントせよ．確認にはwcコマンドを用いよ．

print("10. 行数のカウント")
import sys

fp = open(sys.argv[1], 'r')
i = 0
for line in fp.readlines():
	i += 1
fp.close()
print(i)

## 確認(Linuxコマンド)
## $ wc -l hightemp.txt 
##   24 hightemp.txt

## 11. タブをスペースに置換
## タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

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

## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
## 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

print("12. 1列目をcol1.txtに，2列目をcol2.txtに保存")

fp = open(sys.argv[1], 'r')
fnew1 = open ('col1.txt', 'w')
fnew2 = open ('col2.txt', 'w')
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

## 13. col1.txtとcol2.txtをマージ
## 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
## 確認にはpasteコマンドを用いよ．

print("13. col1.txtとcol2.txtをマージ")

#f2 = open ('col2.txt', 'w')
with open('col1.txt') as f1:
    s1=f1.read()
with open('col2.txt') as f2:
    s2=f2.read()

s1 = s1.split("\n")
s2 = s2.split("\n")
i = 0
merge_file = open ('merge_file.txt', 'w')
for i in range(len(s1)-1):
    if i < len(s1)-2:
        merge_file.write(s1[i] + "\t" + s2[i] + "\n")
    else:
        merge_file.write(s1[i] + "\t" + s2[i])
merge_file.close()

# paste -d "$(printf "\t")" col1.txt col2.txt 