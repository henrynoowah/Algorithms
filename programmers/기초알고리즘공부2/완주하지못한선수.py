def solution(participant, completion)
    dic = {}
    
#   완주 정보 (dictionary) 전환
#   {leo = 1, kiki = 1, eden  1}
    for i in participant
        if i in dic
            dic[i] += 1            
        else
            dic[i] = 1


    for i in completion
        if i in dic
            dic[i] -= 1
#   {leo = 1, kiki = 0, eden  0}    

    for i in dic
        if dic[i] == 1
            return i