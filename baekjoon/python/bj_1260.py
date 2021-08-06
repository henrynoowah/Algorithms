# arr = [int(v) for v in list(input().split())]

# N = arr[0] # 4
# M = arr[1] # 5
# V = arr[2] # 1
from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
visited = [0] * (N + 1)
# [False, False, False, False, False]

# print(graph)
# print(visited)


for i in range(M):

    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

    # [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]

def dfs(V):
    visited[V] = 1
    print(V, end = " ")
    # 방문한 값은 True로 변환 후 출력
    for i in range(1, (N + 1)):
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)
    # 1 부터 N 까지의 길이의 반복문
    # True가 된 이후부터 메소드를 다시 시작하는 시작점인 i 를 재귀함수를 통해 파라미터 반환

def bfs(V):

    queue = deque()
    queue.append(V)
    visited[V] = 1

    while queue:
        V = queue.popleft()
        print(V, end = " ")
        # 시작점 V 출력

        for i in range(1, (N + 1)):
            # 1 ~ 4 까지
            if visited[i] == 0 and graph[V][i] == 1:
                # [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
                queue.append(i)
                visited[i] = 1


# dfs(V)
dfs(V)
visited = [0] * (N + 1)
print()
bfs(V)

# https://kils-log-of-develop.tistory.com/169