import heapq
from heapq import heapify, heappop, heappush


def sort_k(arr, n, k):
    heap = arr[:k + 1]
    heapq.heapify(heap)

    target_index = 0
    for i in range(k + 1, n):
        arr[target_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        target_index += 1

    while heap:
        arr[target_index] = heapq.heappop(heap)
        target_index += 1

    return arr


if __name__ == '__main__':
    # Driver Code
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    n = len(arr)
    print('Sorted array : ', sort_k(arr, n, k))
