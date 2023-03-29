from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    ans = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            ans += 1
        else:
            ans += 5
        cache.append(city)
    return ans
