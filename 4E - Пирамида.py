n = int(input())
blocks = {}
for i in range(n):
    block = list(map(int, input().split()))
    if block[0] in blocks.keys():
        if blocks[block[0]] < block[1]:
            blocks[block[0]] = block[1]
    else:
        blocks[block[0]] = block[1]
height = 0
for key in blocks:
    height += blocks[key]
print(height)


