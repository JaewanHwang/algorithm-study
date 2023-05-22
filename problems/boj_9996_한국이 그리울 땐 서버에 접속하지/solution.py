import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
pattern = input().rstrip()
star = pattern.index('*')
prefix = pattern[:star]
postfix = pattern[star + 1:]
for _ in range(N):
    s = input().rstrip()
    if len(s) >= len(prefix) + len(postfix) and s[:len(prefix)] == prefix and s[-len(postfix):] == postfix:
        print('DA')
    else:
        print('NE')
