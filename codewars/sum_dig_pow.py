def check(number):
    n = len(str(number))
    summa=0
    number2=number
    while number2 > 0:
        summa += (number2 % 10)**n
        number2 //= 10
        n -= 1
    if number == summa:
        return True
    return False



def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    A=[]
    for i in range(a,b+1):
        if i < 10:
            A.append(i)
        elif check(i):
            A.append(i)
    return A

print(sum_dig_pow(40,136))
