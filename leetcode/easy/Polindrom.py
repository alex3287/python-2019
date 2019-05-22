def isPalindrome(x):
    if x < 0: return False
    if str(x) == str(x)[::-1]:
        return True
    return False

if __name__ == '__main__':
    print(isPalindrome(-121))
