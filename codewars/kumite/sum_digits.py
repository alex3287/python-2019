def sum_digits(number):
    sum_even = sum_odd = 0
    while number:
        digit = number % 10
        if digit % 2 == 0:
            sum_even += digit
        else: sum_odd += digit
        number //= 10
    return abs(sum_even - sum_odd)

print(sum_digits(0))

