## 04. 元素記号
## "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

print('04. 元素記号')

a = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
mylist = list()
mydict = {}

# 単語を空白で分割し、カンマやコロンを削除
for i in a.split(" "):
    mylist.append(i.strip('.,'))

# 先頭1文字のリストを作る
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19] # コピペでHPのリストを貼り付ける
num_list = list(map(lambda x: x - 1, num_list)) # lambda関数で全部1引いたリストを作る

for i in range(len(mylist)):
    str_list = mylist[i]
    if i in num_list: # num_list番目の単語は先頭1文字
        atom = str_list[0]
    else: # それ以外は2文字
        atom = str_list[0:2]
    mydict[i+1] = atom
print(mydict) #{1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}