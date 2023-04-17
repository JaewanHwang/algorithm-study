from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cq = deque()
    cs = set()
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            city = city.upper()
            if city in cs:
                cq.remove(city)
                cq.append(city)
                answer += 1
            else:
                if len(cq) == cacheSize:
                    p = cq.popleft()
                    cs.remove(p)
                cq.append(city)
                cs.add(city)
                answer += 5

    return answer
