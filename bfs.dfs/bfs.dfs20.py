import sys
input = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

def check():
    for x, y in teachers:
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            while (0<=nx<n and 0<=ny<n) and (nx, ny) not in walls:
                if (nx, ny) in students:
                    return False
                nx += dx
                ny += dy
    return True

def back_tracking(ii, idx):
    global walls
    if ii == 3:
        return check()
    else:
        for i in range(idx, len(blanks)):
            r, c = blanks[i]
            walls.append((r, c))
            if back_tracking(ii+1, i+1):
                return True
            else:
                walls.pop()
    return False

n = int(input())
blanks = []
students = []
teachers = []
walls = []

for i in range(n):
    line = input().strip().split()
    for j in range(n):
        if line[j] == 'X':
            blanks.append((i, j))
        elif line[j] == 'S':
            students.append((i, j))
        else:
            teachers.append((i, j))

if back_tracking(0, 0):
    print('YES')
else:
    print('NO')