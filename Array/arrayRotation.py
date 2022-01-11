# Different Methods of Array Rotation in Python
# We will write a function for rotation (arr[], E, K)
# which will be used for rotating arr[] of size K = 8 by E = 4 elements.

# Method 1: By using temp array
# Time Complexity: O(K)     [K = size of array]
# Auxiliary Space: O(E)     [E = number of elements to be rotated]

def rotateArray(arr, E, K):
    temp = []
    j = 0
    while j < E:
        temp.append(arr[j])
        j = j + 1
    j = 0
    while E < K:
        arr[j] = arr[E]
        j = j + 1
        E = E + 1
    arr[:] = arr[:j] + temp
    return arr


# Method 2: By using List Slicing
def rotate_List1(arr, E, N):
    arr[:] = arr[E:N] + arr[0:E]
    return arr

    # Driver Program to test above function


arr = [1, 3, 5, 7, 9, 11, 13, 15]
arr2 = [1, 3, 5, 7, 9, 11, 13, 15]

E = 4
N = 8
print('Input array : ', arr)
print('Rotated array is : ', rotateArray(arr, E, N))
print('Rotated array 1 is : ', rotate_List1(arr2, E, N))

