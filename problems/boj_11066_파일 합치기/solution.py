import sys

sys.setrecursionlimit(10 ** 4)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    ret = float('inf')
    for k in range(i, j):
        ret = min(ret, go(i, k) + go(k + 1, j) + s[j] - s[i - 1])
    dp[i][j] = ret
    return ret


T = int(input())
for _ in range(T):
    K = int(input())
    a = [0] + list(map(int, input().split()))
    s = [0] * (K + 1)
    for i in range(1, K + 1):
        s[i] = s[i - 1] + a[i]
    dp = [[-1] * (K + 1) for _ in range(K + 1)]
    for i in range(K + 1):
        dp[i][i] = 0
    print(go(1, K))
