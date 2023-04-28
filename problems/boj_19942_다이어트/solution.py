import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
ans = [float('inf'), [N] * N]
pivot = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(N)]
now = [0] * 4
selected = []


def check():
    for i in range(4):
        if now[i] < pivot[i]:
            return False
    return True


def go(i, cost):
    global ans
    if cost > ans[0]:
        return
    if i == N:
        if not check():
            return
        if ans[0] >= cost:
            if cost < ans[0]:
                ans[1] = sorted(selected)
            else:
                ans[1] = min(ans[1], sorted(selected))
            ans[0] = cost
        return
    for j in range(4):
        now[j] += m[i][j]
    selected.append(i + 1)
    go(i + 1, cost + m[i][-1])
    for j in range(4):
        now[j] -= m[i][j]
    selected.pop()
    go(i + 1, cost)


go(0, 0)
print(ans[0] if ans[0] != float('inf') else -1)
if ans[0] != float('inf'):
    print(*ans[1])
