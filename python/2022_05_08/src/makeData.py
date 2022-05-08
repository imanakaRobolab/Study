
from calendar import calendar
import datetime
from math import floor
from traceback import print_tb
import pandas
import random
import numpy
import csv
import pandas


def makeData(length, date=None):
    date = datetime.date.today() if date == None else date
    dateArray = []
    moveDisArray = []
    sleepTimeArray = []
    deltatime = datetime.timedelta(days=1)
    df = pandas.DataFrame(columns=['date', 'moveDistance', 'sleep'])
    for i in range(length):
        dateArray.append(date.strftime('%Y/%m/%d'))
        moveDistance = 10*random.random()
        moveDisArray.append(moveDistance)
        sleepTime = 8*random.random()
        sleepTimeArray.append(sleepTime)
        df = df.append(pandas.DataFrame([[date, moveDistance, sleepTime]], columns=[
                       'date', 'moveDistance', 'sleep']))
        date = date-deltatime
    retList = [dateArray, moveDisArray, sleepTimeArray]
    print(df)
    return df


def main():
    dataList = makeData(length=100)
    # with open('../data/data.csv', 'w') as dataFile:
    #     writer = csv.writer(dataFile)
    #     writer.writerows(dataList)
    # return
    dataList.to_csv('../data/data.csv', index=False)


if __name__ == '__main__':
    main()
