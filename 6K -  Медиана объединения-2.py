# too much to do

# N, L = list(map(int, input().split()))
# sequences = []
# for _ in range(N):
#     sequences.append(list(map(int, input().split())))

# def slow(sequences, L):
#     for i, seq1 in enumerate(sequences[:-1]):
#         for seq2 in sequences[i+1:]:
#             seq3 = seq1 + seq2
#             seq3 = sorted(seq3)
#             print(seq3[L-1])


# slow(sequences, L)


# def left_bin_search(left, right, check, checkparams):
#     while left < right:
#         m = (left + right) // 2
#         if check(m, checkparams):
#             right = m
#         else:
#             left = m + 1
#     return left


# def check(m, checkparams):
#     seq1, seq2, L = checkparams
#     cnt = 0
#     for seq in sequences:
#         # cnt += wire // m
#     # return cnt >= K    