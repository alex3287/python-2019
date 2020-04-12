# 641. Design Circular Deque
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.items = []
        self.size = k

    def __str__(self):
        items = [str(i) for i in self.items]
        return (' ').join(items)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.items) == self.size:
            return False
        else:
            self.items.insert(0,value)
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.items) == self.size:
            return False
        else:
            self.items.append(value)
            return True
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.items):
            del(self.items[0])
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.items):
            del(self.items[-1])
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.items):
            return self.items[0]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.items):
            return self.items[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if len(self.items) < 1 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if len(self.items) == self.size else False

if __name__=='__main__':
    # Your MyCircularDeque object will be instantiated and called as such:
    obj = MyCircularDeque(5)

    for i in range(2):
        print(obj.insertFront(i))

    for i in range(10,0,-1):
        print(obj.insertLast(i))

    # param_1 = obj.insertFront(7)

    # param_2 = obj.insertLast(value)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    # print(param_7)
    param_8 = obj.isFull()
    print(param_8)
    print(param_3)
    print('*'*100)
    print(obj)
    print(param_5)
    print(param_6)
