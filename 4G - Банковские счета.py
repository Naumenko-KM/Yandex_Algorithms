# Test 5 failed
import math

with open('input.txt') as f:
    queries = f.readlines()
db = {}
for line in queries:
    operation = list(line.split())

    if operation[0] == 'DEPOSIT':
        if operation[1] in db.keys():
            db[operation[1]] += int(operation[2])
        else:
            db[operation[1]] = int(operation[2])

    elif operation[0] == 'INCOME':
        for key in db.keys():
            if db[key] > 0:
                db[key] = math.ceil(db[key]*(1+int(operation[1])/100))

    elif operation[0] == 'BALANCE':
        if operation[1] in db.keys():
            print(db[operation[1]])
        else:
            [print("ERROR")]

    elif operation[0] == 'TRANSFER':
        for name in [operation[1], operation[2]]:
            if name not in db.keys():
                db[name] = 0
        db[operation[1]] -= int(operation[3])
        db[operation[2]] += int(operation[3])

    else:
        if operation[1] in db.keys():
            db[operation[1]] -= int(operation[2])
        else:
            db[operation[1]] = -int(operation[2])
