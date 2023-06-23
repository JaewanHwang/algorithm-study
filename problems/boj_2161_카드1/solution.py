import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
q = deque(range(1, N + 1))
ans = []
while len(q) > 1:
    ans.append(q.popleft())
    q.append(q.popleft())
ans.append(q.popleft())
print(*ans)
