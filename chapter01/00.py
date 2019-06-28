## 00. 文字列の逆順
## 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

print('00. 文字列の逆順')

a = 'stressed'
for i in range(len(a)):
    print(a[len(a)-i-1], end="")
print()

## 後日追記(こんな簡単な方法あるやんけ!!)

print(a[::-1]) ## -1で逆順