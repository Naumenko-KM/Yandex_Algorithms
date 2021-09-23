with open('input.txt') as f:
    lines = f.readlines()
n = len(lines)
db = {}
for line in lines:
    name, product, cnt = list(line.split())
    cnt = int(cnt)
    if name in db.keys():
        if product in db[name].keys():
            db[name][product] += cnt
        else:
            db[name][product] = cnt
    else:
        db[name] = {product: cnt}
for name in sorted(db.keys()):
    print(name+":")
    for product in sorted(db[name].keys()):
        print(product, db[name][product])

