# --*--encoding:utf-8--*--
import re
from traceback import print_tb
import requests
import urllib3


def main():
    url = 'https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%BC%E3%83%99%E3%83%AB%E8%B3%9E'
    r = requests.get(url)
    # print(repr(r.text))
    counter((r.text).split('\n'), 'div')
    # with open('write_file.txt', 'w', encoding='utf-8') as wfile:
    #     for elem in (r.text).split('\n'):
    #         wfile.write(elem+'\n')


def counter(str1, tag):
    for str_elem in str1:
        match_detect = re.match('.*< *{0}.*'.format(tag), str_elem)
        if match_detect:
            print(str_elem)
        else:
            continue


if __name__ == '__main__':
    main()
