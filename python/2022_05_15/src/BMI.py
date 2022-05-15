

from errno import EHOSTDOWN


class BMI:
    weight = None
    height = None
    name = None

    def __init__(self, weight, height, name):
        self.weight = weight
        self.height = height
        self.name = name

    def calcBMI(self):
        return self.weight - (self.height)**2

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height


def main():
    myBmi = BMI(100, 1.8, 'hello')
    print(myBmi.getName())
    print(myBmi.calcBMI())
    print(myBmi.getHeight())
    print(myBmi.getWeight())


if __name__ == '__main__':
    main()
