A = [4, 6, 7, 4, -5, 8]
print(*A)
print(A[5])
print(A[-1])

A.append(0)
A[1] = 0
print(len(A))
print(A)

for i in A:
    print(i)

for i in range(len(A)):
    A[i] += 10
print(A)

s = 0
for i in A:
    s += i
print(s)
print('hello')
