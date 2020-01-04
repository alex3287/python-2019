#5436378
def maxi(num):
    m=10
    while num > 0:
        temp = num % 10
        if temp > m:
            m = temp
        num //= 10
    return m

number = int(input('-> '))
print(maxi(number))

