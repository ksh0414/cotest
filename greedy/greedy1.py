from collections import Counter

n = int(input())
group = 0
count = 0
for x in sorted(list(map(int, input().split()))):
    count += 1
    if count >= x:
        group += 1
        count = 0
print(group)