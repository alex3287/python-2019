class RomanNumerals(object):

    def to_roman(self, number):
        def translate(digit,k):
            #SS = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 50: 'L',
             #     100: 'C', 500: 'D', 1000: 'M'}
            S1 = 'IVX'
            S2 = 'XLC'
            S3 = 'CDM'


        roman = ''
        k=1
        while number:
            digit = number % 10
            if digit > 0:
                roman =translate(digit,k) + roman
            number //= 10
            k*=10
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