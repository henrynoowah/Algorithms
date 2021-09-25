n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

import math
import heapq
def solution(n, edge):
    answer = 0

    node = [[] for _ in range(n+1)]

    for x, y in edge:
        node[x].append(y)
        node[y].append(x)
    
    print(node)

    # [[], 
    # 1: [3, 2], 
    # 2: [3, 1, 4, 5], 
    # 3: [6, 4, 2, 1], 
    # 4: [3, 2], 
    # 5: [2], 
    # 6: [3]]

    dist = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    visited[0] = True
    visited[1] = True
    start = 1

    heap = []
    heapq.heappush(heap, [0, start])

    while False in visited:
        d, now = heapq.heappop(heap)
        print(visited)
        for next in node[now]:
            cnt = d + 1
            if visited[next] == False:
                visited[next] = True
                dist[next] = cnt
                heapq.heappush(heap, [cnt, next])
            if visited[next] == True:
                continue
    
    print(dist)

    dist = list(filter(lambda x : x == max(dist), dist))
    print(dist)

    return answer


solution(n, vertex)
