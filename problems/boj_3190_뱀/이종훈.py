import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

wall = []
for i in range(N):
    wall += [(0, i)]
    wall += [(i, 0)]
    wall += [(N + 1, i + 1)]
    wall += [(i + 1, N + 1)]

wall = set(wall)
K = int(input())
apple = []
for _ in range(K):
    a, b = map(int, input().split())

    apple += [(a + 1, b + 1)]
apple = set(apple)
L = int(input())
time = {}
for _ in range(L):
    a, b = input().split()
    a = int(a)
    time[a] = b
snake = deque()
snake.append([1, 1])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
steering = 100
direction = [dx[steering % 4], dy[steering % 4]]
timer = 0
Live = True
while Live:
    if timer in time:
        if time[timer] == 'D':
            steering += 1
        elif time[timer] == 'L':
            steering -= 1
        direction = [dx[steering % 4], dy[steering % 4]]

    head = snake.pop()
    snake.append([head[0], head[1]])
    head[0] += direction[0]
    head[1] += direction[1]
    if (head[0], head[1]) not in apple:
        snake.popleft() # 꼬리삭제
    if (head[0], head[1]) in apple:
        apple.remove((head[0], head[1])) #사과 삭제
    if (head[0], head[1]) in wall:
        Live = False
    if [head[0], head[1]] in snake:
        Live = False
    snake.append([head[0], head[1]])
    print(snake, apple)
    timer += 1

print(timer)