import datetime

dict = {'6': 'Sun', '0': 'Mon', '1': 'Tue',
        '2': 'Wed', '3': 'Thu', '4': 'Fri', '5': 'Sat'}
a = datetime.date(2022, 11, 5)
print(a.toordinal())
print(dict[str(a.weekday())])
print(a.strftime('%Y/%m/%d'))
list1 = [
    '11/2',
    '04/05',
    '3/11',
    '08/03',
    '10/12',
    '12/3',
    '07/03',
    '09/01',
    '10/2'
]

for listElem in list1:
    monthAndDay = listElem.split('/')
    print(int(monthAndDay[0]))
    if monthAndDay[0] < 5:
