def solution(numbers):
    ans = []
    for number in numbers:
        bin_num = '0' + bin(number)[2:]
        for i in range(len(bin_num) - 1, -1, -1):
            if bin_num[i] == '0':
                tmp = bin_num[i:]
                res = int(tmp, 2) + 2 ** max(0, len(tmp) - 2)
                tmp = bin_num[:i] + '0' * len(tmp)
                res += int(tmp, 2)
                break
        ans.append(res)
    return ans


print(solution([2, 7]))
