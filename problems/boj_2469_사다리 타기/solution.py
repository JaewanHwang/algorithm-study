import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

k = int(input())
n = int(input())
res = list(map(lambda x: ord(x) - 65, input().rstrip()))
ladder = []
for i in range(n):
    line = list(input().rstrip())
    if line[0] == '?':
        target = i
    ladder.append(line)

start = [0] * k
end = [0] * k
for cur in range(k):
    y = cur
    for x in range(target):
        if y - 1 >= 0 and ladder[x][y - 1] == '-':
            y -= 1
        elif y < k - 1 and ladder[x][y] == '-':
            y += 1
    start[cur] = y
for cur in range(k):
    y = cur
    for x in range(target, n):
        if y - 1 >= 0 and ladder[x][y - 1] == '-':
            y -= 1
        elif y < k - 1 and ladder[x][y] == '-':
            y += 1
    end[cur] = y

ans = [0] * (k - 1)
for i in range(k):
    cur = start.index(i)
    if i - 1 >= 0 and ans[i - 1] == '-':
        if res[end[i - 1]] == cur:
            if i < k - 1:
                ans[i] = '*'
        else:
            print('x' * (k - 1))
            sys.exit(0)
    else:
        if res[end[i]] == cur:
            if i < k - 1:
                ans[i] = '*'
        elif i + 1 < k and res[end[i + 1]] == cur:
            if i < k - 1:
                ans[i] = '-'
        else:
            print('x' * (k - 1))
            sys.exit(0)
print(''.join(ans))
