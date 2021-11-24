n = int(input())
m = int(input())
t = int(input())


def left_bin_search(left, right, check, checkparams):
    while left < right:
        m = (left + right) // 2
        if check(m, checkparams):
            right = m
        else:
            left = m + 1
    return left


def right_bin_search(left, right, check, checkparams):
    while left < right:
        m = (left + right + 1) // 2
        if check(m, checkparams):
            left = m
        else:
            right = m - 1
    return left


def check(d, checkparams):
    n, m, t = checkparams
    cnt_tile = n * m - (n - 2*d) * (m - 2*d)
    # print(f'cnt_tile: {cnt_tile}, d: {d}, \
    # flag: {(0 < cnt_tile <= t) and (2*d < n) and (2*d < m)}')
    return (0 < cnt_tile <= t) and (2*d < n) and (2*d < m)


ans = right_bin_search(0, n*m, check,  [n, m, t])
print(ans)
