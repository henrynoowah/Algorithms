def solution(n):
    answer = 0
    
    nums = [i for i in f'{n}']
    
    for i in nums:
        answer += int(i)
        
    return answer