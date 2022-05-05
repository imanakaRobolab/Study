# --*--coding:utf-8--*--
import os


def get_full_path():
    return os.getcwd()


def change_relative_to_full(path):
    pathList = path.split('/')
    print(pathList)
    toParentCount = 0
    currentPath = get_full_path()
    currentList = currentPath.split('\\')
    print(currentList)
    if '..' in pathList:
        toParentCount = pathList.count('..')
        for count in range(toParentCount):
            currentList.pop(-1)
            pathList.pop(0)

    currentList += pathList
    print('/'.join(currentList))


change_relative_to_full('../src')
