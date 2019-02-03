def variants(word):
    n = len(word)
    a = len(set(word))
    result = a ** n
    return result

def listPosition(word):
    if len(word) < 2:
        return 1
    return variants(word)


print(listPosition('1234567890QWERTASDFGZXCVB'))
