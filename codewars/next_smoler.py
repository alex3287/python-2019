def check(digit,A):
    for i in A:
        if digit > i and i != '0':
            return False
    return True

def next_smaller(n):
    if n < 21:
        return -1
    if (20 < n < 100):
        if (n%10 == 0) or (n%10 > n // 10):
            return -1
        return n%10 * 10 + n//10
    A = list(str(n))
    B=[A[-1]]
    A=A[:-1]
    while A:
        if A[-1] > min(B) and not(len(A)==1 and check(A[-1],B)):
            break
        B.append(A[-1])
        A=A[:-1]
    else:
        return -1
    if len(A) > 1 and len(B) > 1:
        if min(B)=='0' and check(A[-1],B):
            B[B.index(min(B))],B[0] = B[0],B[B.index(min(B))]
            if (B[0]=='0' or B[1] == '0') and not(check(B[0],B)):
                B = sorted(B,reverse=True)
        res = ('').join(A[:-1])+B[0]+A[-1]+('').join(B[1:])
        result = int(res)
        return result
    if len(A) == 1 and len(B)>1 or A[-1] == max(B):
        for i in range(len(B)):
            if A[-1] > B[i] and B[i] != '0':
                A[-1],B[i] = B[i],A[-1]
                break
        else:
            return -1
        res = ('').join(A[:])+('').join(B[:])
        result = int(res)
        return result
    res = ('').join(A[:-1])+B[0]+A[-1]
    result = int(res)
    return result
    
if __name__ == '__main__':
    print(next_smaller(1207))
