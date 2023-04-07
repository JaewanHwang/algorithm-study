import sys

sys.stdin = open("input.txt")

t = int(input())
MOD = 2 ** 8
ans = []
for _ in range(t):
    sm, sc, si = map(int, input().split())
    m = [0] * sm
    code = list(input())
    data = list(map(ord, input()))
    jump = [0] * sc
    stack = []
    for i in range(sc):
        if code[i] == '[':
            stack.append(i)
        elif code[i] == ']':
            prev = stack.pop()
            jump[prev] = i
            jump[i] = prev
    pi, mi, di = 0, 0, 0
    l, r = float('inf'), 0
    cnt = 0
    while cnt < 2 * 50_000_000 and pi < sc:
        if cnt >= 50_000_000:
            l, r = min(l, pi), max(r, pi)
        if code[pi] == '-':
            m[mi] = (m[mi] - 1) % MOD
        elif code[pi] == '+':
            m[mi] = (m[mi] + 1) % MOD
        elif code[pi] == '<':
            mi = (mi - 1) % sm
        elif code[pi] == '>':
            mi = (mi + 1) % sm
        elif code[pi] == '[':
            if m[mi] == 0:
                pi = jump[pi]
        elif code[pi] == ']':
            if m[mi] != 0:
                pi = jump[pi]
        elif code[pi] == ',':
            if di < si:
                m[mi] = data[di]
                di += 1
            else:
                m[mi] = 255
        pi += 1
        cnt += 1
    if pi == sc:
        ans.append('Terminates')
    else:
        ans.append(f'Loops {l - 1} {r}')

print('\n'.join(ans))
