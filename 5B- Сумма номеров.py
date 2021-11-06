N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))


def find_count_sets_slow(K, nums):
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


def find_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum


def rsq(prefix_sum, x, y):
    return prefix_sum[y] - prefix_sum[x]


def find_count_sets_fast(K, nums):
    prefix_sum = find_prefix_sum(nums)
    n = 0
    k = 1
    for i in range(len(prefix_sum)):
        for j in range(k, len(prefix_sum)):
            if prefix_sum[j] - prefix_sum[i] > K:
                # k = j
                break
            elif prefix_sum[j] - prefix_sum[i] == K:
                n += 1
                break
            k = j
    return n


print(find_count_sets_fast(K, nums))
