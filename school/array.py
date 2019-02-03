from random import randrange as rnd

def create_array(number):
    return [rnd(10001) for i in range(number)]

def find(array):
    A = [i for i in array if 100 <= i <= 1000]
    return min(A) if A else 'No number'

if __name__ == '__main__':
    B = create_array(10)
    print(B)
    print(find(B))
