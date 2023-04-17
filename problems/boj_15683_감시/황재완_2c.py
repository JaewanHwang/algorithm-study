import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
dir_map = {
    1: [(1,), 4],
    2: [(1, 3), 2],
    3: [(0, 1), 4],
    4: [(0, 1, 3), 4],
    5: [(0, 1, 2, 3), 1]
}


def simulate():
    global ans
    tm = [row[:] for row in m]
    monitored_area = 0
    for ci, (cx, cy) in enumerate(cctvs):
        for d in cctv2dir[ci]:
            x, y = cx, cy
            while True:
                nx, ny = x + dx[d], y + dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= M or tm[nx][ny] == 6:
                    break
                if tm[nx][ny] == 0:
                    tm[nx][ny] = -2
                    monitored_area += 1
                x, y = nx, ny

    ans = min(ans, BLANK_CNT - monitored_area)


def go(ci):
    if ci == len(cctvs):
        simulate()
        return
    dirs, cnt_all_state = dir_map[m[cctvs[ci][0]][cctvs[ci][1]]]
    for k in range(cnt_all_state):
        cctv2dir[ci] = list(map(lambda x: (x + k) % 4, dirs))
        go(ci + 1)


N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
BLANK_CNT = 0
cctvs = []

for x in range(N):
    for y in range(M):
        if 1 <= m[x][y] <= 5:
            cctvs.append((x, y))
        elif m[x][y] == 0:
            BLANK_CNT += 1

cctv2dir = [0] * len(cctvs)
ans = N * M
go(0)
print(ans)
