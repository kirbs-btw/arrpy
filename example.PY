import arrpy


def main():
    # print(arrpy.randList(50, 100, 1000))

    # list2d = arrpy.array2d(4, 3)
    # for i in list2d:
    #     print(i)

    arrB = [0, 2, 3, 1, 5]
    arrA = [1, 2, 3, 4, 5, 6, 7]

    print(arrpy.addArray(arrA, arrB))


if __name__ == '__main__':
    main()