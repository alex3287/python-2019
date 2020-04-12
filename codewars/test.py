def fuc(n):
    e = 2.718282
    n = 20
    Z = 1
    x = 0.1
    for k in range(1,n+1):
        Z = Z * ((e**(0.6 - k) + 3) / (x**k + x**(2 * k - 1))**0.5)
    return Z

print(fuc(5))