def build_heap(data):
    swaps = []
    
    # The following function sifts down the element at index i to its correct position
    # to make sure that the subtree rooted at i is a heap.
    def sift_down(i):
        # We initialize min_index with i, which is the root of the subtree.
        min_index = i
        # We compare the left child of i with min_index and update min_index accordingly.
        left_child = 2 * i + 1
        if left_child < len(data) and data[left_child] < data[min_index]:
            min_index = left_child
        # We compare the right child of i with min_index and update min_index accordingly.
        right_child = 2 * i + 2
        if right_child < len(data) and data[right_child] < data[min_index]:
            min_index = right_child
        # If i is not the minimum element among i and its children, we swap them and continue
        # sifting down the element at min_index.
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            sift_down(min_index)
    
    # We start sifting down elements from the bottom of the heap up to the root.
    for i in range(len(data) // 2, -1, -1):
        sift_down(i)

    return swaps


def main():
    input_type = ""
    while input_type not in ["I", "F"]:
        input_type = input("Enter I to input from keyboard or F to read from file: ")

    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
    else:
        filename = input("Enter the filename: ")
        with open(filename, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
