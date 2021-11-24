w, h, n = list(map(int, input().split()))


def left_bin_search(left, right, check, checkparams):
    while left < right:
        m = (left + right) // 2
        if check(m, checkparams):
            right = m
        else:
            left = m + 1
    return left


def check(m, checkparams):
    w, h, n = checkparams
    area = w * h
    if area * n > m ** 2:
        return False
    else:
        w_cnt = m // w
        h_cnt = m // h
        return w_cnt * h_cnt >= n


ans = left_bin_search(0, (w+h)*n, check,  [w, h, n])
print(ans)
