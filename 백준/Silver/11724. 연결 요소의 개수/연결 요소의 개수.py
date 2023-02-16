import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
visited = [False]*(N + 1)
graph = [[] for _ in range(N + 1)]
list1 = []
count = 0
def DFS(num, visited, graph):
    visited[num] = True
    for a in graph[num]:
        if not visited[a]:
            DFS(a, visited, graph)
for a in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for a in range(1, N + 1):
    if visited[a]:
        pass
    else:
        DFS(a, visited, graph)
        count += 1
print(count)