import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

ans = []

graph = []

def bfs(graph, x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 1

    queue = deque([])

    queue.append((x, y))

    graph[x][y] += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= N or ny < 0 or ny >= N):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] += 1
                queue.append((nx, ny))
                cnt += 1

    return cnt

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# visited = [[False] * N for _ in range(N)]
# print(visited)
# print(graph)
# [
#     [0, 1, 1, 0, 1, 0, 0], 
#     [0, 1, 1, 0, 1, 0, 1], 
#     [1, 1, 1, 0, 1, 0, 1], 
#     [0, 0, 0, 0, 1, 1, 1], 
#     [0, 1, 0, 0, 0, 0, 0], 
#     [0, 1, 1, 1, 1, 1, 0], 
#     [0, 1, 1, 1, 0, 0, 0]
# ]  
cnt = 0

for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            ans.append(bfs(graph, x, y))

ans.sort()

print(len(ans))
# print(ans)
# print(graph)
for a in ans:
    print(a)
