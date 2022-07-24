import random


def randList(count: int, min, max):
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


def randList2d(count: int, min, max):
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


def array2d(row: int, column: int):
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


def addArray(arrA, arrB):
    """
    adds two number arrays
    :param arrA: array number one -> only numbers
    :param arrB: array number two -> only numbers
    :return:
    """

    if len(arrA) > len(arrB):
        arrA, arrB = arrB, arrA


    newArr = []
    lastItemIndex = 0

    for i in range(len(arrA)):
        newItem = arrA[i] + arrB[i]
        newArr.append(newItem)
        lastItemIndex += 1

    for i in range(len(arrB) - lastItemIndex):
        newArr.append(arrB[i + lastItemIndex])

    return newArr

def multiList(dimension, size,min, max):
    newArr = []

    for i in range(dimension):
        tempArr = []
        for j in range(size):
            tempArr.append(random.randint(min, max))
        newArr.append(tempArr)

def shuffle(arr):
    for i in range(len(arr)*10):
        a = random.randint(0, (len(arr)-1))
        b = random.randint(0, (len(arr) - 1))
        arr[a], arr[b] = arr[b], arr[a]

    return arr