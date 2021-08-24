n = int(input())
coins = list(map(int, input().split()))
small_unit = 0
for x in sorted(coins):
    if x > small_unit+1:
        break
    else:
        small_unit += x
print(small_unit+1)