def f(x):
    if x > 1:
        return x % 2 * f(x // 2)
    else:
        return x
k = 0

#a = int(input())
for j in range(101):
    k = 0
    for i in range(1, j+1):
        if f(i) == 1:
            k +=1
    if k == 4:
        print(j)
