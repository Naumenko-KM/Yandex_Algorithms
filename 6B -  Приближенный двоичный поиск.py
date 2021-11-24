N, K = list(map(int, input().split()))
nums1 = list(map(int, input().split()))
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
    if k >= nums1[-1]:
        print(nums1[-1])
    elif k <= nums1[0]:
        print(nums1[0])
    else:
        index = left_bin_search(0, len(nums1) - 1, check,  [nums1, k])
        if abs(nums1[index-1] - k) <= abs(nums1[index] - k):
            print(nums1[index-1])
        else:
            print(nums1[index])
