import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def go(i):
    if dp[i] != -1:
        return dp[i]
    max_val = 0
    for prev in in_graph[i]:
        max_val = max(max_val, go(prev))
    dp[i] = D[i] + max_val
    return dp[i]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    dp = [-1] * (N + 1)
    in_graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split())
        in_graph[y].append(x)
    W = int(input())
    print(go(W))
