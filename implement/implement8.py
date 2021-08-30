#힙은 계속 O(logn)의 연산이 발생하고 정렬은 한 번만 
#발생하기 때문에 배열을 사용하는 것이 유리
arr = []
num = 0
for x in input():
    if x.isalpha():
        arr.append(x)
    else:
        num += int(x)
arr.sort()
arr.append(str(num))
print(''.join(arr))