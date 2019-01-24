#тут описание ката, а ниже его тесты
Description:
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."

#тут тесты с сайта codewars.com для ката
@Test.describe("Basic tests")
def  basicTests():
    test.assert_equals(next_smaller(21),        12)
    test.assert_equals(next_smaller(907),       790)
    test.assert_equals(next_smaller(531),       513)
    test.assert_equals(next_smaller(1027),      -1)
    test.assert_equals(next_smaller(441),       414)
    test.assert_equals(next_smaller(123456798), 123456789)


@Test.describe("Extended tests")
def extendedTests():

    @Test.it("Short ones")
    def short():
        test.assert_equals(next_smaller(513),             351)
        test.assert_equals(next_smaller(351),             315)
        test.assert_equals(next_smaller(315),             153)
        test.assert_equals(next_smaller(153),             135)
        test.assert_equals(next_smaller(135),             -1)
        test.assert_equals(next_smaller(100),             -1)
        test.assert_equals(next_smaller(2071),            2017)
        test.assert_equals(next_smaller(1207),            1072)
        test.assert_equals(next_smaller(414),             144)
            
            
    @Test.it("Longer ones")
    def long():
        test.assert_equals(next_smaller(123456789),       -1)
        test.assert_equals(next_smaller(29009),           20990)
        test.assert_equals(next_smaller(1234567908),      1234567890)
        test.assert_equals(next_smaller(9999999999),      -1)
        test.assert_equals(next_smaller(59884848483559),  59884848459853)
        test.assert_equals(next_smaller(1023456789),      -1)
        test.assert_equals(next_smaller(51226262651257),  51226262627551)
        test.assert_equals(next_smaller(202233445566),    -1)
        test.assert_equals(next_smaller(506789),          -1)



@Test.it("Random tests")
def rndom():
    
    from random import random
    from math import exp
    from operator import itemgetter

    def refSol(n):
        s        = str(n)
        LR_Pairs = list(enumerate(zip(s,s[1:])))
        iP,pivot = next( ((i,l) for i,(l,r) in reversed(LR_Pairs) if l>r), (-1,-1) )
        
        if iP == -1: return -1
        
        iM,m = max( ((i,c) for i,c in enumerate(s[iP+1:],iP+1) if c < pivot), key=itemgetter(1))
        s    = s[:iP] + m + ''.join(sorted(s[iP:iM]+s[iM+1:], reverse=True))
        
        return int(s) if s[0] != '0' else -1
    
    
    for r in range(500):
        n = round(exp(43*random()))
        if r%5:                                                    # Create a huge delta, to disable iterative algorythms
            s = str(n)
            n = n*10**len(s) + int(''.join(sorted(s)))
            
        expected = refSol(n)
        #print(n-expected)
        
        test.assert_equals(next_smaller(n), expected)