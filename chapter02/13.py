## 13. col1.txtとcol2.txtをマージ
## 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
## 確認にはpasteコマンドを用いよ．

# python 13.py

print("13. col1.txtとcol2.txtをマージ")

#f2 = open ('col2.txt', 'w')
with open('output/col1.txt') as f1:
    s1=f1.read()
with open('output/col2.txt') as f2:
    s2=f2.read()

s1 = s1.split("\n")
s2 = s2.split("\n")
i = 0
merge_file = open ('output/merge_file.txt', 'w')
for i in range(len(s1)-1):
    if i < len(s1)-2:
        merge_file.write(s1[i] + "\t" + s2[i] + "\n")
    else:
        merge_file.write(s1[i] + "\t" + s2[i])
merge_file.close()

# paste -d "$(printf "\t")" col1.txt col2.txt