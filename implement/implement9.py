def solution(s):
    l = len(s)
    answer = l
    for i in range(1, l//2+1):
        pre = s[:i]
        tmp = i
        exponent = 0
        count = 1
        for j in range(i, l, i):
            if pre == s[j:j+i]:
                count += 1
                if count >= 10**exponent:
                    tmp += 1
                    exponent += 1
            else:
                pre = s[j:j+i]
                tmp += len(pre)
                exponent = 0
                count = 1
        answer = min(answer, tmp)
                
    return answer