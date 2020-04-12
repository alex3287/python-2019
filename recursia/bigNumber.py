from random import randint as rnd

def bigNum(A):
    if len(A) < 1:
        return 'List Empty'
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return A[0] if A[0] > A[1] else A[1]

    return bigNum([bigNum(A[:2])]+A[2:])

if __name__ == '__main__':
    A = [rnd(-1000, 1000) for i in range(100)]
    B = []
    print(A)
    print(bigNum(A))