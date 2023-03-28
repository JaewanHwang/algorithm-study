def solution(n, arr1, arr2):
    ans = []
    for row1, row2 in zip(arr1, arr2):
        row = ''
        row1, row2 = bin(row1)[2:].zfill(n), bin(row2)[2:].zfill(n)
        for i in range(n):
            row += '#' if int(row1[i]) | int(row2[i]) else ' '
        ans.append(row)
    return ans
