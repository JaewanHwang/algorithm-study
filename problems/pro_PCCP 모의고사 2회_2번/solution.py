from heapq import heappop, heappush, heapify


def solution(ability, number):
    heapify(ability)
    for _ in range(number):
        a, b = heappop(ability), heappop(ability)
        heappush(ability, a + b), heappush(ability, a + b)
    return sum(ability)
