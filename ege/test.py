A = [i for i in range(0, 21, 2)]
print(A)
s = 0
n = 10
for i in range(1, n+1):
    if i == n - i:
        s = s + A[i] + A[i+1]
print(s)