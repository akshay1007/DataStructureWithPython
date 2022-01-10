
if __name__ == '__main__':

    matrix = [[1, 5, 21, 50],
              [6, 12, 39, 62],
              [24, 33, 45, 99]]

    matrix_length = (len(matrix))

# to print last element from each row
    for i in range(matrix_length):
        print(matrix[i][-1])
    print()
# to print first element from each row
    for i in range(matrix_length):
        print(matrix[i][0])
    print()
# to print first row element
    for i in range(matrix_length):
        print(matrix[i][0])
# to find length of column
    columns = len(matrix[0])
    print('total length of column', columns)

