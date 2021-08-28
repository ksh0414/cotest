#https://acmicpc.net/problem/1439
count = [0] * 2
nums = input()
pre_num = nums[0]
count[int(pre_num)] += 1
for x in nums[1:]:
    if pre_num != x:
        count[int(x)] += 1
        pre_num = x
print(min(count))
