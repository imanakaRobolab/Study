# --*--encoding : utf-8 --*--
from operator import rshift, truediv
import re


def main():
    count = 0
    with open('../text_file/sample.html', 'r') as rhtml:
        outputFlag = False
        for rString in rhtml:
            if outputFlag == False:
                m = re.match('\b*<body>', rString)
                if m:
                    outputFlag = True
                    continue
            else:
                m = re.match('\b*</body>', rString)
                if m:
                    outputFlag = False
                    continue
            if outputFlag == True:
                print(rString)
                words = re.split('\W+', rString.lstrip().rstrip())
                if '' in words:
                    words.remove('')
                count += len(words)
    print(count)


if __name__ == '__main__':
    main()
