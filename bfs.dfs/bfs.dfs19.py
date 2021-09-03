def dfs(i, now):
    global add, sub, mul, div, max_value, min_value
    
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / nums[i]))
            div += 1

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_value = int(1e9)
max_value = -int(1e9)

dfs(1, nums[0])
print(max_value)
print(min_value)