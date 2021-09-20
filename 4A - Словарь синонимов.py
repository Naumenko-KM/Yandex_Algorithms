n = int(input())
synonims = {}
for i in range(n):
    a, b = list(input().split())
    synonims[a] = b
    synonims[b] = a
word = input()

print(synonims[word])
