import sys
import math
import heapq

input = sys.stdin.readline
V, E = map(int, input().rstrip().split())
K = int(input())

node = [[] for _ in range(V + 1)]
dist = [math.inf for _ in range(V + 1)]

dist[K] = 0

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    node[u].append([v, w])
    
# print(node)
# 0 : [[], 
# 1 : [[2, 2], [3, 3]], 
# 2 : [[4, 3], [5, 4]], 
# 3 : [[6, 4]], 
# 4 : [], 
# 5 : [[1, 1]]]

heap = []
heapq.heappush(heap, [0, K])

while heap:
    d, now = heapq.heappop(heap)
    for next in node[now]:
        cnt = d + next[1]
        if dist[next[0]] > cnt:
            dist[next[0]] = cnt
            heapq.heappush(heap, [cnt, next[0]])

dist = list(map(lambda x : 'INF' if x == math.inf else x, dist))

for i in range(1, len(dist)):
    print(dist[i])
