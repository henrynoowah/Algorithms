# ord("a") - 96
# 50 점...????
# import sys

# L = int(input())
# N = sys.stdin.readline().rstrip()

# M = 31
# answer = 0

# arr = [(ord(i) - 96) for i in N]

# for i in range(0, len(arr)):
#     # print(type(arr[i]))
#     answer += (arr[i] * (M ** i))

# print(answer)

# Try 2
import sys

L = int(input())
N = sys.stdin.readline().rstrip()

M = 1234567891
answer = 0

for i in range(len(N)):
    # print(type(arr[i]))
    answer += ((ord(N[i]) - 96) * (31 ** i))

print(answer % M)