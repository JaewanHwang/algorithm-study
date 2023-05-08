import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
N, L, M = map(int, input().split())
fishes = []
for _ in range(M):
    x, y = map(int, input().split())
    fishes.append((x, y))
ans = 0

lengths = []
for h in range(1, L):
    for w in range(1, L):
        if 2 * w + 2 * h > L:
            continue
        if 2 * w + 2 * h == L:
            lengths.append((h, w))

for cx, cy in fishes:
    for h, w in lengths:
        for x in range(cx - h, cx + 1):
            for y in range(cy - w, cy + 1):
                if x >= 1 and x + h <= N and y >= 1 and y + w <= N:
                    cnt = 0
                    for fx, fy in fishes:
                        if x <= fx <= x + h and y <= fy <= y + w:
                            cnt += 1
                    ans = max(ans, cnt)
print(ans)
