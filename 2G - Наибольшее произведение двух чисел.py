numbers = list(map(int, input().split()))


def find_max_mult(numbers):

    max1 = max(numbers)
    numbers2 = numbers.copy()
    numbers2.remove(max1)
    max2 = max(numbers2)

    min1 = min(numbers)
    numbers2 = numbers.copy()
    numbers2.remove(min1)
    min2 = min(numbers2)

    if max1*max2 > min1*min2:
        if max2 > max1:
            return max1, max2
        else:
            return max2, max1
    else:
        if min2 > min1:
            return min1, min2
        else:
            return min2, min2


print(*find_max_mult(numbers))
