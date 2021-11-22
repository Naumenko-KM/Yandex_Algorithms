N, K = list(map(int, input().split()))
nums1 = sorted(list(map(int, input().split())))
nums2 = list(map(int, input().split()))


def left_bin_search(left, right, check, checkparams):
    while left < right:
        m = (left + right) // 2
        if check(m, checkparams):
            right = m
        else:
            left = m + 1
    return left


def check(m, checkparams):
    nums, k = checkparams
    return nums[m] >= k


for k in nums2:
    ans = left_bin_search(0, len(nums1) - 1, check,  [nums1, k])
    if nums1[ans] == k:
        print('YES')
    else:
        print('NO')
