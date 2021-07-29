# first try
# 시간초과

N = int(input())
arrN = [int(i) for i  in input().split()]

M = int(input())
arrM = [int(i) for i  in input().split()]

arrA = [0 for i in range(M)]

for i, cardNum in enumerate(arrM):
    for j in arrN:
        if cardNum == j:
            arrA[i] += 1

answer = " ".join(list(map(str, arrA)))

print(answer)

# 이분탐색 방법 고려하여 이분탐색 재귀함수을 통해하는 방법 고려

# 	upB = find index of R + 1
# 	downB = find index of L
# 	count of each value = upB - downB
# 	answer.append(count)


# java HashMap과 흡사한 자료구조 딕셔너리 사용



# Solution

N = int(input())
arrN = [int(i) for i  in input().split()]

M = int(input())
arrM = [int(i) for i  in input().split()]

arrA = [0 for i in range(M)]

dic = {}
arrA = []

# arrN의 반복 숫자들을 key로 지정 // 기본 value = 1
# 중복된 값이 있을 시 value += 1
for num in arrN:
  if num in dic:
    dic[num] += 1
  else:
    dic[num] = 1

# arrM에 있는 딕셔너리 아이디에 value 를 arrA에 반환
# 없을 시 0 반환
for num in arrM:
  if num in dic:
    arrA.append(dic[num])
  else:
    arrA.append(0)

answer = " ".join(list(map(str, arrA)))

print(answer)





