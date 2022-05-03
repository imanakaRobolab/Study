# --*--encoding: utf-8 --*--

from doctest import REPORT_UDIFF
import re


# 10桁の文字を含む場合返却する
def intCheck(input):
    s = re.match(pattern='\d{10}', string=input)
    return s

# アルファベット10文字を含むかどうかを確認している


def strCheck(input):
    s = re.match(pattern='[a-z,A-Z]{10}', string=input)
    return s


def telephoneNumberCheck(input):
    s = re.match(pattern='\d{3}-\d{3}-\d{4}', string=input)
    return s


def main():
    digit10 = '0123456789'
    str10 = 'abcdefghij'
    telephone_code = '012-123-3456'

    print('処理を開始する')
    if strCheck(str10) and len(str10) == 10:
        print('10桁の数字です')
    else:
        print('10桁の数字ではありません')

    if telephoneNumberCheck(telephone_code):
        print('これは電話番号です')
    else:
        print('これは電話番号ではない')
    str1 = 'abcdeefg'
    list1 = re.findall(pattern='\d{3}', string=digit10)
    print(list1)
    print('処理を終了します')


if __name__ == '__main__':
    main()
