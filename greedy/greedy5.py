from collections import Counter

n, m = map(int, input().split())
balls = list(map(int, input().split()))

counter = Counter(balls)
ans = 0
for x in counter.keys():
    n -= counter[x]
    ans += counter[x] * n
print(ans)