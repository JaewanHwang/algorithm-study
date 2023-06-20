import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
S = int(input())
a = list(map(int, input().split()))
frame = dict()
for turn, who in enumerate(a):
    if who in frame:
        frame[who][0] += 1
    else:
        if len(frame) < N:
            frame[who] = [1, turn]
        else:
            removed_who = min(frame, key=lambda x: frame[x])
            frame.pop(removed_who)
            frame[who] = [1, turn]
print(*sorted(frame))
