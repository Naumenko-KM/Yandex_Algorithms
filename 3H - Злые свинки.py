n = int(input())
birds = set()
for i in range(n):
    birds.add(tuple(map(int, input().split()))[0])
print(len(birds))
