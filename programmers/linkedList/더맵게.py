import heapq
from collections import deque
scoville = [1, 2, 3, 9, 10, 12]
K = 7

# # 정확성 테스트 100% 효율성 테스트 0% ㅠㅠ
# # 정렬 혹은 index값을 사용하기 때문에 그런거 같음
# def solution(scoville, K):
#     cnt = 0
#     if min(scoville) > K:
#         return 0

#     while min(scoville) < K:
#         scoville.sort()
#         a = heapq.heappop(scoville)
#         if scoville:
#             scoville[0] = a + (scoville[0] * 2)
#             cnt += 1
#         else:
#             return -1

#     return cnt


# Soulution
# 효율성 테스트 실패 원인 
# heapify 를 사용하면 heap 구조상 내림차순 정렬이 됨
# * scoville[0]이 항상 가장 작은 수이기
# * min()를 추가로 사용하게 되면 이중작업을 하게되며 비효율적

# sort()를 사용해도 효율성테스트를 통과
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, (a + (b * 2)))
        cnt += 1
    
    if scoville[0] >= K:
        return cnt
    else:
        return -1

solution(scoville, K)
