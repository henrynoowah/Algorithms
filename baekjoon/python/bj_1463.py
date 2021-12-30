import sys

input = sys.stdin.readline

X = int(input())

dp = [0] * (X + 1)

# f(n) = 1 + min(f(n/3), f(n/2), f(n-1))
# Bottom Up
# 계산된 값을 저장, 
# X + 1 : 1번쨰 수는 dp[1]이 아니고 dp[2]이기 때문에 계산의 편의를 위해 추가된 더미데이터
# dp = [0] * (X + 1)
# dp[3] 까지는 1이 확실
for i in range(2, X + 1):
    # 세가지 계산 조건
    # 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    # 2. X가 2로 나누어 떨어지면, 2로 나눈다.
    # 3. 1을 뺀다.

    # initialization
    # 4부터는 최소 2번의 연산이 필요
    # dp[4] = dp[3] + 1 : 1 + 1 == 2  

    # -1 을 빼는 기준
    dp[i] = dp[i - 1] + 1

    # 1,2 번 째 조건과 -1을 했을 때의 최소값을 다음 연산으로 추가
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)


print(dp[X])
