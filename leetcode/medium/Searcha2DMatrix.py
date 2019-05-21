# task accepted
from random import randint as rnd

def searchMatrix(matrix, target):
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return False
    m = len(matrix)
    n = len(matrix[0])
    if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
        return False
    for i in matrix:
        if target in i:
            return True
    return False

# my test
if __name__ == '__main__':
    size1= rnd(2,10)
    M = [[rnd(1,9) for i in range(size1)] for j in range(rnd(2,10))]

    for i in M:
        print(i)
    print(searchMatrix(M,4))