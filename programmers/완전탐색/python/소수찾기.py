from itertools import permutations

def solution(numbers):
    answer = []                                   
    nums = [i for i in numbers]              
    permutatedL = []
    
#   순열 리스트 만들기
#   0개인 순열은 필요없음 1부터 시작
    for i in range(1, len(numbers)+1):            
        permutatedL += list(permutations(nums, i))  
    
#   순열로 받은 이상한 데이터
#   "".join()으로 문자열 변환 후 숫자로 변환
    arrP = [int(("").join(p)) for p in permutatedL]
#   set()의 mutable값 제거로 반복된 리스트 제거
    arrS = list(set(arrP))

#   소수찾기
    for i in arrS:                           
        if i >= 2:                                
            flag = True            
            for j in range(2,int(i**0.5) + 1):       
                if i % j == 0:                       
                    flag = False
                    break
            if flag:
                answer.append(i)
                

    return len(answer) 