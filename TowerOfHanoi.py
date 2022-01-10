def TowerOfHanoi(n, source, destination, helper):
    if n == 1:
        print("Move Disk 1 from source ", source, " to Destination ", destination)
        return
    TowerOfHanoi(n - 1, source, helper, destination)
    print("Move Disk ", n, " from source  ", source, " to Destination ", destination)
    TowerOfHanoi(n - 1, helper, destination, source)


# Driver code

n = 4
arr = [None] * n
print(arr)
print(len(arr))
# TowerOfHanoi(n, 'A', 'B', 'C')
