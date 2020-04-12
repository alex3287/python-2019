# 12. Integer to Roman
def intToRoman(num):
    roman = ''
    k = 0
    while num:
        digit = num %10
        if digit > 0:
            roman = translate(digit,k) + roman
        k+=1
        num //= 10
    return roman

def translate(digit,k):
    R = ['IVX','XLC','CDM']
    result = ''
    if k > 2:
        for i in range(digit):
            result += 'M'
    elif digit < 4:
        for i in range(digit):
            result += R[k][0]
    elif digit == 4:
        result += R[k][:2]
    elif digit == 5:
        result += R[k][1]
    elif digit > 5 and digit != 9:
        result += R[k][1] + translate(digit-5,k)
    else:
        result += R[k][0]+R[k][2]
    return result



