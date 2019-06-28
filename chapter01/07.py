## 07. テンプレートによる文生成
## 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
# https://www.kichie.club/entry/python-typeerror-strobject/

x = 2
y = '気温'
z = 22.4

def template(x,y,z):
    print(str(x) + '時の' + str(y) + 'は' + str(z))

template(x,y,z)