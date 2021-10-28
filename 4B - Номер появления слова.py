with open('input.txt') as f:
    lines = f.read()
words_dict = {}
cnt_words = []
for word in lines.split():
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 0
    cnt_words.append(words_dict[word])
print(*cnt_words)
