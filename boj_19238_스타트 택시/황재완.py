import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M, fuel = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
x, y = map(lambda x: int(x) - 1, input().split())
taxi = [x, y, fuel]
customer_map = {i: list(map(lambda x: int(x) - 1, input().split())) for i in range(1, M + 1)}

while customer_map:
    d = [[-1] * N for _ in range(N)]
    tx, ty, fuel = taxi
    q = deque([(tx, ty)])
    d[tx][ty] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

    candidate = []
    for customer_num in customer_map:
        sx, sy, _, _ = customer_map[customer_num]
        if d[sx][sy] == -1:
            print(-1)
            sys.exit(0)
        candidate.append((d[sx][sy], sx, sy, customer_num))
    dist, sx, sy, customer_num = min(candidate)
    ex, ey = customer_map[customer_num][2], customer_map[customer_num][3]
    q = deque([(sx, sy)])
    d = [[-1] * N for _ in range(N)]
    d[sx][sy] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0 and d[nx][ny] == -1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))
    if d[ex][ey] == -1:
        print(-1)
        sys.exit(0)
    total = dist + d[ex][ey]
    if fuel >= total:
        taxi = [ex, ey, fuel - total + d[ex][ey] * 2]
    else:
        print(-1)
        sys.exit(0)
    customer_map.pop(customer_num)
print(taxi[2])
