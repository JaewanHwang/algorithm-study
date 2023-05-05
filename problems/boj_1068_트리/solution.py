import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = list(map(int, input().split()))
R = int(input())
graph = [[] for _ in range(N)]
for ni, p in enumerate(tree):
    if p == -1:
        root = ni
    else:
        graph[p].append(ni)
if root == R:
    print(0)
    sys.exit(0)
ans = 0
q = deque([root])
while q:
    n = q.popleft()
    cnt = 0
    for c in graph[n]:
        if c != R:
            q.append(c)
            cnt += 1
    if cnt == 0:
        ans += 1
print(ans)
