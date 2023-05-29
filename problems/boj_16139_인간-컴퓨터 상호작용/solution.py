import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input().rstrip()
s = [0] * (len(S) + 1)
s[0] = [0] * 26
for i in range(1, len(S) + 1):
    s[i] = s[i - 1][:]
    s[i][ord(S[i - 1]) - ord('a')] += 1

q = int(input())
ans = []
for _ in range(q):
    ai, li, ri = input().split()
    li, ri = int(li) + 1, int(ri) + 1
    ans.append(s[ri][ord(ai) - ord('a')] - s[li - 1][ord(ai) - ord('a')])
print('\n'.join(map(str, ans)))
