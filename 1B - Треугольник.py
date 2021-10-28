a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0:
    print('NO')
elif a < b+c and a > b-c and b < a+c and b > a-c and c < a+b and c > a-b:
    print('YES')
else:
    print('NO')
