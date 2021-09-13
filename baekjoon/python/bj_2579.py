N = int(input())

steps = [int(input()) for _ in range(N)]
# for i in range(N):
#     steps.append(int(input()))
    
# steps = [10, 20, 15, 25, 10, 20]
# steps = [11, 20, 30, 10, 15, 10, 18]

# def solution(steps):
#     if len(steps) <= 2:
#         return (sum(steps))
#     else:
#         for i in range(len(steps)-1, 2, -1): 
#             answer = steps[i] #20
#             steps[i-2] = answer + max(steps[i-1], steps[i-2])
#             return solution(steps[:i-1])

# print(solution(steps))

def solution(steps):
    if len(steps) <= 2:
        return (sum(steps))
    else:
        for i in range(len(steps)-1, len(steps)-4, -1): 
            answer = steps[i] #20
            steps[i-2] = answer + max(steps[i-1], steps[i-2])
            return solution(steps[:i-1])


print(solution(steps))