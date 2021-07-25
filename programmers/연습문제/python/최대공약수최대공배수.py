def solution(n, m):
    answer = []
    
    for i in range (m, 0, -1):
        if m % i == 0 and n % i == 0:
                answer.append(i)
                break;
                
                
    j = 1
    while True:
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
        j += 1
            
                
    return answer