n = int(input())  # количество чисел
mini = 1001  # минимальное число
ch = 1001  # минимальное четное число
min_p = 1001 * 1001  # минимальное четное произведение
s = 6  # количество элементов в массиве
A = [0] * s  # массив из 6 элементов

# считывание первых 6 элементов и заполнение их в массив
for i in range(s):
    x = int(input())  # числа вводимы пользователем
    A[i] = x

# считываем остальные элементы
for i in range(s, n):
    x = int(input())  # числа вводимы пользователем
    # ищем минимальное число
    if A[i % s] < mini:
        mini = A[i % s]
    # ищем минимальное четное число
    if A[i % s] % 2 == 0 and A[i % s] < ch:
        ch = A[i % s]
    # ищем минимальное четное произведение
    if x % 2 == 0:
        if mini * x < min_p:
            min_p = mini * x
    else:
        if ch < 1001 and ch * x < min_p:
            min_p = ch * x
    # добавляем Х в массив
    A[i % s] = x

if min_p == 1001*1001:
    print(-1)
else:
    print(min_p)