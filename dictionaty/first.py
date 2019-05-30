test = {i:i*2 for i in range(10)}

def check_item(test,item):
    if test.get(item):
        print('Ok')
    else:
        test[item] = item ** 2
        print('add item')


check_item(test, 10)

print(test)

