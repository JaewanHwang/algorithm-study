import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(map(int, input().rstrip())) for _ in range(N)]
K = int(input())
ans = 0
for x in range(N):
    zero_cnt = M - sum(m[x])
    now = 0
    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        for nx in range(x, N):
            if m[nx] == m[x]:
                now += 1
    ans = max(ans, now)
print(ans)
