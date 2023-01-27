import sys
sys.stedin = open('jh_input.txt')

obstacle = ['#','R','B']
def rollingup(location):
    return location
def rollingdown(location):
    stop = False
    rstop = False
    bstop = False
    rgoal = False
    bgoal = False
    goal = False

    while stop == False:
        for i in range(N):
            for j in range(M):
                if location[i][j] == 'R':
                    if location[i+1][j] in obstacle:
                        rstop = True
                    elif location[i+1][j] == 'B':
                        rstop = True
                    elif location[i+1][j] == '0':
                        rgoal = True
                        location[i][j] == '.'
                        location[i + 1][j] = '1' #0을 지나가고 있는 R인 경우 1로 표시
                    else:
                        location[i][j] == '.'
                        location[i + 1][j] = 'R'

                if location[i][j] == '1':
                    if location[i+1][j] in obstacle:
                        rstop = True
                    elif location[i+1][j] == 'B':
                        rstop = True
                    else:
                        location[i][j] == '0'
                        location[i + 1][j] = 'R'


                if location[i][j] == 'B':
                    if location[i + 1][j] in obstacle:
                        bstop = True
                    elif location[i + 1][j] == 'A':
                        bstop = True
                    elif location[i + 1][j] == '0':
                        bgoal = True
                        location[i][j] == '.'
                        location[i + 1][j] = '2'  # 0을 지나가고 있는 B인 경우 2로 표시
                    else:
                        location[i][j] == '.'
                        location[i + 1][j] = 'B'

                if location[i][j] == '2':
                    if location[i + 1][j] in obstacle:
                        bstop = True
                    elif location[i + 1][j] == 'R':
                        bstop = True
                    else:
                        location[i][j] == '0'
                        location[i + 1][j] = 'B'
                if rstop and bstop == True:
                    stop = True
                    stop = True
    if bgoal == True:
        return


    return location
def rollingleft(location):
    return location
def rollingright(location):
    return location

def beedescape(progress,direction,count):
    if direction == 'up':
        progress = rollingdown(progress)
        beedescape(progress,'up',count + 1)
        beedescape(progress, 'down', count + 1)
        beedescape(progress, 'left', count + 1)
        beedescape(progress, 'right', count + 1)
    elif direction == 'down':
        progress = rollingdown(progress)
        beedescape(progress,'up',count + 1)
        beedescape(progress, 'down', count + 1)
        beedescape(progress, 'left', count + 1)
        beedescape(progress, 'right', count + 1)
    elif direction == 'left':
        progress = rollingdown(progress)
        beedescape(progress,'up',count + 1)
        beedescape(progress, 'down', count + 1)
        beedescape(progress, 'left', count + 1)
        beedescape(progress, 'right', count + 1)

    elif direction == 'right':
        progress = rollingdown(progress)
        beedescape(progress,'up',count + 1)
        beedescape(progress, 'down', count + 1)
        beedescape(progress, 'left', count + 1)
        beedescape(progress, 'right', count + 1)

answer = -1
top = 10
N, M = map(int,input().split())
board = []
for _ in range(N):
    board += [list(input())]
print(board)
beedescape(board,'up',1)
beedescape(board,'down',1)
beedescape(board,'left',1)
beedescape(board,'right',1)