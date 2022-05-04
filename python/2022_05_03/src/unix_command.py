import os
import glob


def main():
    list1 = os.listdir('../text_file/')
    print(list1)
    list2 = glob.glob('*sample*')
    print(list2)


if __name__ == '__main__':
    main()
