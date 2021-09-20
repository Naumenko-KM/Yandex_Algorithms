with open('input.txt') as f:
    lines = f.read()
words = lines.split()
words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
max_cnt = max(words_dict.values())
max_cnt_words = [word for word in words_dict if words_dict[word] == max_cnt]
print(sorted(max_cnt_words)[0])