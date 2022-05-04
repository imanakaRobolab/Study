# --*--coding:utf-8--*--

from queue import PriorityQueue
from string import whitespace

from anyio import open_cancel_scope


def main():
    file_path = '../text_file/sample.txt'
    print('処理の開始')
    with open('../text_file/sample.txt', 'w') as ofile:
        # 書込み可能かどうかを確認する。
        print(ofile.writable())
        # fileに書込みを行う
        name = input('What\'s your name?')
        ofile.write(name+'\n')
        list1 = []
        for i in range(10):
            list1.append(f'For loop count is :{i}.\n')
        ofile.writelines(list1)
    rfile = open(file_path, 'r')
    for rline in rfile:
        print(rline)
    rfile.close()
    with open(file=file_path, mode='r') as rfile:
        print(rfile.read())
        print(rfile.readlines())


if __name__ == '__main__':
    main()
