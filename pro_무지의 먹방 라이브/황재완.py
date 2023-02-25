def solution(food_times, k):
    sorted_times = [(time, i) for i, time in enumerate(food_times, start=1)]
    sorted_times.sort()
    i, t = 0, 0
    food_set = set(range(1, len(food_times) + 1))
    last = 0
    while i < len(sorted_times):
        cur = i
        remove_set = {sorted_times[cur][1]}
        while i < len(sorted_times) and sorted_times[i][0] == sorted_times[cur][0]:
            remove_set.add(sorted_times[i][1])
            i += 1
        dt = len(food_set) * (sorted_times[cur][0] - last)
        if t + dt > k:
            return sorted(food_set)[(k - t) % len(food_set)]
        t += dt
        food_set -= remove_set
        last = sorted_times[cur][0]

    return -1


print(solution([3, 1, 1, 2], 3))
