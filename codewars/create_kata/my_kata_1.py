def sum_max_min(n):
    if -10 < n < 10:
        return 0
    maxi = -1
    mini = 10
    n = abs(n)
    while n:
        if maxi < n % 10: maxi = n % 10
        if mini > n % 10: mini = n % 10
        n //= 10
    if maxi == mini:
        return -1
    return maxi + mini

if __name__ == '__main__':
    print(sum_max_min(10))