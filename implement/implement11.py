import sys
from collections import deque
input = sys.stdin.readline
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
now_d = 0
change_d = {'L':-1, 'D':1, 'E':0}

n = int(input())
apples = set()
for _ in range(int(input())):
    i, j = map(int, input().split())
    apples.add((i-1, j-1))

body = deque([(0, 0)])
time = 0
flag = False
data = [tuple(input().split()) for _ in range(int(input()))]
data.append((100000, 'E'))
for t, d in data:
    t = int(t)
    if flag:
        continue
    for i in range(time, t):
        time += 1
        dr, dc = D[now_d]
        now_r, now_c = body[-1][0]+dr, body[-1][1]+dc
        if (0 <= now_r < n and 0 <= now_c < n) and (now_r, now_c) not in body:
            body.append((now_r, now_c))
            if (now_r, now_c) in apples:
                apples.remove((now_r, now_c))
            else:
                body.popleft()
        else:
            flag = True
            break
    now_d += change_d[d]
    if now_d < 0:   now_d = 3
    elif now_d > 3:   now_d = 0
print(time)
        