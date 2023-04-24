import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
N, *percentage = map(int, input().split())
ans = 0


def go(i, tot, path, x, y):
    global ans
    if i == N:
        ans += tot
        return
    for k in range(4):
        key = x + dx[k], y + dy[k],
        if key in path or percentage[k] == 0:
            continue
        path.add(key)
        go(i + 1, tot * percentage[k], path, *key)
        path.remove(key)


path = {(0, 0)}
go(0, 1, path, 0, 0)
ans = ans / (100 ** N)
print(ans)
