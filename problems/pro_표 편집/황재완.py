def solution(n, k, cmd):
    linked_list, removed, stack = [[i - 1, i + 1] for i in range(n)], [False] * n, []
    linked_list[-1][1] = -1
    cur = k
    for q in cmd:
        if len(q) > 1:
            op, x = q.split(' ')
            x = int(x)
            if op == 'U':
                for _ in range(x):
                    cur = linked_list[cur][0]
            else:
                for _ in range(x):
                    cur = linked_list[cur][1]
        else:
            op = q
            if op == 'C':
                removed[cur] = True
                stack.append(cur)
                prev, next = linked_list[cur]
                if prev >= 0:
                    linked_list[prev][1] = next
                if next >= 0:
                    linked_list[next][0] = prev
                if linked_list[cur][1] == -1:
                    cur = prev
                else:
                    cur = next

            else:
                z = stack.pop()
                removed[z] = False
                prev, next = linked_list[z]
                if prev >= 0:
                    next = linked_list[prev][1]
                    if next != -1:
                        linked_list[next][0] = z
                    linked_list[z][1] = next
                    linked_list[prev][1] = z
                elif next >= 0:
                    prev = linked_list[next][0]
                    if prev != -1:
                        linked_list[prev][1] = z
                    linked_list[z][0] = prev
                    linked_list[next][0] = z

    ans = ''.join(map(lambda x: 'X' if x else 'O', removed))
    return ans
