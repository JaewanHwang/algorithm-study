import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline


def go(i):
    if i == L:
        ans.add(''.join(cur))
        return
    for c in word:
        if word[c] > 0:
            word[c] -= 1
            cur.append(c)
            go(i + 1)
            word[c] += 1
            cur.pop()


N = int(input())
for _ in range(N):
    ans = set()
    line = input().rstrip()
    L = len(line)
    word = Counter(line)
    cur = []
    go(0)
    print(*sorted(ans), sep='\n')
