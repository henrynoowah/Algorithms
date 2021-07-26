def solution(array, commands):
    answer = []

    for i, arr in enumerate(commands):
        
        k = []
        v = arr[2] - 1
        
        for j in range(arr[0]-1,arr[1]):
            
            k.append(array[j])
            k.sort()
            
        answer.append(k[v])
                  
    return answer