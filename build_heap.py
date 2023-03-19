import os

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    l = 2*i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2*i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)

def main():
    input_type = input().strip()
    
    if input_type == "I":
        n = int(input().strip())
        data = list(map(int, input().strip().split()))
    elif input_type == "F":
        file_path = os.path.join("04")
        with open(file_path, "r") as file:

            n = int(file.readline().strip()) 
            data = list(map(int, file.readline().strip().split()))

    else:
        print("Invalid input type. Please enter either 'I' or 'F'.")
        return
    
    assert len(data) == n
    
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
