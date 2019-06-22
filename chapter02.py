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

# cut -f 1 -d "$(printf "\t")" hightemp.txt > col1_linux.txt 
# cut -f 2 -d "$(printf "\t")" hightemp.txt > col2_linux.txt 
# diff col1.txt col1_linux.txt 
# diff col2.txt col2_linux.txt 


## 13. col1.txtとcol2.txtをマージ
## 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

## 14. 先頭からN行を出力
## 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

## 15. 末尾のN行を出力
## 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

## 16. ファイルをN分割する
## 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

## 17. １列目の文字列の異なり
## 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

## 18. 各行を3コラム目の数値の降順にソート
## 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

## 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
## 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．