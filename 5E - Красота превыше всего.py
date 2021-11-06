# timelimit error

import random


N, K = list(map(int, input().split()))
trees = list(map(int, input().split()))


def is_segment_full(segment, classes):
    if set(segment) == classes:
        return True
    else:
        return False


def find_shortest_segment_slow(N, trees):
    i_best = 1
    j_best = len(trees)
    classes = set(trees)
    for i in range(N):
        for j in range(N):
            if i > j:
                continue
            segment = trees[i:j+1]
            if is_segment_full(segment, classes):
                if j - i < j_best - i_best:
                    i_best = i + 1
                    j_best = j + 1
    return i_best, j_best




def find_shortest_segment_fast(N, trees):
    classes = set(trees)
    i_best = 1
    j_best = len(trees)
    k = 0
    for i in range(N):
        for j in range(k, N):
            k = j
            segment = trees[i:j+1]
            if is_segment_full(segment, classes):
                if j - i < j_best - i_best:
                    i_best = i + 1
                    j_best = j + 1
                break
    return i_best, j_best


def checking(N, K):
    for i in range(1, N):
        for j in range(1, K):
            trees = [random.randint(1, K+1) for _ in range(N)]

            slow = find_shortest_segment_slow(N, trees)
            fast = find_shortest_segment_fast(N, trees)

            if abs(slow[1]-slow[0]) != abs(fast[1]-fast[0]):
                print(N, K, trees)
                print(slow)
                print(fast)
                print()
                break


# N = 10
# K = 5
# checking(N, K)

# print(*find_shortest_segment_slow(N, trees))
print(*find_shortest_segment_fast(N, trees))
