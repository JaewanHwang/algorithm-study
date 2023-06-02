import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
R, C = map(int, input().split())
m = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = {'o': 0, 'v': 0}


def bfs(x, y):
    cnt = {'o': 0, 'v': 0, '.': 0}
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and m[nx][ny] != '#':
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt[m[nx][ny]] += 1

    if cnt['o'] > cnt['v']:
        ans['o'] += cnt['o']
    else:
        ans['v'] += cnt['v']


for x in range(R):
    for y in range(C):
        if not visited[x][y]:
            bfs(x, y)

print(ans['o'], ans['v'])
