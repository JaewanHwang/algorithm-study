import sys
from collections import Counter

sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input().rstrip()
counter = Counter(S)
ans = 0
cur = [''] * len(S)
alphabet = set(S)


def go(i):
    global ans
    if i == len(S):
        ans += 1
        return
    for char in list(alphabet):
        if i > 0 and cur[i - 1] == char:
            continue
        counter[char] -= 1
        if counter[char] == 0:
            alphabet.remove(char)
        cur[i] = char
        go(i + 1)
        if counter[char] == 0:
            alphabet.add(char)
        counter[char] += 1


go(0)
print(ans)
