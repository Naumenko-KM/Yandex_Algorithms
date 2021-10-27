N = int(input())
tshorts_list = list(map(int, input().split()))
M = int(input())
jeans_list = list(map(int, input().split()))


jeans_ind = 0

tshort_best = tshorts_list[0]
jeans_best = jeans_list[0]

for i in range(N):
    if M != 1:
        for j in range(jeans_ind, M-1):
            if abs(tshorts_list[i] - jeans_list[j+1]) < abs(tshort_best-jeans_best):
                tshort_best = tshorts_list[i]
                jeans_best = jeans_list[j+1]
            if abs(tshorts_list[i] - jeans_list[j]) <= abs(tshorts_list[i] - jeans_list[j+1]):
                jeans_ind = j
                break
            if tshort_best == jeans_best:
                break

        if tshort_best == jeans_best:
            break
    else:
        if abs(tshorts_list[i] - jeans_list[0]) < abs(tshort_best-jeans_best):
            tshort_best = tshorts_list[i]
            jeans_best = jeans_list[0]

print(tshort_best, jeans_best)
