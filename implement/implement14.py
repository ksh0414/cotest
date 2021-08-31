from itertools import permutations

def solution(n, weak, dist):
    l = len(weak)
    if l == 1:
        return 1
    answer = len(dist)
    weak += [n+x for x in weak]
    flag = False
    for order in permutations(dist):
        for start in range(0, l):
            now = start
            count = 1
            idx = 0
            friend = order[0]
            try:
                while count < l:
                    if friend+weak[now] >= weak[now+1]:
                        friend -= (weak[now+1] - weak[now])
                    else:
                        idx += 1
                        friend = order[idx]
                    now += 1
                    count += 1
                flag = True
                answer = min(answer, idx+1)
            except IndexError:
                continue
    return answer if flag else -1