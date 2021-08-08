from collections import deque

T = int(input())
C = int(input())
infected = [0] * (T + 1)

virus = 0

graph = [[0]*(T+1) for _ in range(T+1)]
# print(graph)

for i in range(C):

    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1


# [[0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 1, 0, 0, 1, 0, 0], 
# [0, 1, 0, 1, 0, 1, 0, 0], 
# [0, 0, 1, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 1], 
# [0, 1, 1, 0, 0, 0, 1, 0], 
# [0, 0, 0, 0, 0, 1, 0, 0], 
# [0, 0, 0, 0, 1, 0, 0, 0]]


def bfs(virus, infected):

    count = 0

    queue = deque()
    queue.append(virus)
    infected[virus] = 1

    while queue:
        virus = queue.popleft()

        for i in range(1, (T + 1)):

            if graph[virus][i] == 1 and infected[i] == 0:
                queue.append(i)
                count += 1
                infected[i] = 1
        
    print(count)

bfs(1, infected)