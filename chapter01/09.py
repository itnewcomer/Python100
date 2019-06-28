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