# --*--coding:utf-8--*--
# from operator import truediv, truth
# import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def sample():
    wb = Workbook()
    dest_filename = 'empty_book.xlsx'
    ws1 = wb.active
    ws1.title = "range names"
    for row in range(1, 40):
        ws1.append(range(600))
    ws2 = wb.create_sheet(title="Pi")
    ws2['F5'] = 3.14
    ws3 = wb.create_sheet(title="Data")
    for row in range(10, 20):
        for col in range(27, 54):
            _ = ws3.cell(column=col, row=row,
                         value="{0}".format(get_column_letter(col)))
    print(ws3['AA10'].value)
    wb.save(filename=dest_filename)


def makeWorkBook():
    wb = openpyxl.Workbook()
    print('make sheet')
    wb.create_chartsheet()
    print(wb.sheetnames)
    sheet = wb[wb.sheetnames[0]]
    for count1 in range(1, 4):
        for count2 in range(1, 4):
            sheet.cell(row=count1, column=count2, value='●')
    wb.save('aaa.xlsx')


def main():
    # workBook = openpyxl.load_workbook('../text_file/work.xlsx', data_only=True)
    # # print(workBook.sheetnames)
    # sheetList = workBook.sheetnames
    # sheet0 = workBook[sheetList[0]]
    # print(type(sheet0))
    # for row in sheet0.values:
    #     print(row)
    # makeWorkBook()
    sample()


if __name__ == '__main__':
    main()
