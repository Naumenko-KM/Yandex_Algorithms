# Hard

from math import factorial
n, k = list(map(int, input().split()))
nums = sorted(list(map(int, input().split())))


def is_perm_valid(a, b, c, k):
    if max(a, b, c) / min(a, b, c) <= k:
        return True


def find_num_perms_slow(n, k, nums):
    perms_set = set()
    for i in range(n):
        for j in range(n):
            for m in range(n):
                if i == j or i == m or j == m:
                    continue
                elif is_perm_valid(nums[i], nums[j], nums[m], k):
                    perms_set.add((nums[i], nums[j], nums[m]))
    num_perms = len(perms_set)
    return num_perms


def calc_perms(nums):
    len_nums = len(nums)
    len_uniq = len(set(nums))
    dublicates = len_uniq - len_nums
    num_perms = (factorial(len_nums) / factorial(3) / factorial(len_nums-3))
    num_perms = int(num_perms - dublicates) * 6
    return num_perms


def find_num_perms_fast(n, k, nums):
    num_perms = 0
    m = 2
    for i in range(n-2):
        for j in range(m, n):
            if nums[j] / nums[i] <= k and \
               (j == n-1 or nums[j+1] / nums[i] > k):
                num_perms += calc_perms(nums[i:j+1])
                m = j + 1
                # print(n)
                # print(n, i, j, m)/
                break
            if j == n-1:
                m = i + 2
                break
    return num_perms


print(find_num_perms_fast(n, k, nums))
print(calc_perms([1, 1, 3, 4, 5]))
