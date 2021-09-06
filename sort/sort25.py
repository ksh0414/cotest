from collections import Counter

def solution(N, stages):
    tmp = {}
    stages.sort()
    counter = Counter(stages)
    for i in range(1, N+1):
        tmp[i] = counter[i] / N
        N -= i
    answer = [x[0] for x in sorted(tmp.items(), key = lambda x: x[1], reverse = True)]
    return answer
    
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))