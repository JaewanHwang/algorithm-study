import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, r1, r2 = map(int, input().split())
graph = [dict() for _ in range(N + 1)]
for _ in range(N - 1):
    x, y, w = map(int, input().split())
    graph[x][y] = w
    graph[y][x] = w

visited = [-1] * (N + 1)
visited[r1] = r1
q = deque([r1])
while q:
    cur = q.popleft()
    if cur == r2:
        break
    for nxt in graph[cur]:
        if visited[nxt] == -1:
            q.append(nxt)
            visited[nxt] = cur
cur = r2
max_path, sum_path = 0, 0
while visited[cur] != cur:
    sum_path += graph[cur][visited[cur]]
    if max_path < graph[cur][visited[cur]]:
        max_path = graph[cur][visited[cur]]
    cur = visited[cur]
print(sum_path - max_path)
