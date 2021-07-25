def solution(priorities, location):
    indexList = [i for i in range(len(priorities))]
    # [0,1,2,3]
    answer = 0
    maximum = max(priorities)
    
    while True:
        index = indexList.pop(0)
        if priorities[index] < maximum:
            indexList.append(index)
        else:
            answer += 1
            priorities[index] = 0
            maximum = max(priorities)
            if index == location:
                return answer
            
    return answer