import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [tuple(map(int, input().split())) for _ in range(n + 2)]
    q = deque([graph[0]])
    visited = {position: False for position in graph}
    visited[graph[0]] = True
    while q:
        x, y = q.popleft()
        for nx, ny in graph:
            if abs(nx - x) + abs(ny - y) <= 1000 and not visited[(nx, ny)]:
                visited[(nx, ny)] = True
                q.append((nx, ny))

    if visited[graph[-1]]:
        print('happy')
    else:
        print('sad')
