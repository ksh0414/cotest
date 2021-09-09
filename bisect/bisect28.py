def binary_search(arr):
    start = 0
    end = n
    while start < end:
        mid = (start+end) // 2
        if arr[mid] > mid:
            start = mid + 1
        else:
            end = mid
    if end == n:
        return -1
    return end

n = int(input())
nums = list(map(int, input().split()))
print(binary_search(nums))