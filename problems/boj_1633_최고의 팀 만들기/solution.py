import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
a = []
while True:
    line = input()
    if not line:
        break
    a.append(tuple(map(int, line.split())))

dp = [[0] * 16 for _ in range(16)]

for w, b in a:
    for i in range(15, -1, -1):
        for j in range(15, -1, -1):
            if i >= 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + w)
            if j >= 1:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + b)
print(dp[15][15])
