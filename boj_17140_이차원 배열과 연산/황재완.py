import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
A = [list(map(int, input().split())) for _ in range(3)]
ans = -1


def do(operation):
    tmpA = []
    max_len = 0
    for row in A if operation == 'R' else zip(*A):
        counter = Counter(filter(lambda x: x > 0, row))
        row = []
        for item in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            row.extend(item)
            if len(row) == 100:
                break
        tmpA.append(row)
        max_len = max(max_len, len(row))
    for row in tmpA:
        row.extend([0] * (max_len - len(row)))
    if operation == 'C':
        tmpA = list(zip(*tmpA))
    return tmpA


for t in range(0, 101):
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        ans = t
        break
    A = do('R') if len(A) >= len(A[0]) else do('C')

print(ans)
