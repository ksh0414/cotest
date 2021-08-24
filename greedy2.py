nums = input()
ans = 0 if nums[0] == '1' else 1
for x in nums:
    x = int(x)
    if x in (0, 1):
        ans += x
    else:
        ans *= x
print(ans)