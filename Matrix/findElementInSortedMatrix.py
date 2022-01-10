if __name__ == '__main__':
    matrix = [[1, 5, 21, 50],
              [6, 12, 39, 62],
              [24, 33, 45, 99]]

    # searchable element
    element = 24

    # start searching from right top corner from the matrix
    # i = rows , j = columns

    i = 0
    j = len(matrix[0])-1
    n = 3
    while i < n and j >= 0:
        print('inside 1')
        if element == matrix[i][j]:
            print('inside 2')
            print('found the element at position : ', i, j)
            break
        else:
            if element < matrix[i][j]:
                print('inside 3')
                j = j - 1
            else:
                print('inside 4')
                i = i + 1
