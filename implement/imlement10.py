def solution(key, lock):
    def turn(arr, l):
        tmp = [[0] * l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                tmp[j][l-i-1] = arr[i][j]
        return tmp
    
    def check(key, lock):
        l = len(lock)
        for i in range(l):
            for j in range(l):
                if lock[i][j] + key[i][j] != 1:
                    return False
        return True
    
    kl, ll = len(key), len(lock)
    board = [[0]*(3*ll) for _ in range(3*ll)]
    for x in range(4):
        for i in range(ll,kl+ll):
            for j in range(ll, kl+ll):
                board[i][j] = key[i%ll][j%ll]
        for r in range(1, ll+kl):
            for c in range(1, ll+kl):
                tmp = []
                for i in range(ll):
                    tmp.append(board[r+i][c:c+ll])
                if check(tmp, lock):
                    return True
        key = turn(key, kl)
    return False