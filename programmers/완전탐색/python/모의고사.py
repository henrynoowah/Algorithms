def solution(answers):
    answer = []

    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    abc = [a,b,c]
    scores = []
    for i in abc:
        count = 0
        for j in range(len(answers)):
            k = i.pop(0)
            if k == answers[j]:
                count += 1
            i.append(k)
        scores.append(count)
        
        
    if max(scores) == scores[0]:
        answer.append(1)
    if max(scores) == scores[1]:
        answer.append(2)
    if max(scores) == scores[2]:
        answer.append(3)
            
    return answer