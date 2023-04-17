import sys

sys.stdin = open("input.txt", "r")


def check(x, max_cons, last_cons):
    res = True
    for y in range(W):
        if x - 1 >= 0 and m[x - 1][y] == m[x][y]:
            last_cons[y] += 1
        else:
            last_cons[y] = 1
        max_cons[y] = max(max_cons[y], last_cons[y])
        if max_cons[y] >= K:
            continue
        else:
            res = False
    return res


def go(i, n, max_cons, last_cons):
    global ans
    if n >= ans:
        return
    max_cons, last_cons = max_cons[:], last_cons[:]
    if i > 0 and check(i - 1, max_cons, last_cons):
        ans = min(ans, n)
    if i == len(m):
        return
        # 색을 안바꿀 경우
    go(i + 1, n, max_cons, last_cons)
    # 색을 바꿀 경우
    original_row = m[i][:]
    for c in range(2):
        m[i] = [c] * W
        go(i + 1, n + 1, max_cons, last_cons)
        m[i] = original_row


T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(D)]
    ok = False

    ans = D
    go(0, 0, [1] * W, [1] * W)
    print(f'#{test_case} {ans}')
