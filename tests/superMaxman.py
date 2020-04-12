from random import randint as rnd
import time

def fuc():
    print('Fuck')
    time.sleep(1)
    print('you!!!!!')
    time.sleep(1)
    print('Virus!!!')
    time.sleep(1)
    print('AAAAAAAAAAA!!!!')
    time.sleep(1)
    while True:
        print('Fuck you!!!!!!\nVirus!!!!!!')

print('hello, my old monkey!!!! \nLet\'s talk?')
name = input('What is your name? \n(Enter your name and press ENTER)\n-> ')
print('Hello, monkey', name+'!')
game = input('Let\'s play? (write yes/no)\nif you choose no, you will regret\n-> ')
if game.lower() == 'yes':
    print('''A game called rock scissors paper 
            Make a choice
                1 - rock
                2 - scissors
                3 - paper
                ''')
    try:
        user = int(input('Enter a number from 1 to 3 and press ENTER\n-> '))
        if user > 3 or user < 1:
            print('What did you write?????')
            time.sleep(2)
            print('FUCK!!!!')
            time.sleep(1)
            fuc()
        else:
            comp = rnd(1,3)
            if comp == user:
                print('Draw((')
            elif user == 1 and comp == 2 or user == 2 and comp == 3 or user == 3 and comp == 1:
                print('Fuck! Fuck! Fuck!!! YOU WIN!!!!!')
            else:
                print('ha-ha-ha!!! You lost a stupid monkey!!!')
            input('press ENTER')
    except:
        print('What did you write?????')
        time.sleep(2)
        print('FUCK!!!!')
        time.sleep(1)
        fuc()
else:
    fuc()