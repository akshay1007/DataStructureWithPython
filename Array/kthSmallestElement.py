import heapq


class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def top(self):
        return -self.data[0]

    def push(self, item):
        heapq.heappush(self.data, -item)

    def pop(self):
        return -heapq.heappop(self.data)

    def replace(self, item):
        return heapq.heapreplace(self.data, -item)


def kthSmallest(arr, k):
    # base case
    if not arr or len(arr) < k:
        exit(-1)
    # build the max heap from first K element in list
    pq = MaxHeap(arr[0:k])

    # do the remaining element
    for i in range(k, len(arr)):
        if arr[i] < pq.top():
            # replace root with the current element
            pq.replace(arr[i])
    return pq.top()


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    input = range(0,len(arr))
    for i in input:
        print('For K = ', i+1 , 'smallest element is ', kthSmallest(arr, i+1))
