num = [int(x) for x in input()]
l = len(num)
front, behind = sum(num[:l//2]), sum(num[l//2:])
if front == behind:
    print('LUCKY')
else:
    print('READY')