def factorial(num):
    fct = 1
    for i in range(num, 1, -1):
        fct *= i
    # print(f'factorial{fct}')
    return fct

# while 1:
#     N = input()
#     if N == '0':
#         break
#     else:
#         arr = [int(i) for i in map(str, N)]
#         answer = 0
#     for i in range(len(N)):
#         answer += arr[i] * factorial(len(arr)-i)
  
#     print(answer)

# inpit()을 사용하게되면 시간초과가 나옴

import sys 

while 1:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    else:
        arr = [int(i) for i in map(str, N)]
        answer = 0
    for i in range(len(N)):
        answer += arr[i] * factorial(len(arr)-i)
  
    print(answer)