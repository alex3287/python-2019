def swap(dig,B):
    if min(B) == B[-1]:
        return dig, B
    dig, B[B.index(min(B))] = B[B.index(min(B))], dig
    return dig, B
            
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
            buf = min(B)
            B.remove(min(B))
            B+=A[-1]
            A=A[:-1]
            break
        B.append(A[-1])
        A=A[:-1]
    else:
        return -1
    
    if buf =='0':
        buf, B = swap(buf,B)
    B.sort(reverse=1)
    res = ('').join(A)+buf+('').join(B)
    result = int(res)
    return result 
    
if __name__ == '__main__':
    next_smaller(513)
    next_smaller(1207)
    B=['5','3','8','6','1','0','5']
    B.sort(reverse=1)
    print(B)
