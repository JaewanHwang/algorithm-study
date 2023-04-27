import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
graph1 = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]
cnt1 = [set() for _ in range(N + 1)]
cnt2 = [set() for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph1[u].append(v)
    graph2[v].append(u)


def go(u, graph, cnt):
    if cnt[u]:
        return cnt[u]
    for v in graph[u]:
        cnt[u] |= go(v, graph, cnt) | {v, }
    return cnt[u]


for n in range(1, N + 1):
    if not cnt1[n]:
        go(n, graph1, cnt1)
    if not cnt2[n]:
        go(n, graph2, cnt2)

ans = 0
THRESHOLD = N // 2
for i in range(1, N + 1):
    if len(cnt1[i]) > THRESHOLD or len(cnt2[i]) > THRESHOLD:
        ans += 1
print(ans)
