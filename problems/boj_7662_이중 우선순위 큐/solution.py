import sys
from heapq import heappop, heappush
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline


def insert(num):
    heappush(max_pq, -num)
    heappush(min_pq, num)
    remain[num] += 1


def delete(num):
    if num == 1:
        while max_pq:
            res = -heappop(max_pq)
            if remain[res] > 0:
                remain[res] -= 1
                return
    else:
        while min_pq:
            res = heappop(min_pq)
            if remain[res] > 0:
                remain[res] -= 1
                return


T = int(input())
for _ in range(T):
    k = int(input())
    max_pq = []
    min_pq = []
    remain = defaultdict(int)
    for _ in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            insert(num)
        else:
            delete(num)

    ans = sorted(filter(lambda x: remain[x] > 0, remain))

    if not ans:
        print('EMPTY')
    else:
        print(ans[-1], ans[0])
