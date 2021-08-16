# import re

# def solution(phone_book):
#     answer = True
    
#     while phone_book:

#         v = phone_book.pop(0)
        
#         for i in phone_book:
#             if len(re.findall(v, i)):
#                 return False
    
#     return answer
# 접두어 = 맨 앞 숫자에서만 비교연산을 해야 하기 때문에 틀림


# from collections import deque

# def solution(phone_book):
#     book = deque(sorted(phone_book))
    
#     while(book):
#         v = book.popleft()
        
#         for num in book:
#             if v == num[0:len(v)]:
#                 return False
            
#     return True

# 시간초과가 나오기 때문에 pop(0) 문제인 줄 알고 deque 를 사용했지만 여전히 효율성 테스트 3,4실패
# 이중 for문/ 반복문이 원인이라는 말이 많다


# SOLUTION
def solution(phone_book):
    phone_book.sort()
    # sorting 을 하여 접두어를 가진 문자가 다음 순서로 오게 만든다

    for i in range(1, len(phone_book)):
        numLen = len(phone_book[i-1])
        # 첫번 째 비교값의 숫자의 길이를 가져와 슬라이싱
        if phone_book[i-1] == phone_book[i][0:numLen]:
            return False
            
    return True