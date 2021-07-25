#first try

def solution(a, b):
    answer = 0
    list = [a, b]
    
    if a > b:
        list = [b,a]
    elif a == b: 
        return a
    
    for i in range(list[0], (list[1] + 1)):
        answer += i
        
    return answer


# other solution
# 다른사람의 풀이 시간복잡도 0.00ms... 이해하고 싶다..

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2

#  (abs(3-5)+1)*(3+5)//2
# == (abs(-2)+1) * (8) // 2
# == (2 + 1) * 8 // 2
# == 3 * 8 // 2
# == 24 // 2
# == 12  