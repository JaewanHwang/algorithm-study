import sys

sys.stdin = open('input.txt')

N = int(input())
m = [[0] * N for _ in range(N)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
priorities = [0] * (N * N + 1)
for _ in range(N * N):
    n, *priority = map(int, input().split())
    priority = set(priority)
    priorities[n] = priority
    candidates = []
    for x in range(N):
        for y in range(N):
            if m[x][y] > 0:
                continue
            like, blank = 0, 0
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if m[nx][ny] in priority:
                        like += 1
                    elif m[nx][ny] == 0:
                        blank += 1
            candidates.append((like, blank, x, y))
    _, _, x, y = max(candidates, key=lambda x: (x[0], x[1], -x[2], -x[3]))
    m[x][y] = n
ans = 0
for x in range(N):
    for y in range(N):
        like = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] in priorities[m[x][y]]:
                like += 1
        ans += 10 ** (like - 1) if like > 0 else 0
print(ans)
