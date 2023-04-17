import sys

sys.setrecursionlimit(10 ** 6)


def go(l, r, tree, visited):
    cur = (l + r) // 2
    if cur - l != r - cur:
        return
    if tree[cur] == '1':
        visited[cur] = True
    else:
        return
    if l == r:
        return
    go(l, cur - 1, tree, visited)
    go(cur + 1, r, tree, visited)


def solution(numbers):
    ans = [0] * len(numbers)
    for ni, number in enumerate(numbers):
        number = bin(number)[2:]
        for i, c in enumerate(number):
            if i > len(number) // 2:
                break
            if c == '0':
                continue
            failed = False
            size = (len(number) - 1 - i) * 2 + 1
            tree = number.zfill(size)
            visited = [False] * size
            go(0, size - 1, tree, visited)
            for i in range(size):
                if tree[i] == '1' and not visited[i]:
                    failed = True
                    break
            if not failed:
                ans[ni] = 1
    return ans
