# first try - 효울성 실패
# 기초 안풀고 stack 문제 풀고 와서 하니까 이렇게밖에 생각이 안된다....

def solution(arr):
    answer = []
    
    answer.append(arr.pop(0))
    
    while arr:
        if answer[-1] != arr[0]:
            answer.append(arr.pop(0))
        else:
            arr.pop(0)
           
    return answer


# solution

def solution(arr):
    answer = []
    
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
            
    return answer

# 효율성 테스트 말고는 처리속도가 비슷한데 왜 첫 번 째 솔루션은 효율성 테스트에서 떨어질까?