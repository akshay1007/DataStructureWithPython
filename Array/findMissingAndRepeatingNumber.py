def findMissingRepeating(arr, n):
    i = 0
    missing = []
    duplicate = set()
    while i != n:
        if arr[i] != arr[arr[i] - 1]:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
        else:
            i = i + 1
    print(arr)
    for i in range(n):
        if arr[i] != i + 1:
            missing.append(i + 1)
            duplicate.add(arr[i])
    print('duplicate number are  : ')
    for dup in list(duplicate):
        print(dup, end=" ")
    print('\nmissing number  are :')
    for mis in missing:
        print(mis, end=" ")


# Driver Program
if __name__ == '__main__':
    arr = [4, 3, 6, 2, 1, 1]
    arr_1 = [1, 2, 2, 2, 4, 5, 7]
    n = len(arr)
    findMissingRepeating(arr_1, n)
