# # 7 -> 58 2 3 5 4 1 29
# n = int(input())
# k = 0  # количество пар кратных 29
# A = []  # массив для хранения чисел
#
# # сохраним числа в массиве А
# for i in range(n):
#     x = int(input())  # числа вводимые пользователем
#     A.append(x)
#
# # найдем количество подходящих пар
# for i in range(n-4):
#     for j in range(i+4,n):
#         if A[i] * A[j] % 29 == 0:  # проверяем делится ли произведение на 29
#             k += 1
# print(k)

# задача 2

# 1 3
# 5 12
# 6 9
# 5 4
# 3 3
# 1 1

A = []  # массив для хранения чисел
smax = 0
for i in range(6):
    x, y = map(int, input().split())
    A.append([x, y])

for i in range(2):
    for j in range(2):
        for k in range(2):
            for h in range(2):
                for t in range(2):
                    for f in range(2):
                        s = A[0][i]+A[1][j] + A[2][k]+A[3][h] + A[4][t]+A[5][f]
                        if s % 3 != 0 and s > smax:
                            smax = s
print(smax)

