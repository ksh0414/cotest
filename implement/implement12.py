PILLAR, DAM = DELETE, BUILD = 0, 1
def check(data):
    for x, y, a in data:
        if a == PILLAR:
            if not (y == 0 or [x, y-1, PILLAR] in data or [x, y, DAM] in data or [x-1, y, DAM] in data):
                return False
        else:
            if not ([x, y-1, PILLAR] in data or [x+1, y-1, PILLAR] in data or ([x-1, y, DAM] in data and [x+1, y, DAM] in data)):
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == BUILD:
            answer.append([x, y, a])
            if not check(answer):
                answer.pop()
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    return sorted(answer)