Lette = 'ABCD'
A = []

for i in Lette:
    for j in Lette:
        for k in Lette:
            if (i == 'A' and j=='D') or (j=='A' and (i == 'D' or k =='D')) or (k=='A' and j=='D'):
                s = i+j+k
                A.append(s)
print(A)
print(len(A))


