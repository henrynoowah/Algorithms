# first try
# 시간초과

n = int(input())
nArr = [int(i) for i  in input().split()]

m = int(input())
mArr = [int(i) for i  in input().split()]

answer = [0 for i in range(m)]

for i, cardNum in enumerate(mArr):
    for j in nArr:
        if cardNum == j:
            answer[i] += 1

print(answer)
