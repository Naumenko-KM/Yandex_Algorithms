num = input()
num1 = input()
num2 = input()
num3 = input()


def format_num(number):
    number = number.replace('(','')
    number = number.replace(')','')
    number = number.replace('-','')
    
    if len(number) == 12:
        number = number[2:]
    elif len(number) == 11:
        number = number[1:]
    elif len(number) == 7:
        number = '495' + number
    else:
        print('Error')

    return number 

num1 = format_num(num1)
num2 = format_num(num2)
num3 = format_num(num3)
num = format_num(num)

def is_equel(number1,number2):
    if number1 == number2:
        print('YES')
    else:
        print('NO')

is_equel(num,num1)
is_equel(num,num2)
is_equel(num,num3)
