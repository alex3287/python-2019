from random import randint

for r in range(500):
        n = randint(-1000000000000000000, 1000000000000000000)
        if r%5:
            s = str(n)
            n = n*10**len(s) + int(''.join(sorted(s)))
        print(n)