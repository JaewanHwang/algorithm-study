import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
w = list(map(int, input().split()))
prime = [True] * 9001
prime[0] = prime[1] = False
for num in range(2, 9001):
    if num * num > 9000:
        break
    if not prime[num]:
        continue
    for m_num in range(num * num, 9001, num):
        prime[m_num] = False

ans = set()


def go(i, start, tot):
    if i == M:
        if prime[tot]:
            ans.add(tot)
        return
    for j in range(start, N):
        go(i + 1, j + 1, tot + w[j])


go(0, 0, 0)
if ans:
    print(*sorted(ans))
else:
    print(-1)
