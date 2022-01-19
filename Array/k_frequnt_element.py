# Using heapq data structure
import heapq


def top_k(dict, k):
    heap = [(value, key) for key, value in dict.items()]
    heapq.heapify(heap)
    print(heap)

    # Get the top k elements
    largest = heapq.nlargest(k, heap)
    print(largest)
    return largest


def frequency(arr):
    dict = {}
    for item in arr:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict


if __name__ == '__main__':
    random_list = ['A', 'A', 'B', 'C','C','C', 'B', 'D', 'D', 'A', 'B']
    k = 2
    dict = frequency(random_list)
    top_elem = top_k(dict, k)
    for i in top_elem:
        print(i[1])
