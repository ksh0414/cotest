from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline
BLANK, WALL, VIRUS = range(3)
nodes = [[] for _ in range(3)]
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(safe_area, new_walls):
    dummy = copy.deepcopy(board)
    for i, j in new_walls:
        dummy[i][j] = 1
    q = deque(nodes[VIRUS])
    while q:
        x, y  = q.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if (0<=nx<n and 0<=ny<m) and dummy[nx][ny] == 0:
                dummy[nx][ny] = 2
                safe_area -= 1
                q.append((nx, ny))
    return safe_area

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        nodes[board[i][j]].append((i, j))

safe_area = len(nodes[BLANK]) - 3
ans = 0
for new_walls in combinations(nodes[BLANK], 3):
    ans = max(bfs(safe_area, new_walls), ans)
print(ans)
