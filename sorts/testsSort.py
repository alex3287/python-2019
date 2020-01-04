from quickSort import quick_sort
from bubbleSort import bubble_sort
from random import randint as rnd

def tests(sort_algoritm):
    print("testcase #1: ", end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    print('Ok' if sort_algoritm(A) == A_sorted else 'Fail')

tests(quick_sort)
# A = [rnd(-10,10) for i in range(10)]
# print(A)
# print(quick_sort(A))
# print(bubble_sort(A))
