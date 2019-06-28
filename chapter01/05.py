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