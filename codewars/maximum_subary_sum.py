def summa(array):
    m1 = -float('inf')
    m2 = -float('inf')
    for i in range(len(array)):
        if sum(array[i:])> m1:
            m1 =sum(array[i:])
        if sum(array[:len(array)-1-i]) > m2:
            m2 = sum(array[:len(array)-1-i])
    return m1, m2

def maxSequence(arr):
    if len(arr) < 1:
        return 0
    return None

print(summa([2,3,-8,2,2,2]))