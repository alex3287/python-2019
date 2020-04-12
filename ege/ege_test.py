m = 120
# создаем фиксированный массив остатков
A = [0] * 120
first = 0  # первый элемент в паре
second = 0  # второй элемент в паре

n = int(input())
for i in range(n):
    x = int(input())  # новый элемент
    d = x % 120
    if d == 0:
        d = 120
    if A[m - d] > x and A[m-d] + x > first + second:
        first = A[m-d]
        second = x
    if x > A[d%120]:
        A[d%120] = x
print(first, second)

