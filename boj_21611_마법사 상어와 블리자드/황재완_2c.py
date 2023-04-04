import sys
from collections import deque

sys.stdin = open('input.txt')
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
change_dir = (0, 2, 0, 3, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
ans = [0] * 4
sx, sy = N // 2, N // 2


def move_and_bomb():
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    q = deque()
    x, y, d = sx, sy - 1, 3
    while x + y >= 0:
        visited[x][y] = True
        if m[x][y] > 0:
            q.append(m[x][y])
            m[x][y] = 0
        nd = (d + 1) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if visited[nx][ny]:
            nd = d
            nx, ny = x + dx[nd], y + dy[nd]
        x, y, d = nx, ny, nd

    original_q = q
    new_q = deque()
    while True:
        original_len = len(original_q)
        last, cnt = 0, 0
        while original_q:
            cur = original_q.popleft()
            if cur == last:
                cnt += 1
            else:
                if cnt >= 4:
                    ans[last] += cnt
                    for _ in range(cnt):
                        new_q.pop()
                last = cur
                cnt = 1
            new_q.append(cur)
        if cnt >= 4:
            ans[last] += cnt
            for _ in range(cnt):
                new_q.pop()
        if original_len == len(new_q):
            return new_q
        original_q = new_q
        new_q = deque()


def mutate(q):
    if not q:
        return q
    new_q = deque()
    last, cnt = q.popleft(), 1
    while q:
        cur = q.popleft()
        if last == cur:
            cnt += 1
        else:
            new_q.append(cnt)
            new_q.append(last)
            cnt = 1
            last = cur
    new_q.append(cnt)
    new_q.append(last)
    return new_q


def insert(q):
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    x, y, d = sx, sy - 1, 3
    while x + y >= 0 and q:
        visited[x][y] = True
        m[x][y] = q.popleft()
        nd = (d + 1) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if visited[nx][ny]:
            nd = d
            nx, ny = x + dx[nd], y + dy[nd]
        x, y, d = nx, ny, nd


def simulate(di, si):
    for k in range(1, si + 1):
        nsx, nsy = sx + dx[di] * k, sy + dy[di] * k
        m[nsx][nsy] = 0
    q = move_and_bomb()
    q = mutate(q)
    insert(q)


for _ in range(M):
    di, si = map(int, input().split())
    di = change_dir[di]
    simulate(di, si)

ans = sum(i * ans[i] for i in range(1, 4))
print(ans)
