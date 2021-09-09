def lower_bound(arr, x):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end) // 2
        if arr[mid] < x:
            start = mid+1
        else:
            end = mid
    return end

def upper_bound(arr, x):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end) // 2
        if arr[mid] <= x:
            start = mid + 1
        else:
            end = mid
    return start

n, x = map(int, input().split())
nums = list(map(int, input().split()))
a, b = lower_bound(nums, x), upper_bound(nums, x)
print(b-a if b-a != 0 else -1)