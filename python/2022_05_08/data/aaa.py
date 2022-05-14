# --*--coding:utf-8--*--
import re


def datamake():
    data = open('topix_data.csv', 'w', encoding='utf-8')
    with open('./topix.html', 'r', encoding='utf-8') as rfile:
        count = 0
        matchCon = re.compile('\b+<td[\w\W\s\S]*')
        for row in rfile:
            m = re.match(pattern='\s+<td\s+data-', string=row)
            if bool(m):
                print(row)
                indexStart = row.index('>')
                indexFin = row.index('<', indexStart)
                # print(row[indexStart+1:indexFin])
                data.write(row[indexStart+1:indexFin] + '\n')
    data.close()


def main():
