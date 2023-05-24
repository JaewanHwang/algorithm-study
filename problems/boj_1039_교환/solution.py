import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
SIZE = len(str(N))
visited = set()
visited.add((N, 0))
q = deque([(N, 0)])
ans = -1
while q:
    num, cnt = q.popleft()
    if cnt == K:
        ans = max(ans, num)
        continue

    num = list(str(num))
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if i == 0 and num[j] == '0':
                continue
            num[i], num[j] = num[j], num[i]
            res = int(''.join(num))
            if (res, cnt + 1) not in visited:
                visited.add((res, cnt + 1))
                q.append((res, cnt + 1))
            num[i], num[j] = num[j], num[i]
print(ans)
