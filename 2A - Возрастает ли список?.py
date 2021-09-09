numbers = list(map(int, input().split()))

def is_growing(numbers):
    flag = 'YES'
    if numbers:
        for i in range(len(numbers)-1):
            x = numbers[i]
            y = numbers[i+1]
            if y > x:
                flag = 'YES'
            else:
                flag = 'NO' 
                break
    print(flag)

is_growing(numbers)