N, M, K = list(map(int, input().split()))
mines = []
for i in range(K):
    mines.append(list(map(int, input().split())))

field = []
for i in range(N):
    field.append([0 for i in range(M)])

for mine in mines:
    x = mine[0] - 1
    y = mine[1] - 1
    field[x][y] = '*'

for i in range(N):
    for j in range(M):
        n_mines = 0
        if field[i][j] != '*':
            for x in [i-1, i, i+1]:
                for y in [j-1, j, j+1]:
                    if x < 0 or y < 0 or x > N-1 or y > M-1:
                        continue
                    else:
                        if field[x][y] == '*':
                            n_mines += 1

            field[i][j] = n_mines

for i in range(N):
    print(*field[i])
