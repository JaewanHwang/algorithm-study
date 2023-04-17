import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
m = [[0] * N for _ in range(N)]
like = [0 for _ in range(N * N + 1)]
for _ in range(N * N):
    n, *l = map(int, input().split())
    like[n] = set(l)
    candidate_list = []
    for x in range(N):
        for y in range(N):
            if m[x][y] == 0:
                cnt_like, cnt_blank = 0, 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if m[nx][ny] in l:
                            cnt_like += 1
                        elif m[nx][ny] == 0:
                            cnt_blank += 1
                candidate_list.append((cnt_like, cnt_blank, x, y))
    _, _, x, y = max(candidate_list, key=lambda x: (x[0], x[1], -x[2], -x[3]))
    m[x][y] = n
ans = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and m[nx][ny] in like[m[x][y]]:
                cnt += 1
        ans += 10 ** (cnt - 1) if cnt > 0 else 0
print(ans)
