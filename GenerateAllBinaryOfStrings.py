# Time complexity – O(2n)
# Space complexity – O(n)


def printTheArray(ele, x):
    for i in range(0, x):
        print(ele[i], end=" ")

    print()


def generateAllBinaryStrings(x, ele, i):
    if i == x:
        printTheArray(ele, x)
        return

    ele[i] = 0
    generateAllBinaryStrings(x, ele, i + 1)
    ele[i] = 1
    generateAllBinaryStrings(x, ele, i + 1)


if __name__ == '__main__':
    n = 4
    arr = [None] * 4
    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
