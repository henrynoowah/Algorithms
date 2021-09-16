n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    answer = [1 for _ in range(n)]
    # [1, 1, 1, 1, 1]
    for i in lost:
        answer[i-1] -= 1
    for i in reserve:
        answer[i-1] += 1

    for i in range(n):
        student = answer[i]

        # 유니폼을 2개 가진 학생들만 확인
        # index out of range를 더 깔끔하게 할 방법이 없을까...?
        if student == 2:
            if i == 0:
                if answer[i + 1] == 0:
                    answer[i] -= 1
                    answer[i + 1] += 1
            elif i != 0 and i < n-1:
                if answer[i - 1] == 0 or answer[i + 1] == 0:
                    answer[i] -= 1
                    answer[i + (-1 if answer[i-1] == 0 else 1)] += 1
            elif i == n-1:
                if answer[i - 1] == 0:
                    answer[i] -= 1
                    answer[i - 1] += 1
    
    # return answer
    answer = filter(lambda x : x > 0, answer)
    return len(list(answer))

solution(n, lost, reserve)