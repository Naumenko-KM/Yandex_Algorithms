import math


K1, M, K2, P2, N2 = list(map(int, input().split()))

floors_on_staircase = math.ceil(K2/(M*(P2-1)+N2))
floors_entrance = floors_on_staircase * M

P1 = K1//floors_entrance + 1
N1 = (K1 - P1*(floors_entrance-1))%floors_on_staircase

if M == 1:
    P1 = 0
    N1 = 1
if N2 > M or P2 > K2/M:
    P1 = -1
    N1 = -1

print(P1, N1)


