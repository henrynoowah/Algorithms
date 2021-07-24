import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = []
    
    for i in range(n):
        pLeft = 100 - progresses[i]
        daysLeft = math.ceil(pLeft / speeds[i])
        days.append(daysLeft)
        
    while days and len(days) != 0:
        count = 1
        d = days.pop(0)
        while d >= days[0]:
            count += 1
            days.pop(0)
            
        answer.append(count)   
         
    return answer