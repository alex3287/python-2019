# 767. Reorganize String
# Input: S = "aab"
# Output: "aba"

def max_dic(D):
    m = 0
    for i in D:
        if D[i] > m:
            m = D[i]
    return m

def reorganizeString(S):
    Letters = {}
    for i in S:
        Letters.setdefault(i , 0)
        Letters[i] += 1
    return Letters


S = 'aaabcdd'
print(reorganizeString(S))
print(max_dic(reorganizeString(S)))

F = reorganizeString(S)
m = 0
for i in F:
    if F[i] > m:
         m = F[i]
print(i)
