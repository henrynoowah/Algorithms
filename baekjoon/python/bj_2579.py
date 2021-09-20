import sys
N = int(sys.stdin.readline())

steps = [int(sys.stdin.readline()) for _ in range(N)]
dp = []

if N == 1:
    print(steps[0])
    exit()
elif N == 2:
    print(max(steps[1], steps[0] + steps[1]))
    exit()

dp.append(steps[0])
dp.append(steps[0] + steps[1])
dp.append(max(steps[0] + steps[2], steps[1] + steps[2]))
# [10, 30, 35]

print(dp)

for i in range(3, N):
    dp.append(max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i]))
    print(dp)

print(dp[-1])


