
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A <= D and B <= E:
    print('YES')
elif A <= E and B <= D:
    print('YES')

elif A <= D and C <= E:
    print('YES')
elif A <= E and C <= D:
    print('YES')

elif B <= D and C <= E:
    print('YES')
elif B <= E and C <= D:
    print('YES')

else:
    print('NO')
