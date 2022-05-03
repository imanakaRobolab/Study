# --*--coding:utf-8--*--
import re

str1 = '01234'
# 4文字の数字の連続を含むか判断している
m = re.match(pattern='\d{4}', string=str1)
if bool(m):
    print('4桁の数字を含まない')
else:
    print('4桁の数字を含む')

# 名前のカンマと空白で区切ってリストに格納している
str2 = '安藤, 田中, 佐藤, 吉田'
list1 = re.split(',\s', str2)
print(list1)

# 数字の並びを抽出
str3 = '012-888-919'
list3 = re.findall(pattern='\d+', string=str3)
print(list3)

# ()とsplitを用いた処理
str4 = '123a567b789'
list4 = re.split(pattern='[a-z,A-Z]', string=str4)
print(list4)
list5 = re.split(pattern='([a-z,A-Z])', string=str4)
print(list5)
