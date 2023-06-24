import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def go(node, depth):
    global cnt
    visited[node] = True
    child_cnt = 0
    for child in tree[node]:
        if not visited[child]:
            child_cnt += 1
            go(child, depth + 1)
    if child_cnt == 0:
        cnt += depth
        return


cnt = 0
visited = [False] * (N + 1)
go(1, 0)
if cnt % 2 == 0:
    print('No')
else:
    print('Yes')
