import math
from collections import deque, defaultdict

m, group, N, H, parents = None, 0, 0, 0, None
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y, gm):
    global group
    gm[x][y] = group
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and gm[nx][ny] == -1 and abs(m[x][y] - m[nx][ny]) <= H:
                gm[nx][ny] = group
                q.append((nx, ny))
    group += 1


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x == root_y:
        return False
    parents[root_y] = root_x
    return True


def solution(land, height):
    global m, N, H, parents
    m = land
    H, N = height, len(land)
    gm = [[-1 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if gm[x][y] == -1:
                bfs(x, y, gm)
    edges = defaultdict(lambda: math.inf)
    for x in range(N):
        for y in range(N):
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and gm[x][y] != gm[nx][ny]:
                    key = tuple(sorted((gm[x][y], gm[nx][ny])))
                    edges[key] = min(edges[key], abs(m[x][y] - m[nx][ny]))

    ans = 0
    parents = list(range(group))
    cnt = 0
    for u, v in sorted(edges, key=lambda x: edges[x]):
        if not union(u, v):
            continue
        w = edges[(u, v)]
        ans += w
        cnt += 1
        if cnt == group - 1:
            break

    return ans


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
