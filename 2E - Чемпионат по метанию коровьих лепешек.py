# Test 9 failed 
n = int(input())
numbers = list(map(int, input().split()))


def find_max_place(numbers):
    vasya_place = 0
    vasya_value = 0
    if len(numbers) > 2:
        max_value = max(numbers)
        max_index = numbers.index(max_value)
        min_value = min(numbers)
        min_index = numbers.index(min_value)

        for i in range(min_index-1, len(numbers)-1):
            if max_index < i and numbers[i+1] == min_value:
                if numbers[i]%5 == 0 and (numbers[i]/5)%2==1:
                    if numbers[i] > vasya_value:
                        vasya_value = numbers[i]

        if vasya_value != 0:
            vasya_place = 1
            for value in numbers:
                if value > vasya_value:
                    vasya_place += 1
    return vasya_place 

print(find_max_place(numbers))