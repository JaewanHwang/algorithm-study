import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
m = [input().rstrip() for _ in range(N)]
cnt = [0] * N
for me in range(N):
    for otr in range(me + 1, N):
        if m[me][otr] == 'Y':
            cnt[me] += 1
            cnt[otr] += 1
        else:
            for brk in range(N):
                if m[me][brk] == 'Y' and m[brk][otr] == 'Y':
                    cnt[me] += 1
                    cnt[otr] += 1
                    break
print(max(cnt))
