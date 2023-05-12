import sys
from collections import defaultdict, deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
pipe = defaultdict(lambda: defaultdict(list))
for _ in range(N):
    a, b, w = input().split()
    pipe[a][b].append(int(w))


def bfs(start):
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur not in pipe:
            continue
        if cur != 'Z' and not pipe[cur]:
            for node in pipe:
                if cur in pipe[node]:
                    pipe[node].pop(cur)
            pipe.pop(cur)
            return True
        for nxt in list(pipe[cur]):
            if len(pipe[cur][nxt]) == len(pipe[nxt]) == 1 == len(pipe[nxt][list(pipe[nxt].keys())[0]]):
                (nnxt,) = pipe[nxt].keys()
                pipe[cur][nnxt].append(min(pipe[nxt][nnxt][0], pipe[cur][nxt][0]))
                for node in pipe:
                    if nxt in pipe[node]:
                        pipe[node].pop(nxt)
                pipe.pop(nxt)
                return True
            if len(pipe[cur][nxt]) >= 2:
                pipe[cur][nxt] = [sum(pipe[cur][nxt])]
                return True
            q.append(nxt)
    return False


while True:
    if not bfs('A'):
        break
print(pipe['A']['Z'][0])

# import sys
# from collections import defaultdict, deque
#
# input = sys.stdin.readline
#
# N = int(input())
# pipe = defaultdict(lambda: defaultdict(list))
# weight = {}
# for _ in range(N):
#     a, b, w = input().split()
#     pipe[a][b] = int(w)
#     weight[a] = float('inf')
#     weight[b] = float('inf')
#
#
# def bfs(start):
#     q = deque([(start, float('inf'))])
#     while q:
#         cur, w = q.popleft()
#         for nxt in pipe[cur]:
#             weight[nxt] = min(weight[nxt], min(w, pipe[cur][nxt]))
#             q.append((nxt, weight[nxt]))
#
#
# bfs('A')
# print(weight['Z'])
