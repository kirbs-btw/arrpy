import random

def randList(count, min, max):
    """
    creates a list containing random elements
    :param count: number of elements
    :param min: smallest possible number
    :param max: highest possible number
    :return: random list
    """
    arr = []
    for i in range(count):
        arr.append(random.randint(min, max))

    return arr

def randList2d(count, min, max):
    """
    creates a 2d cubic list containing random elements

    e.g.:
    [2, 4, 7]
    [4, 8, 3]
    [9, 8, 10]

    :param count: number of elements
    :param min: smallest possible number
    :param max: highest possible number
    :return: random list
    """

    arr = []

    for i in range(count):
        tempArr = []
        for j in range(count):
            tempArr.append(random.randint(min, max))
        arr.append(tempArr)

    return arr

def array2d(row, column):
    """
    creates empty 2d array
    :param row: number of rows -> must be integer
    :param column: number of column -> must be integer
    :return: returns empty 2d array
    """
    
    arr = []
    tempArr = []
    for j in range(column):
        tempArr.append(None)
    for i in range(row):
        arr.append(tempArr)

    return arr




