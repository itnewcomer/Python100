## 00. 文字列の逆順
## 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

print('00. 文字列の逆順')

a = 'stressed'
for i in range(len(a)):
    print(a[len(a)-i-1], end="")
print()

## 後日追記(こんな簡単な方法あるやんけ!!)

print(a[::-1]) ## -1で逆順

## 01. 「パタトクカシーー」
## 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

print('01. 「パタトクカシーー」')
a = 'パタトクカシーー'
i = 0
for i in range(0,8,2): #1以上8未満の数字の中で2ずつ増える
    print(a[i], end ="")
print()

## 後日追記(一行でかけるやんけ！！)

print(a[0:8:2]) 

## 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
## 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

print('02. 「パトカー」＋「タクシー」＝「パタトクカシーー」')
a = 'パトカー'
b = 'タクシー'

for i in range(len(a)):
    print(a[i] + b[i], end="")
print()

## 03. 円周率
## "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

print('03. 円周率')
a = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
mylist = list()
for i in a.split(" "):
    mylist.append(len(i.strip('.,')))
print(mylist) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


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

## 05. n-gram
## 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

print('05. n-gram')

def n_gram(sentence,n,CorW):
    if CorW == 'W':
        sentence = sentence.split(' ')
    elif CorW == 'C':
        sentence = sentence
    else:
        print('n_gram(sentence,n,CorW)')
        print('CorW:Plsease Write C (Character) or W (Word)')
    x_list = list()
    for i in range(len(sentence)-n+1):
        x_list.append(sentence[i:i+n])
    return(x_list)

a = 'I am an NLPer'

print(n_gram(a,2,'C'))
#['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
print(n_gram(a,2,'W'))
#[['I', 'am'], ['am', 'an'], ['an', 'NLPer']]

## 06. 集合
## "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
## さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(sentence,n,CorW):
    if CorW == 'W':
        sentence = sentence.split(' ')
    elif CorW == 'C':
        sentence = sentence
    else:
        print('n_gram(sentence,n,CorW)')
        print('CorW:Plsease Write C (Character) or W (Word)')
    x_list = list()
    for i in range(len(sentence)-n+1):
        x_list.append(sentence[i:i+n])
    return(x_list)

a = 'paraparaparadise'
b = 'paragraph'

#リストからsetオブジェクトにして集合関数を使う
X = set(n_gram(a,2,'C'))
Y = set(n_gram(b,2,'C'))

print('和集合')
print(X | Y)
# {'pa', 'ag', 'ar', 'di', 'se', 'ad', 'ph', 'ra', 'ap', 'gr', 'is'}
print('積集合')
print(X & Y)
# {'pa', 'ar', 'ap', 'ra'}
print('差集合')
print(X - Y)
# {'is', 'ad', 'se', 'di'}
se = {'se'}
print(se <= X)
print(se <= Y)

## 07. テンプレートによる文生成
## 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
# https://www.kichie.club/entry/python-typeerror-strobject/

x = 2
y = '気温'
z = 22.4

def template(x,y,z):
    print(str(x) + '時の' + str(y) + 'は' + str(z))

template(x,y,z)

## 08. 暗号文
## 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

## 英小文字ならば(219 - 文字コード)の文字に置換
## その他の文字はそのまま出力
## この関数を用い，英語のメッセージを暗号化・復号化せよ．

print('08. 暗号文')

def cipher(x):
    ciphersentence = ''
    for i in x:
        if i.islower() == True:
            ciphersentence += chr(219 - ord(i))
        else:
            ciphersentence += i
    return(ciphersentence)

print(cipher('Test aNd test'))

## 09. Typoglycemia
## スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．
## 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

print('09. Typoglycemia')

import random

def Typoglycemia(sentence):
    mylist = sentence.split(' ')
    new_list = list()
    for i in mylist:
        if len(i) <= 4:
            new_list.append(i)
        else:
            temp = i[1:len(x)-1]
            temp = ''.join(random.sample(temp, len(temp)))
            new_list.append(i[0] + temp + i[len(i)-1])
    return ' '.join(map(str, new_list))

x = r"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(x))