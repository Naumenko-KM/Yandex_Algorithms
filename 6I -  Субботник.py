# too much to do
# N, K = list(map(int, input().split()))
# wires = []
# for _ in range(N):
#     wires.append(int(input()))


# def left_bin_search(left, right, check, checkparams):
#     while left < right:
#         m = (left + right) // 2
#         if check(m, checkparams):
#             right = m
#         else:
#             left = m + 1
#     return left


# def right_bin_search(left, right, check, checkparams):
#     while left < right:
#         m = (left + right + 1) // 2
#         if check(m, checkparams):
#             left = m
#         else:
#             right = m - 1
#     return left


# def check(m, checkparams):
#     K, wires = checkparams
#     return cnt >= K


# ans = right_bin_search(0, 10**11, check,  [K, wires])
# print(ans)
