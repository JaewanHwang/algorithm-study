import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
sdx, sdy = (-1, 0, 1, 0), (0, -1, 0, 1)
M, S = map(int, input().split())
m = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    x, y, d = map(lambda x: int(x) - 1, input().split())
    m[x][y].append(d)
sx, sy = map(lambda x: int(x) - 1, input().split())
s = [[0] * 4 for _ in range(4)]
max_cnt, max_path = -1, None
visited = [[0] * 4 for _ in range(4)]


def go(i, x, y, cnt, visited, path, nm):
    global max_path, max_cnt
    if visited[x][y] == 1:
        cnt += len(nm[x][y])
    if i == 3:
        if cnt > max_cnt:
            max_cnt = cnt
            max_path = path[:]
        return
    for d in range(4):
        nx, ny = x + sdx[d], y + sdy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            path[i] = d
            visited[nx][ny] += 1
            go(i + 1, nx, ny, cnt, visited, path, nm)
            visited[nx][ny] -= 1


def simulate():
    global max_cnt, max_path, sx, sy
    # 1. 상어가 모든 물고기에게 복제 마법을 시전한다.
    nm = [[[] for _ in range(4)] for _ in range(4)]
    # 2. 모든 물고기가 한 칸 이동한다.
    for x in range(4):
        for y in range(4):
            for d in m[x][y]:
                for i in range(8):
                    nd = (d - i) % 8
                    nx, ny = x + dx[nd], y + dy[nd]
                    if 0 <= nx < 4 and 0 <= ny < 4 and (sx, sy) != (nx, ny) and s[nx][ny] == 0:
                        nm[nx][ny].append(nd)
                        break
                else:
                    nm[x][y].append(d)
    # 3. 상어가 연속해서 3칸 이동한다.
    max_cnt, max_path = -1, [0] * 3
    go(0, sx, sy, 0, visited, [0] * 3, nm)

    for d in max_path:
        sx, sy = sx + sdx[d], sy + sdy[d]
        if len(nm[sx][sy]) > 0:
            s[sx][sy] = 3
            nm[sx][sy] = []

    # 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    for x in range(4):
        for y in range(4):
            if s[x][y] > 0:
                s[x][y] -= 1

    # 5. 1에서 사용한 복제 마법이 완료된다.
    for x in range(4):
        for y in range(4):
            m[x][y].extend(nm[x][y])


for _ in range(S):
    simulate()
ans = sum(sum(map(lambda x: len(x), row)) for row in m)
print(ans)
