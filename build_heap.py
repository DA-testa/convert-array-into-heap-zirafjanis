import sys

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2, -1, -1):
        swaps += sift_down(data, i, n)
    return swaps

def sift_down(data, i, n):
    swaps = []
    max_idx = i
    l = 2*i + 1
    if l < n and data[l] > data[max_idx]:
        max_idx = l
    r = 2*i + 2
    if r < n and data[r] > data[max_idx]:
        max_idx = r
    if i != max_idx:
        swaps.append((i, max_idx))
        data[i], data[max_idx] = data[max_idx], data[i]
        swaps += sift_down(data, max_idx, n)
    return swaps


def heap_sort(data):
    swaps = []
    n = len(data)

    # Build the heap in O(n) time complexity
    build_heap(data)

    # Perform heap sort by removing the root element and re-heapifying
    for i in range(n-1, 0, -1):
        swaps.append((0, i))
        data[0], data[i] = data[i], data[0]
        sift_down(data[:i], 0, swaps)

    return swaps

def main():
    # Read input from either keyboard or file
    if len(sys.argv) == 1 or sys.argv[1] == 'I':
        n = int(input())
        data = list(map(int, input().split()))
    else:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    # Check if the length of data is the same as the given length
    assert len(data) == n

    # Perform heap sort and count the number of swaps
    swaps = heap_sort(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
