N, L = list(map(int, input().split()))
sequences = []
for _ in range(N):
    sequences.append(list(map(int, input().split())))

def slow(sequences, L):
    for i, seq1 in enumerate(sequences[:-1]):
        for seq2 in sequences[i+1:]:
            seq3 = seq1 + seq2
            seq3 = sorted(seq3)
            print(seq3[L-1])


slow(sequences, L)