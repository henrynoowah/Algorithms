# Fail

# YES 조건
# ( 로 시작할때 
# ( 다음이 ) 일 떄
# ( 이면 마지막이 )일떄

# ()() (()()) 는 만족하나
# (()())() 와 같이 2차원 형태가 1 개 이상일 때 조건을 갖추지 못함

# T = int(input())

# for i in range(T):
    
#     b = list(input())
#     ans = 'YES'

#     while b:
#       # 총 길이가 홀수 일 때 'NO'
#       if len(b) % 2 != 0:
#         ans = 'NO'
#         break

#       else: 

#         j = b.pop(0)

#         if j == '(':
#           if b[0] == ')':
#             b.pop(0)
#           elif j != b[-1]:
#             b.pop()
#         else:
#           ans = 'NO'       
    
#     print(ans)

#  SOLUTION
#  '(' 일 때마다 count += 1
#  ')' 일 때 coun count -= 1
#  count 0보다 작아지면 ')' break
#  반복 문 완료 후 count == 0 이면 'YES'

T = int(input())

for i in range(T):
    
    b = list(input())
    ans = 'NO'

    count = 0

    if b[0] == '(':
      while b and count >= 0:
        j = b.pop(0)        
        if j == '(':
          count += 1
        else:
          count -= 1  

      if count == 0:
        ans = 'YES'
    
    print(ans)

