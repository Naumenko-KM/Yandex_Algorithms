x, y, z = list(map(str, input().split()))
N = int(input())

nums = set(str(N))


print(len([num for num in nums if num not in (x, y, z)]))