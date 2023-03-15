def build_heap(data):
    swaps = []
    n = len(data)

    # Build the heap bottom-up using the Floyd's algorithm
    for i in range(n // 2 - 1, -1, -1):
        min_index = i

        left_child = 2 * i + 1
        if left_child < n and data[left_child] < data[min_index]:
            min_index = left_child

        right_child = 2 * i + 2
        if right_child < n and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]

    return swaps


def sift_down(i, data, swaps):
    n = len(data)
    while 2*i+1 < n:
        j = 2*i+1
        if j+1 < n and data[j+1] < data[j]:
            j = j+1
        if data[i] > data[j]:
            swaps.append((i, j))
            data[i], data[j] = data[j], data[i]
            i = j
        else:
            break

def main():
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output how many swaps were made
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
