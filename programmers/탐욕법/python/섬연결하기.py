n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
import math
from collections import deque

def solution(n, costs):
    arr = [math.inf for _ in range(n)]
    visited = [False for _ in range(n)]

    queue = deque()
    queue.append(costs[0][0])
    arr[costs[0][0]] = 0

    # print(arr)
    while queue:
        start = queue.popleft()
        visited[start] = True
        for v in costs:
            if v[0] == start and visited[v[1]] == False:
                arr[v[1]] = arr[v[1]] = min(arr[v[1]], v[2])
                queue.append(arr[v[1]])
        
    #     # print(queue)
    
    # # print(arr)

    print(sum(arr))



    # [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    # [[0,1,1],[1,3,1],[0,2,2],[1,2,5],[2,3,8]]
    # answer = 0
    # costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    # link = set([costs[0][0]]) # 연결을 확인하는 집합
    # link = set([0])

    # https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html
    # Kruskal 알고리즘으로 최소 비용 구하기
    # while len(link) != n:
    #     for v in costs:
    #         # 현재위치, 다음위치가 둘 다 이미 set 안에 있을 경우
    #         # 즉 현재위치와 다음위치가 연결이 완료되었을 때를 의미
    #         if v[0] in link and v[1] in link:
    #             continue
    #         # 둘 중 하나만 있을 때, 연결이 성사되지 않았을 때
    #         if v[0] in link or v[1] in link:
    #             # 중복을 자동으로 제거하는 과정 (update)
    #             link.update([v[0], v[1]])
    #             answer += v[2]
    #             break
                
    # return answer

solution(n, costs)