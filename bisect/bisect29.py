import sys
input = sys.stdin.readline

def binary_search():
    start = 1
    end = lists[-1] - lists[0]+1
    ans = 0
    while start < end:
        mid = (start+end) // 2
        pre = lists[0]
        cnt = 1
        for x in lists[1:]:
            if x-pre >= mid:
                cnt += 1
                pre = x
        if cnt >= c:
            ans = mid
            start = mid + 1
        else:
            end = mid
    return ans

n, c = map(int, input().split())
lists = []
for _ in range(n):
    lists.append(int(input()))
lists.sort()
print(binary_search())