import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

def dfs(x, y, graph):

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    graph[x][y] = 0

    for i in range(8):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                dfs(nx, ny , graph)

            
while True:
    w, h = list(map(int, input().split()))
    cnt = 0

    if w == 0 and h == 0:
        break
    
    graph = []

    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j, graph)
                cnt += 1
    
    print(cnt)
        
