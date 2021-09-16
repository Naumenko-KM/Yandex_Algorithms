nums_a = set(map(int, input().split()))
nums_b = set(map(int, input().split()))

print(*sorted([a for a in nums_a if a in nums_b]))