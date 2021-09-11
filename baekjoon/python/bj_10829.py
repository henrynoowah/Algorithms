# N = int(input())
# print(bin(N)[2:])

# print(format(53, 'b'))

# 재귀함수를 써야 하니 다시 ㅎ

arr = []
def binFn(n):
    if n == 1:
        arr.append(n)
    else:
        arr.append(n % 2)
        binFn(n // 2)

N = int(input())
binFn(N)

# [1,0,1,0,1,1]
for i in range(len(arr)):
    print(arr.pop(), end = "")


