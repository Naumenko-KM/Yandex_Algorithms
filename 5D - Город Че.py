n, r = list(map(int, input().split()))
monuments = sorted(list(map(int, input().split())))


def finddistances(monuments):
    distances = [0] * len(monuments)
    for i in range(1, len(distances)):
        distances[i] = monuments[i] - monuments[i-1]
    return distances


def findprefixsum(distances):
    prefixsum = [0] * (len(distances) + 1)
    for i in range(1, len(prefixsum)):
        prefixsum[i] = prefixsum[i-1] + distances[i-1]
    return prefixsum


def rsq(prefixsum, x, y):
    result = prefixsum[y] - prefixsum[x]
    return result


def findallperms(n, r, monuments):
    distances = finddistances(monuments)
    prefixsum = findprefixsum(distances)
    allperms = 0
    k = 0
    for i in range(1, n):
        for j in range(k, n+1):
            k = j
            if rsq(prefixsum, i, j) > r:
                allperms += n + 1 - j
                break
    return allperms


print(findallperms(n, r, monuments))
