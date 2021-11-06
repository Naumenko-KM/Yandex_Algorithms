n, r = list(map(int, input().split()))
monuments = sorted(list(map(int, input().split())))


def find_distances(monuments):
    distances = [0] * len(monuments)
    for i in range(1, len(distances)):
        distances[i] = monuments[i] - monuments[i-1]
    return distances


def find_prefix_sum(distances):
    prefix_sum = [0] * (len(distances) + 1)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + distances[i-1]
    return prefix_sum


def rsq(prefixsum, x, y):
    result = prefixsum[y] - prefixsum[x]
    return result


def find_allperms(n, r, monuments):
    distances = find_distances(monuments)
    prefixsum = find_prefix_sum(distances)
    allperms = 0
    k = 0
    for i in range(1, n):
        for j in range(k, n+1):
            k = j
            if rsq(prefixsum, i, j) > r:
                allperms += n + 1 - j
                break
    return allperms


print(find_allperms(n, r, monuments))
