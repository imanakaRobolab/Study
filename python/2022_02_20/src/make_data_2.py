from sys import prefix
from turtle import right
from unicodedata import name
from numpy import column_stack
import pandas
import random

itemList = ['Pen', 'Book', 'Eraser', 'PC', 'Medicine', 'BAG']


def makeCategory():
    prefixCode = 'C'
    data = pandas.DataFrame()
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    for count in range(4):
        id = prefixCode + '{0:03d}'.format(count)
        Name = 'Category{}'.format(count)
        print('id is : '+id)
        print('category is : '+Name)
        dataElem = pandas.DataFrame(data=[[id, Name]], columns=['ID', 'Name'])
        data = data.append(dataElem)
    print(data)
    data.to_csv('Category.csv', index=False)
    return data


def makeItems():
    idPrefix = 'A'
    idPrefixUniCode = ord(idPrefix)
    data = pandas.DataFrame()
    random.seed(a=10)
    for itemElem in itemList:
        if itemElem != 'Pen':
            idPrefixUniCode += 1
        for count in range(1, 3):
            idPrefix = chr(idPrefixUniCode)
            id = idPrefix + '{0:04d}'.format(count)
            itemName = itemElem + str(count)
            price = random.randint(500, 1000)
            dataElem = pandas.DataFrame(
                data=[[id, itemName, price]], columns=['ID', 'Name', 'Price'])
            data = data.append(dataElem)
    print(data)
    data.to_csv('Item.csv', index=False)
    return data

# Pen1はCategory1とCategory2に所属するとする
# Book1はCategory1とCategory2に所属するとする
# Eraser1はCategory1とCategory2に所属するとする
# PC1はCategory1とCategory2に所属するとする
# Medicine1はCategory1とCategory2に所属するとする


def makeItemCategoryList(ItemData, CategoryData):
    itemID = ItemData['ID']
    data = pandas.DataFrame()
    for itemIDElem in itemID:
        if '1' in itemIDElem:
            for count in range(2):
                dataElem = pandas.DataFrame(
                    data=[[itemIDElem, 'C{0:03d}'.format(count)]], columns=['ItemID', 'CategoryID'])
                data = data.append(dataElem)
        else:
            dataElem = pandas.DataFrame(
                data=[[itemIDElem, 'C{0:03d}'.format(count)]], columns=['ItemID', 'CategoryID'])
            data = data.append(dataElem)
    return data


def main():
    CategoryData = makeCategory()
    ItemData = makeItems()
    itemCategoryList = makeItemCategoryList(ItemData, CategoryData)
    itemDataJoinWork = pandas.merge(
        left=ItemData, right=itemCategoryList, how='inner', left_on='ID', right_on='ItemID')
    itemCategory = pandas.merge(
        left=itemDataJoinWork, right=CategoryData, left_on='CategoryID', right_on='ID')
    itemCategory.drop('ID_y', axis=1, inplace=True)
    itemCategory.drop('ID_x', axis=1, inplace=True)
    itemCategory.rename(columns={'Name_y': 'CategoryName'}, inplace=True)
    itemCategory.rename(columns={'Name_x': 'ItemName'}, inplace=True)
    itemCategory = itemCategory.reindex(
        columns=['ItemID', 'ItemName', 'Price', 'CategoryID', 'CategoryName'])
    itemCategory.sort_values('ItemID', inplace=True)
    print(itemCategory)
    itemCategory.to_csv('item_category_list.csv')


if __name__ == '__main__':
    main()
