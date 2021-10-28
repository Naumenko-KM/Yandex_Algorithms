n = int(input())
numbers = list(map(int, input().split()))
x = int(input())


def find_nearest(numbers, x):
    if numbers:
        nearest = numbers[0]
        for y in numbers:
            if abs(x - nearest) > abs(x - y):
                nearest = y
    return nearest


print(find_nearest(numbers, x))
