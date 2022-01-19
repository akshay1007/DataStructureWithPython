import heapq


def kClosest(arr, k, x):
    heap = []
    for i in range(k):
        heapq.heappush(heap,(-abs(arr[i]-x), i))
        print(heap[0][0])
    for i in range(k, len(arr)):
        diff = abs(arr[i] - x)
        curr = arr[-heap[0][0]]
        print ('dif ', diff , 'curr : ', curr)
        if abs(arr[i] - k) > heap[0][0]:
            continue
        else:
         heapq.heapreplace(heap, (abs(x - arr[i]), arr[i]))
         heapq.heapify(heap)
    print(heap)


if __name__ == '__main__':
    input = [5, 6, 7, 8, 9]
    k = 3
    x = 7
    kClosest(input, k, x)
