def solution(n):
    answer = []
    n = list(f'{n}')
    
    for i in range(len(n) - 1, -1, -1):
        answer.append(int(n[i]))
    
    
    return answer


#better solution by someone else
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
