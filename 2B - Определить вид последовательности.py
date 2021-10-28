numbers = []
while True:
    x = int(input())
    if x == -2*10**9:
        break
    numbers.append(x)


def what_a_numbers(numbers):
    flag = 'NO'
    if numbers:
        for i in range(len(numbers)-1):
            x = numbers[i]
            y = numbers[i+1]
            if y == x:
                if flag == 'CONSTANT' or flag == 'NO':
                    flag = 'CONSTANT'
                elif flag == 'WEAKLY ASCENDING' or flag == 'ASCENDING':
                    flag = 'WEAKLY ASCENDING'
                elif flag == 'WEAKLY DESCENDING' or flag == 'DESCENDING':
                    flag = 'WEAKLY DESCENDING'
                else:
                    flag = 'RANDOM'
            elif y > x:
                if flag == 'ASCENDING' or flag == 'NO':
                    flag = 'ASCENDING'
                elif flag == 'WEAKLY ASCENDING' or flag == 'CONSTANT':
                    flag = 'WEAKLY ASCENDING'
                else:
                    flag = 'RANDOM'
            elif y < x:
                if flag == 'DESCENDING' or flag == 'NO':
                    flag = 'DESCENDING'
                elif flag == 'WEAKLY DESCENDING' or flag == 'CONSTANT':
                    flag = 'WEAKLY DESCENDING'
                else:
                    flag = 'RANDOM'
    if flag == 'NO':
        flag = 'RANDOM'

    return flag


print(what_a_numbers(numbers))
