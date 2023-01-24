def solution(n, arr1, arr2):
    answer = []
    for r1, r2 in zip(arr1, arr2):
        row = r1 | r2
        tmp = 1
        res = ''
        for _ in range(n):
            if tmp & row:
                res += '#'
            else:
                res += ' '
            tmp <<= 1
        answer.append(res[::-1])
        
    return answer
