def solution(n, k):
    k_num = ''
    while n != 0:
        n, mod = divmod(n, k)
        k_num += str(mod)
    k_num = k_num[::-1]
    nums = k_num.split('0')
    ans = 0
    for num in nums:
        if not num:
            continue
        num = int(num)
        if num == 1:
            prime = False
        else:
            prime = True
            for i in range(2, num):
                if i * i > num:
                    break
                if num % i == 0:
                    prime = False
                    break
        if prime:
            ans += 1
    return ans
