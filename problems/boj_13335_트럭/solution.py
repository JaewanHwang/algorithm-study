import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = deque(map(int, input().split()))

cur_w = 0
bridge = deque()
t = 0
while a:
    t += 1
    if bridge and bridge[0][0] == t:
        _, ai = bridge.popleft()
        cur_w -= ai
    if cur_w + a[0] <= L:
        ai = a.popleft()
        bridge.append((t + w, ai))
        cur_w += ai
t += w
print(t)
