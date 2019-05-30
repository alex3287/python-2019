class Fraction():
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def show(self):
        print(self.top, '/', self.bottom, sep='')

    def __str__(self):
        return str(self.top)+'/'+str(self.bottom)

if __name__ == '__main__':
    test = Fraction(45, 5)
    test.show()
    print(test)