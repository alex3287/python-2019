a = []
size = 6
for i in range(size):
    x = int(input('x-> '))
    y = int(input('y-> '))
    a.append([x, y])
smax = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            for m in range(2):
                for t in range(2):
                    for h in range(2):
                        s = a[0][i] + a[1][j] + a[2][k] + a[3][m] + a[4][t] + a[5][h]
                        if s % 3 != 0 and s > smax:
                            smax = s
print(smax)