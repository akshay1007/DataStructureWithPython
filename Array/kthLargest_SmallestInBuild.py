import heapq
from heapq import heapreplace, heappush


def kthLargest(arr, k):
    minHeap = []
    for i in range(k):
        minHeap.append(arr[i])
        heapq.heapify(minHeap)
    print('==========', minHeap)

    for i in range (k, len(arr)):
        if arr[i] > minHeap[0]:
            heapq.heapreplace(minHeap,arr[i])
            heapq.heapify(minHeap)

    print(k, ' Largest number :',minHeap[0])

def kthSmallest(arr, k):
    maxHeap = []
    for i in range(k):
        maxHeap.append(-arr[i])
        heapq.heapify(maxHeap)

    for i in range (k, len(arr)):
        if -arr[i] > maxHeap[0]:
            heapq.heapreplace(maxHeap,-arr[i])
            heapq.heapify(maxHeap)

    print(k,' smallest number :',-maxHeap[0])

input = [7, 4, 6, 3, 9, 1]

for i in range(1,len(input)):
    kthLargest(input, i)
    # kthSmallest(input, i)
