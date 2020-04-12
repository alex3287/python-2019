from random import randint as rnd

n = int(input())
m = 120
# A = []   # массив для хранения чисел
A = [rnd(50, 200) for i in range(n)]
print(A)
first = 0  # первый элемент в паре
second = 0  # второй элемет в паре

# сохраняем элементы в списке
# for i in range(n):
#     number = int(input())  # очередное число вводимое пользователем
#     A.append(number)

# нахождение элементов
for i in range(n-1):
    for j in range(i+1, n):
        if A[i] > A[j] and (A[i] + A[j]) % 120 == 0:
            print(A[i], A[j])

# print(first, second)