import arrpy


def main():
    print(arrpy.randList(50, 100, 1000))

    list2d = arrpy.array2d(4, 3)
    for i in list2d:
        print(i)


if __name__ == '__main__':
    main()