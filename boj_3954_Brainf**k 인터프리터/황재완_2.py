import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
MOD = 2 ** 8
MAX = 50_000_000
t = int(input())
for _ in range(t):
    sm, sc, si = map(int, input().split())
    memory = [0] * sm
    program = list(input().rstrip())
    inputs = list(input().rstrip())
    op_cnt, mem_p, op_p, in_p = 0, 0, 0, 0
    jump = [0] * sc
    left_loop_idx = float('inf')
    right_loop_idx = 0

    stack = []
    # '['와 짝인 ']'의 위치를 찾는다. ']'와 짝인 '['의 위치를 찾는다.
    for i in range(sc):
        if program[i] == '[':
            stack.append(i)
        elif program[i] == ']' and stack[-1]:
            pi = stack.pop()
            jump[i] = pi
            jump[pi] = i

    while op_cnt < 2 * MAX and op_p < sc:
        if op_cnt >= MAX:
            left_loop_idx = min(left_loop_idx, op_p)
            right_loop_idx = max(right_loop_idx, op_p)

        # 포인터가 가리키는 수를 1 감소시킨다. (modulo 28)
        if program[op_p] == '-':
            memory[mem_p] = (memory[mem_p] - 1 + MOD) % MOD

        # 포인터가 가리키는 수를 1 증가시킨다. (modulo 28)
        elif program[op_p] == '+':
            memory[mem_p] = (memory[mem_p] + 1) % MOD

        # 포인터를 왼쪽으로 한 칸 움직인다.
        elif program[op_p] == '<':
            mem_p = (mem_p - 1) % sm

        # 포인터를 오른쪽으로 한 칸 움직인다.
        elif program[op_p] == '>':
            mem_p = (mem_p + 1) % sm

        # 만약 포인터가 가리키는 수가 0이라면, [ 와 짝을 이루는 ] 의 다음 명령으로 점프한다.
        elif program[op_p] == '[':
            if memory[mem_p] == 0:
                op_p = jump[op_p]

        # 만약 포인터가 가리키는 수가 0이 아니라면, ] 와 짝을 이루는 [ 의 다음 명령으로 점프한다.
        elif program[op_p] == ']':
            if memory[mem_p] != 0:
                op_p = jump[op_p]

        # 포인터가 가리키는 수를 출력한다.

        # 문자 하나를 읽고 포인터가 가리키는 곳에 저장한다. 입력의 마지막(EOF)인 경우에는 255를 저장한다.
        elif program[op_p] == ',':
            if in_p < si:
                memory[mem_p] = ord(inputs[in_p])
                in_p += 1
            else:
                memory[mem_p] = 255
        op_cnt += 1
        op_p += 1
        print(op_p, mem_p, in_p)
    if op_p == sc:
        print("Terminates")
    elif op_cnt == 2 * MAX:
        print(f"Loops {left_loop_idx - 1} {right_loop_idx}")
