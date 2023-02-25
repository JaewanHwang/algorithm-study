import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    board[ri - 1][ci - 1].append([mi, si, di])

for _ in range(K):
    tboard = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not board[x][y]:
                continue
            for m, s, d in board[x][y]:
                nx, ny = (x + s * dx[d]) % N, (y + s * dy[d]) % N
                tboard[nx][ny].append([m, s, d])

    for x in range(N):
        for y in range(N):
            if len(tboard[x][y]) < 2:
                continue
            total_m, total_s, odd, even = 0, 0, False, False
            for m, s, d in tboard[x][y]:
                total_m += m
                total_s += s
                if d % 2 == 0:
                    even = True
                else:
                    odd = True
            nm = total_m // 5
            if nm == 0:
                tboard[x][y] = []
                continue
            ns = total_s // len(tboard[x][y])
            nds = (0, 2, 4, 6) if odd ^ even else (1, 3, 5, 7)
            tboard[x][y] = [[nm, ns, nd] for nd in nds]
    board = tboard

ans = 0
for x in range(N):
    for y in range(N):
        for m, _, _ in board[x][y]:
            ans += m
print(ans)
