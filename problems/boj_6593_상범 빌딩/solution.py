import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline
ans = []
dl, dr, dc = (0, 0, 0, 0, -1, 1), (0, 0, 1, -1, 0, 0), (1, -1, 0, 0, 0, 0)


def find_start():
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if m[l][r][c] == 'S':
                    return l, r, c


while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    m = []
    for _ in range(L):
        m.append([list(input().rstrip()) for _ in range(R)])
        input()
    d = [[[-1] * C for _ in range(R)] for _ in range(L)]
    sl, sr, sc = find_start()
    d[sl][sr][sc] = 0
    q = deque([(sl, sr, sc)])

    while q:
        l, r, c = q.popleft()
        if m[l][r][c] == 'E':
            ans.append(f'Escaped in {d[l][r][c]} minute(s).')
            break
        for k in range(6):
            nl, nr, nc = l + dl[k], r + dr[k], c + dc[k]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and m[nl][nr][nc] != '#' and d[nl][nr][nc] == -1:
                d[nl][nr][nc] = d[l][r][c] + 1
                q.append((nl, nr, nc))
    else:
        ans.append('Trapped!')

print('\n'.join(ans))
