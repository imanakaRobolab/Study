from calendar import calendar
from operator import index
from turtle import heading
import pandas
import random
import datetime


def makeWeight():
    return random.randint(40, 120)


def makeHeight():
    return random.randint(140, 210)


def makeID(unicodeNum, idNum):
    prefixChar = chr(unicodeNum)
    return '{0}{1:07d}'.format(prefixChar, idNum)


def makeTelephoneNum():
    telephoneNumFir = random.randint(0, 999)
    telephoneMiddle = random.randint(0, 9999)
    telephoneFin = random.randint(0, 9999)
    return '{:03d}-{:04d}-{:04d}'.format(telephoneNumFir, telephoneMiddle, telephoneFin)


def makeCalendar():
    startDate = datetime.date(2000, 1, 1).toordinal()
    endDate = datetime.date(2030, 3, 31).toordinal()
    randomDay = random.randint(startDate, endDate)
    return datetime.date.fromordinal(randomDay)


def main():
    prefixCode = 'A'
    uniCodeNum = ord(prefixCode)
    data = pandas.DataFrame(
        columns=['id', 'height', 'weight', 'telephone', 'calendar'])
    for s in range(11):
        if s != 0:
            # 10回ごとにアルファベットが変わる
            uniCodeNum = ord(prefixCode)+1
            prefixCode = chr(uniCodeNum)
        for t in range(11):
            id = makeID(uniCodeNum, t)
            height = makeHeight()
            weight = makeWeight()
            telephone = makeTelephoneNum()
            calendarNum = makeCalendar()
            dataAppend = pandas.DataFrame(
                data=[[id, height, weight, telephone, calendarNum]], columns=['id', 'height', 'weight', 'telephone', 'calendar'])
            data = data.append(dataAppend)
    data.to_csv('data.csv', index=False)


if __name__ == '__main__':
    main()
