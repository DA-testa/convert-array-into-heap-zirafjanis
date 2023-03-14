# python3


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        swaps = sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    n = len(data)
    min_idx = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_idx]:
        min_idx = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_idx]:
        min_idx = r
    if i != min_idx:
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps.append((i, min_idx))
        swaps = sift_down(data, min_idx, swaps)
    return swaps

    

def main():
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if length of data is the same as the said length
    assert len(data) == n

    # add input for I or F
    sort_type = input("Enter sort type (I for increasing, F for decreasing): ").strip()
    assert sort_type in ["I", "F"]

    # convert data to min-heap using O(n) swaps
    swaps = build_heap(data)

    # output how many swaps were made (less than 4n)
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)

    # output the sorted data in increasing or decreasing order
    if sort_type == "I":
        sorted_data = heap_sort(data)
    else:
        # read data from file
        filename = input("Enter filename: ").strip()
        with open(filename, 'r') as file:
            lines = file.readlines()
            # convert each line to an integer and append to a list
            sorted_data = [int(x) for x in lines]
        sorted_data = heap_sort(sorted_data, reverse=True)
    print(*sorted_data)



def heap_sort(data, reverse=False):
    n = len(data)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        sift_down(data, 0, i)
    if reverse:
        data.reverse()
    return data



if __name__ == "__main__":
    main()
