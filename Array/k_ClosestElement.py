from queue import PriorityQueue


def printKclosest(arr, x, k, n):
    # create priority queue
    pq = PriorityQueue()

    # process first K element and store in PQ
    # first k elements.
    for i in range(k):
        pq.put((-abs(arr[i] - x), i))

    # process rest of the elements
    for i in range(k, n):
        diff = abs(arr[i] - x)
        p, pi = pq.get()
        curr = -p
        if diff > curr:
            pq.put((-curr, pi))
            continue
        else:
            pq.put((-diff, i))

    # Print contents of heap.
    while not pq.empty():
        p, q = pq.get()
        print("{} ".format(arr[q]), '    ', p)


if __name__ == '__main__':
    arr = (-10, -50, 20, 17, 80)
    x = 20
    k = 2
    printKclosest(arr, x, k, len(arr))
