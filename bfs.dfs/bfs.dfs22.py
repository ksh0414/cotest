from collections import deque

def get_next_pos(board, pos, m):
    result = []
    pos = sorted(list(pos))
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    if m == 'wid':
        u = d = False
        if board[x1-1][y1] == 0 and board[x2-1][y2] == 0:#상
            result.append([{(x1-1, y1), (x2-1, y2)}, 'wid'])
            u = True
        if board[x1+1][y1] == 0 and board[x2+1][y2] == 0:#하
            result.append([{(x1+1, y1), (x2+1, y2)}, 'wid'])
            d = True
        if board[x1][y1-1] == 0:#좌
            result.append([{(x1, y1-1), (x2, y2-1)}, 'wid'])
        if board[x2][y2+1] == 0:#우
            result.append([{(x1, y1+1), (x2, y2+1)}, 'wid'])
        if u:
            result.append([{(x1-1, y1), (x1, y1)}, 'len'])
            result.append([{(x2-1, y2), (x2, y2)}, 'len'])
        if d:
            result.append([{(x1+1, y1), (x1, y1)}, 'len'])
            result.append([{(x2+1, y2), (x2, y2)}, 'len'])
    else:
        l = r = False
        if board[x1-1][y1] == 0: #상
            result.append([{(x1-1, y1), (x2-1, y2)}, 'len'])
        if board[x2+1][y2] == 0: #하
            result.append([{(x1+1, y1), (x2+1, y2)}, 'len'])
        if board[x1][y1-1] == 0 and board[x2][y2-1] == 0: #좌
            result.append([{(x1, y1-1), (x2, y2-1)}, 'len'])
            l = True
        if board[x1][y1+1] == 0 and board[x2][y2+1] == 0: #우
            result.append([{(x1, y1+1), (x2, y2+1)}, 'len'])
            r = True
        if l:
            result.append([{(x1, y1-1), (x1, y2)}, 'wid'])
            result.append([{(x2, y2-1), (x2, y1)}, 'wid'])
        if r:
            result.append([{(x1, y1+1), (x1, y2)}, 'wid'])
            result.append([{(x2, y2+1), (x2, y1)}, 'wid'])
    return result
            
def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[1+i][1+j] = board[i][j]
    pos = {(1, 1), (1, 2)}
    q = deque([(pos, 0, 'wid')])
    
    visited = [pos]
    while True:
        pos, cnt, m = q.popleft()
        if (n, n) in pos:
            answer = cnt
            break
        for next_pos in get_next_pos(new_board, pos, m):
            if next_pos[0] not in visited:
                q.append((next_pos[0], cnt+1, next_pos[1]))
                visited.append(next_pos[0])
    return answer