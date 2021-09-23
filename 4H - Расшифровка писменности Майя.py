# Time limit

with open('input.txt') as f:
    lines = f.readlines()

lenW, lenS = list(map(int, lines[0].split()))
word = lines[1][:-1]
syms = lines[2]


def is_word_in_syms(word_dict, syms_dict):
    cnt = 0
    for letter in word_dict:
        if letter in syms_dict.keys():
            if word_dict[letter] == syms_dict[letter]:
                cnt += 1
    if cnt == len(word_dict):
        return 1
    else:
        return 0


word_dict = {i: 0 for i in word}


for letter in word:
    word_dict[letter] += 1

syms_dict = {i: 0 for i in syms}
for letter in syms[0:lenW]:
    syms_dict[letter] += 1


cnt = is_word_in_syms(word_dict, syms_dict)

for i in range(1, lenS-lenW+1):
    syms_dict[syms[i+lenW-1]] += 1
    syms_dict[syms[i-1]] -= 1
    cnt += is_word_in_syms(word_dict, syms_dict)
print(cnt)


