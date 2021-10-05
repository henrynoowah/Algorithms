from collections import deque
import sys
sys.setrecursionlimit(100000)
# https://www.acmicpc.net/board/view/35897

input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            dfs(i)

N , M = map(int, input().split())

visited = [0 for _ in range(N+1)]
visited[0] = 1
cnt = 0


arr= deque([[] for _ in range(N+1)])
# print(arr)
for _ in range(M):
    u, v = map(int, input().split())
    # arr[u][v] = arr[v][u] = 1

    arr[u].append(v)
    arr[v].append(u)

# [[], 
# [2, 5], 
# [1, 5],
# [4],
# [3, 6],
# [2, 1], 
# [4]]
# print(arr)

for j in range(1, N+1):
    if(visited[j] == 0):
        dfs(j)
        cnt += 1


print(cnt)    
