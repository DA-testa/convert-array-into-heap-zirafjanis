def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        sift_down(i, data, swaps)
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
