a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == c**2:
        sol = 'MANY SOLUTIONS'
    else:
        sol = 'NO SOLUTION'
elif c < 0:
    sol = 'NO SOLUTION'
else:
    sol = (c**2 - b)/a
    if int(sol) != sol:
        sol = 'NO SOLUTION'

print(sol)


