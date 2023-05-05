import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
m = [list(input().rstrip()) for _ in range(N)]
d = [(i, j) for i in range(-9, 10) for j in range(-9, 10)]
squared_set = set()
i = 0
while i * i < 1_000_000_000:
    squared_set.add(i * i)
    i += 1


def go(x, y, k):
    global ans
    cur = []
    dx, dy = d[k]
    while 0 <= x < N and 0 <= y < M:
        cur.append(m[x][y])
        n_cur = int(''.join(cur))
        if n_cur in squared_set:
            ans = max(ans, n_cur)
        if dx == dy == 0:
            return
        x, y = x + dx, y + dy


ans = -1
for x in range(N):
    for y in range(M):
        for k in range(len(d)):
            go(x, y, k)

print(ans)
