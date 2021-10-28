cnt_a, cnt_b = list(map(int, input().split()))

cubes_a = set()
cubes_b = set()
for _ in range(cnt_a):
    cubes_a.add(int(input()))
for _ in range(cnt_b):
    cubes_b.add(int(input()))


a_b_cubes = sorted([cube for cube in cubes_a if cube in cubes_b])
only_a_cubes = sorted([cube for cube in cubes_a if cube not in cubes_b])
only_b_cubes = sorted([cube for cube in cubes_b if cube not in cubes_a])
print(len(a_b_cubes))
print(*a_b_cubes)
print(len(only_a_cubes))
print(*only_a_cubes)
print(len(only_b_cubes))
print(*only_b_cubes)
