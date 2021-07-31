# # 실질적인 리스트를 시각화 하면서 알고리즘의 규칙을 찾음
# # 구현 자체는 틀리지 않았으나 시간초과

# T = int(input())

# last = 0
# arr = [i for i in range(1, T + 1)]

# arr2 = []
# flag = True
# answer = []

# for i in range(T):

#   num = int(input())
#   if num in arr:  
#     while num in arr:
#       arr2.append(arr.pop(0))
#       answer.append('+')
#     answer.append('-')
#   else:
#     if num in arr2:
#       while num in arr2:
#         arr2.pop()
#       answer.append('-')
#     else:
#       flag = False

# if flag:
#   for i in answer:
#     print(i)
# else:
#   print('NO')



# SOLUTION
# 비교대상으로 사용한 arr 리스트를 미리 만들지 않고 count 변수 를 사용하여 반복문 안에서만 사용
# 반복문 내부 조건문도 최소화 하여 더 메모리효율적이지 않은가 싶다

T = int(input())
count = 0

arr = []
answer = []
flag = True

for i in range(T):
  
  num = int(input())

  while count < num:
    count += 1
    arr.append(count)
    answer.append('+')
    # print(answer)
  
  if arr[-1] == num:
    arr.pop()
    answer.append('-')
    # print(answer)
  else:
    flag = False

if flag:
  print("\n".join(answer))
else:
  print('NO')


    