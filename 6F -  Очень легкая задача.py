n, x, y = list(map(int, input().split()))


def left_bin_search(left, right, check, checkparams):
    while left < right:
        m = (left + right) // 2
        if check(m, checkparams):
            right = m
        else:
            left = m + 1
    return left


def check(m, checkparams):
    n, x, y = checkparams
    slow = max(x, y)
    fast = min(x, y)
    return m // fast + (m - fast) // slow >= n


ans = left_bin_search(0, n*x*y*2, check,  [n, x, y])
print(ans)
