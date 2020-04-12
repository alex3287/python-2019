# команды исполнителя
# +1
# +5
# ^2
# c 2 до 26 проходящих через 5
A=[0]*26
A[0]=1
for i in range(1,26):
    if i == 24:
        A[i] = A[i-1] + A[i-5] + A[4]
    elif i > 8:
        A[i] = A[i-1] + A[i-5]
    elif i == 3:
        A[i] = A[i-1] + A[i-2]
    else:
        A[i] = A[i-1]
print(A)
