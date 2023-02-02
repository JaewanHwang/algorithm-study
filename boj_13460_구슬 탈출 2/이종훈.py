import sys

sys.stdin = open('jh_input.txt')

obstacle = ['#', 'R', 'B', '1', '2']


def rollingup(location, signal):
    stop = False
    rstop = False
    bstop = False
    rgoal = False
    bgoal = False

    while not stop:
        for i in range(N):
            for j in range(M):
                if location[i][j] == 'R':
                    if location[i - 1][j] in obstacle:
                        rstop = True
                    elif location[i - 1][j] == 'B':
                        rstop = True
                    elif location[i - 1][j] == '0':
                        rgoal = True
                        location[i][j] = '.'
                        location[i - 1][j] = '1'  # 0을 지나가고 있는 R인 경우 1로 표시
                    else:
                        location[i][j] = '.'
                        location[i - 1][j] = 'R'


                if location[i][j] == '1':
                    if location[i - 1][j] in obstacle:
                        rstop = True
                    elif location[i - 1][j] == 'B':
                        rstop = True
                    else:
                        location[i][j] = '0'
                        location[i - 1][j] = 'R'

                if location[i][j] == 'B':
                    if location[i - 1][j] in obstacle:
                        bstop = True
                    elif location[i - 1][j] == 'A':
                        bstop = True
                    elif location[i - 1][j] == '0':
                        bgoal = True
                        location[i][j] = '.'
                        location[i - 1][j] = '2'  # 0을 지나가고 있는 B인 경우 2로 표시
                    else:
                        location[i][j] = '.'
                        location[i - 1][j] = 'B'

                if location[i][j] == '2':
                    if location[i - 1][j] in obstacle:
                        bstop = True
                    elif location[i - 1][j] == 'R':
                        bstop = True
                    else:
                        location[i][j] = '0'
                        location[i - 1][j] = 'B'
                if rstop and bstop == True:
                    stop = True
    if bgoal == True:  # 파란공이 goal에 들어가면 signal은 2
        signal = 2
    elif rgoal == True:  # 파란공이 들어가지 않고 빨간공이 들어가면 signal은 1
        signal = 1

    return location, signal


def rollingdown(location, signal):
    stop = False
    rstop = False
    bstop = False
    rgoal = False
    bgoal = False

    while not stop:
        for i in range(N - 1, -1, -1):
            for j in range(M):
                if location[i][j] == 'R':
                    if location[i + 1][j] in obstacle:
                        rstop = True
                    elif location[i + 1][j] == 'B':
                        rstop = True
                    elif location[i + 1][j] == '0':
                        rgoal = True

                        location[i][j] = '.'
                        location[i + 1][j] = '1'  # 0을 지나가고 있는 R인 경우 1로 표시
                    else:
                        location[i][j] = '.'
                        location[i + 1][j] = 'R'

                if location[i][j] == '1':
                    if location[i + 1][j] in obstacle:
                        rstop = True
                    elif location[i + 1][j] == 'B':
                        rstop = True
                    else:
                        location[i][j] = '0'
                        location[i + 1][j] = 'R'

                if location[i][j] == 'B':
                    if location[i + 1][j] in obstacle:
                        bstop = True
                    elif location[i + 1][j] == 'A':
                        bstop = True
                    elif location[i + 1][j] == '0':
                        bgoal = True
                        location[i][j] = '.'
                        location[i + 1][j] = '2'  # 0을 지나가고 있는 B인 경우 2로 표시
                    else:
                        location[i][j] = '.'
                        location[i + 1][j] = 'B'

                if location[i][j] == '2':
                    if location[i + 1][j] in obstacle:
                        bstop = True
                    elif location[i + 1][j] == 'R':
                        bstop = True
                    else:
                        location[i][j] = '0'
                        location[i + 1][j] = 'B'
                if rstop and bstop == True:
                    stop = True
    if bgoal == True:  # 파란공이 goal에 들어가면 signal은 2
        signal = 2
    elif rgoal == True:  # 파란공이 들어가지 않고 빨간공이 들어가면 signal은 1
        signal = 1

    return location, signal


