import shelve

name = input('Enter your name -> ')
age = int(input('Enter your age -> '))
pay = int(input('Enter your pay -> '))
job = input('Enter your job -> ')

new = name.split()[0].lower()
data = {'name': name, 'age': age, 'pay': pay, 'job': job}
# print(new)
# print(data)

db = shelve.open('people-shelve')
db[new] = data
db.close()
