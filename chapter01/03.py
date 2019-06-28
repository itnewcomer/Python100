## 03. 円周率
## "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

print('03. 円周率')
a = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
mylist = list()
for i in a.split(" "):
    mylist.append(len(i.strip('.,')))
print(mylist) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]