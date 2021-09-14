numbers = list(map(int, input().split()))

def find_max_mult(numbers):

    if len(numbers) >= 6:
        n = 6
        abs_numbers = []
        for i in range(3):
            max_num = max(numbers)
            min_num = min(numbers)
            abs_numbers.append(max_num)
            abs_numbers.append(min_num)
            numbers.remove(max_num)
            numbers.remove(min_num)
    else:
        n = len(numbers)
        abs_numbers = numbers
    
    max_mult = float('-inf')
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:
                    continue
                max_mult_new = abs_numbers[i] * abs_numbers[j] * abs_numbers[k]
                if max_mult_new > max_mult:
                    num1, num2, num3 = abs_numbers[i], abs_numbers[j], abs_numbers[k]
                    max_mult = max_mult_new
    return num1, num2, num3            

print(*find_max_mult(numbers))