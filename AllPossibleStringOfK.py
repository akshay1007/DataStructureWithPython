# Using Subtraction and Conquer Master theorem we get: T(n) =O(k").

def printAllKLength(set, k):
    n = len(set)
    printAllKLengthRec(set, "", n, k)


def printAllKLengthRec(set, prefix, n, k):
    if k == 0:
        print(prefix)
        return
    for i in range(n):
        newPrefix = prefix + set[i]
        printAllKLengthRec(set, newPrefix, n, k - 1)


if __name__ == '__main__':
    print("First test case ")
    set1 = ['A', 'B']
    k = 3
    printAllKLength(set1, k)




