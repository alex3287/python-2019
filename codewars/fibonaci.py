def fibonacci(n):
    if n in [0, 1]:
        return n
    Fib=[0,1]
    for i in range(2,n+1):
        Fib.append(Fib[i-1]+Fib[i-2])
    return Fib[-1]


print(fibonacci(500))
#Fib={0:0,1:56}
#print(Fib.setdefault(2,5))