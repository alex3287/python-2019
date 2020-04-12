class RomanNumerals(object):

    def to_roman(self, number):
        S = ('IVX','XLC','CDM')
        def translate(digit, k):
            result=''
            if k > 2:
                for i in range(digit):
                    result += 'M'
                return result
            if digit < 4:
                for i in range(digit):
                    result += S[k][0]
            elif digit == 4:
                result += S[k][:2]
            elif digit == 5:
                result += S[k][1]
            elif 5 < digit < 9:
                result += S[k][1] + translate(digit-5, k)
            elif digit == 0:
                pass
            else:
                result +=S[k][0]+S[k][2]
            return result
        roman = ''
        k=0
        while number:
            digit = number % 10
            if digit > 0:
                roman =translate(digit,k) + roman
            number //= 10
            k += 1
        return roman


    def from_roman(self, roman):
        SS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for i in range(len(roman)):
            if i < len(roman)-1:
                if SS[roman[i]] < SS[roman[i+1]]:
                    number -= SS[roman[i]]
                    flag = 1
                    continue
            number += SS[roman[i]]
        return number


if __name__ == '__main__':
    #SS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #print(SS['I'] < SS['V'])
    #test = RomanNumerals()
    print(RomanNumerals().from_roman('M'))
    print(RomanNumerals().to_roman(1000))