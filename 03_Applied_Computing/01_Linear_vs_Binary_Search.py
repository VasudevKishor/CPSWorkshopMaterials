# 01_Linear_vs_Binary_Search.py
import time

def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

def main():
    large_data = list(range(1000000))
    target = 999999 

    print(f"Searching for {target} in 1,000,000 items...\n")

    # Test Linear
    start = time.time()
    idx, steps = linear_search(large_data, target)
    end = time.time()
    print(f"Linear Search: Found at {idx} in {steps} steps ({end - start:.6f} s)")

    # Test Binary
    start = time.time()
    idx, steps = binary_search(large_data, target)
    end = time.time()
    print(f"Binary Search: Found at {idx} in {steps} steps ({end - start:.6f} s)")

if __name__ == "__main__":
    main()
