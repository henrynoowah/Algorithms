def solution(priorities, location):
    indexList = [i for i in range(len(priorities))]
    # [0,1,2,3]
    answer = 0
    # highest priority
    maximum = max(priorities)
    
    while indexList:
        index = indexList.pop(0)
        # maximum 보다 우선순위가 낮으면 맨 뒤로 보냄
        if priorities[index] < maximum:
            indexList.append(index)
        
        # 우선순위일 때 answer += 1
        # maximum의 다음 우선순위 지정
        # 우선순위가 location값과 일치하면 answer 반환
        else:
            answer += 1
            priorities[index] = 0
            maximum = max(priorities)
            if index == location:
                return answer
            
    return answer