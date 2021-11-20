import sys
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= N or ny < 0 or ny >= M) or (graph[nx][ny] == 0):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[N-1][M-1]

input = sys.stdin.readline

N, M = map(int, input().split())

x = y = 0

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

print(bfs(x,y))

# [
#     '101111', 
#     '101010', 
#     '101011', 
#     '111011'
# ]
