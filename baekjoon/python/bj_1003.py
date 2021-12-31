import sys

input = sys.stdin.readline

T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

def fib(n):

    # 0, 1, 2 때 기준은 이미 알고 있음
    # n > 2일 때 계산
    # 피보나치 수의 0의 개숫 와 1의 개수를 피보나치방식으로 연산
    length = len(zero)
    if length <= n:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    
    print(f"{zero[n]} {one[n]}")

for i in range(T):
    N = int(input())

    fib(N)

