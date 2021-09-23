g, S = list(map(int, input().split()))
word = input()
syms = input()

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

all_words = [word for word in all_perms(word)]

cnt = 0
for word in all_words:
    cnt += syms.count(word)
print(cnt)
