n = int(input())
if n%2 == 0:
    n = n//2 - 1
else:
    n //= 2
print(sorted(list(map(int ,input().split())))[n])