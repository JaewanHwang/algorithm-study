import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]


def go(x, y, cnt, tot):
    global ans
    if cnt == 4:
        ans = max(ans, tot)
        return
    for k in range(1, 4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            go(nx, ny, cnt + 1, tot + m[nx][ny])
            visited[nx][ny] = False


def go2(x, y):
    global ans
    block = [0] * 4
    block_cnt = 0
    tot = m[x][y]

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            tot += m[nx][ny]
            block[k] = m[nx][ny]
            block_cnt += 1

    if block_cnt == 4:
        for k in range(4):
            ans = max(ans, tot - block[k])
    elif block_cnt == 3:
        ans = max(ans, tot)


ans = 0
visited = [[False] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        visited[x][y] = True
        go(x, y, 1, m[x][y])
        visited[x][y] = False
        go2(x, y)

print(ans)

# def go(x, y, cnt, tot, candidates):
#     global ans
#     if cnt == 4:
#         ans = max(ans, tot)
#         return
#     candidates = set(candidates)
#     visited[x][y] = True
#     candidates.remove((x, y))
#
#     for k in range(3):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
#             candidates.add((nx, ny))
#
#     for nx, ny in candidates:
#         go(nx, ny, cnt + 1, tot + m[x][y], candidates)
#     visited[x][y] = False
#
#
# visited = [[False] * M for _ in range(N)]
# ans = 0
# for x in range(N):
#     for y in range(M):
#         go(x, y, 0, 0, {(x, y)})
#
# print(ans)
