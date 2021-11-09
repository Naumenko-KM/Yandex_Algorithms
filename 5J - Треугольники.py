# TL error

n = int(input())
points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))


def is_triangle_isosceles(a, b, c):

    def calc_len(a, b):
        return ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5

    ab_len = calc_len(a, b)
    ac_len = calc_len(a, c)
    bc_len = calc_len(b, c)

    if (a[0] == b[0] and a[0] == c[0] and b[0] == c[0]) or \
       (a[1] == b[1] and a[1] == c[1] and b[1] == c[1]):
        return False
    elif ab_len == ac_len or ab_len == bc_len or ac_len == bc_len:
        return True
    else:
        return False


def find_all_triangles_slow(points):
    num = 0
    triangles = set()
    for i in range(len(points)):
        for j in range(len(points)):
            for k in range(len(points)):
                if i == j or i == k or j == k:
                    continue
                triangle = tuple(sorted([points[i], points[j], points[k]]))
                if is_triangle_isosceles(points[i], points[j], points[k]) and \
                   triangle not in triangles:
                    triangles.add(triangle)
                    num += 1
    return num


print(find_all_triangles_slow(points))
