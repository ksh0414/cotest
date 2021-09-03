import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    distance = [-1] * (n+1)
    distance[start] = 0
    result = []
    q.append(start)
    while q:
        now = q.popleft()
        if distance[now] == k:
            result.append(now)
        elif distance[now] > k:
            return result
        for n_n in graph[now]:
            if distance[n_n] == -1:
                distance[n_n] = distance[now] + 1
                q.append(n_n)
    tmp = [i for i in range(1, n+1) if distance[i] == k]
    return tmp if tmp else [-1]

n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for x in bfs(start):
    print(x)