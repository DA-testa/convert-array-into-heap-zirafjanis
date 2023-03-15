def build_heap(data):
    swaps = []
    n = len(data)

    # Starting from the last non-leaf node and going up to the root
    # perform sift down operation to convert the array into a min-heap
    for i in range(n // 2, -1, -1):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and data[left_child] < data[min_index]:
            min_index = left_child

        if right_child < n and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            # swap the current element with the minimum of its children
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            swaps += build_heap(data[min_index:])

    return swaps


def main():
    input_type = input("Enter 'I' to enter input manually or 'F' to read from file: ")
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == "F":
        filename = input("Enter the filename: ")
        with open(filename, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input type. Please enter 'I' or 'F'.")
        return

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()

