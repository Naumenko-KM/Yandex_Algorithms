n = int(input())
rooms = sorted(list(map(int, input().split())))
m = int(input())
conds = []
for _ in range(m):
    conds.append(tuple(map(int, input().split())))
conds = sorted(conds, key=lambda x: x[1])


def calc_conds_price(rooms, conds):
    price = 0
    k = 0
    for i in range(len(rooms)):
        for j in range(k, len(conds)):
            k = j
            if conds[j][0] >= rooms[i]:
                price += conds[j][1]
                break
    return price


print(calc_conds_price(rooms, conds))
