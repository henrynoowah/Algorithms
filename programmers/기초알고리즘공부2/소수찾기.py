# first try = 시간초과
def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        if i == 2 or i == 3:
            answer += 1
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
                if j == i - 1 and i % j != 0:
                    answer += 1
        
    return answer

# solution
def prime(num):
    for j in range(2, int(num ** 0.5) +1):
        if num % j == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        if prime(i) == 1:
            answer += 1
                           
        
    return answer
