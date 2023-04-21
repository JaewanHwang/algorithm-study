import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(M + 1):
            if j + coin > M:
                break
            dp[j + coin] += dp[j]
    ans.append(dp[M])
print(*ans, sep='\n')
