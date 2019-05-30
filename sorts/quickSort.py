from random import randint as rnd, choice

def sort(A):
    if len(A) < 2:
        return A
    item = choice(A)
    L = [i for i in A if i < item]
    M = [i for i in A if i == item]
    R = [i for i in A if i > item]
    return sort(L) + M + sort(R)



if __name__ == '__main__':
    A = [rnd(-100,100) for i in range(10)]
    print(A)
    print(sorted(A))
    print(sort(A))