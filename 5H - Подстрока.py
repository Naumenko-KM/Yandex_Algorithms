#  WA test 5 failed


n, k = list(map(int, input().split()))
string = input()


def find_max_string(n, k, string):
    # print(string)
    sym_dict = {sym: 0 for sym in set(list(string))}
    m = 0
    max_i = 0
    max_j = 0
    sym_dict[string[0]] = 0
    for i in range(n):
        for j in range(m, n):
            # print(i, j)
            sym_dict[string[j]] += 1
            if sym_dict[string[j]] > k:
                sym_dict[string[j]] -= 1
                break
            else:
                if j - i + 1 > max_j - max_i:
                    # print('max!')
                    max_i = i
                    max_j = j + 1
            m = j

        sym_dict[string[i]] -= 1

    # print(sym_dict)
    return max_j - max_i, max_i + 1


def find_max_string_slow(n, k, string):
    max_i = 0
    max_j = 0
    for i in range(n):
        for j in range(n):
            if j < i:
                continue
            counts = dict()
            for sym in string:
                counts[sym] = counts.get(sym, 0) + 1
            if max(counts.values()) < k:
                if j - i + 1 > max_j - max_i:
                    # print('max!')
                    max_i = i
                    max_j = j + 1
    return max_j - max_i, max_i + 1


print(*find_max_string_slow(n, k, string))
