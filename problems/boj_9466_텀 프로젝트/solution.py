import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (n + 1)
    tot = n
    for x in range(1, n + 1):
        if visited[x]:
            continue
        q = deque([x])
        visited[x] = True
        history = {x: 0}
        while q:
            now = q.popleft()
            next = arr[now - 1]
            if visited[next]:
                if next in history:
                    tot -= len(history) - history[next]
                break
            else:
                q.append(next)
                visited[next] = True
                history[next] = len(history)
    ans.append(tot)

print(*ans, sep='\n')
