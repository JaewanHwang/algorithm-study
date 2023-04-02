import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
N, M, K = map(int, input().split())
balls = {}
for i in range(1, M + 1):
    x, y, m, s, d = map(int, input().split())
    balls[i] = [x - 1, y - 1, m, s, d]  # ri, ci, mi, si, di
new_bi = M + 1
for _ in range(K):
    tm = [[[] for _ in range(N)] for _ in range(N)]
    duplicate_set = set()
    for bi, (x, y, m, s, d) in balls.items():
        nx, ny = (x + dx[d] * s) % N, (y + dy[d] * s) % N
        if tm[nx][ny]:
            duplicate_set.add((nx, ny))
        else:
            balls[bi][:2] = [nx, ny]
        tm[nx][ny].append(bi)

    for x, y in duplicate_set:
        tot_m, tot_s, even_odd = 0, 0, [False] * 2
        for bi in tm[x][y]:
            _, _, m, s, d = balls.pop(bi)
            tot_m += m
            tot_s += s
            even_odd[d % 2] = True
        m, s = tot_m // 5, tot_s // len(tm[x][y])
        tm[x][y] = []
        if m == 0:
            continue
        for d in (0, 2, 4, 6) if not all(even_odd) else (1, 3, 5, 7):
            balls[new_bi] = [x, y, m, s, d]
            tm[x][y].append(new_bi)
            new_bi += 1
    m = tm

ans = sum(m for _, _, m, _, _ in balls.values())
print(ans)
