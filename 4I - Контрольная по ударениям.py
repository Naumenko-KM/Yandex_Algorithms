N = int(input())
right_words = []
right_words_lower = []
for i in range(N):
    word = input()
    right_words.append(word)
    right_words_lower.append(word.lower())
words = list(input().split())

cnt = 0

# print(right_words)
# print(right_words_lower)
for word in words:
    upper=0
    lower=0
    for i in range(len(word)):
      #to lower case letter
        if(word[i]>='a' and word[i]<='z'):
            lower+=1
      #to upper case letter
        elif(word[i]>='A' and word[i]<='Z'):
            upper+=1
    # print(word)
    if word not in right_words and word.lower() in right_words_lower:
        cnt += 1
    elif upper != 1:
        cnt += 1
print(cnt)