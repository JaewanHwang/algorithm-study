import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
A = [list(map(int, input().split())) for _ in range(3)]


def do_r():
    global A
    nA = []
    max_len = 0
    for row in A:
        nA.append([])
        counter = Counter(row)
        counter.pop(0, 0)
        counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        for num_cnt in counter[:min(len(counter), 50)]:
            nA[-1].extend(num_cnt)
        max_len = max(max_len, len(nA[-1]))
    for row in nA:
        row.extend([0] * (max_len - len(row)))
    A = nA


def do_c():
    global A
    A = list(zip(*A))
    do_r()
    A = list(zip(*A))


def simulate():
    R, C = len(A), len(A[0])
    if R >= C:
        do_r()
    else:
        do_c()


for ans in range(102):
    if 0 <= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == k:
        break
    simulate()

if ans == 101:
    ans = -1
print(ans)
