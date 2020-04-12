from random import randint as rnd
def removeElement(nums,val):
    n = nums.count(val)
    for i in range(n):
        nums.remove(val)
    #return nums

if __name__ == '__main__':
    A = [rnd(0,10) for i in range(15)]
    A[2] = 4
    print(A)
    print(removeElement(A, 4))