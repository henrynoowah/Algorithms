# import sys
# import math
# import heapq

# N, M, K, X = map(int, sys.stdin.readline().rstrip().split())

# dist = [math.inf for _ in range(N+1)]
# location = []

# for _ in range(M):
#     input = list(map(int, sys.stdin.readline().rstrip().split()))
#     location.append(input)
# # print(location)
# dist[X] = 0
# # print(dist)
# heap = []
# heapq.heappush(heap, [0, X])
# # print(heap)
# #  [0, 0, 0, 0, 0]

# while len(heap) > 0:
#     d, now = heapq.heappop(heap)
#     for loc in location:
#         if loc[0] == now:
#             dist[loc[1]] = min(dist[loc[1]], d + 1)
#             heapq.heappush(heap, [dist[loc[1]], loc[1]])

#     # print(f'heap : {heap}')
# # print(dist)

# if K not in dist:
#     print(-1)
#     exit()
# else:
#     for i in range(len(dist)):
#         if dist[i] == K:
#             print(i)

# 위의 답은 시간초과가 나온다
# https://sojeong-lululala.tistory.com/28


import sys
import math
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

location = []
dist = [math.inf] * (N+1)
dist[X] = 0

location = [[] for _ in range(N+1)]

for _ in range(M):
    num = list(map(int, input().split()))
    location[num[0]].append(num[1])

print(location)

heap = []
heapq.heappush(heap, [0, X])
# 반복문에서 시간초과
# heap index에 어떤게 먼저 들어가는지도 중요하다는 것을 뼈저리게 느낀다
while heap:
    d, now = heapq.heappop(heap)
    for loc in location[now]:
        cnt = d + 1
        if d < dist[loc]:
            dist[loc] = cnt
            heapq.heappush(heap, [cnt, loc])

result = []

for i in range(len(dist)):
    if dist[i] == K:
        result.append(i)
if(len(result) == 0):
    print(-1)
else:
    result.sort()
    for j in result:
        print(j)