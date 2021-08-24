#https://programmers.co.kr/learn/courses/30/lessons/42891
from collections import Counter
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    l = len(food_times)
    counter = Counter(sorted(food_times))
    time = answer = last = pre = 0
    remain = l
    for t, c in counter.items():
        if time + (t-pre)*remain > k:
            last = t
            time += ((k-time) // remain) * remain
            break
        time += (t-pre)*remain
        pre = t
        remain -= c
    for i in range(l):
        if last > food_times[i]:
            continue
        time += 1
        if time > k:
            answer = i+1
            break
    return answer