'''
  j ->  0 1 2 3
i ->  0 5 6 6 7
      1 0 5 6 7
      2 0 0 5 6
      3 0 0 0 5

основные понятия:
1. главная диаганаль
2. вспомогательная (побочная)
3. элементы выше
4. элементы на главной диагонали
'''


from random import randint as rnd

n = rnd(3,5)

A = [[rnd(0,9) for i in range(n)] for j in range(n)]
#print(A)

#A = [[0]*4 for j in range(4)]
for i in A:
    print(*i)


#1. главная диаганаль сумма

def sumD(A):
    s = 0
    for i in range(len(A)):
        s += A[i][i]
    return s

print(sumD(A))

def sumUp(A):
    s = 0
    n = len(A)
    for i in range(n):
        for j in range(n):
            if j > i:
                s += A[i][j]
    return s

print(sumUp(A))
