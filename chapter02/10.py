## hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
## 以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
## さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

## 10. 行数のカウント
## 行数をカウントせよ．確認にはwcコマンドを用いよ．

## python 10.py hightemp.txt 

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