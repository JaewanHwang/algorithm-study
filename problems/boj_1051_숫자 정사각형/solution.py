import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().rstrip())) for _ in range(N)]
ans = 0
for l in range(1, min(N, M) + 1):
    for x in range(N - l + 1):
        for y in range(M - l + 1):
            if m[x][y] == m[x + l - 1][y] == m[x][y + l - 1] == m[x + l - 1][y + l - 1]:
                ans = max(ans, l)
print(ans * ans)
