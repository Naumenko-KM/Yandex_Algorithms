import random


def findbestpairslow(N, tshorts_list, M, jeans_list):
    tshort_best = tshorts_list[0]
    jeans_best = jeans_list[0]

    for i in range(N):
        for j in range(M):
            if abs(tshorts_list[i] - jeans_list[j]) < \
                    abs(tshort_best - jeans_best):
                tshort_best = tshorts_list[i]
                jeans_best = jeans_list[j]
    return tshort_best, jeans_best


def findbestpairfast(N, tshorts_list, M, jeans_list):
    jeans_ind = 0
    tshort_best = tshorts_list[0]
    jeans_best = jeans_list[0]

    for i in range(N):
        for j in range(jeans_ind, M):
            if abs(tshorts_list[i] - jeans_list[j]) < \
                    abs(tshort_best - jeans_best):
                tshort_best = tshorts_list[i]
                jeans_best = jeans_list[j]

            if j != M-1 and (abs(tshorts_list[i] - jeans_list[j]) <=
                             abs(tshorts_list[i] - jeans_list[j+1])):
                jeans_ind = j
                break
            else:
                jeans_ind = j

    return(tshort_best, jeans_best)


def checking(N, M):
    for i in range(1, N):
        for j in range(1, M):
            tshorts_list = [random.randint(1, 100) for iter in range(i)]
            tshorts_list = sorted(list(dict.fromkeys(tshorts_list)))

            jeans_list = [random.randint(1, 100) for iter in range(j)]
            jeans_list = sorted(list(dict.fromkeys(jeans_list)))

            slow = findbestpairslow(len(tshorts_list), tshorts_list,
                                    len(jeans_list), jeans_list)
            fast = findbestpairfast(len(tshorts_list), tshorts_list,
                                    len(jeans_list), jeans_list)

            if abs(slow[0]-slow[1]) != abs(fast[0]-fast[1]):
                print(tshorts_list)
                print(jeans_list)
                print()
                break


n = 20
checking(n, n)

# N = int(input())
# tshorts_list = list(map(int, input().split()))
# M = int(input())
# jeans_list = list(map(int, input().split()))

# print(*findbestpairfast(N, tshorts_list, M, jeans_list))
