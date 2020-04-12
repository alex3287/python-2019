class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        s = ''
        for i in self.items:
            s += str(i) + ' '
        return s if s else '*'

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


test = Stack()
test.push(56)
test.push('Hello')
print(test)
print(test.isEmpty())
