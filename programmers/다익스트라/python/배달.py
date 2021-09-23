import math
import heapq

def solution(N, road, K):
    heap = []
    # 현 위치에서 연결된 관계 그래프 형태 배열 만들기
    dist = [math.inf for _ in range(N+1)]
    # 방문기록
    delivery = [[] for _ in range(N+1)]

    for x, y, z in road:
        delivery[x].append([y, z])
        delivery[y].append([x, z])

    # [[], 
    # [[2, 1], [4, 2]], 
    # [[1, 1], [3, 3], [5, 2]], 
    # [[2, 3], [5, 1]], 
    # [[1, 2], [5, 2]], 
    # [[2, 2], [3, 1], [4, 2]]]    
    # return answer

    # 시작지점인 1 : 0으로 초기화
    dist[1] = 0

    # 우선순위큐에 방문기록 저장 [1, 0]
    # 설명 : 1번동네까지 거리 = 0
    # heapq.heappush(heap, [1, dist[1]])
    heap.append([1, dist[1]])

    while len(heap) > 0:
        loc = heapq.heappop(heap)
        # deliver[loc[0]] =  [[2, 1], [4, 2]]
        for next in delivery[loc[0]]:
            # print(f'loc[0] : {next}')
            
            if dist[next[0]] > loc[1] + next[1]:
                dist[next[0]] = loc[1] + next[1]
                # heapq.heappush(heap, [next[0], dist[next[0]]])
                heap.append([next[0], dist[next[0]]])
    
    count = 0
    for i in range(1, len(dist)):
        # print(f'count : {i}')
        if dist[i] <= K:
            count += 1
            
    return count

