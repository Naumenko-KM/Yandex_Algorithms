n = input()
seq = list(map(int, input().split()))

def is_symmetric(seq):
    if seq == seq[::-1]:
        return True
    else:
        return False


def how_many_numbers_add(seq):
    seq_add =[]
    s = 1
    for i in range(len(seq)+1):
        if is_symmetric(seq+seq_add):
            print(len(seq_add))
            print(*seq_add)
            break
        else:
            seq_add = [seq[i]] + seq_add
	  	  	
	  	
how_many_numbers_add(seq)