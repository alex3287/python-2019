# записи
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 3000, 'job': 'def'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 7000, 'job': 'hdw'}
tom = {'name': 'Tom Li', 'age': 32, 'pay': 5000, 'job': 'None'}

# база данных
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>', db[key])