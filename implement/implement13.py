from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
BLANK, HOUSE, CHICKEN = 0, 1, 2
block = [[] for _ in range(3)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        block[line[j]].append((i, j))

ans = 987654321
for now in combinations(block[CHICKEN], m):
    total_distance = 0
    for i, j in block[HOUSE]:
        total_distance += min([abs(ni-i)+abs(nj-j) for ni, nj in now])
        if total_distance > ans:
            break
    else:
        ans = total_distance
print(ans)