def rollingleft(location, signal):
    stop = False
    rstop = False
    bstop = False
    rgoal = False
    bgoal = False

    while not stop:
        for i in range(N):
            for j in range(M):
                if location[i][j] == 'R':
                    if location[i][j - 1] in obstacle:
                        rstop = True
                    elif location[i][j - 1] == 'B':
                        rstop = True
                    elif location[i][j - 1] == '0':
                        rgoal = True
                        location[i][j] = '.'
                        location[i][j - 1] = '1'  # 0을 지나가고 있는 R인 경우 1로 표시
                    else:
                        location[i][j] = '.'
                        location[i][j - 1] = 'R'

                if location[i][j] == '1':
                    if location[i][j - 1] in obstacle:
                        rstop = True
                    elif location[i][j - 1] == 'B':
                        rstop = True
                    else:
                        location[i][j] = '0'
                        location[i][j - 1] = 'R'

                if location[i][j] == 'B':
                    if location[i][j - 1] in obstacle:
                        bstop = True
                    elif location[i][j - 1] == 'A':
                        bstop = True
                    elif location[i][j - 1] == '0':
                        bgoal = True
                        location[i][j] = '.'
                        location[i][j - 1] = '2'  # 0을 지나가고 있는 B인 경우 2로 표시
                    else:
                        location[i][j] = '.'
                        location[i][j - 1] = 'B'

                if location[i][j] == '2':
                    if location[i][j - 1] in obstacle:
                        bstop = True
                    elif location[i][j - 1] == 'R':
                        bstop = True
                    else:
                        location[i][j] = '0'
                        location[i][j - 1] = 'B'
                if rstop and bstop == True:
                    stop = True
    if bgoal == True:  # 파란공이 goal에 들어가면 signal은 2
        signal = 2
    elif rgoal == True:  # 파란공이 들어가지 않고 빨간공이 들어가면 signal은 1
        signal = 1

    return location, signal


def rollingright(location, signal):
    stop = False
    rstop = False
    bstop = False
    rgoal = False
    bgoal = False

    while not stop:
        for i in range(N):
            for j in range(M - 1, -1, -1):
                if location[i][j] == 'R':
                    if location[i][j + 1] in obstacle:
                        rstop = True

                    elif location[i][j + 1] == 'B':
                        rstop = True

                    elif location[i][j + 1] == '0':

                        rgoal = True
                        location[i][j] = '.'
                        location[i][j + 1] = '1'  # 0을 지나가고 있는 R인 경우 1로 표시

                    else:
                        location[i][j] = '.'
                        location[i][j + 1] = 'R'

                if location[i][j] == '1':
                    if location[i][j + 1] in obstacle:
                        rstop = True
                    elif location[i][j + 1] == 'B':
                        rstop = True
                    else:
                        location[i][j] = '0'
                        location[i][j + 1] = 'R'

                if location[i][j] == 'B':
                    if location[i][j + 1] in obstacle:
                        bstop = True
                    elif location[i][j + 1] == 'A':
                        bstop = True
                    elif location[i][j + 1] == '0':
                        bgoal = True
                        location[i][j] = '.'
                        location[i][j + 1] = '2'  # 0을 지나가고 있는 B인 경우 2로 표시
                    else:
                        location[i][j] = '.'
                        location[i][j + 1] = 'B'

                if location[i][j] == '2':
                    if location[i][j + 1] in obstacle:
                        bstop = True
                    elif location[i][j + 1] == 'R':
                        bstop = True
                    else:
                        location[i][j] = '0'
                        location[i][j + 1] = 'B'
                if rstop and bstop == True:
                    stop = True
    if bgoal == True:  # 파란공이 goal에 들어가면 signal은 2
        signal = 2
        print(2)
    elif rgoal == True:  # 파란공이 들어가지 않고 빨간공이 들어가면 signal은 1
        signal = 1
        print(1)

    return location, signal


def beedescape(progress, direction, count):
    global top
    global answer
    if count <= top:
        if direction == 'up':
            status = 0  # status가 0이면 킵고잉 status가 1이면 성공 status가 2면 스톱
            progress, status = rollingup(progress, status)
            if status == 0:
                beedescape(progress, 'up', count + 1)
                beedescape(progress, 'down', count + 1)
                beedescape(progress, 'left', count + 1)
                beedescape(progress, 'right', count + 1)
            elif status == 1:
                if count <= top:
                    top = count
                    answer = count

        elif direction == 'down':
            status = 0
            progress, status = rollingdown(progress, status)
            if status == 0:
                beedescape(progress, 'up', count + 1)
                beedescape(progress, 'down', count + 1)
                beedescape(progress, 'left', count + 1)
                beedescape(progress, 'right', count + 1)
            elif status == 1:
                if count <= top:
                    top = count
                    answer = count
        elif direction == 'left':
            status = 0
            progress, status = rollingleft(progress, status)
            if status == 0:
                beedescape(progress, 'up', count + 1)
                beedescape(progress, 'down', count + 1)
                beedescape(progress, 'left', count + 1)
                beedescape(progress, 'right', count + 1)
            elif status == 1:
                if count <= top:
                    top = count
                    answer = count

        elif direction == 'right':
            status = 0
            progress, status = rollingright(progress, status)
            if status == 0:
                beedescape(progress, 'up', count + 1)
                beedescape(progress, 'down', count + 1)
                beedescape(progress, 'left', count + 1)
                beedescape(progress, 'right', count + 1)
            elif status == 1:
                if count <= top:
                    top = count
                    answer = count


answer = -1
top = 10
N, M = map(int, input().split())
board = []
for _ in range(N):
    board += [list(input())]
print(board)
beedescape(board, 'up', 1)
beedescape(board, 'down', 1)
beedescape(board, 'left', 1)
beedescape(board, 'right', 1)
print(answer)
