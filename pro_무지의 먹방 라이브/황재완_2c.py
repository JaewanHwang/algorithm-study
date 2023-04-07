def solution(food_times, k):
    food_times = [[i, val] for i, val in enumerate(food_times)]
    food_times.sort(key=lambda x: (x[1], x[0]), reverse=True)
    N = len(food_times)
    table = [[(i - 1) % N, (i + 1) % N, False] for i in range(N)]
    cur_time = 0
    cur_size = 0
    while food_times and cur_time + N * (food_times[-1][1] - cur_size) <= k:
        cur_time += N * (food_times[-1][1] - cur_size)
        cur_size = food_times[-1][1]
        while food_times and food_times[-1][1] == cur_size:
            i, _ = food_times.pop()
            prev, next, _ = table[i]
            table[prev][1], table[next][0], table[i][2] = next, prev, True
            N -= 1

    if N == 0:
        return -1

    for p in range(len(table)):
        if not table[p][2]:
            break
    for _ in range((k - cur_time) % N):
        prev, next, _ = table[p]
        p = next
    ans = p + 1
    return ans


print(solution([5, 3, 1, 2, 4, 3], 8))
