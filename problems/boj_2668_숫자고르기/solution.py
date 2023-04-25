import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) - 1 for _ in range(N))
ans = []
visited = [-1] * N
finished = [False] * N
for i in range(N):
    if i == arr[i]:
        visited[i] = 0
        finished[i] = True
        ans.append(i)


def go(i, hist):
    visited[i] = len(hist)
    hist.append(i)
    if visited[arr[i]] == -1:
        go(arr[i], hist)
    elif not finished[arr[i]]:
        for j in range(visited[arr[i]], visited[i] + 1):
            ans.append(hist[j])
    finished[i] = True


for i in range(N):
    if visited[i] == -1:
        go(i, [])

ans = sorted(ans)
print(len(ans), *map(lambda x: int(x) + 1, ans), sep='\n')
