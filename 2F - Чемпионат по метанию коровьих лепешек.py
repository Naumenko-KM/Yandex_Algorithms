numbers = list(map(int, input().split()))


def bigger_then_neighbors(numbers):
    count = 0
    if len(numbers) > 2:
        for i in range(len(numbers)-2):
            if numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]:
                count += 1
    return count 

print(bigger_then_neighbors(numbers))