import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0, -1, 1, 1, -1), (0, 0, -1, 1, 1, 1, -1, -1)
H, W = map(int, input().split())
m = [list(map(lambda x: int(x) if x.isdigit() else x, input().rstrip())) for _ in range(H)]
d = [[-1] * W for _ in range(H)]
cnt = [[0] * W for _ in range(H)]
q = deque()
for x in range(H):
    for y in range(W):
        if m[x][y] == '.':
            d[x][y] = 0
            q.append((x, y))
while q:
    x, y = q.popleft()
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < H and 0 <= ny < W and d[nx][ny] == -1:
            if m[nx][ny] == '.':
                q.appendleft((nx, ny))
                d[nx][ny] = d[x][y]
            else:
                cnt[nx][ny] += 1
                if cnt[nx][ny] >= m[nx][ny]:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    m[nx][ny] = '.'

ans = max(max(row) for row in d)
print(ans)

# # DEBUG - START
# for row in m:
#     print(row)
# print()
# for row in d:
#     print(row)
# print()
# # DEBUG - END
