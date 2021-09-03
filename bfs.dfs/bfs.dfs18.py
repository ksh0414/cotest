def solve(w):
    if w == '':
        return w
    idx = 0
    c1 = c2 = 0
    for x in w:
        if x == '(':
            c1 += 1
        else:
            c2 += 1
        if c1 == c2:
            break
    u = w[:c1+c2]
    v = w[c1+c2:]
    if check(u):
        u += solve(v)
        return u
    else:
        tmp = '('
        tmp += solve(v)
        tmp += ')'
        for x in u[1:len(u)-1]:
            if x == ')':
                tmp += '('
            else:
                tmp += ')'
        return tmp
    
def check(arr):
    stk = []
    for x in arr:
        if x == ')':
            if stk:
                stk.pop()
            else:
                return False
        else:
            stk.append(x)
    if stk:
        return False
    return True
def solution(p):
    return solve(p)