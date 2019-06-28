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