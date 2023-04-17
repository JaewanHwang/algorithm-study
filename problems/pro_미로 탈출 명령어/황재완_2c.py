import sys

sys.setrecursionlimit(10 ** 6)

dx, dy = (1, 0, 0, -1), (0, -1, 1, 0)
num_to_dir = ['d', 'l', 'r', 'u']


def go(x, y, rest):
    global ans
    if rest == 0:
        if (x, y) == (ex, ey):
            ans = ''.join(path)
            return True
        return False
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][rest - 1]:
            path[K - rest] = num_to_dir[d]
            visited[nx][ny][rest - 1] = True
            if go(nx, ny, rest - 1):
                return True
    return False


N, M, K, ex, ey, ans, path, visited = 0, 0, 0, 0, 0, 'impossible', None, None


def solution(n, m, x, y, r, c, k):
    global N, M, K, ex, ey, path, visited
    N, M, K, ex, ey = n, m, k, r - 1, c - 1
    path = [0] * K
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[x - 1][y - 1][K] = True
    go(x - 1, y - 1, K)
    return ans


print(solution(3, 4, 2, 3, 3, 1, 5))
