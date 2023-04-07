import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())
population = list(map(int, input().split()))
adj_list = [[] for _ in range(N)]
for i in range(N):
    line = list(map(lambda x: int(x) - 1, input().split()))
    adj_list[i].extend(line[1:])
ans = -1


def bfs(n, case, visited):
    visited[n] = True
    q = deque([n])
    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if bool(case & 1 << u) == bool(case & 1 << v) and not visited[v]:
                q.append(v)
                visited[v] = True


def simulate(case):
    global ans
    if case == 0 or case == 2 ** N - 1:
        return
    visited = [False] * N
    call = 0
    for n in range(N):
        if not visited[n]:
            if call >= 2:
                return
            bfs(n, case, visited)
            call += 1
    tot = [0] * 2
    for i in range(N):
        tot[bool(case & 1 << i)] += population[i]
    res = abs(tot[0] - tot[1])
    if ans == -1 or 0 <= res < ans:
        ans = res


for case in range(1 << N):
    simulate(case)
print(ans)
