N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))


def findcountsetsslow(K, nums):
    n = 0
    cur_sum = 0
    j = 0
    for i in range(N):
        cur_sum = nums[i]
        if cur_sum == K:
            n += 1
            # print(i, j)
            continue
        if cur_sum > K:
            continue

        k = i+1
        for j in range(k, N):
            cur_sum += nums[j]
            # print(i, j)
            if cur_sum > K:
                break
            if cur_sum == K:
                n += 1
                break
    return(n)


def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum


def rsq(prefixsum, x, y):
    return prefixsum[y] - prefixsum[x]


def findcountsetsfast(K, nums):
    prefixsum = makeprefixsum(nums)
    n = 0
    k = 1
    for i in range(len(prefixsum)):
        for j in range(k, len(prefixsum)):
            if prefixsum[j] - prefixsum[i] > K:
                # k = j
                break
            elif prefixsum[j] - prefixsum[i] == K:
                n += 1
                break
            k = j
    return n


print(findcountsetsfast(K, nums))
