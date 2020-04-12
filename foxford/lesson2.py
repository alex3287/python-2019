def perimeter(n):
    f = fib(n)
    return f * 4


def fib(n):
    A = [1, 1]
    if n < 3:
        return A[n - 1]
    for i in range(2, n + 1):
        A.append(A[i - 1] + A[i - 2])
    return sum(A)

print(perimeter(5))