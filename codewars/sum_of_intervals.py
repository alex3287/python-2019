def sum_of_intervals(intervals):
    A=[list(i) for i in intervals]
    A = sorted(A)
    litl = A[0][0]
    big = A[0][1]
    summa = 0
    A = A[1:]
    while A:
        mini = A[0]
        if mini[0] < big and mini[1] > big:
            big = mini[1]
            A.remove(mini)
        elif litl <= mini[0] <= big and litl <= mini[1] <= big:
            A.remove(mini)
        else:
            summa += big - litl
            big,litl = mini[1],mini[0]
            A.remove(mini)
    summa += big - litl
    return summa

#print(sum_of_intervals([[1,5],[10,20],[1,6],[16,19],[5,11]]))
print(sum_of_intervals([[100,102],[5,7],[500,501],[99,100],[111,113]]))
#print(sum_of_intervals([[4,6],[8,10],[9,15],[16,20]]))
#print(sum_of_intervals([[4,6]]))
#B=[[1,5],[10,20],[1,6],[16,19],[5,11]]
#C=sorted(B)
#print(C)