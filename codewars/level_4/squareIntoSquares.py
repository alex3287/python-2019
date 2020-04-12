def find(A, num):
    l = 0
    r = len(A)-1
    x = A[(r+l)//2]
    while x != num and r > l:
        if x > num:
            r = (r+l) // 2 - 1
        else:
            l = (r+l) // 2 + 1
        x = A[(r + l) // 2]
    if num < x:
        x = A[l-1]
    return x


def decompose(n):
    A = [i*i for i in range(1,n)]
    new_n = n*n
    result = []
    i = -1
    x = A[i]
    while new_n > 0 and len(A) > (n-1) // 2:
        result = [int(x**0.5)] + result
        new_n -= x
        if new_n:
            x = find(A, new_n)
            if int(x**0.5) in result:
                result.clear()
                new_n = n*n
                A = A[:len(A) - 1]
                i = -1
                x = A[i]
    if new_n:
        return None
    else:
        return result

print(decompose(12))
# A = [i*i for i in range(2, 10, 2)]
# print(A)
# print(find(A, 25))