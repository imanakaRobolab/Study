# 2022_05_03の目標

- Pythonを用いた正規表現の学習
  - 簡単な内容で数値の10桁の判別を行う。
  - またアルファベット10文字の判別を行う。
  - 最後に「●●●-●●●-●●●●」といった電話番号の判別を行う

- 文章を単語区切りでリストに格納するような処理を作成する。
- reのmatchとsplitとfindallを用いたプログラムを作成する。
  - matchに関しては、startメソッドとendメソッドを使用すること

## 正規表現簡単表

最低限正規表現を使用する時に覚えておかないといけないももの

- 正規表現の特殊な文字を表す記号
正規表現の文字 | 意味
------- | -------
\s | 空白
\S | 空白以外
\b | 単語の先頭の空白
\B | 単語の先頭の空白以外の文字列
\w | [a-z,0-9,A-Z]のAsciiコードの文字（_を含む）
\W | [a-z,0-9,A-Z]以外の文字列
\d | 数字（0-9）
\D | 数字以外

- 複数回などの意味を持つ文字

特殊なもの | 意味
------- | -------
? | 空白
\* | 空白以外
+ | 単語の先頭の空白
. | 単語の先頭の空白以外の文字列

## 正規表現の例

```python
# --*--coding:utf-8--*--
import re

str1 = '01234'
# 4文字の数字の連続を含むか判断している
m = re.match(pattern='\d{4}',string = str1)
if bool(m):
    print('4桁の数字を含まない')
else:
    print('4桁の数字を含む')

# 名前のカンマと空白で区切ってリストに格納している
str2 = '安藤, 田中, 佐藤, 吉田'
list1 = re.split(',\s',str2)
print(list1)

# 数字の並びを抽出
str3 = '012-888-919'
list3 = re.findall(pattern='\d+',string=str3)
print(list3)

# ()とsplitを用いた処理
str4 = '123a567b789'
list4 = re.split(pattern='[a-z,A-Z]', string=str4)
print(list4)
list5 = re.split(pattern='([a-z,A-Z])', string=str4)
print(list5)
```