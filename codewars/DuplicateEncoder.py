def duplicate_encode(word):
    result=''
    word=word.lower()
    for i in word:
        if word.count(i.lower()) > 1:
            result+=')'
        else:
            result+='('
    return result

#print(duplicate_encode('Success'))
print('HjhHH'.lower())
