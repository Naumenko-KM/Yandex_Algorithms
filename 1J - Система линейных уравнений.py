a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

det = a*d - b*c
detx = e*d - f*b
dety = a*f - c*e

if a == 0 and b == 0 and c == 0 and d == 0:
    print(5)

elif b == 0 and d == 0:
        print(3, e/a)

elif a == 0 and c == 0:
        print(4, e/b)

# elif b == 0 and d == 0:
#     if a == 0:
#         print(3, f/c)
#     else:
#         print(3, e/a)

# elif a == 0 and c == 0:
#     if b == 0:
#         print(3, f/d)
#     else:
#     	print(3, e/b)

elif det != 0:
    x = detx / det
    y = dety / det
    print(2, x, y)

elif det == 0 and detx != 0:
    print(0)

elif det == 0 and dety != 0:
    print(0)

elif det == 0 and detx == 0 and dety == 0:
    if b == 0:
        print(1, -c/d, f/d)
    else:
        print(1, -a/b, e/b)