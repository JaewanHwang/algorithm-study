import sys

sys.stdin = open("input.txt", "r")

T = int(input())
dx, dy = (1, 1, -1, -1), (1, -1, -1, 1)


def go(sx, sy, l1, l2):
    x, y, d = sx, sy, 0
    history = {m[sx][sy]}
    for l in (l1, l2, l1, l2 - 1):
        for _ in range(l):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                return 0
            if m[nx][ny] in history:
                return 0
            history.add(m[nx][ny])
            x, y = nx, ny
        d += 1
    return len(history)


for test_case in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for sx in range(N):
        for sy in range(N):
            for l1 in range(1, N):
                for l2 in range(1, N):
                    if l1 + l2 >= N:
                        break
                    ans = max(ans, go(sx, sy, l1, l2))
    ans = -1 if ans == 0 else ans
    print(f'#{test_case} {ans}')
