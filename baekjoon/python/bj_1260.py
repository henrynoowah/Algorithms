arr = [int(v) for v in list(input().split())]

N = arr[0] # 4
M = arr[1] # 5
V = arr[2] # 1

graph = [[0] * (M) for _ in range(M)]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
visited = [False for _ in range(M)]
# [False, False, False, False, False]

# print(graph)
# print(visited)


for i in range(M):

    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

    # [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 1, 1, 0]]

    # print(graph)

def dfs(V):
    visited[V] = True
    print(V, end = " ")
    # 방문한 값은 True로 변환 후 출력
    for i in range(1, M):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)
    # 1 부터 N 까지의 길이의 반복문

def bfs(V):
    visited[V] = False
    # dfs에서 True가 된 값을 False로 재정의
    queue = [V]
    # fase 재정의 후 큐에 반환
    while queue:
        V = queue.pop(0)
        print(V, end = " ")
        for i in range(1, M):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False

    for i in range(1, M):
        if graph[V][i] == 1:
            visited[i] = True


# dfs(V)
dfs(V)
print()
bfs(V)

#   [[1, 2], [1, 3], [1, 4]]
#   [[2, 4], [3, 4]]

# dequeue rotate 사용??