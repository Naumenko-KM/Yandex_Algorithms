a = int(input())
b = int(input())
c = int(input())


def left_bin_search(left, right, check, checkparams):
    while left < right:
        m = (left + right) // 2
        if check(m, checkparams):
            right = m
        else:
            left = m + 1
    return left


def check(m, checkparams):
    a, b, c = checkparams
    cur_sum = a * 2 + b * 3 + c * 4 + m * 5
    return cur_sum >= 3.5 * (a + b + c + m)


ans = left_bin_search(0, (a+b+c)*2, check,  [a, b, c])
print(ans)
