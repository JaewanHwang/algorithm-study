import sys

sys.stdin = open("input.txt", "r")

T = int(input())
change_dir = [0, 0, 3, 1, 2]
dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)


def simulate(m):
    for _ in range(M):
        tm = [[0] * N for _ in range(N)]
        history = dict()
        for x in range(N):
            for y in range(N):
                if not m[x][y]:
                    continue
                s, d = m[x][y]
                nx, ny = x + dx[d], y + dy[d]
                if 1 <= nx < N - 1 and 1 <= ny < N - 1:
                    if tm[nx][ny]:
                        ns, nd = tm[nx][ny][0] + s, tm[nx][ny][1] if history[(nx, ny)] > s else d
                        history[(nx, ny)] = max(history[(nx, ny)], s)
                    else:
                        ns, nd = s, d
                        history[(nx, ny)] = s
                else:
                    ns, nd = s // 2, 3 - d
                    if ns == 0:
                        continue
                tm[nx][ny] = [ns, nd]
        m = tm
    ans = 0
    for x in range(N):
        for y in range(N):
            if m[x][y]:
                ans += m[x][y][0]
    return ans


for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    m = [[0] * N for _ in range(N)]
    for _ in range(K):
        x, y, s, d = map(int, input().split())
        m[x][y] = [s, change_dir[d]]
    print(f'#{test_case} {simulate(m)}')
