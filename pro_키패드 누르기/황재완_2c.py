def solution(numbers, hand):
    ans = []
    l, r = 9, 11
    for number in numbers:
        if number in (1, 4, 7):
            ans.append('L')
            l = number - 1
        elif number in (3, 6, 9):
            ans.append('R')
            r = number - 1
        else:
            if number == 0:
                number = 11
            lx, ly = l // 3, l % 3
            rx, ry = r // 3, r % 3
            number -= 1
            nx, ny = number // 3, number % 3
            ld, rd = abs(lx - nx) + abs(ly - ny), abs(rx - nx) + abs(ry - ny)
            if ld < rd:
                ans.append('L')
                l = number
            elif ld > rd:
                ans.append('R')
                r = number
            else:
                ans.append(hand[0].upper())
                if hand == 'left':
                    l = number
                else:
                    r = number
    return ''.join(ans)
