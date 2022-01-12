# Given a sorted array arr[] of N integers,
# The task is to find the multiple missing elements
# in the array between the ranges [arr[0], arr[N-1]]

# Time Complexity: O(M), where M is the maximum element of the array.
# Auxiliary Space: O(M)


def findMissing(arr, n):
    missing = []
    cnt = 0
    for i in range(arr[0], arr[n - 1]):
        if arr[cnt] == i:
            cnt = cnt + 1
        else:
            missing.append(i)

        # Driver Program
    print('Missing numbers are : ', missing)


if __name__ == '__main__':
    arr = [6, 7, 10, 11, 13]
    n = len(arr)
    findMissing(arr, n)
