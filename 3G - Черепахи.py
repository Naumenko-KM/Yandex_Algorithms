n = int(input())
turtles = set()
for i in range(n):
    turtles.add(tuple(map(int, input().split())))
turtles_vars = set([(n-i-1,i) for i in range(n)])
cnt = 0
for turtle in turtles:
    if turtle in turtles_vars:
        cnt += 1
print(cnt)

